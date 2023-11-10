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
            decoded = base64.b64decode(encoded).decode()  # decode base64
        elif encoding == "hex":
            decoded = bytes.fromhex(encoded).decode()  # decode hex
        elif encoding == "rot13":
            decoded = codecs.decode(encoded, 'rot_13')  # decode rot13
        elif encoding == "bigint":
            # decode bigint (remove '0x' and convert from hex)
            decoded = bytes.fromhex(encoded[2:]).decode()
        elif encoding == "utf-8":
            decoded = "".join([chr(b) for b in encoded])  # decode utf-8

        print("[*] {} | Succesfully decoded : {}".format(stage + 1, encoded), encoding)
        tn.write(json.dumps({"decoded": decoded}).encode())
        stage += 1

except:
    print("\n[+] Flag : {}".format(received["flag"]))
