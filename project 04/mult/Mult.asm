// The inputs of this program are the current values stored in R0 and R1 (i.e. the two top RAM locations).
// The program computes the product R0*R1 and stores the result in R2.

	@R2
	M=0	// Set R2=0
(LOOP)
	@R1
	D=M	// Get R1 (D=R1)
	@END
	D;JLE	// Exit if R1<0
	@R1
	M=M-1	// R1 = R1 - 1
	@R0
	D=M	// D = R0
	@R2
	M=M+D	// R2 = R2 + R0
	@LOOP
	0;JMP	// Loop
(END)
	@END
	0;JMP
	