> Name이 CodeEngn일때 Serial을 구하시오

![1](https://github.com/king-raccoon/Yoom/assets/78426205/5fadb3b8-39ea-40c6-8988-0fbf9aa220da)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/a3a3c4d0-d554-42f3-8b4b-9fb1089da125)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/2800c3a6-f475-41f1-9994-fd6a898ded68)
이름과 비밀번호를 입력 → 틀리면 null 파일 생성

![4](https://github.com/king-raccoon/Yoom/assets/78426205/6870c7d6-c597-42fa-bfd5-ea0e7a7eed8d)
문자열을 검색해서 Good Job!이 있는 곳으로 이동

![5](https://github.com/king-raccoon/Yoom/assets/78426205/51956df1-af2a-409d-b442-9e6e9c2e2a5c)
분기의 조건 cmp eax, [ebp+var_3C] 확인

![6](https://github.com/king-raccoon/Yoom/assets/78426205/ac94cd52-7aef-4f55-9acb-57c85b51926d)
분기문에다 bp 걸고 실행해서 이름에 CodeEngn, 비밀번호에 1234를 넣고 eax와 ebp 확인하면 eax 값이 4D2이여서 내가 입력한 비밀번호 1234가 eax에 들어감을 알 수 있다.

ebp+var_3C에 커서를 올려두면 해당 위치를 알 수 있다 ⇒ Stack[00003590]:0070FEEC

![7](https://github.com/king-raccoon/Yoom/assets/78426205/5517fb93-e70f-4bb2-a581-886763f5e37a)
stack 70feec를 확인하면 E4C60D97이 나온다

![8](https://github.com/king-raccoon/Yoom/assets/78426205/d3791ec9-d9bf-4d80-b22c-d59456afe824)

`비밀번호: 3838184855`
![9](https://github.com/king-raccoon/Yoom/assets/78426205/fa546aad-cc5b-4ff0-a8ba-cd1da3cabe74)
