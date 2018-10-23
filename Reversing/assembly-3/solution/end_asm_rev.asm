offset:		03 02 01 00
ebp+0x08 =  b5 e8 e9 71
ebp+0x0c =  c6 b5 8a 95
ebp+0x10 =  e2 07 37 e9

asm3(0xb5e8e971, 0xc6b58a95, 0xe20737e9):
	push   	ebp
	mov    	ebp,esp
	mov	eax,0x19 ; eax = 0x0019
	xor	al,al 	 ; eax = 0x0000
	mov	ah,BYTE PTR [ebp+0xa]  ; eax = 0xe8+al = 0xe800
	sal	ax,0x10				   ; eax = 0x0000
	sub	al,BYTE PTR [ebp+0xd]  ; 0x8a
	add	ah,BYTE PTR [ebp+0xc]  ; 0x95
	xor	ax,WORD PTR [ebp+0x12] ; ax = ax ^ 0xe207 = 0x7771
	mov	esp, ebp
	pop	ebp
	ret

=> asm3(0xb5e8e971,0xc6b58a95,0xe20737e9) == 0x7771