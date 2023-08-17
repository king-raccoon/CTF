> For all elements `g` in the field, there exists a unique integer `d` such that `g * d ≡ 1 mod p`
> <br>What is the inverse element: `3 * d ≡ 1 mod 13`?

암산하면 3\*9 = 27 ≡ 1 mod 13임을 알 수 있다

확장 유클리드 호제법을 활용한 역원 구하기

3 _ x + 13 _ y = 1

3 _ x + 13 _ y ≡ 1 mod 13

3 \* x ≡ 1 mod 13

```
def modInverse(a, m):
    g = gdc(a, m)
    if (g != 1):
        # Inverse doesn't exist
        return -1
    else:
        return pow(a, m - 2, m)

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
```

**OR**

```
pow(e, -1, n)
```

근데 사실 암산이 된다

`9`
