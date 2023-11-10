> Now you've got the hang of the various encodings you'll be encountering, let's have a look at automating it.
>
>
> Can you pass all 100 levels to get the flag?
> 
> The *[13377.py](http://13377.py)* file attached below is the source code for what's running on the server. The *pwntools_example.py* file provides the start of a solution using the incredibly convenient pwntools library. which we recommend. If you'd prefer to use Python's in-built telnetlib, *telnetlib_example.py* is also provided.

```
#!/usr/bin/env python3
#13377.py

from Crypto.Util.number import bytes_to_long, long_to_bytes
from utils import listener # this is cryptohack's server-side module and not part of python
import base64
import codecs
import random

FLAG = "crypto{????????????????????}"
ENCODINGS = [
    "base64",
    "hex",
    "rot13",
    "bigint",
    "utf-8",
]
with open('/usr/share/dict/words') as f:
    WORDS = [line.strip().replace("'", "") for line in f.readlines()]


class Challenge():
    def __init__(self):
        self.challenge_words = ""
        self.stage = 0

    def create_level(self):
        self.stage += 1
        self.challenge_words = "_".join(random.choices(WORDS, k=3))
        encoding = random.choice(ENCODINGS)

        if encoding == "base64":
    decoded = base64.b64decode(encoded).decode() # decode base64
elif encoding == "hex":
    decoded = bytes.fromhex(encoded).decode() # decode hex
elif encoding == "rot13":
    decoded = codecs.decode(encoded, 'rot_13') # decode rot13
elif encoding == "bigint":
    decoded = bytes.fromhex(encoded[2:]).decode() # decode bigint (remove '0x' and convert from hex)
elif encoding == "utf-8":
    decoded = "".join([chr(b) for b in encoded]) # decode utf-8

        return {"type": encoding, "encoded": encoded}

    #
    # This challenge function is called on your input, which must be JSON
    # encoded
    #
    def challenge(self, your_input):
        if self.stage == 0:
            return self.create_level()
        elif self.stage == 100:
            self.exit = True
            return {"flag": FLAG}

        if self.challenge_words == your_input["decoded"]:
            return self.create_level()

        return {"error": "Decoding fail"}


listener.start_server(port=13377)
```
challenge 함수를 통해 100번째 stage에서 flag를 받을 수 있는 것 같다

```
import base64
import codecs
import json
import telnetlib
from Crypto.Util.number import bytes_to_long 

HOST = "socket.cryptohack.org"
PORT = 13377
FLAG = "crypto{????????????????????}"

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

try:
    stage = 0
    while stage <= 100:
        received = json_recv()
        encoding = received["type"]
        encoded = received["encoded"]
        # received = json.loads(tn.read_until(b"\n").decode)

        if encoding == "base64":
            decoded = base64.b64decode(encoded).decode() # decode base64
        elif encoding == "hex":
            decoded = bytes.fromhex(encoded).decode() # decode hex
        elif encoding == "rot13":
            decoded = codecs.decode(encoded, 'rot_13') # decode rot13
        elif encoding == "bigint":
            decoded = bytes.fromhex(encoded[2:]).decode() # decode bigint (remove '0x' and convert from hex)
        elif encoding == "utf-8":
            decoded = "".join([chr(b) for b in encoded]) # decode utf-8

        print("[*] {} | Succesfully decoded : {}".format(stage + 1, encoded), encoding)
        tn.write(json.dumps({"decoded" : decoded}).encode())
        stage += 1

except:
    print("\n[+] Flag : {}".format(received["flag"]))
```

endcode랑 decode를 잘못 써서 답이 안 나왔다

[solution](./Encoding%20Challange.py)

`crypto{3nc0d3_d3c0d3_3nc0d3}`