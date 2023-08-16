> StolenByte를 구하시오 Ex) 75156A0068352040

[StolenByte](https://brainfreeee.tistory.com/35)

StolenByte란 훔친 바이트라는 뜻으로 패킹된 프로그램에서 코드의 일부를 OEP로 점프하기 이전에 숨기는 것
![1](https://github.com/king-raccoon/Yoom/assets/78426205/2822a987-827c-4c23-9d63-3b8bfe12927d)
[POPAD](https://8jz5.tistory.com/48)

PUSHAD는 범용 레지스터에 저장된 값들을 스택에 저장하는 명령어

upx 패킹 방법 : 패킹 전 프로그램은 패킹 전 레지스터 상태를 스택에 저장하고 패킹 후 popad로 레지스터 복구

![2](https://github.com/king-raccoon/Yoom/assets/78426205/d2896111-4486-4ed5-a840-ceeb1652816f)

따라서 POPAD 명령어를 찾으면 다음과 같은 위치가 나온다

디버거를 통해  POPAD명령을 검색해서 찾으면 이 부분 밖에 안 나온다
현재 필요로하는 부분이다.  POPAD 이후 PUSH를 통해 값을 현재 스택에 저장한다
따라서 이 코드들이 StolenByte다

`StolenByte : 6A0068002040006812204000`
