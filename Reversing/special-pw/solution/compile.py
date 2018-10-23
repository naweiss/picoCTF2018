#!/usr/bin/python2
from pwn import *

context.clear(arch='i386')
filename = make_elf_from_assembly("""
.intel_syntax noprefix
	
.global main

main:
	push   ebp
	mov    ebp,esp
	sub    esp,0x10
	mov    DWORD PTR [ebp-0xc],0x0
	mov    eax,DWORD PTR [ebp+0xc]
	mov    eax,DWORD PTR [eax+0x4]
	mov    DWORD PTR [ebp-0x4],eax
	jmp    part_b
part_a:
	add    DWORD PTR [ebp-0xc],0x1
	add    DWORD PTR [ebp-0x4],0x1
part_b:	
	mov    eax,DWORD PTR [ebp-0x4]
	movzx  eax,BYTE PTR [eax]
	test   al,al
	jne    part_a
	mov    DWORD PTR [ebp-0x8],0x0
	jmp    part_d
part_c:	
	mov    eax,DWORD PTR [ebp+0xc]
	add    eax,0x4
	mov    edx,DWORD PTR [eax]
	mov    eax,DWORD PTR [ebp-0x8]
	add    eax,edx
	mov    DWORD PTR [ebp-0x4],eax
	mov    eax,DWORD PTR [ebp-0x4]
	movzx  eax,BYTE PTR [eax]
	xor    eax,0x9d
	mov    edx,eax
	mov    eax,DWORD PTR [ebp-0x4]
	mov    BYTE PTR [eax],dl
	mov    eax,DWORD PTR [ebp-0x4]
	movzx  eax,WORD PTR [eax]
	ror    ax,0x5
	mov    edx,eax
	mov    eax,DWORD PTR [ebp-0x4]
	mov    WORD PTR [eax],dx
	mov    eax,DWORD PTR [ebp-0x4]
	mov    eax,DWORD PTR [eax]
	rol    eax,0xb
	mov    edx,eax
	mov    eax,DWORD PTR [ebp-0x4]
	mov    DWORD PTR [eax],edx
	add    DWORD PTR [ebp-0x8],0x1
part_d:	
	mov    eax,DWORD PTR [ebp-0xc]
	sub    eax,0x3
	cmp    eax,DWORD PTR [ebp-0x8]
	jg     part_c
	mov    eax,DWORD PTR [ebp+0xc]
	mov    eax,DWORD PTR [eax+0x4]
	mov    DWORD PTR [ebp-0x4],eax
	mov    DWORD PTR [ebp-0x10],0x14890ba
	jmp    part_f
part_e:	
	mov    eax,DWORD PTR [ebp-0x4]
	movzx  edx,BYTE PTR [eax]
	mov    eax,DWORD PTR [ebp-0x10]
	movzx  eax,BYTE PTR [eax]
	cmp    dl,al
	je     part_k
	mov    eax,0x0
	jmp    part_h
part_k:	
	add    DWORD PTR [ebp-0x4],0x1
	add    DWORD PTR [ebp-0x10],0x1
part_f:	
	mov    eax,DWORD PTR [ebp-0x10]
	movzx  eax,BYTE PTR [eax]
	test   al,al
	jne    part_e
	mov    eax,DWORD PTR [ebp+0xc]
	add    eax,0x4
	mov    eax,DWORD PTR [eax]
	mov    edx,DWORD PTR [ebp-0x10]
	mov    ecx,0x14890ba
	sub    edx,ecx
	add    eax,edx
	movzx  eax,BYTE PTR [eax]
	test   al,al
	je     part_g
	mov    eax,0x0
	jmp    part_h
part_g:	
	mov    eax,0x1
part_h:	
	leave
	ret""", extract=True)
    
# Debug this file using gdb
with open('special_pw','w') as out:
    out.write(filename)