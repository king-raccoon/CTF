> Password는 무엇인가

![1](https://github.com/king-raccoon/Yoom/assets/78426205/80503320-3638-4c03-90b1-c6fd5c06fc44)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/65f37e30-e4bd-4b38-bfd0-4274c95b7d14)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/408f6d2e-a69f-482b-be14-2d8a41c273e1)
![4](https://github.com/king-raccoon/Yoom/assets/78426205/bff7afe1-3f95-4cc5-845a-4fbd21d0a683)
00CB12AD에서 JE 분기문 실행 후 같으면 “Sorry …” 실패문으로 가기 때문에 저기에 bp를 걸었다

![5](https://github.com/king-raccoon/Yoom/assets/78426205/3f968138-4505-441b-920d-ac1e306d13b4)
해당 조건문으로 오는 조건문도 존재하는지 화살표가 있어서 Test BL, BL을 확인하면 Jump from 00CB1097 이라고 나온다

![6](https://github.com/king-raccoon/Yoom/assets/78426205/4a3c27d4-2b8f-40b4-8128-48a8866d9700)
거기에서 좀 더 올라가면 DonaldDuck과 내가 입력한 1234를 비교한걸 봐선 도날드덕이 유저네임니다.

![7](https://github.com/king-raccoon/Yoom/assets/78426205/1e2fc659-bfd6-4c79-b094-abdaf88d0e0d)
![8](https://github.com/king-raccoon/Yoom/assets/78426205/aa7a418b-eed8-4d6f-93bf-fb09fe1af968)
?

감이 안 잡혀서 유저네임과 비밀번호를 묻는 곳으로 가봤다

![9](https://github.com/king-raccoon/Yoom/assets/78426205/7c1a3739-a93c-4db4-8b0c-1f4650878999)
그럼 이렇게 뭔가 돌아가는데 캡쳐를 못 했지만 몇 번 시행착오로 저 bp건 함수가 좀 중요했다

![10](https://github.com/king-raccoon/Yoom/assets/78426205/6fb72194-c8de-4b88-9f48-70dbda473bd5)
함수 입구에 bp걸고 돌려보면 밑에 bp건 곳 바로 윗줄이 sete bl이다. bl을 0으로 세팅하는건데 위에 캡쳐한 사진보면 je 분기문 윗줄이 test bl, bl이다. 즉, 여기가 중요해보인다

![11](https://github.com/king-raccoon/Yoom/assets/78426205/6bfe48f6-ca57-475a-94b2-1f37dde7251e)
DS:[00DD02A0]=0088228F
EAX=000004D2

진짜 eax에는 내가 입력한 1234의 16진수값이, ecx에는 0088228F, 10진수로 8921743가 들어간다.

![12](https://github.com/king-raccoon/Yoom/assets/78426205/09174f6b-c381-4435-b3da-fad67e4564e1)
근데 킹받게 틀린다고 나온다 왜

![13](https://github.com/king-raccoon/Yoom/assets/78426205/6f2a4bd4-417e-4b7f-a8bb-8d211c7f1bce)
구글링 결과 bl을 0으로 설정했고 je 분기문을 사용하기 때문에 답정너 수준으로 틀렸다고 나온다고 한다.

![14](https://github.com/king-raccoon/Yoom/assets/78426205/cf16c9d7-067c-4a56-b10f-9ab8ccf08bd3)
je를 jne로 패치하면 된다
