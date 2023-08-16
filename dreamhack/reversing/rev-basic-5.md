<https://dreamhack.io/wargame/challenges/19>

![image](https://github.com/king-raccoon/write-up/assets/78426205/ce860f85-5587-4a96-b6f7-4ab0f2fa38ec)
![스크린샷_2023-01-10_오후_4 43 11](https://github.com/king-raccoon/write-up/assets/78426205/1998df23-29cb-4ec3-a743-d13807efa389)
flag의 unsigned **int8 _)(a1 + i + 1) + _(unsigned **int8 \*)(a1 + i)는 input[i+1]+input[i] = byte140003000[i]인지를 판단한다.

(편의를 위해 input[] => res[], byte140003000[] => arr[]로 하자)

res[0] + res[1] = arr[0]

res[1] + res[2] = arr[1]

...

res[22] + res[23] = arr[22]

res[23] + res[24] = arr[23]

인데 우리가 알아내야하는건 res인데 arr[23] = 0x00이므로 res[23] = res[24] = 0이 된다

res[22] = arr[22] - res[23]이 되므로 res[i-1] = arr[i-1] - res[i]이 된다

```
#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    int arr[24] = {0xAD, 0xD8, 0xCB, 0xCB, 0x9D, 0x97, 0xCB, 0xC4,0x92, 0xA1, 0xD2, 0xD7, 0xD2, 0xD6, 0xA8, 0xA5, 0xDC, 0xC7, 0xAD, 0xA3, 0xA1, 0x98, 0x4C, 0x00};
    int res[24] = {0};
    for(int i = 23; i >= 0; i--){
        res[i-1] = arr[i-1] - res[i];
    }
    for(int i = 0; i < 24; i++) printf("%c", res[i]);
    printf("\n");
}
/*
res[i] + res[i+1] = arr[i]

 */

```

`All_l1fe_3nds_w1th_NULL`
