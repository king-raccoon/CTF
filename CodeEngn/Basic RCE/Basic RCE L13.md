> 정답은 무엇인가

![1](https://github.com/king-raccoon/Yoom/assets/78426205/0715b9a4-2c98-4a6d-b733-2869b08a9a63)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/3d0b3994-4a08-4dda-9d1e-29e21c9bf30b)

올리디버거에 작동이 안되서 확인해보니 이상한거다

찾아보니 Basic.NET은 무슨 객체지향언어인 것 같다

C# .NET 프로그램의 특징은 아래와 같다.

- 관리 기반 코드이다. ( = java JVM처럼 중간언어로 컴파일 되는데, MSIL 이란 언어로 컴파일 된다. )
- 디컴파일이 매우 쉽게 된다.
- 난독화 솔루션 존재하지만, 완벽하진 않더라도 복원해주는 솔루션도 존재한다.

대표적인 디컴파일러는 아래와 같다.

- .NET Reflector
- JetBrains dotpeek(https://www.jetbrains.com/decompiler/)

[ref](https://sean.tistory.com/280)

결국 JetBrains dotpeek을 다운받았는데 뭔가 점점 다운받는 것만 느는 기분이다

![3](https://github.com/king-raccoon/Yoom/assets/78426205/3d2669fa-22a2-4278-bf88-08ae43ccd52e)
뭔가 눌러보다가 Main을 찾았다

분기문 조건은 str과 같냐이기 때문에 str이 키값이다.

이때 RijndaelSimple.Encrypt(변수들)이므로 RijndaelSimple라는 클래스의 맴버함수 Encrypt를 사용하는 것같다

![4](https://github.com/king-raccoon/Yoom/assets/78426205/4f3745ea-f5ca-464c-b65e-af16c06ce923)
이걸 export하여 vscode로 열고 test 파일에 str을 출력하는 명령어를 추가한ㄷ

![5](https://github.com/king-raccoon/Yoom/assets/78426205/aed95494-aa42-461d-a618-882dd81e0df8)
그 다음 터미널에 **dotnet new console --force** 을 입력하고 dotnet run을 한다(C#.net 실행 명령어)

![6](https://github.com/king-raccoon/Yoom/assets/78426205/60b90d98-821a-4e0a-9b23-c8df762fead8)

`비밀번호 : Leteminman`
