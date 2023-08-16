> 남은 군생활은 몇일 인가  
> 정답인증은 MD5 해쉬값(대문자) 변환 후 인증하시오

![1](https://github.com/king-raccoon/Yoom/assets/78426205/f3521fc0-2d45-494e-bb80-50ae874f2f77)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/e4c50a72-cf3b-446c-9d58-eeb6b98f5716)
확인을 누르면 숫자가 계속 증가한다

![3](https://github.com/king-raccoon/Yoom/assets/78426205/12dac2eb-af1b-49ca-a52c-4ab36900a696)
![4](https://github.com/king-raccoon/Yoom/assets/78426205/225accd6-9e00-4939-8be8-c455e6c5084f)
디버거 탐지를 한다

![5](https://github.com/king-raccoon/Yoom/assets/78426205/b39d2bbb-d800-4dae-924d-9edda0ac6e1a)
IsDebuggerPresent 함수를 찾아서 bp를 걸면 실행 후 처음에 걸리는 곳이 윗 사진이고 그 밑에 test eax, eax하고 jnz 실행문이 있다.

jnz는 0이 아닐때 점프하므로 리턴값을 0으로 바꾸면 될 것 같다

> test 명령어는 op1과 op2를 and 연산하여 연산값이 0이면 zf가 1
> <br>cmp 명령어는 dest와 src을 빼고 그 값을 사용
> <br>⇒ test는 op1과 op2가 0인지 확인할때 사용
> <br>cmp는 dest와 src가 동일한지 판단할때 사용

test를 cmp로 바꾼다

![6](https://github.com/king-raccoon/Yoom/assets/78426205/0fe1176a-1854-46d8-9b42-c0f214e1a8f0)
메세지박스마다 bp걸고 보니까 너무 길다

근데 검색해보니까 Exe2Aut 다운 받고 패치된 파일 실행하면
![7](https://github.com/king-raccoon/Yoom/assets/78426205/cb146721-708b-48e4-acce-8c9f691d6da0)
다음과 같다

790일 남았다

790을 MD5 해쉬 제너레이터에 돌리면 답이 나온다

`답 : 2dace78f80bc92e6d7493423d729448e`

> > 참고
> > <br>Exe2Aut 프로그램은 무엇인가
> > <br>exe file → aut file
> > <br>aut file : 오토잇. MS 윈도우를 위한 프리웨어 자동화 언어
> > <br>이때 자동화란 사람이 프로그램을 테스트할 것을 대신해주는 것(ex. 타이핑하기, 마우스 제어하기, 이벤트 테스트 하기 등) ⇒ 아마 여기서 실행파일을 오토잇으로 바꾸는 이유는 790번의 무지성 반복을 오토잇으로 간편하게 하기 위해선가..?
