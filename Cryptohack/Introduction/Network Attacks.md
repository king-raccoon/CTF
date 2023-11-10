>For this challenge, connect to socket.cryptohack.org on port 11112. Send a JSON object with the key buy and value flag.

>Connect at socket.cryptohack.org 11112


```
#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())
print(readline())
print(readline())
print(readline())


request = {
		#"buy": "clothes"
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)
```

“clothes”를 “flag”로 바꾼 후 실행

`crypto{sh0pp1ng_f0r_fl4g5}`