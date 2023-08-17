> 11 ≡ x mod 6
> <br>8146798528947 ≡ y mod 17
> <br>x, y 중 작은 것이 flag

```
a = 11 % 6
b = 8146798528947 % 17
print(a if a < b else b)
```

`4`
