> … A few structured formats have been standardised to help send and receive cryptographic data…
> 
> 
> PEM is a popular format for sending keys, certificates, and other cryptographic material. It looks like:
> `-----BEGIN RSA PUBLIC KEY---—
> MIIBCgKC... *(a whole bunch of base64)
> -----END RSA PUBLIC KEY---—*`
> 
> It wraps base64-encoded data by a one-line header and footer to indicate how to parse the data within. Perhaps unexpectedly, it's important for there to be the correct number of hyphens in the header and footer, otherwise cryptographic tools won't be able to recognise the file.
> Extract the private key *d* as a decimal integer from this PEM-formatted RSA key.
> 
> > There are two main approaches for solving this challenge. The data in the certificate can be read with the openssl command line tool, or in Python using PyCryptodome. We recommend using PyCryptodome: first import the RSA module with `from Crypto.PublicKey import RSA` and you can read the key data using `RSA.importKey()`.
> >

우선 챌린지 파일이 pem 형식이라 pem이 뭔지 알아보자

[theory](https://www.notion.so/kingplatypus/Crypto-Advanced-2nd-76cc16825398402e9da8ac57e0bd7bd1)

```
`----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAzvKDt+EO+A6oE1LItSunkWJ8vN6Tgcu8Ck077joGDfG2NtxD
4vyQxGTQngr6jEKJuVz2MIwDcdXtFLIF+ISX9HfALQ3yiedNS80n/TR1BNcJSlzI
uqLmFxddmjmfUvHFuFLvxgXRga3mg3r7olTW+1fxOS0ZVeDJqFCaORRvoAYOgLgu
d2/E0aaaJi9cN7CjmdJ7Q3m6ryGuCwqEvZ1KgVWWa7fKcFopnl/fcsSecwbDV5hW
fmvxiAUJy1mNSPwkf5YhGQ+83g9N588RpLLMXmgt6KimtiWnJsqtDPRlY4Bjxdpu
V3QyUdo2ymqnquZnE/vlU/hn6/s8+ctdTqfSCwIDAQABAoIBAHw7HVNPKZtDwSYI
djA8CpW+F7+Rpd8vHKzafHWgI25PgeEhDSfAEm+zTYDyekGk1+SMp8Ww54h4sZ/Q
1sC/aDD7ikQBsW2TitVMTQs1aGIFbLBVTrKrg5CtGCWzHa+/L8BdGU84wvIkINMh
CtoCMCQmQMrgBeuFy8jcyhgl6nSW2bFwxcv+NU/hmmMQK4LzjV18JRc1IIuDpUJA
kn+JmEjBal/nDOlQ2v97+fS3G1mBAaUgSM0wwWy5lDMLEFktLJXU0OV59Sh/90qI
Jo0DiWmMj3ua6BPzkkaJPQJmHPCNnLzsn3Is920OlvHhdzfins6GdnZ8tuHfDb0t
cx7YSLECgYEA7ftHFeupO8TCy+cSyAgQJ8yGqNKNLHjJcg5t5vaAMeDjT/pe7w/R
0IWuScCoADiL9+6YqUp34RgeYDkks7O7nc6XuABi8oMMjxGYPfrdVfH5zlNimS4U
wl93bvfazutxnhz58vYvS6bQA95NQn7rWk2YFWRPzhJVkxvfK6N/x6cCgYEA3p21
w10lYvHNNiI0KBjHvroDMyB+39vD8mSObRQQuJFJdKWuMq+o5OrkC0KtpYZ+Gw4z
L9DQosip3hrb7b2B+bq0yP7Izj5mAVXizQTGkluT/YivvgXcxVKoNuNTqTEgmyOh
Pn6w+PqRnESsSFzjfWrahTCrVomcZmnUTFh0rv0CgYBETN68+tKqNbFWhe4M/Mtu
MLPhFfSwc8YU9vEx3UMzjYCPvqKqZ9bmyscXobRVw+Tf9llYFOhM8Pge06el74qE
IvvGMk4zncrn8LvJ5grKFNWGEsZ0ghYxJucHMRlaU5ZbM6PEyEUQqEKBKbbww65W
T3i7gvuof/iRbOljA9yzdwKBgQDT9Pc+Fu7k4XNRCon8b3OnnjYztMn4XKeZn7KY
GtW81eBJpwJQEj5OD3OnYQoyovZozkFgUoKDq2lJJuul1ZzuaJ1/Dk+lR3YZ6Wtz
ZwumCHnEmSMzWyOT4Rp2gEWEv1jbPbZl6XyY4wJG9n/OulqDbHy4+dj5ITb/r93J
/yLCBQKBgHa8XYMLzH63Ieh69VZF/7jO3d3lZ4LlMEYT0BF7synfe9q6x7s0ia9b
f6/QCkmOxPC868qhOMgSS48L+TMKmQNQSm9b9oy2ILlLA0KDsX5O/Foyiz1scwr7
nh6tZ+tVQCRvFviIEGkaXdEiBN4eTbcjfc5md/u9eA5N21Pzgd/G
-----END RSA PRIVATE KEY-----`

```python
from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as key_file:
    key = RSA.importKey(key_file.read())
    print(key)
```

결과값 : Private RSA key at 0x10622CE90

근데 문제를 보면 Extract the private key *d* as a decimal integer from this PEM-formatted RSA key.이런 말이 나온다

```
from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as key_file:
    key = RSA.importKey(key_file.read()).d
    print(key)
```

15682700288056331364787171045819973654991149949197959929860861228180021707316851924456205543665565810892674190059831330231436970914474774562714945620519144389785158908994181951348846017432506464163564960993784254153395406799101314760033445065193429592512349952020982932218524462341002102063435489318813316464511621736943938440710470694912336237680219746204595128959161800595216366237538296447335375818871952520026993102148328897083547184286493241191505953601668858941129790966909236941127851370202421135897091086763569884760099112291072056970636380417349019579768748054760104838790424708988260443926906673795975104689
```

```
from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as key_file:
    key = RSA.importKey(key_file.read())
    print(key)
```

결과값 : Private RSA key at 0x10622CE90

근데 문제를 보면 Extract the private key *d* as a decimal integer from this PEM-formatted RSA key.이런 말이 나온다

```
from Crypto.PublicKey import RSA

with open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r') as key_file:
    key = RSA.importKey(key_file.read()).d
    print(key)
```

```
15682700288056331364787171045819973654991149949197959929860861228180021707316851924456205543665565810892674190059831330231436970914474774562714945620519144389785158908994181951348846017432506464163564960993784254153395406799101314760033445065193429592512349952020982932218524462341002102063435489318813316464511621736943938440710470694912336237680219746204595128959161800595216366237538296447335375818871952520026993102148328897083547184286493241191505953601668858941129790966909236941127851370202421135897091086763569884760099112291072056970636380417349019579768748054760104838790424708988260443926906673795975104689
```