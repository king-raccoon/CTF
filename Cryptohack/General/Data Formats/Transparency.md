> Attached is an RSA public key in PEM format. Find the subdomain of cryptohack.org which uses these parameters in its TLS certificate, and visit that subdomain to obtain the flag.
> 

`---BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuYj06m5q4M8SsEQwKX+5
NPs2lyB2k7geZw4rP68eUZmqODeqxDjv5mlLY2nz/RJsPdks4J+y5t96KAyo3S5g
mDqEOMG7JgoJ9KU+4HPQFzP9C8Gy+hisChdo9eF6UeWGTioazFDIdRUK+gZm81c1
iPEhOBIYu3Cau32LRtv+L9vzqre0Ollf7oeHqcbcMBIKL6MpsJMG+neJPnICI36B
ZZEMu6v6f8zIKuB7VUHAbDdQ6tsBzLpXz7XPBUeKPa1Fk8d22EI99peHwWt0RuJP
0QsJnsa4oj6C6lE+c5+vVHa6jVsZkpl2PuXZ05a69xORZ4oq+nwzK8O/St1hbNBX
sQIDAQAB
-----END PUBLIC KEY-----`

서브 도메인 컴네때 들었는데 뭐더라

우선 위의 PEM 코드를 통해 얻은 공개키는 다음과 같다

Public RSA key at 0x1024BC890

```
23421622285641341405633616890150413771071492791662619237015532689271209254675255214187772835143801809039951016782376679973376782695533167272817148034946155291022588458116896449130547957859630601417029406537713697722216484126508404669492574651738700785323627803802967097814192155713988206765677255996453746570221203605464683698139759068201745805643226602309648177720842369737425307662674524530757570626970232537549824005998393609021861773134215542450556839250804799098903483152012713520167414613141526302727512388972623173809195225592109964416682348203058784103484962051844890398766510080562420295832329553237528041393
```

근데 이걸로는 뭘 할 수 없을 것 같아서 서브도메인을 알아보다가 이런걸 발견했다

[Subdomain finder](https://subdomainfinder.c99.nl/scans/2020-09-10/cryptohack.org)

<img width="637" alt="스크린샷 2023-09-27 오후 1 49 28 (1)" src="https://github.com/king-raccoon/king-raccoon/assets/78426205/55421713-98e5-4d14-802d-e5e19fbec652">

4번째에 transparencyflagishere이라고 떡하니 나와있다

`crypto{thx_redpwn_for_inspiration}`