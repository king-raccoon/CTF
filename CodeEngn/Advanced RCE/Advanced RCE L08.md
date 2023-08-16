> Key 값이 5D88-53B4-52A87D27-1D0D-5B09 일때 Name은 무엇인가
> <br>힌트 : Name은 두자리인데.. 알파벳일수도 있고 숫자일수도 있고..
> <br>정답인증은 Name의 MD5 해쉬값(대문자)

![1](https://github.com/king-raccoon/Yoom/assets/78426205/882566be-767e-4dec-af81-a5957218e6c3)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/cfd4e1f8-e23f-4c72-8cfa-8e545a87784e)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/a0471ab8-b250-4aea-b90e-73e4de396c11)
![4](https://github.com/king-raccoon/Yoom/assets/78426205/b8e87a65-878f-43fe-8a9f-45ffc120829e)
첫번째 반복문의 edx 상위 4개가 입력받은 name을 통해 만들어진 상위 4자리 key이므로 00~zz까지 5D88이 나오는 문자 두개 조합을 찾자

![5](https://github.com/king-raccoon/Yoom/assets/78426205/270ae880-b651-4ddd-9b2d-978ddb21a882)

```
def solution(name, edx):
    esi = edx + name
    esi = esi * 0x772
    edx = esi
    edx = edx * esi
    esi += edx
    esi *= 0x474
    esi += esi
    edx = esi
    return edx

if __name__ == '__main__' :
    for i in range(0x30, 0x7a):
        edxFirst = solution(i, 0)
        for j in range(0x30, 0x7a):
            serial = solution(j, edxFirst)

            length = len(hex(serial))

            if '5d88' == hex(serial)[length - 8 : length - 4]:
                print(chr(i) + chr(j))
                break
```

<img width="348" alt="6" src="https://github.com/king-raccoon/Yoom/assets/78426205/ca62ca79-4f79-436d-b9fd-b8010c889de1">

name : C6<br>
`정답 : 7e8b9f5cab4a8fe24fad9fe4b7452702`
