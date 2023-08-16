<https://dreamhack.io/wargame/challenges/49>

![스크린샷_2023-01-10_오후_2 36 05](https://github.com/king-raccoon/write-up/assets/78426205/c2576d5a-0d3d-4bee-b686-31ddd4ab34dd)
파일을 다운받고 실행하면 다음과 같은 킹받는 화면이 나온다

patch는 WinAPI로 만들어진 GUI이기 때문에 WinMain을 찾아야한다

**Reference**
<https://learn.microsoft.com/en-us/windows/win32/api/>
<https://junk-s.tistory.com/48>

![스크린샷_2023-01-10_오후_2 40 52](https://github.com/king-raccoon/write-up/assets/78426205/55dea244-cf59-4fcd-b3ee-f38e10b54024)
디컴파일하면 다음과 같은 코드가 나온다

위 링크들을 통해 RegisterClassExW(&v11)이 윈도우 클래스를 등록하여 윈도우를 생성함을 알 수 있다

또한 v11.lpfnWndProc = (WNDPROC)sub_1400032F0;를 통해 콜벡함수 포인터를 저장하기 때문에 sub_1400032F0가 콜벡함수임을 알 수 있다

![스크린샷_2023-01-10_오후_2 50 53](https://github.com/king-raccoon/write-up/assets/78426205/d83bbd16-6e7d-4598-98df-2317b3923ada)
sub_1400032F0는 input값 a2에 의해 switch문이 실행됨을 알 수 있다

그 중 0xFu에서 DH={ 에 값을 지우는 역할을 한다

28번째 줄에 있는 함수가 paint와 관련된 flag이다

![스크린샷_2023-01-10_오후_2 54 57](https://github.com/king-raccoon/write-up/assets/78426205/917015fe-eee9-4784-8734-6f46a80da974)
_sub_140002C40_

51~75번째 줄까지는 sub_140002B80를 호출하고 이후는 각각 다른 함수들을 호출합니다.

![스크린샷_2023-01-10_오후_2 57 04](https://github.com/king-raccoon/write-up/assets/78426205/f75f2eeb-62b0-4568-a0d6-cd172475def8)
_sub_140002B80_

여기서 펜을 부르고 선을 긋는다는 걸 알 수 있다

![스크린샷_2023-01-10_오후_2 58 38](https://github.com/king-raccoon/write-up/assets/78426205/870009c8-2f9b-4563-a20f-0054e873da08)
_sub_140002B80 이후 함수 sub_1400017A0_

그 이후 함수 sub_1400017A0에서는 펜을 여러번 사용한다.

![스크린샷_2023-01-10_오후_3 31 16](https://github.com/king-raccoon/write-up/assets/78426205/1eb59b92-bed0-4b0e-bd3c-7fc79308ff83)
처음 함수에 bp를 걸고 run하면 위의 사진처럼 선이 없는 백지가 나온다.

여기서 F8을 누르면 선이 하나 그러짐을 알 수 있다. 즉, 답을 알기 위해선 선을 긋지 않게 하는 패치가 필요하다

![스크린샷_2023-01-10_오후_3 44 07](https://github.com/king-raccoon/write-up/assets/78426205/576e435a-68c3-4a07-b53c-253abc9a0983)
어셈블 패치를 이용하여 ret로 변경하면 위처럼 retn으로 바뀐다

패치를 실제로 적용시키기 위해 edit->patch program->apply pathces to input file...를 누르고 아무것도 변경 안한 상태로 ok를 누른다

변경된 파일을 실행하면 된다

![9594852623056bf46d27850a2f921b61a6414e8519d292f7b432e6667a07b35f](https://github.com/king-raccoon/write-up/assets/78426205/a6c64850-cd28-4a90-82fe-8a75bf722f38)

`답: UPATCHED`
