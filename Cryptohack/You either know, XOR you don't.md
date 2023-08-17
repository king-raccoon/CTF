> I've encrypted the flag with my secret key, you'll never be able to guess it.
> Remember the flag format and how it might help you in this challenge!
> 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

```
#for test
from Crypto.Util.number import *

str= bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(str)
flag_key = b"crypto{"
test = [0x0e, 0x0b, 0x21, 0x3f, 0x26, 0x04, 0x1e]
for i in range(len(flag_key)):
    print(chr(flag_key[i] ^ test[i]), end="")
```

result : b"\x0e\x0b!?&\x04\x1eH\x0b&!\x7f'4.\x17]\x0e\x07\n<[\x10>%&!\x7f'4.\x17]\x0e\x07~&4Q\x15\x01\x04"
myXORke%

위 코드를 통해 str은 flag 형식으로 나오고, 힌트에 나온 것처럼 crypto{라는 flag 형식을 str와 xor 연산을 한 결과 myXORke가 나옴을 확인했다.

```
from Crypto.Util.number import *

str = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
# print(str)
flag_key = b"crypto{"
# test = [0x0e, 0x0b, 0x21, 0x3f, 0x26, 0x04, 0x1e]
# for i in range(len(flag_key)):
#     print(chr(flag_key[i] ^ test[i]), end="")

i = 0
for c in str:
    print(chr(c ^ flag_key[i%7]), end="")
    i += 1
```

이렇게 했더니 flag_key의 길이가 7이라 7로 나눌 경우 인덱스 범위를 넘어가서 안된다는데 왜 넘는다고 하는지 모르겠다

```
from Crypto.Util.number import *

str = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
# print(str)
flag_key = b"crypto{"
test = [0x0e, 0x0b, 0x21, 0x3f, 0x26, 0x04, 0x1e]
flag = []
for i in range(len(flag_key)):
    flag.append(flag_key[i] ^ test[i])
flag.append(ord('y'))
#flag_key = [ord('c'), ord('r'),ord('y'),ord('p'),ord('t'),ord('o'),ord('{')]
i = 0
for c in str:
    print(chr(c ^ flag[i%8]), end="")
    i += 1
```

`crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`
