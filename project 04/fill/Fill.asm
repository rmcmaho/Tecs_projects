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
	@color
	M=0
	(PRINT_LOOP)
		@color		// Get the current color
		D=M		// Save the color for use
		@addr		// A = addr
		A=M		// A = M[A] -- Get the address of the current place in the screen buffer
		M=D		// M[A] = -1 -- Set the screen buffer in the current address to the current color
		@addr		// A = addr
		D=M		// D = M[A] -- Get the address of the current place in the screen buffer
		D=D+1		// D = D + 1 -- Increment the address by one
		@addr		// A = addr
		M=D		// M[A] = D -- Set the new incremented address
		@KBD		// A = KBD -- Get the address of the keyboard buffer which is also the end of the screen buffer
		D=D-A		// D = D - KBD
		@MAIN_LOOP
		D;JGE		// If current address minus KBD is greater than 0, than jump to main loop
		@color
		M=0
		@KBD
		D=M		// D = M[KBD] -- Get the keyboard memory map value
		@PRINT_LOOP
		D;JEQ		// If the keyboad buffer is equal to zero (no key is pressed), jump to the beginning of the print loop
		@color
		M=-1
		@PRINT_LOOP	
		0;JMP
	(END_PRINT)
	@MAIN_LOOP
	0;JMP
(END_MAIN)
	@END_MAIN
	0;JMP


