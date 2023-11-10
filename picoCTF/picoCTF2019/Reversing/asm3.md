> What does asm3(0xd73346ed,0xd48672ae,0xd3c8b139) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format.

esp+0x10 = 0xd3c8b139
<br>esp+0xc = 0xd48672ae
<br>esp+0x8 = 0xd73346ed

```
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax !eax = 0
	<+5>:	mov    ah,BYTE PTR [ebp+0xa] !ah <- ebp+0xa (=0x33)
	<+8>:	shl    ax,0x10 ! 0x000000000
	<+12>:	sub    al,BYTE PTR [ebp+0xc] !0x00 - 0xae = 0x52
	<+15>:	add    ah,BYTE PTR [ebp+0xd] !0x00 + 0x72 = 0x72
	<+18>:	xor    ax,WORD PTR [ebp+0x10] !0x7252 xor 0xb139 = 0xc36b
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret
```

![Untitled](https://github.com/king-raccoon/Yoom/assets/78426205/1e8a0939-ee6c-4cd8-8fee-0d2548d12eff)

x86 → little endian

x86 음수 표기법 : 2의 보수 → +1

`flag : 0xc36b`
