> With all the attacks on MD5 and SHA1 floating around, we thought it was time to start rolling our own hash algorithm. We've set the block size to 256 bits, so I doubt anyone will find a collision.
>

```
# 2^128 collision protection!
BLOCK_SIZE = 32

# Nothing up my sleeve numbers (ref: Dual_EC_DRBG P-256 coordinates)
W = [0x6b17d1f2, 0xe12c4247, 0xf8bce6e5, 0x63a440f2, 0x77037d81, 0x2deb33a0, 0xf4a13945, 0xd898c296]
X = [0x4fe342e2, 0xfe1a7f9b, 0x8ee7eb4a, 0x7c0f9e16, 0x2bce3357, 0x6b315ece, 0xcbb64068, 0x37bf51f5]
Y = [0xc97445f4, 0x5cdef9f0, 0xd3e05e1e, 0x585fc297, 0x235b82b5, 0xbe8ff3ef, 0xca67c598, 0x52018192]
Z = [0xb28ef557, 0xba31dfcb, 0xdd21ac46, 0xe2a91e3c, 0x304f44cb, 0x87058ada, 0x2cb81515, 0x1e610046]

# Lets work with bytes instead!
W_bytes = b''.join([x.to_bytes(4,'big') for x in W])
X_bytes = b''.join([x.to_bytes(4,'big') for x in X])
Y_bytes = b''.join([x.to_bytes(4,'big') for x in Y])
Z_bytes = b''.join([x.to_bytes(4,'big') for x in Z])

def pad(data):
    padding_len = (BLOCK_SIZE - len(data)) % BLOCK_SIZE
    return data + bytes([padding_len]*padding_len)

def blocks(data):
    return [data[i:(i+BLOCK_SIZE)] for i in range(0,len(data),BLOCK_SIZE)]

def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])

def rotate_left(data, x):
    x = x % BLOCK_SIZE
    return data[x:] + data[:x]

def rotate_right(data, x):
    x = x % BLOCK_SIZE
    return  data[-x:] + data[:-x]

def scramble_block(block):
    for _ in range(40):
        block = xor(W_bytes, block)
        block = rotate_left(block, 6)
        block = xor(X_bytes, block)
        block = rotate_right(block, 17)
    return block

def cryptohash(msg):
    initial_state = xor(Y_bytes, Z_bytes)
    msg_padded = pad(msg)
    msg_blocks = blocks(msg_padded)
    for i,b in enumerate(msg_blocks):
        mix_in = scramble_block(b)
        for _ in range(i):
            mix_in = rotate_right(mix_in, i+11)
            mix_in = xor(mix_in, X_bytes)
            mix_in = rotate_left(mix_in, i+6)
        initial_state = xor(initial_state,mix_in)
    return initial_state.hex()
```

함수 분석을 하면 코드를 다시 분석하면 msg를 32에 맞게 패딩하고(pad 함수), 32마다 블록으로 쪼갠다(block 함수).

scramble_block에선 쪼갠 block을 W_bytes와 xor 연산하고, 6만큼 왼쪽으로 rotate시키고, X_bytes와 xor 연산 후 오른쪽으로 17 rotate시킨다.

어떻게 해야할지 몰라서 다른 사람의 write-up을 봤다
[uvicorn's_wite-up](https://github.com/uvicorn/writeups/blob/master/cryptohack/Hash_Stuffing.md)

다른 사람 write up을 봤는데 해당 코드에 두 개의 문자가 있다고 한다.

1. pad 함수에서 pad(b’\x01’*31) == pad(b’\x01’*32)처럼 서로 다른 두 문자열의 패딩값이 같다
2. 모든 연산이 반전 가능하다. 즉, 원래라면 해시함수는 일방향성을 갖기 때문에 원래 데이터로 복구가 불가능해야하지만 가능
    1) cryptohash 함수에서 마지막 부근에 initial_state = xor(initial_state, mix_in) 하는 과정에서 xor 연산 특에 따라 같은 블록을 여러 번 xor 연산하면 원래 값이 나오기 때문에 해시 저항성이 성립하지 않는다 
```
import os
import json

# 2^128 collision protection!
BLOCK_SIZE = 32

# Nothing up my sleeve numbers (ref: Dual_EC_DRBG P-256 coordinates)
W = [0x6b17d1f2, 0xe12c4247, 0xf8bce6e5, 0x63a440f2, 0x77037d81, 0x2deb33a0, 0xf4a13945, 0xd898c296]
X = [0x4fe342e2, 0xfe1a7f9b, 0x8ee7eb4a, 0x7c0f9e16, 0x2bce3357, 0x6b315ece, 0xcbb64068, 0x37bf51f5]
Y = [0xc97445f4, 0x5cdef9f0, 0xd3e05e1e, 0x585fc297, 0x235b82b5, 0xbe8ff3ef, 0xca67c598, 0x52018192]
Z = [0xb28ef557, 0xba31dfcb, 0xdd21ac46, 0xe2a91e3c, 0x304f44cb, 0x87058ada, 0x2cb81515, 0x1e610046]

# Lets work with bytes instead!
W_bytes = b''.join([x.to_bytes(4,'big') for x in W])
X_bytes = b''.join([x.to_bytes(4,'big') for x in X])
Y_bytes = b''.join([x.to_bytes(4,'big') for x in Y])
Z_bytes = b''.join([x.to_bytes(4,'big') for x in Z])

def pad(data):
    padding_len = (BLOCK_SIZE - len(data)) % BLOCK_SIZE
    return data + bytes([padding_len]*padding_len)

def blocks(data): #리턴값의 최대 길이
    return [data[i:(i+BLOCK_SIZE)] for i in range(0,len(data),BLOCK_SIZE)]

def xor(a,b):
    return bytes([x^y for x,y in zip(a,b)])

def rotate_left(data, x):
    x = x % BLOCK_SIZE
    return data[x:] + data[:x]

def rotate_right(data, x):
    x = x % BLOCK_SIZE
    return  data[-x:] + data[:-x]

def scramble_block(block):
    for _ in range(40):
        block = xor(W_bytes, block)
        block = rotate_left(block, 6)
        block = xor(X_bytes, block)
        block = rotate_right(block, 17)
    return block

def cryptohash(msg):
    initial_state = xor(Y_bytes, Z_bytes)
    msg_padded = pad(msg)
    msg_blocks = blocks(msg_padded)
    for i,b in enumerate(msg_blocks):
        mix_in = scramble_block(b)
        for _ in range(i):
            mix_in = rotate_right(mix_in, i+11)
            mix_in = xor(mix_in, X_bytes)
            mix_in = rotate_left(mix_in, i+6)
        initial_state = xor(initial_state,mix_in)
    return initial_state.hex()

#cryptohash의 역과정 수행
def reverse_scramble_block(b):
    for _ in range(40):
        b = rotate_left(b,17)
        b = xor(X_bytes, b)
        b = rotate_right(b, 6)
        b = xor(W_bytes, b)
    return b

def solution():
    initial_state = xor(Y_bytes, Z_bytes)
    b = os.urandom(BLOCK_SIZE) #32바이트의 난수값 생성 -> pad 필요없어짐
    mix_in1 = scramble_block(b)
    mix_in2 = os.urandom(BLOCK_SIZE)
    mix_in1 = xor(mix_in1, mix_in2)

    #32바이트인 b이기 때문에 cryptohash 함수에서 enumerate에 넣으면 i = 1밖에 안 나온다
    #cryptohash 함수의 for문의 역과정 실행
    mix_in2 = rotate_right(mix_in2, 7)
    mix_in2 = xor(mix_in2, X_bytes)
    mix_in2 = rotate_left(mix_in2, 12)

    b1 = reverse_scramble_block(mix_in1)
    b2 = reverse_scramble_block(mix_in2)

    assert cryptohash(b1+b2) == cryptohash(b)
    return json.dumps({"m1": (b1+b2).hex(), "m2": b.hex()})

print(solution())
```

`crypto{Always_add_padding_even_if_its_a_whole_block!!!}`