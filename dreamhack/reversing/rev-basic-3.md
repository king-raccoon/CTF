<https://dreamhack.io/wargame/challenges/17>
![스크린샷_2023-01-10_오후_1 58 12](https://github.com/king-raccoon/write-up/assets/78426205/dddefef9-4f99-4167-8977-120040beb970)
correct가 main에 있음을 확인하고 pseudo code를 생성하자

![스크린샷_2023-01-10_오후_1 58 57](https://github.com/king-raccoon/write-up/assets/78426205/ab33d683-2175-4c7f-a1cd-5186c04647dc)
이번에도 if문 조건이 flag가 되기에 이를 확인하여 암호를 찾자.

![스크린샷_2023-01-10_오후_1 59 36](https://github.com/king-raccoon/write-up/assets/78426205/51d2adeb-cd3f-4135-b364-99a8989a4eee)
main의 pseudo code이고 이번에는 for문의 형태로 답을 찾아가야한다.

if문의 flag 의미는 byte_140003000와 (i)XOR(입력값 + i) + 2\*i가 같은지를 판단한다.

즉, 입력값은 byte_140003000 - 2\*i

이번에는 byte_140003000에 있는 값을 확인해야한다.

```
#include <stdio.h>

int main(){
    int arr[24] = {0x49, 0x60, 0x67, 0x74, 0x63, 0x67, 0x42, 0x66, 0x80, 0x78, 0x69, 0x69, 0x7B, 0x99, 0x6D, 0x88, 0x68, 0x94, 0x9F, 0x8D, 0x4D, 0xA5, 0x9D, 0x45};
    int i;
    for ( i = 0; i < 0x18; i++ )
  {
      printf("%c", ((arr[i] - 2*i)^i));
  }
}
```

`정답: I_am_X0_xo_Xor_eXcit1ng`
