> It is essential that keys in symmetric-key algorithms are random bytes, instead of passwords or other predictable data. The random bytes should be generated using a cryptographically-secure pseudorandom number generator (CSPRNG). If the keys are predictable in any way, then the security level of the cipher is reduced and it may be possible for an attacker who gets access to the ciphertext to decrypt it.
> 
> 
> Just because a key looks like it is formed of random bytes, does not mean that it necessarily is. In this case the key has been derived from a simple password using a hashing function, which makes the ciphertext crackable.
> 
> For this challenge you may script your HTTP requests to the endpoints, or alternatively attack the ciphertext offline. Good luck!
> 
> Play at
> 
> https://aes.cryptohack.org/passwords_as_keys
>

```
from Crypto.Cipher import AES
import hashlib
import random


# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("/usr/share/dict/words") as f:
    words = [w.strip() for w in f.readlines()]
keyword = random.choice(words)

KEY = hashlib.md5(keyword.encode()).digest()
FLAG = ?


@chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


@chal.route('/passwords_as_keys/encrypt_flag/')
def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_ECB)
    encrypted = cipher.encrypt(FLAG.encode())

    return {"ciphertext": encrypted.hex()}
```

ENCRYPT_FLAG() : {"ciphertext":"c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"}

hash.**digest**() : 지금까지 `update()` 메서드에 전달된 데이터의 요약을 반환한다. 이것은 `digeste_size` 크기의 바이트열 객체이며 0에서 255까지의 전체 범위에 있는 바이트를 포함할 수 있다.

hash.**hexdigest**(): `digeste_size`와 유사하지만, 요약은 16진수 숫자만 포함하는 두 배 길이의 문자열 객체로 반환된다. 전자 메일이나 기타 바이너리가 아닌 환경에서 값을 안전하게 교환하는 데 사용할 수 있다.

주어진 코드를 수정했다. 문제 코드를 보면 word를 받을 수 있는데 양이 진짜 많아서 word라는 파일로 저장했다. 근데 돌려보면 저 많은게 한 번에 안 돌아가는 것 같아서 잘라서 찾아준다.

사실 노가다하기 싫어서 flag[:7] == ‘crypto’와 같은지 확인하고 맞으면 플래그만 출력하려고 했는데 *********unhashable type: slice*********라는 오류가 나왔다

아 돌려보니까 flag가 {'plaintext': '41f7bb30f9713c5089fe779d054ca185c6d21d6792e927e36e7286cedcb1c346'} 형식이여서 힘내자,,,ㅎ

걍 노다가 뛰자,,,

하려다가 이건 진짜 아닌 것 같아서 구글링했다 😢

https://gist.github.com/rarecoil/afcbcbf830fedc654043060d22424de6