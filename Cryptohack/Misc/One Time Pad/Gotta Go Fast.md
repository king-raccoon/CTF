> I won't have have to worry about running out of entropy, I'm going to have my OTP generated forever with this new script!
> 
> 
> Connect at `nc socket.cryptohack.org 13372`
>

```
#13372.py
#!/usr/bin/env python3

import time
from Crypto.Util.number import long_to_bytes
import hashlib
from utils import listener


FLAG = b'crypto{????????????????????}'


def generate_key():
    current_time = int(time.time())
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()


def encrypt(b):
    key = generate_key()
    assert len(b) <= len(key), "Data package too large to encrypt"
    ciphertext = b''
    for i in range(len(b)):
        ciphertext += bytes([b[i] ^ key[i]])
    return ciphertext.hex()


class Challenge():
    def __init__(self):
        self.before_input = "Gotta go fast!\n"

    def challenge(self, your_input):
        if not 'option' in your_input:
            return {"error": "You must send an option to this server"}

        elif your_input['option'] == 'get_flag':
            return {"encrypted_flag": encrypt(FLAG)}

        elif your_input['option'] == 'encrypt_data':
            input_data = bytes.fromhex(your_input['input_data'])
            return {"encrypted_data": encrypt(input_data)}

        else:
            return {"error": "Invalid option"}


"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
listener.start_server(port=13372)
```

현재 시간을 이용해 키를 생성한다

```
#!/usr/bin/env python3

import time
from Crypto.Util.number import long_to_bytes
import hashlib
# from utils import listener
import telnetlib
import json

FLAG = b'crypto{????????????????????}'
HOST = "socket.cryptohack.org"
PORT = 13372

def generate_key():
    current_time = int(time.time())
    key = long_to_bytes(current_time)
    return hashlib.sha256(key).digest()

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

print(readline()) #"Gotta go fast!" 출력
json_send({"option": 'get_flag'}) #'get_flag' 보냄
received = json_recv() #그에 대한 응답 받음

input = received['encrypted_flag'] 
json_send({"option": "encrypt_data","input_data": input})
received = json_recv()

flag = received['encrypted_data']
print(bytes.fromhex(flag))
```

`crypto{t00_f4st_t00_furi0u5}`