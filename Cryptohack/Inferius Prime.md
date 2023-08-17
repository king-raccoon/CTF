> Here is my super-strong RSA implementation, because it's 1600 bits strong it should be unbreakable... at least I think so!

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

```python
#inferius.py
#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3

# n will be 8 * (100 + 100) = 1600 bits strong which is pretty good
while True:
p = getPrime(100)
q = getPrime(100)
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
if d != -1 and GCD(e, phi) == 1:
break

n = p * q

flag = b"XXXXXXXXXXXXXXXXXXXXXXX"
pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
assert decrypted == flag
```

해당 파일은 p, q, totient function, d를 생성하는 파일같다

그러나 우린 n, e, ct를 알고있기 때문에 그냥 *factordb*로 n을 소인수분해하여 p, q를 구한다

```python
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

p = 752708788837165590355094155871
q = 986369682585281993933185289261

d = pow(e, -1, (p-1)*(q-1))
print(hex(pow(ct, d, n)))

#여기까지의 결과 : 0x63727970746f7b4e3333645f6231675f7052316d33357d

str = "63727970746f7b4e3333645f6231675f7052316d33357d"
print(bytearray.fromhex(str))
```

result : bytearray(b'crypto{N33d_b1g_pR1m35}')

`crypto{N33d_b1g_pR1m35}`
