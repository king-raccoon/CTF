> 컴퓨터 C 드라이브의 이름이 CodeEngn 일경우 시리얼이 생성될때 CodeEngn은 'ß어떤것'으로 변경되는가

[getVolumeInformation Function](https://devluna.blogspot.com/2015/01/c-windows-getvolumeinformation.html)

![Untitled](https://github.com/king-raccoon/Yoom/assets/78426205/155e8ee1-eff5-45fc-a527-cf18a18c73f0)
![₩](https://github.com/king-raccoon/Yoom/assets/78426205/05aa4b7d-b48f-485c-8dc2-79e2f415964f)
![1](https://github.com/king-raccoon/Yoom/assets/78426205/5637bb84-ebb4-40a2-89c7-92df40039400)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/f641e94d-3005-4399-beb5-a168059ab030)
정답 문자열 위로 좀만 올라가보면 GetVolumeInfomationA 라는 함수가 있다
![3](https://github.com/king-raccoon/Yoom/assets/78426205/5e59d111-026c-41ab-aa1f-a11d9e39d22d)
메세지 박스에 시리얼로 aaaaaaaa를 넣고 그 위치를 확인한다
![4](https://github.com/king-raccoon/Yoom/assets/78426205/27abe453-948e-46c8-b54d-55b1e5cf1412)
![5](https://github.com/king-raccoon/Yoom/assets/78426205/403f3e8e-6958-4034-b8f7-424b94af9d0e)
헥스 덤프를 보면 버퍼의 주소가 402324
![6](https://github.com/king-raccoon/Yoom/assets/78426205/a8ff83ff-5923-493e-80bf-0035ceff8b22)
여기서 보면 40225C에 4562가 들어가고 for문을 돌면서 다음과 같이 변함을 알 수 있다.
4562

5562

5662

5672

5673

6673

6773

6783

6784

즉, 각 자리에 +2를 해준 값이 나오고 그 값을 L2C-5781과 합치고 -ABEX와 합쳐서 L2C-57816784-ABEX라는 시리얼 값이 나온다

이때 40225C에 들어간 값은 GetVolumeInformationA라는 함수의 리턴값으로 이 함수는 드라이브의 이름이다.

즉, 문제가 원하는 답은 40225C의 리턴값이 CodeEngn이고 이를 맨 앞 4자리의 각 자리에 2를 더한 값을 구하라는 것이다.
`답 : EqfgEngn`
