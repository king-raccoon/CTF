> p = 65537. Calculate 273246787654^65536 mod 6553

```
a = 273246787654
p = 65537
print(pow(a, p-1)%p if a%p != 0 else 1)
```

`1`
