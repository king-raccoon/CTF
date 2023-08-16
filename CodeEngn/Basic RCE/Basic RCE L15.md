> Name이 CodeEngn일때 Serial을 구하시오

![1](https://github.com/king-raccoon/Yoom/assets/78426205/de6e73f8-b295-4837-a1b8-e0b4f0146ec5)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/43c8a530-b5a9-4b49-baa4-ae4ab430fc63)
패킹은 안 됐는데 Delphi라는걸로 작성됐다

![3](https://github.com/king-raccoon/Yoom/assets/78426205/d62363f5-5d74-44f3-a1c2-3ff29e7efbbf)
우선 문자열 검색해서 실패 시 나오는 “Try Again !” 근처로 가서 cmp 명령어에 bp를 걸었다

CodeEngn, 1234 입력하니까 eax에 4D2가 나오는데 이게 1234의 16진수이다

![4](https://github.com/king-raccoon/Yoom/assets/78426205/2fb6b4f1-129f-4351-b9ff-3a8cbe74b44c)
eax와 비교하는 값에는 6160h가 들어간다. 6160의 십진수는 24928이므로 비밀번호를 찾을 수 있다

`Name : CodeEngn`

`Serial : 24928`
![5](https://github.com/king-raccoon/Yoom/assets/78426205/284ad866-1514-4613-a4bf-7d7b26a7b479)
