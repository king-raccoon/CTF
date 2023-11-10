> Check out my document system about particle physics, where every document is uniquely referenced by hash.
> 
> 
> Connect at `socket.cryptohack.org 13389`
>

```
import hashlib
from utils import listener


FLAG = "crypto{???????????????????????????????????}"


class Challenge():
    def __init__(self):
        self.before_input = "Give me a document to store\n"
        self.documents = {
            "508dcc4dbe9113b15a1f971639b335bd": b"Particle physics (also known as high energy physics) is a branch of physics that studies the nature of the particles that constitute matter and radiation. Although the word particle can refer to various types of very small objects (e.g. protons, gas particles, or even household dust), particle physics usually investigates the irreducibly smallest detectable particles and the fundamental interactions necessary to explain their behaviour.",
            "cb07ff7a5f043361b698c31046b8b0ab": b"The Large Hadron Collider (LHC) is the world's largest and highest-energy particle collider and the largest machine in the world. It was built by the European Organization for Nuclear Research (CERN) between 1998 and 2008 in collaboration with over 10,000 scientists and hundreds of universities and laboratories, as well as more than 100 countries.",
        }

    def challenge(self, msg):
        if "document" not in msg:
            self.exit = True
            return {"error": "You must send a document"}

        document = bytes.fromhex(msg["document"])
        document_hash = hashlib.md5(document).hexdigest()

        if document_hash in self.documents.keys():
            self.exit = True
            if self.documents[document_hash] == document:
                return {"error": "Document already exists in system"}
            else:
                return {"error": f"Document system crash, leaking flag: {FLAG}"}

        self.documents[document_hash] = document

        if len(self.documents) > 5:
            self.exit = True
            return {"error": "Too many documents in the system"}

        return {"success": f"Document {document_hash} added to system"}


"""
When you connect, the 'challenge' function will be called on your JSON
input.
"""
listener.start_server(port=13389)
```

맨 위 if문 이후에 document msg인 16진수 값을 바이트로 변환하여 document에 저장 후 md5 연산한 바이트 값을 16진수로 바꿔 document_hash에 저장

바로 다음에 나오는 if문에서 document_hash가 documents.key()이고 해당 해시에 대한 document가 document와 같지 않다면 `Document system crash, leaking flag`라고 하면서 플래그를 알려준다

즉, 해시 충동 나는 값을 찾아야할 것 같다

이때 document_hash를 만들기 위해 md5 연산을 했기 때문에 md5를 좀 더 알아보자

[MD5](https://ko.wikipedia.org/wiki/MD5)

[Create_MD5_Collision](https://stackoverflow.com/questions/933497/create-your-own-md5-collisions)

```d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70

d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70
```

md5 collision 발생시키는 두 수를 다음과 같이 document에 넣으면 된다


<img width="742" alt="스크린샷 2023-10-31 오후 11 29 00" src="https://github.com/king-raccoon/king-raccoon/assets/78426205/d5b3fd00-38e7-423e-a8cd-f1d17847e9e0">


`crypto{m0re_th4n_ju5t_p1g30nh0le_pr1nc1ple}`