> 이 프로그램의 등록키는 무엇인가

<img width="341" alt="스크린샷 2023-01-31 오후 4 31 16" src="https://github.com/king-raccoon/Yoom/assets/78426205/a3fed4cd-d955-49a9-b49f-55a1f3bd19bd">
<img width="339" alt="스크린샷 2023-01-31 오후 4 31 41" src="https://github.com/king-raccoon/Yoom/assets/78426205/c9939ea3-b983-44c4-84cb-6b262f492790">
<img width="444" alt="스크린샷 2023-01-31 오후 4 34 41" src="https://github.com/king-raccoon/Yoom/assets/78426205/8b2d048a-eab6-4eb9-8630-5f615032ac31">
<img width="1512" alt="스크린샷 2023-01-31 오후 4 52 27" src="https://github.com/king-raccoon/Yoom/assets/78426205/28855dc1-2136-4f05-a52f-30be5c5a39a1">

맨 위에 함수가 UPX1에 의해 chunk됐다는데 인터넷에 따르면 뭐 코드가 분리됐다는 것 같다

<img width="1512" alt="스크린샷 2023-01-31 오후 4 54 30" src="https://github.com/king-raccoon/Yoom/assets/78426205/eb2cfead-c251-4cfd-b29c-a62bfd64813e">

윗 줄에 나와있는 위치로 가면 xchg 라는 inst.가 있다.

두 피연산자의 내용을 서로 교환한다.

```
XCHG	register,register
XCHG	register,memory
XCHG	memory,register
```

약간 swap 명령어 같다.

별로 의미없는 것 같아서 UPX1이 뭔지 찾아보니까 압축 형식 같다! 즉, 코드가 UPX1 형식으로 압축이 된 것 같다

[UPX0 과 UPX1의 차이점](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=qlfydehd&logNo=110084297544)

<img width="1512" alt="스크린샷 2023-01-31 오후 6 16 52" src="https://github.com/king-raccoon/Yoom/assets/78426205/b05f7fc9-aa34-4ee7-a8d5-ab9d3f8d42ef">

`register : Registered User
GFX-754-IER-954`
