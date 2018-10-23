#include <stdio.h>
 
int run_asm()
{
	// ebp and esp are disallowed via the asm command
	// so everything related to them was swapped with appropriate command (or none)
	
	// Note: ecx will be the function argument (0x15e)
    
	asm(   
		".intel_syntax noprefix;"
		"asm1:"
		"   mov ecx, 0x15e;" // argument
		"	cmp	ecx, 0xdc;"
		"	jg 	part_a;"
		"	cmp	ecx, 0x8;"
		"	jne	part_b;"
		"	mov	eax, ecx;"
		"	add	eax, 0x3;"
		"	jmp	part_d;"
		"part_a:"
		"	cmp	ecx, 0x68;"
		"	jne	part_c;"
		"	mov	eax, ecx;"
		"	sub	eax, 0x3;"
		"	jmp	part_d;"
		"part_b:"
		"	mov	eax, ecx;"
		"	sub	eax, 0x3;"
		"	jmp	part_d;"
		"	cmp	ecx, 0xfc;"
		"	jne	part_c;"
		"	mov	eax, ecx;"
		"	sub	eax, 0x3;"
		"	jmp	part_d;"
		"part_c:"
		"	mov	eax, ecx;"
		"	add	eax, 0x3;"
		"part_d:"
        ".att_syntax;"
    );
}
int main(void)
{
    return printf("The answer is 0x%x.\n", run_asm());
}