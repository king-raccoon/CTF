> We say that an integer `x` is a *Quadratic Residue* if there exists an `a` such that `a2 = x mod p`. If there is no such solution, then the integer is a *Quadratic Non-Residue*.
> <br>> Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.
> <br>>p = 29
> <br>>ints = [14, 6, 11]

```
import math
p = 29
ints = [14, 6, 11]

for i in range(29):
    x = pow(i, 2) % p
    if x in ints:
            print(x, i)
```

result :
<br>6 8
<br>6 21

`6`
