<https://dreamhack.io/wargame/challenges/559>

암호화 : 평문을 16진수로 바꾼 후 키와 XOR 연산

복호화 : 암호문을 키와 XOR

키가 단일바이트이므로 2^8개가 가능

```
a = [0x54,0x58,0x6b,0x64,0x58,0x75,0x4f,0x7b,0x21,0x5c,0x7c,0x75,0x42,0x4f,0x21,0x63,0x4f,0x74,0x42,0x75,0x51,0x7d,0x6d]

for i in range(255):
    for j in a:
        print(chr(i^int(j)), end="")
    print("\n")
```

<img width="234" alt="스크린샷 2023-07-05 오후 3 52 41" src="https://github.com/king-raccoon/write-up/assets/78426205/3bc1d1ec-326a-4886-8475-c7dd1575f2bf">
