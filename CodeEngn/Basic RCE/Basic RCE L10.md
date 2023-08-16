> OEP를 구한 후 '등록성공' 으로 가는 분기점의 OPCODE를 구하시오.
> 정답인증은 OEP + OPCODE
> EX) 00400000EB03

![1](https://github.com/king-raccoon/Yoom/assets/78426205/7bf7c497-c194-4345-854d-21f993b286bc)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/afdc6e99-c30e-4fae-8a03-efb5298c3dff)
이번에는 Aspack이라는 패킹이 되어있다

![3](https://github.com/king-raccoon/Yoom/assets/78426205/5c9e4485-e3fb-42e9-8443-60e8e42663b9)
우선 얘도 upack 문제니까 pushad에서 f8을 눌러보면 esp, 즉 현재 스텍포인트가 19FF54인걸 알 수 있다.

![4](https://github.com/king-raccoon/Yoom/assets/78426205/c6772ee1-645f-4eb3-9364-f7360ad0418e)
![5](https://github.com/king-raccoon/Yoom/assets/78426205/f314b797-55a6-4ce9-a537-8adbdfc4cd15)
그 후 덤프로 ESP 위치를 간 다음 해당 4바이트를 하드웨어 브레이크 포인트를 걸어 실행한다.

![6](https://github.com/king-raccoon/Yoom/assets/78426205/4f469af1-8dc6-4f5f-8864-a3130be99557)
그럼 다음과 같이 popad의 다음줄이 되는 걸 볼 수 있다

그걸 따라가면 445834가 나온다

OEP : 00445834

![7](https://github.com/king-raccoon/Yoom/assets/78426205/a621c3fa-bcac-4af1-b78b-70ab95b8fb26)
그후 OllyDump를 설치하고 다음과 같이 실행시킨 후 Rebuild Import를 해제하고 Dump를 눌러 새로운 파일로 저장한다

![8](https://github.com/king-raccoon/Yoom/assets/78426205/3aad251f-8ba1-4b75-90a5-052b46c7babc)
이렇게 해서 Exeinfo PE로 파일을 확인해보면 Not Packed라고 나온다

![9](https://github.com/king-raccoon/Yoom/assets/78426205/8a69dcd2-5ead-48f6-b748-023d300a231f)
이걸 다시 올리디버거로 돌릴려고 하면 import address table이 손상됐다는 에러가 나온다. 이걸 해결하기 위해 LoadPE를 깔고 Rebuild PE를 한다.

![10](https://github.com/king-raccoon/Yoom/assets/78426205/bc66b038-b6f2-423e-81e4-0ee9124d1399)
이제는 문자열이 복구가 됐기 때문에 Register…well done!으로 간다

![11](https://github.com/king-raccoon/Yoom/assets/78426205/4a54b5e1-e9e1-43c5-b014-aba5fcb3e926)
그러면 해당 문자열이 나올 수 있는 분기문이 나온다.

OPCODE : 7555

`정답 : 004458347555`
