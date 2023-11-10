> Adrien's been looking at ways to encrypt his messages with the help of symbols and minus signs. Can you find a way to recover the flag?

```
from random import randint

a = 288260533169915
p = 1007621497415251

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


print(encrypt_flag(FLAG))
```

플래그를 찾는 문제다

bin(i) : 숫자 i를 0b를 붙여 이진수로 변환

zfill : 0 패딩

n(a^e mod p) == 1 → a^e mod p append

n(a^e mod p) != 1 → -a^e mod p append

근데 a가 2차잉여면 a에 몇 제곱을 해도 2차잉여이기 때문에 르장드르 기호를 통해 2차잉여인지 판단한다

result : b'crypto{p4tterns_1n_re5idu3s}'

`crypto{p4tterns_1n_re5idu3s}`
