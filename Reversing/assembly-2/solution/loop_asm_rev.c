#include <stdio.h>
 
int run_asm()
{
	// ebp and esp are disallowed via the asm command
	// so everything related to them was swapped with appropriate command (or none)
	
	// Note: ecx will be the first function argument (0x21)
	// 		 edx will be the second function argument (0x0e)
    
	asm(
		".intel_syntax noprefix;"
		"	mov    	ecx, 0x21;"
		"	mov    	edx, 0x0e;"
		"asm2:"
		"	mov    	eax, edx;"
		"	mov 	ebx, eax;"
		"	mov    	eax, ecx;"
		"	mov		esi,eax;"
		"	jmp    	part_b;"
		"part_a:;"
		"	add    	ebx,0x1;"
		"	add		ecx,0x41;"
		"part_b:;"
		"	cmp    	ecx,0x9886;"
		"	jle    	part_a;"
		"	mov    	eax, ebx;"
        ".att_syntax;"
    );
}
int main(void)
{
    return printf("The answer is 0x%x.\n", run_asm());
}