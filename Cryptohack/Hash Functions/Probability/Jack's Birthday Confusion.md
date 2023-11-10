> Given no other data of the `JACK11` hash algorithm, how many unique secrets would you expect to hash to have (on average) a 75% chance of a collision between two distinct secrets?
>

```
import math
n = 2048 # 11-bit 암호 개수
for i in range(n):
    if 0.75 <= 1 - math.factorial(n)/(pow(n, i) * math.factorial(n-i)):
        print(i)
        break
```

`76`