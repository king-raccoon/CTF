<https://dreamhack.io/wargame/challenges/14>

파일 내 string들을 검색하니까 Wrong과 Correct가 있으니 Correct에 암호문이 있다는 것을 알 수 있다.
![shot1](https://github.com/king-raccoon/write-up/assets/78426205/d81ca41e-c81b-4856-92de-1165d561c626)

Correct로 들어가 다음과 같은 상황에서 상호참조를 확인하면 Correct가 main 안에 있음을 알 수 있다.
![shot2](https://github.com/king-raccoon/write-up/assets/78426205/32ce6944-38d9-40ce-a5a3-77e1e9dd46ac)
<img width="464" alt="shot3" src="https://github.com/king-raccoon/write-up/assets/78426205/cdc02f10-df4c-4f77-a592-821f0e995daf">

이를 디컴파일하여 C코드로 된 pseudo code를 얻은 후 정적분석하면 된다.
![shot4](https://github.com/king-raccoon/write-up/assets/78426205/858c663c-9bb8-4956-876f-031ceb992060)

Input을 받는 함수 sub*140001190은 printf, 그 밑 줄의 함수 sub_1400011F0는 암호를 입력받는 scanf임을 알 수 있다.
scanf 밑에 if문이 있고 그 조건이 맞으면 Correct를 출력하는 걸 보면 if문 조건이 암호임을 알 수 있다.
![스크린샷\_2023-01-10*오후\_1 26 16](https://github.com/king-raccoon/write-up/assets/78426205/9fb01953-a3c6-49ec-8cf6-a9c2a9c140b1)

a1은 우리가 scanf를 통해 입력한 문자열이고 이와 비교되는 것이 Compar3_the_str1ng이기 때문에 Compar3_the_str1ng가 암호이다.

`정답 : Compar3_the_str1ng`
