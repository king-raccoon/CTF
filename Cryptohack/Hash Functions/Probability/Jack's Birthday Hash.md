> Today is Jack's birthday, so he has designed his own cryptographic hash as a way to celebrate.
> 
> 
> Reading up on the key components of hash functions, he's a little worried about the security of the `JACK11` hash.
> 
> Given any input data, `JACK11` has been designed to produce a deterministic bit array of length 11, which is sensitive to small changes using the avalanche effect.
> 
> Using `JACK11` , his secret has the hash value: `JACK(secret) = 01011001101`
> 
> Given no other data of the `JACK11` hash algorithm, how many unique secrets would you expect to hash to have (on average) a 50% chance of a collision with Jack's secret?
>

```
n = 2048 # 11-bit 암호 개수
for i in range(n):
    if 0.5 <= 1 - ((n-1)/n)**i : #Jack의 비밀과 다를 확률 = (n-1)/n, 그런 비밀번호가 i개 존재
        print(i)
        break
```

`1420`