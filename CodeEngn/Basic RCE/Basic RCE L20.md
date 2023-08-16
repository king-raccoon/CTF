> 이 프로그램은 Key파일을 필요로 하는 프로그램이다.
> 'Cracked by: CodeEngn!' 문구가 출력 되도록 하려면 crackme3.key 파일안의 데이터는 무엇이 되어야 하는가
> Ex) 41424344454647
> (정답이 여러개 있는 문제로 인증시 맞지 않다고 나올 경우 Contact로 연락주시면 확인 해드리겠습니다)

![1](https://github.com/king-raccoon/Yoom/assets/78426205/a0b41832-bca0-4e44-aac1-a26cf6837f67)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/4280a99d-e8f6-41ba-b00e-ae16f7100aa5)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/e9d7ca35-3f93-49cf-bb37-51a7891c32be)
![4](https://github.com/king-raccoon/Yoom/assets/78426205/c7f397e2-5a85-4e11-9c53-683a7fb3d661)
401037로 안 가면 바로 위에 있는 사진처럼 실행

![5](https://github.com/king-raccoon/Yoom/assets/78426205/872e5467-07b0-46a6-b0d6-79b8be3afe8d)
sub_401311로 가면 다음과 같음 → CrackMe v3.0 파일 내 문자열을 A~O까지 비교 ⇒ 파일 내 문자열을 잘 수정하면 결과가 CodeEngn! 나올 수 있다

![6](https://github.com/king-raccoon/Yoom/assets/78426205/49ed01c6-6a78-46c4-a536-1c8ba9f2c230)

```
//각 알파벳별로 암호화? 실행
#include <stdio.h>

char arr[] = "CodeEngn";
int bl = 0x41;
int x = 0;
int main()
{
    for(int i = 0; i < 9; i++){
        printf("%x ", arr[i]^bl);
        x+=arr[i];
        bl++;
    }
    printf("\n");
    printf("%x\n", x^0x12345678);
}
```

```
//결과
2 2d 27 21 0 28 20 26 49
1234557b
```
