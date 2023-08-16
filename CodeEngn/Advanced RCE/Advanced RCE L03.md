> Name이 CodeEngn 일때 Serial은 무엇인가

![1](https://github.com/king-raccoon/Yoom/assets/78426205/eed83beb-e80c-4018-9510-bc6bb02af7c8)

![2](https://github.com/king-raccoon/Yoom/assets/78426205/ea05e63d-7056-40f9-9921-2b88c167079e)
실행이 안되서 그냥 문자열 검색해서 찾아봤다

![3](https://github.com/king-raccoon/Yoom/assets/78426205/43015bdc-e73a-4b72-8c7e-ca2b0ace60f6)
해당 분기 맨 위에 bp를 걸고 실행해보니까 String1과 String2가 주어지고 이를 비교하는 istrcmpA 함수를 돌린다.

push offset String2

push offset String1

명령어를 돌리면 Stack에 .data String1 .data String2가 쌓이고 그 곳의 hex view를 보면 String1이 내가 입력한 문자열, String2가 CodeEngn에 해당되는 시리얼이다

`정답 : 3265754874`
