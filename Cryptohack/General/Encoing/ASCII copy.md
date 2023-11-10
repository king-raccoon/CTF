> ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.
> <br>Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
> <br>[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

```
arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73,
       73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for i in arr:
    result = chr(i)
    print(result, end='')
```

`crypto{ASCII_pr1nt4bl3`
