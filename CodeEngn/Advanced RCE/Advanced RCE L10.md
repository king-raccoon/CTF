> Serial이 WWWCCCJJJRRR 일때 Name은 무엇인가
> <br>Hint 1 : 4글자임
> <br>Hint 2 : 정답으로 나올 수 있는 문자열 중 (0~9, a~z, A~Z) 순서상 가장 먼저 오는 문자열

![1](https://github.com/king-raccoon/Yoom/assets/78426205/d3860b8e-e63f-4d56-bdec-9cba0ab3497c)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/b9309131-d468-421f-991d-fb8c4ca8526c)
성공문 윗줄이 je 분기문으로 같으면 실패문으로 간다. 분기문 조건은 ebp-a5가 0이 되면 실패문으로 간다

![3](https://github.com/king-raccoon/Yoom/assets/78426205/10dc958f-0050-4319-a882-73bbf825a854)
근데 위에 뭔가 ebp- … 이런 느낌이라 좀 올려보니까 ebp-a5에 al값을 넣는 명령어가 있다

윗줄 함수에 bp걸고 확인해보자

![4](https://github.com/king-raccoon/Yoom/assets/78426205/a9cf039b-0bc9-4a69-883f-316b46e8174f)
리턴값이 eax에 저장되고 eax에는 ebp-c4가 저장된다

![5](https://github.com/king-raccoon/Yoom/assets/78426205/4aa4fc75-164c-40fa-80f4-7e4fc107edcf)
ebp-c4 ← edx ← ebp-10c ← eax ← ebp -69 ← 0

![6](https://github.com/king-raccoon/Yoom/assets/78426205/64ea35df-4ac0-4821-a936-1d0f61e7b0af)
이 부분이 eax가 5보다 작거나 같으면 401b65로 아니면 61로 가는데 즉, eax가 5보다 커지면 ebp-69를 0으로 바꾼다.

![7](https://github.com/king-raccoon/Yoom/assets/78426205/b9a3d801-7b91-4a9e-b3ac-4148a92d0a67)
더럽지만 내가 잘 알아보기 위해 bp를 걸었는데 eax는 eax-edx이고, eax = ebp-78, edx=ebp-7c이다

근데 생각해보면 위에서 ebp-a5가 0이 되면 안되고, ebp-a5에는 al, 즉 지금 보고있는 함수의 리턴값 eax가 들어가기 때문에 eax는 5보다 작거나 같아야한다

![8](https://github.com/king-raccoon/Yoom/assets/78426205/efe1966c-440c-4329-bcf5-9749ff23c439)
ebp-78 = 00000030

![9](https://github.com/king-raccoon/Yoom/assets/78426205/8358a4ec-5346-4ae6-b0db-338ecd0b276a)
ebp-7c = 00000025

eax = 00000005

근데 도저히 모르겠고 눈 앞아서 아이다로 디컴파일 돌릴거다.

![10](https://github.com/king-raccoon/Yoom/assets/78426205/a1118130-84a0-4ef7-8f1f-6ff423c68183)
![11](https://github.com/king-raccoon/Yoom/assets/78426205/cceae3e1-00c9-416e-9643-a9dc612838ad)
![12](https://github.com/king-raccoon/Yoom/assets/78426205/2d523878-06e9-443d-86e8-326072cf0b8c)
v20이 1이ㅕㅑ하는데 v20은 check_serial함수 결과값에 의존하고 그 반환값은 v23이다. v23은 1이 나와야하는데 Second-v19가 5보다 커야한다.

v19는 stringFindSecond 함수의 결과값이다

stringFindSecond의 첫번째 인자는 v25인데 string의 이상한 문구다

![13](https://github.com/king-raccoon/Yoom/assets/78426205/c1367a9e-48d8-4693-98ab-05367fb10de1)
AJXGRFV6BKOW3Y9TM4S2ZU I70H5Q81PDECLNAJXGRFV6BKOW3Y9TM4S2ZU I70H5Q81PDECLNAJXGRFV6BKOW3Y9TM4S2ZU I70H5Q81PDECLN

그냥 실행해서 보니까 시리얼 WWWCCCJJJRRR는 결국 WCJR을 3번씩 쓴거고, 이걸 저 이상한 문구랑 비교한다. 이때 힌트에서 가장 먼저 나온거라니까 한 단락당 인덱스 차이가 가장 작은 문자들을 조합하면 네임이 될 것이다.

`name : 31A6`
