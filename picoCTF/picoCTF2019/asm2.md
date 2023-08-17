> What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format.

esp-0x4 : 0x2d
<br>esp-0x8 : 0x4

```
asm2:
	<+0>:	push   ebp !stack <- ebp
	<+1>:	mov    ebp,esp !ebp <- esp
	<+3>:	sub    esp,0x10 !esp -= 0x10 => 16byte 확보
	<+6>:	mov    eax,DWORD PTR [ebp+0xc] !eax <- ebp + 0xc
	<+9>:	mov    DWORD PTR [ebp-0x4],eax !ebp-0x4 <- eax = ebp + 0xc == 0x2d
	<+12>:	mov    eax,DWORD PTR [ebp+0x8] !eax <- ebp + 0x8
	<+15>:	mov    DWORD PTR [ebp-0x8],eax !ebp-0x8 <- eax = ebp + 0x8 == 0x4
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1 !0x2d + 0x1 = 0x2e
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1 !0x4 + 0xd1 = 0xd5
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1 !jump. 0x4와 0x5fa1 비교
	<+38>:	jle    0x501 <asm2+20> !branch asm2+20
	<+40>:	mov    eax,DWORD PTR [ebp-0x4] !eax <- 0x2e
	<+43>:	leave
	<+44>:	ret
```

결국 반복문이다

```
a = 0x2d
b = 0x4

while b <= 0x5fa1:
	a += 0x1
	b += 0xd1

print(hex(a))
```

`0xa3`
