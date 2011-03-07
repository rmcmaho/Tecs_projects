// I/O handling: This program runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen, i.e. writes "black" in every pixel.
// When no key is pressed, the screen should be cleared.

// You may choose to blacken and clear the screen in any visual order, as long as pressing a key continuously for long enough will result in a fully blackened screen and not pressing any key for long enough will result in a cleared screen.
// This program has a test script (Fill.tst) but no compare file – it should be checked visually by inspecting the simulated screen.


(MAIN_LOOP)
	@SCREEN
	D=A	// Get start of screen memory map
	@addr
	M=D	// Set M[addr] to the start of screen memory map ( M[addr] = SCREEN )
	(PRINT_LOOP)
		@addr		// A = addr
		A=M		// A = M[A]
		M=-1		// M[A] = -1
		@addr		// A = addr
		D=M		// D = M[A]
		@32		// A = 32
		D=D+1		// D = D + 1
		@addr		// A = addr
		M=D		// M[A] = D
		@KBD
		D=D-A
		@MAIN_LOOP
		D;JGE
		@KBD
		D=M		// Get the keyboard memory map value
		@PRINT_LOOP
		0;JMP
	(END_PRINT)
	@MAIN_LOOP
	0;JMP
(END_MAIN)
	@END_MAIN
	0;JMP


