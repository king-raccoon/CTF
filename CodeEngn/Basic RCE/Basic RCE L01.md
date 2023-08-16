<https://ch.codeengn.com/>

> HDD를 CD-Rom으로 인식시키기 위해서는 GetDriveTypeA의 리턴값이 무엇이 되어야 하는가

 <img width="239" alt="Untitled" src="https://github.com/king-raccoon/Yoom/assets/78426205/1b48a5e2-4f4b-460f-b58f-67735f6f69b4">
<img width="216" alt="스크린샷 2023-01-31 오전 9 16 46" src="https://github.com/king-raccoon/Yoom/assets/78426205/ebf0eb22-bbf0-43d0-ad3f-e017027fdbc4">

CD-ROM로 인식을 시켜야한다
<img width="1512" alt="스크린샷 2023-01-31 오전 10 13 51" src="https://github.com/king-raccoon/Yoom/assets/78426205/296561ea-45a1-4221-9951-212a1c04e034">
메세지 박스가 열리고 esi와 eax를 비교해서 같다면 정답 메세지 박스로 점프한다.

edit→patch program→assemble → 수정 → apply pathces to input file(패치한 파일 저장)

⇒00401026에서 jz를 jmp로 패치
<img width="283" alt="스크린샷 2023-01-31 오전 10 28 51" src="https://github.com/king-raccoon/Yoom/assets/78426205/0a9e822a-2d4b-4363-9c1a-4212dc8b5b69">
