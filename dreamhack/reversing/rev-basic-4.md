<https://dreamhack.io/wargame/challenges/18>

![스크린샷_2023-01-10_오후_4 04 45](https://github.com/king-raccoon/write-up/assets/78426205/dfa05b5f-13a3-46cc-8f43-847027250d10)
![스크린샷_2023-01-10_오후_4 05 02](https://github.com/king-raccoon/write-up/assets/78426205/79b1274e-dda6-4c9b-83d5-8c3b0df0ba1e)
((unsigned **int8)(16 \* _(\_BYTE _)(a1 + i)) | ((int)\*(unsigned **int8 \*)(a1 + i) >> 4)와 byte_140003000를 비교한다

즉, (input\*16) OR (input >>4)을 실행하는데 input>>4가 결국 오른쪽으로 4번 비트 이동이므로 16으로 나누는 것과 같다.

예를 들어, a1 = 0000 1101(11)일때 a1\*16 = 1101 0000(176)이고, a1>>4 = 0000 0000이다. 이를 OR하면 1101 0000이 된다. 즉, flag는 input값을 앞 4비트와 뒤 4비트를 바뀐 값이기 때문에 주어진 byte_140003000를 앞, 뒤 4비트를 바꾼다.

​```
#include <stdio.h>
using namespace std;

int main() {
int arr[27] = {0x24, 0x27, 0x13, 0xC6, 0xC6,0x13, 0x16, 0xE6, 0x47,0xF5, 0x26, 0x96, 0x47, 0xF5, 0x46,0x27, 0x13, 0x26, 0x26, 0xC6,0x56, 0xF5, 0xC3, 0xC3, 0xF5, 0xE3,0xE3};
for(int i = 0; i < 0x1c; i++){
printf("%c", ((16\*arr[i])|(arr[i]>>4)));
}
printf("\n");
}

```

정답: Br1ll1ant_bit_dr1bble_<<_>>
```
