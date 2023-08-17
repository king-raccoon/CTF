> Unpack을 한 후 Serial을 찾으시오 정답인증은 OEP + Serial  
>  Ex) 00400000PASSWORD

<img width="282" alt="스크린샷 2023-02-07 오전 9 23 30" src="https://github.com/king-raccoon/Yoom/assets/78426205/9f9f6b41-5a78-41b9-9446-f3104a7d51ac">
<img width="292" alt="스크린샷 2023-02-07 오전 9 23 56" src="https://github.com/king-raccoon/Yoom/assets/78426205/362cf916-7c96-495b-8e17-853a09f861ec">
이렇게 뜬다

![Untitled](https://github.com/king-raccoon/Yoom/assets/78426205/03c7b44d-3e4d-445c-8378-0bb91850642a)
올리디버거로 열면 문제대로 unpack을 해야하는 것 같다

![1](https://github.com/king-raccoon/Yoom/assets/78426205/51de7c47-bf5a-4228-8bd2-87dceb32162e)
Exeinfo pe로 파일을 확인했더니 upx로 압축이 되어있다.
![2](https://github.com/king-raccoon/Yoom/assets/78426205/d3ae8799-7a35-4185-bf34-907c1135c5ab)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/77812274-a8fb-45f6-b650-64eac39c07fb)
![4](https://github.com/king-raccoon/Yoom/assets/78426205/c81c3062-1e1d-4034-a39d-dd33ba09bd8b)
![5](https://github.com/king-raccoon/Yoom/assets/78426205/388ece79-f866-4343-8c61-31e6b67d367a)

serial key : AD46DFS547

정답은 OEP+password였는데 OEP = Original Entry Point로 패킹된 파일의 실제 프로그램 시작 부분이다.

프로그램 시작점이 여기이기 때문에 OEP = 00401360

`정답 : 00401360AD46DFS547`
