> What integer does this program print with argument 3736234946? File: chall_2.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})

```
.arch armv8-a
	.file	"chall_2.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #32
	str	w0, [sp, 12] @w0=8 ->sp+12
	str	wzr, [sp, 24] @sp+24 <- 0
	str	wzr, [sp, 28] @sp+28 <- 0
	b	.L2
.L3:
	ldr	w0, [sp, 24] @w0 = 0
	add	w0, w0, 3 @w0 = 3
	str	w0, [sp, 24] @sp + 24 <- 3
	ldr	w0, [sp, 28] @w0 <- sp+28 = 0
	add	w0, w0, 1 @w0 = 1
	str	w0, [sp, 28] @sp+28 = 1
.L2:
	ldr	w1, [sp, 28] @w1 <- sp+28 = 0
	ldr	w0, [sp, 12] @w0 <- sp + 12=8
	cmp	w1, w0
	bcc	.L3
	ldr	w0, [sp, 24] @w0 = 3
	add	sp, sp, 32
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0 @x29 <- sp
	str	w0, [x29, 28] @w0->x29+28
	str	x1, [x29, 16] @x1->x29+16
	ldr	x0, [x29, 16] @x29+16<-x0
	add	x0, x0, 8 @x0+=8
	ldr	x0, [x0]
	bl	atoi
	bl	func1
	str	w0, [x29, 44] @x29+44 <- w0=3
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	ldr	w1, [x29, 44]
	bl	printf
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

3736234946
<br>9c174346

`picoCTF{9c174346}`
