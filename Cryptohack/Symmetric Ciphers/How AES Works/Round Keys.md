> Complete the `add_round_key` function, then use the `matrix2bytes` function to get your next flag.
>

```
#add_round_key.py
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    ???


print(add_round_key(state, round_key))
```

```
#solution.py
def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    for i in range(4):
        for j in range(4):
            print(chr(matrix[i][j]), end='')

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    matrix = []
    for i in range(4):
        line = []
        for j in range(4):
            line.append(s[i][j] ^ k[i][j])
        matrix.append(line)
    return matrix
    # return [[(state[j] ^ round_key[j]) for j in range(4)] for i in range(4)]



matrix = add_round_key(state, round_key)


print(matrix2bytes(matrix))
```

`crypto{r0undk3y}`