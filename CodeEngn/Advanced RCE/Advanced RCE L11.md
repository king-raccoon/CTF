**solved yet**

> Serial이 94E7DB1B 일때 Name은 무엇인가
> <br>해당 Serial에 대한 정답이 여러개 나오는 문제이며 Contact로 보내주시면 인증키를 보내드리겠습니다
> <br>해당 Serial에 대해서 'Serial accepted' 메시지가 나와야 합니다.

![1](https://github.com/king-raccoon/Yoom/assets/78426205/06663702-ac03-46b6-b2c1-dc439343aa41)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/cceecb84-a268-4c3c-a4ba-2f02854380b2)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/45c13419-1a0c-4d09-9a3c-9b061b69650f)
명령어 jecxz : ECX = 0이면 점프 ⇒ ECX가 0이면 됨

명령어 repe : repeat if equal

![4](https://github.com/king-raccoon/Yoom/assets/78426205/91d43eba-b07f-446d-8747-3a92e7648359)
실행시켜보면 esi에 시리얼이, esi에 옮겨진다

4010F2에 bp걸고 다시 실행하고 그 함수로 들어간다

![5](https://github.com/king-raccoon/Yoom/assets/78426205/b628b3da-f064-4337-b8e9-23adfc72246f)
함수로 들어가면 401146에서 시작해 cmp문들을 지나 40137B 리턴문을 지나 401380의 함수콜을 만나고 나면 계속 401164로 돌아오면서 반복적으로 시행된다

```
//Repeated statement decoding code
int sub_401146()
{
  unsigned int v0; // ebx
  unsigned int i; // ecx
  int result; // eax
  unsigned int v3; // ebx
  unsigned int v4; // ecx
  int v5; // ecx
  int v6; // ecx
  int v7; // eax
  int v8; // ecx
  int v9; // ecx
  int v10; // eax
  int v11; // ecx
  int v12; // ecx
  int v13; // ecx
  int v14; // ecx
  void *v15; // edx
  int v16; // eax
  int v17; // ecx
  int v18; // [esp-Ch] [ebp-20h]
  int v19; // [esp-4h] [ebp-18h]
  int v20; // [esp-4h] [ebp-18h]
  int v21; // [esp+0h] [ebp-14h]

  v0 = 0;
  for ( i = 1; ; sub_40138A(i, v21) )
  {
    result = (unsigned __int8)byte_40217B[20 * BYTE1(v0) + (unsigned __int8)v0];
    if ( (_BYTE)result == 34 )
    {
      v3 = _byteswap_ulong(v0);
      LOBYTE(v3) = v3 ^ 1;
      v0 = _byteswap_ulong(v3);
      continue;
    }
    if ( (unsigned __int8)_byteswap_ulong(v0) )
    {
      sub_4013AB(i);
      continue;
    }
    if ( (unsigned __int8)result >= 0x30u && (unsigned __int8)result <= 0x39u || (_BYTE)result == 126 )
      return sub_4013AB(i);
    switch ( (_BYTE)result )
    {
      case ',':
        v4 = _byteswap_ulong(i);
        unk_402439 = byte_402534[(unsigned __int16)v4];
        return sub_4013BF(_byteswap_ulong(v4), &loc_401380);
      case '>':
        LOWORD(i) = 1;
        continue;
      case '<':
        LOWORD(i) = 255;
        continue;
      case 'v':
        LOWORD(i) = 256;
        continue;
      case '^':
        LOWORD(i) = -256;
        continue;
      case '+':
      case '-':
        sub_4013BF(i, &loc_401380);
        sub_4013BF(v5, v19);
        return sub_4013AB(v6);
      case '*':
        v7 = sub_4013BF(i, &loc_401380);
        sub_4013BF(v8, v7);
        return sub_4013AB(v9);
    }
    if ( (_BYTE)result == 47 )
      break;
    if ( (_BYTE)result == 92 )
    {
      sub_4013BF(i, &loc_401380);
      sub_4013BF(v14, v20);
      ((void (*)(void))sub_4013AB)();
      return ((int (*)(void))sub_4013AB)();
    }
    if ( (_BYTE)result == 95 )
    {
      if ( (int)sub_4013BF(i, &loc_401380) )
        v15 = &loc_401200;
      __asm { jmp     edx }
    }
    switch ( (_BYTE)result )
    {
      case '#':
        return sub_40138A(i, &loc_401380);
      case ':':
        sub_4013BF(i, &loc_401380);
        ((void (*)(void))sub_4013AB)();
        return ((int (*)(void))sub_4013AB)();
      case '!':
        sub_4013BF(i, &loc_401380);
        return ((int (*)(void))sub_4013AB)();
      case 'l':
        sub_4013BF(i, &loc_401380);
        result = ((int (*)(void))sub_4013AB)();
        break;
    }
    if ( (_BYTE)result == 96 )
    {
      v16 = sub_4013BF(i, &loc_401380);
      sub_4013BF(v17, v16);
      result = ((int (*)(void))sub_4013AB)();
    }
    if ( (_BYTE)result == 36 )
      return sub_4013BF(i, &loc_401380);
    if ( (_BYTE)result == 64 )
      return result;
  }
  v10 = sub_4013BF(i, i);
  sub_4013BF(v11, v10);
  v12 = v18;
  if ( !v18 )
    v12 = 0;
  sub_4013AB(v12);
  return sub_4013AB(v13);
}
```

![6](https://github.com/king-raccoon/Yoom/assets/78426205/1729a004-ac40-4fd3-8c67-95db1c7eb516)
반복문을 돌리면 40217B에 있는 이상한 문자들을 eax에 넣는다

$5%$#wv#\_"as"_3$$v+8v_"~x"<\^`\"9":<;x"->~:!4#v$_"md8"G+%+l:!#@_>87+/\"0"^v>,+

![7](https://github.com/king-raccoon/Yoom/assets/78426205/b70f9eab-487d-4588-8147-a4404c0d5ab4)
![Untitled](https://github.com/king-raccoon/Yoom/assets/78426205/28fd10ad-6b7d-4f43-9942-18378250a4c0)
004013B1 |. 8982 38254000 MOV DWORD PTR DS:[EDX+402538],EAX

![8](https://github.com/king-raccoon/Yoom/assets/78426205/6ac7af98-198f-48a7-843f-9f3e0ac327ee)
반복문은 크게 3개인것같다

```
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	int a;
	int b = 0x426C;
	char aa[81];
	char aaa[9] = { "94E7DB1B" };

	int i, j;

	for (i = 0x0; i <= 0xFFFF; i++)
	{
		memset(aa, 0, sizeof(aa));
		j = 0;

		a = b * i + 0x3B10;

		while (a != 0)
		{
			aa[j] = a % 0xF + 0x30;
			if (aa[j] >= 0x3A)
				aa[j] += 0x8;
			a = a / 0xF * 2;
			j++;
		}

		if (strncmp(aa, aaa, 8) == 0)
			break;
	}

	printf("%s\n%X", aa, i);

	return 0;
}
```

사실 구글링 했는데 모르겠다
