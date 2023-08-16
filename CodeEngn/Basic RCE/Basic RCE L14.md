> Name이 CodeEngn 일때 Serial을 구하시오  
> (이 문제는 정답이 여러개 나올 수 있는 문제이며 5개의 숫자로 되어있는 정답을 찾아야함, bruteforce 필요)  
> Ex) 11111
> ![1](https://github.com/king-raccoon/Yoom/assets/78426205/963d414d-d5c3-4ca8-9c40-60f4047eb33d)
> ![2](https://github.com/king-raccoon/Yoom/assets/78426205/8ee94c17-4efa-4080-bcf9-d8e9c667ba6a)
> ![3](https://github.com/king-raccoon/Yoom/assets/78426205/0973dbff-cfb2-4920-9592-7441572b8e6b)
> ![4](https://github.com/king-raccoon/Yoom/assets/78426205/e6c11e6b-8abc-4ccf-91bd-2428c235290b)
> ![5](https://github.com/king-raccoon/Yoom/assets/78426205/4a1fb7e5-bfe4-40a9-95ef-d6ef1137512b)
> OEP : 00401000

![6](https://github.com/king-raccoon/Yoom/assets/78426205/a430ff49-91a0-48fb-9c2d-7737884a1a75)
정답 문구 위를 좀 더 올라가보면 입력값을 받는 함수가 있는데 여기에 bp를 걸고 실행한다

![7](https://github.com/king-raccoon/Yoom/assets/78426205/bdd72cb3-2510-46c1-b014-4ecebd8c9f95)
디버깅 실행 후 아이디 : CodeEngn 비밀번호 : aaaaaaaa를 넣으면 다음처럼 아이디 비밀번호가 들어간다

![8](https://github.com/king-raccoon/Yoom/assets/78426205/b2bbe9b3-9794-4d9c-96b9-64f06ea80e07)
그 다음 비밀번호가 어떤 함수에 들어간 후 16진수값이 esi에 저장된다

## ![9](https://github.com/king-raccoon/Yoom/assets/78426205/28306eb3-5d61-4fa2-a9d1-e1da3c949176)

IDA 풀이
![10](https://github.com/king-raccoon/Yoom/assets/78426205/1813029d-1da8-4d68-9ceb-ea6648a07420)
이 사진 위에 있는 byte_403138을 보면 다음과 같다![Untitled](https://github.com/king-raccoon/Yoom/assets/78426205/27c4e13a-e2f2-4177-b83a-3bf8e5ff154d)
즉, 이 부분이 내가 입력한 password가 들어가는 곳임을 알 수 있다.

이후 sub_401383를 호출하고 반환값을 esi에 넣은 뒤 eax와 esi를 비교한다

esi는 내가 입력한 비밀번호이므로 eax가 CodeEngn의 비밀번호이다.

![11](https://github.com/king-raccoon/Yoom/assets/78426205/a0985158-9b6b-4a96-9b1f-604d3adf3bd6)
eax가 이상하게 나왔는데 초반에 숫자를 입력했으면 그 숫자를 16진수로 변환한 값이다.

⇒ ESI에 저장된 129A1은 십진수로 바꾸면 76193이 된다

`정답 : 76193`
![12](https://github.com/king-raccoon/Yoom/assets/78426205/93fbaec2-e2c9-4f1c-a291-76a7096a8f13)
