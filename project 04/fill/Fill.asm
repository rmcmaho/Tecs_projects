// I/O handling: This program runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen, i.e. writes "black" in every pixel.
// When no key is pressed, the screen should be cleared.

// You may choose to blacken and clear the screen in any visual order, as long as pressing a key continuously for long enough will result in a fully blackened screen and not pressing any key for long enough will result in a cleared screen.
// This program has a test script (Fill.tst) but no compare file – it should be checked visually by inspecting the simulated screen.


(MAIN_LOOP)
	@SCREEN
	D=A	// Get start of screen memory map
	@32
	D=D-A
	@addr
	M=D	// Set R0 to just before the start of screen memory map
	(PRINT_LOOP)
		@32
		D=A
		@addr
		M=M+D		// Go to the next screen section
		@KBD
		D=M		// Get the keyboard memory map value
		@BLACK
		D;JGT		// If the keyboard memory map > 0, then jump to printing black
		@SCREEN
		D=A
		@R0
		A=D+A
		M=0		// Otherwise, set current screen section to white
		@PRINT_LOOP
		0;JMP
		(BLACK)
		@SCREEN
		D=A
		@R0
		A=D+A
		M=-1
		@PRINT_LOOP
		0;JMP
	(END_PRINT)
	@MAIN_LOOP
	0;JMP
(END_MAIN)
	@END_MAIN
	0;JMP


