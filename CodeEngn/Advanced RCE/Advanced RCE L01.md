> 이 프로그램은 몇 밀리세컨드 후에 종료 되는가.
> 정답인증은 MD5 해쉬값(대문자) 변환 후 인증하시오

![1](https://github.com/king-raccoon/Yoom/assets/78426205/fcf5f156-f111-4e40-aaad-e6f3a5c14a22)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/ec5143d1-5220-491d-8fbc-d00cd2ff3371)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/e5acc1e2-c737-45e6-bbe0-006865835866)
아이다에서 실행시키면 저런 경고창이 뜨는데 이전 문제들 중 저런게 뜨는 문제가 있었다. IsDebuggerPresent라는 안티 디버깅이 돌아가고 있다.

![4](https://github.com/king-raccoon/Yoom/assets/78426205/524a7117-c58d-41b6-aa76-f700d28ce633)
IsDebiggerPresent 함수 실행 후 리턴값 eax를 이용하여 test eax, eax하고 결과값을 기준으로 분기를 진행한다.

> test 명령어 : 두 개 인자를 and 연산 실행. 주로 해당값의 true, false를 판별 시 사용

![5](https://github.com/king-raccoon/Yoom/assets/78426205/c7565433-546f-4275-81ea-6634d71bdc97)
정말 if문에서 true 즉, 1(jnz)일때 Autolt로 컴파일됐다는 메세지 박스가 출력된다.

jnz loc_4338F7을 jz loc_4338F7로 패치한다.

![6](https://github.com/king-raccoon/Yoom/assets/78426205/5d700983-6443-42d1-8341-4d74f84cae06)
time을 검색해서 관련 함수를 찾았더니 timeGetTime, KillTimer, SetTimer 3개의 함수가 존재한다.

```//timeGetTime 함수
//윈도우(운영체제)가 시작되어서 지금까지 흐른 시간을 1/1000 초 (milliseconds) 단위로 DWORD형을 리턴하는 함수다.
```

```
//SetTimer(타이머번호, 설정된 시간간격, 타이머 메시지가 발생되었을때 실행되는 함수
UINT_PTR SetTimer(
  [in, optional] HWND      hWnd,
  [in]           UINT_PTR  nIDEvent,
  [in]           UINT      uElapse,
  [in, optional] TIMERPROC lpTimerFunc
);
```

```
BOOL KillTimer(
  [in, optional] HWND     hWnd,
  [in]           UINT_PTR uIDEvent
);
//타이머를 생성할 때는 SetTimer 함수를 이용하고 해제할 때는 KillTimer를 사용합니다.
```

**SetTimer 확인**
![7](https://github.com/king-raccoon/Yoom/assets/78426205/9dcf4023-2f09-4fce-b2ca-239ca541d060)
인자값이 0x2ee이므로 750밀리세컨드인데 MD5 uppercase로 바꾸면 B137FDD1F79D56C7EDF3365FEA7520F2 이지만 틀렸다.

**timeGetTime 확인**

하나하나 찾아보다가 sleep이라는 함수가 있고 timeGetTime이 두 번 호출되어 그 값들의 차와 어떤 값을 비교하는 것이 나온다
![8](https://github.com/king-raccoon/Yoom/assets/78426205/84d0d8a0-2f49-4e5e-bb93-066611522cfc)
![9](https://github.com/king-raccoon/Yoom/assets/78426205/71c9fa47-163c-47c7-80d8-447ce81451c6)
eax : 34ba, ebx+4 : 0x337b

이 두값이 작거나 같으면 메세지 박스가 실행된다

즉, 이 프로그램음 0x337b(13179) 밀리세컨드에 종료된다

13179를 MD5 실행하면 DB59260CCE0B871C7B2BB780EEE305DB 이다.

```
//Sleep 함수 : 프로그램을 일정시간 작업을 대기시킬때 사용
Sleep(millisecond);
```

`정답: DB59260CCE0B871C7B2BB780EEE305DB`
