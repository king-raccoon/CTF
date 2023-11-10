> I've invented a nice simple version of HMAC authentication, hopefully it isn't vulnerable to the same problems as Merkle–Damgård construction hash functions…
>

```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
from utils import listener


FLAG = "crypto{???????????????}"


def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def hash(data):
    data = pad(data, 16)
    out = b"\x00" * 16
    for i in range(0, len(data), 16):
        blk = data[i:i+16]
        out = bxor(AES.new(blk, AES.MODE_ECB).encrypt(out), out)
    return out


class Challenge():
    def __init__(self):
        self.before_input = "You'll never forge my signatures!\n"
        self.key = os.urandom(16)

    def challenge(self, msg):
        if "option" not in msg:
            return {"error": "You must send an option to this server."}

        elif msg["option"] == "sign":
            data = bytes.fromhex(msg["message"])
            if b"admin=True" in data:
                return {"error": "Unauthorized to sign message"}
            sig = hash(self.key + data)

            return {"signature": sig.hex()}

        elif msg["option"] == "get_flag":
            sent_sig = bytes.fromhex(msg["signature"])
            data = bytes.fromhex(msg["message"])
            real_sig = hash(self.key + data)

            if real_sig != sent_sig:
                return {"error": "Invalid signature"}

            if b"admin=True" in data:
                return {"flag": FLAG}
            else:
                return {"error": "Unauthorized to get flag"}

        else:
            return {"error": "Invalid option"}


"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
listener.start_server(port=13388)
```

<img width="450" alt="스크린샷 2023-11-01 오후 2 41 02" src="https://github.com/king-raccoon/king-raccoon/assets/78426205/bbec15d8-52f5-47d3-86eb-19e541b3674a">


data = msg[”message”] 16진수 값을 바이트로 변환한 값

sig = 16바이트의 난수값인 key와 data를 hash 함수에 돌린 값

hash 함수 : data를 16바이트로 패딩하고, data 길이에 비례하게 b"\x00" * 16를 ecb 모드로 data[i:i+16]을 해시한 값과 xor 연산한다

challenge함수를 보면 data에 b"admin=True"가 있어야 flag를 얻을 수 있기 때문에 가짜 데이터를 만들자

```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import telnetlib
import json
# from utils import listener


FLAG = "crypto{???????????????}"

HOST = "socket.cryptohack.org"
PORT = 13388

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def hash(data):
    data = pad(data, 16)
    out = b"\x00" * 16
    for i in range(0, len(data), 16):
        blk = data[i:i+16]
        out = bxor(AES.new(blk, AES.MODE_ECB).encrypt(out), out)
    return out


class Challenge():
    def __init__(self):
        self.before_input = "You'll never forge my signatures!\n"
        self.key = os.urandom(16)

    def challenge(self, msg):
        if "option" not in msg:
            return {"error": "You must send an option to this server."}

        elif msg["option"] == "sign":
            data = bytes.fromhex(msg["message"])
            if b"admin=True" in data:
                return {"error": "Unauthorized to sign message"}
            sig = hash(self.key + data)

            return {"signature": sig.hex()}

        elif msg["option"] == "get_flag":
            sent_sig = bytes.fromhex(msg["signature"])
            data = bytes.fromhex(msg["message"])
            real_sig = hash(self.key + data)

            if real_sig != sent_sig:
                return {"error": "Invalid signature"}

            if b"admin=True" in data:
                return {"flag": FLAG}
            else:
                return {"error": "Unauthorized to get flag"}

        else:
            return {"error": "Invalid option"}

def solution():
    print(readline())
    json_send({"option": "sign","message": ""})
    received = json_recv()
    sig = bytes.fromhex(received["signature"])
    data = pad(b"admin=True" 16)
    fake = bxor(AES.new(data, AES.MODE_ECB).encrypt(sig), sig).hex()
    data = data.hex()
    json_send({"option": "get_flag", "signature": "{fake}", "message": "{data}"})
    print(readline())

solution()
    

# """
# When you connect, the 'challenge' function will be called on your JSON
# input.
# """
# listener.start_server(port=13388)
```
실패했다.

사실 data만들때 pad(b'\x00' * 10, 16) 사용한게 좀 마음에 걸리는데 이거 아니면 뭔데

**더미를 넣자!**

```
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import telnetlib
import json
# from utils import listener


FLAG = "crypto{???????????????}"

HOST = "socket.cryptohack.org"
PORT = 13388

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def hash(data):
    data = pad(data, 16)
    out = b"\x00" * 16
    for i in range(0, len(data), 16):
        blk = data[i:i+16]
        out = bxor(AES.new(blk, AES.MODE_ECB).encrypt(out), out)
    return out


class Challenge():
    def __init__(self):
        self.before_input = "You'll never forge my signatures!\n"
        self.key = os.urandom(16)

    def challenge(self, msg):
        if "option" not in msg:
            return {"error": "You must send an option to this server."}

        elif msg["option"] == "sign":
            data = bytes.fromhex(msg["message"])
            if b"admin=True" in data:
                return {"error": "Unauthorized to sign message"}
            sig = hash(self.key + data)

            return {"signature": sig.hex()}

        elif msg["option"] == "get_flag":
            sent_sig = bytes.fromhex(msg["signature"])
            data = bytes.fromhex(msg["message"])
            real_sig = hash(self.key + data)

            if real_sig != sent_sig:
                return {"error": "Invalid signature"}

            if b"admin=True" in data:
                return {"flag": FLAG}
            else:
                return {"error": "Unauthorized to get flag"}

        else:
            return {"error": "Invalid option"}

def solution():
    dummy = b"a" * 16
    print(readline())
    json_send({"option": "sign","message": dummy.hex()})
    received = json_recv()
 
    print(received["signature"])

    data = pad(b"admin=True", 16)
    print(data)

    sig = bytes.fromhex(received["signature"])
    fake = bxor(AES.new(data, AES.MODE_ECB).encrypt(sig), sig)
    data = pad(dummy, 16) + b"admin=True"
    json_send({"option": "get_flag", "signature": fake.hex(), "message": data.hex()})
    print(readline())

solution()
    

# """
# When you connect, the 'challenge' function will be called on your JSON
# input.
# """
# listener.start_server(port=13388)
```

`crypto{l3ngth_3xT3nd3r}`