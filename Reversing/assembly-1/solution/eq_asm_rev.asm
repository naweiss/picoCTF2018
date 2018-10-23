asm1(0x15e):
	push	ebp
	mov	ebp,esp
	cmp	DWORD PTR [ebp+0x8],0xdc
	jg 	part_a ; 0x15e >? 0xdc => goto part_a
	cmp	DWORD PTR [ebp+0x8],0x8
	jne	part_b
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x68 ; 0x15e !=? 0x68 => goto part_c
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
	cmp	DWORD PTR [ebp+0x8],0xfc
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3 ; 0x15e + 0x3 = 0x161
part_d:
	pop	ebp
	ret
	
=> asm1(0x15e) === 0x161