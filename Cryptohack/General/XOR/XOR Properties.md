> Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.
> `KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf`

```
from Crypto.Util.number import *

key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key12 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
key23 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
key123 = key1 ^ key23
flag_key = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
flag = flag_key ^ key123
print(long2str(flag))
```

result : b'crypto{x0r_i5_ass0c1at1v3}'

`crypto{x0r_i5_ass0c1at1v3}`
