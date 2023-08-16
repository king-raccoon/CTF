> Key 값이 BEDA-2F56-BC4F4368-8A71-870B 일때 Name은 무엇인가

> 힌트 : Name은 한자리인데.. 알파벳일수도 있고 숫자일수도 있고..

> 정답인증은 Name의 MD5 해쉬값(대문자)

![1](https://github.com/king-raccoon/Yoom/assets/78426205/871e36ba-ef84-4436-a5a6-9fdcd5af0be9)
name : a, key : BEDA-2F56-BC4F4368-8A71-870B 입력했을 때 나오는 창

![2](https://github.com/king-raccoon/Yoom/assets/78426205/5d7f8938-4231-49ea-b28c-d8d142559264)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/b6451fca-0137-42d4-b6ae-b9177cacf8da)
eax와 edx 비교

![4](https://github.com/king-raccoon/Yoom/assets/78426205/3ccc3d85-c8db-4a7f-8c32-99cd12a2f68c)
eax에 저장된 값의 헥스값에 key가 들어갔다 ⇒ eax : 내가 입력한 값

![5](https://github.com/king-raccoon/Yoom/assets/78426205/8811a9f3-f9a2-4c9a-8d7b-c33d9c6663b3)
edx에 저장된 값의 헥스값 : 825C-FBB1-C5FA4DC9-FFB7-7607 ⇒ edx : 해당 name의 비밀번호

![6](https://github.com/king-raccoon/Yoom/assets/78426205/664f65ad-5509-4d9d-ab1c-68029d87ddfe)
![7](https://github.com/king-raccoon/Yoom/assets/78426205/acb44938-a54d-402b-85b0-5be59e4f9976)
name을 기반으로 비밀번호 생성하는 sub_45B89D 확인

![8](https://github.com/king-raccoon/Yoom/assets/78426205/3e4cc50f-b5ce-4e3c-ac5f-564445accf87)
![9](https://github.com/king-raccoon/Yoom/assets/78426205/55e2897d-8af4-4f43-bc29-d24ec451b37b)
name 길이만큼 위의 연산 진행

![20](https://github.com/king-raccoon/Yoom/assets/78426205/6afc86d8-b51f-4386-b71d-b1e238135eee)

```
//위의 사진 코드
#include <stdio.h>

int main()
{
    int esi = 0;
    int edx = 0;
    int input = 0;
    for(input = 0x30; input <= 0x7a; input++){
        esi = input;
        esi *= 0x772;
        edx = esi;
        edx *= esi;
				esi += edx;
        esi *= 0x474;
        esi += esi;
        printf("%c : %x\n", input, esi);
    }
}
```

```
0 : 52fd7f00
1 : 63e2ebf0
2 : 502d5c20
3 : 17dccf90
4 : baf14640
5 : 396ac030
6 : 93493d60
7 : c88cbdd0
8 : d9354180
9 : c542c870
: : 8cb552a0
; : 2f8ce010
< : adc970c0
= : 76b04b0
> : 3c719be0
? : 4cdd3650
@ : 38add400
A : ffe374f0
B : a27e1920
C : 207dc090
D : 79e26b40
E : aeac1930
F : bedaca60
G : aa6e7ed0
H : 71673680
I : 13c4f170
J : 9187afa0
K : eaaf7110
L : 1f3c35c0
M : 2f2dfdb0
N : 1a84c8e0
O : e1409750
P : 83616900
Q : e73df0
R : 59d21620
S : 8e21f190
T : 9dd6d040
U : 88f0b230
V : 4f6f9760
W : f1537fd0
X : 6e9c6b80
Y : c74a5a70
Z : fb5d4ca0
[ : ad54210
\ : f5b23ac0
] : bbf436b0
^ : 5d9b35e0
_ : daa73850
` : 33183e00
a : 66ee46f0
b : 76295320
c : 60c96290
d : 26ce7540
e : c8388b30
f : 4507a460
g : 9d3bc0d0
h : d0d4e080
i : dfd30370
j : ca3629a0
k : 8ffe5310
l : 312b7fc0
m : adbdafb0
n : 5b4e2e0
o : 39111950
p : 47d25300
q : 31f88ff0
r : f783d020
s : 98741390
t : 14c95a40
u : 6c83a430
v : 9fa2f160
w : ae2741d0
x : 98109580
y : 5d5eec70
z : fe1246a0
```

![11](https://github.com/king-raccoon/Yoom/assets/78426205/b754c200-f120-4e6f-aa6b-71ccec35a030)
![12](https://github.com/king-raccoon/Yoom/assets/78426205/1a8bd3eb-d5b2-4851-8f55-1ca9f7ba03fb)

`F의 MD5 해시값 : 800618943025315f869e4e1f09471012`
