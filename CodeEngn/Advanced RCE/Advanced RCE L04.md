> Name이 CodeEngn 일때 Serial은 무엇인가

![2](https://github.com/king-raccoon/Yoom/assets/78426205/9e61552f-7991-4760-b89e-d4a0afc2ab75)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/ac71254d-3b41-41ca-ae3e-faf822a55a3a)
LoadPE로 pe 복구

![4](https://github.com/king-raccoon/Yoom/assets/78426205/3ddd82b6-6f08-4591-a953-347525f8691e)
![Untitled](https://github.com/king-raccoon/Yoom/assets/78426205/fb8c689b-0fc7-406f-a5d1-dd4c4fc77007)
F8을 눌러보면 저 구간에서 무한루프를 돌기 때문에 그 다음 줄에 bp를 걸고 F9

![5](https://github.com/king-raccoon/Yoom/assets/78426205/3eacd22a-2142-4f00-9c04-657cf496c901)
그러면 4011C3(맞나)에서 401006으로 이동

?가 있는걸 봐서 뭔가 잘못됐다. Crtl+A 눌러서 재정렬

![6](https://github.com/king-raccoon/Yoom/assets/78426205/ee35a5e6-18af-4b18-8d9b-406ff187e1cf)
![7](https://github.com/king-raccoon/Yoom/assets/78426205/46984e12-69ba-4b1a-9807-9b9b800f0196)
![8](https://github.com/king-raccoon/Yoom/assets/78426205/700615be-47b4-4863-a5ed-8bb536529b1f)
정답같은 문구가 있는 곳으로 이동해서 바로 위를 보면 String2랑 String1을 비교하는 것으로 봐서 3번 문제랑 유사하다

IstrcmpA에 bp를 건다
![9](https://github.com/king-raccoon/Yoom/assets/78426205/dfd7563d-b874-48dd-a4f3-b9ca05a62b53)
String2가 내가 입력한 시리얼 값, String1이 CodeEngn의 시리얼 값이다

`정답 : LOD-59919-A0024900`
