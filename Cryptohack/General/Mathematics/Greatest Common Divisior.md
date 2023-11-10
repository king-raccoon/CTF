> `gcd(a,b)` for `a = 66528, b = 52920`

```
#GCD iteration
def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a
```

```
#GCD recursion
def Euclidean(a, b):
    r = b % a
    if r == 0:
        return a
    return Euclidean(r, a)
```

```
#solution
def GCD(a, b):
    while b != 0:
        [a, b] = [b, a % b]
    return a

print(GCD(66528, 52920))
```

`1512`
