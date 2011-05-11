# Hack assembler

import sys
import HackAssemblyParser
import HackBinaryCode

def main():
    # Get the input filename (required)
    inputFileName = sys.argv[1]
    # Set the default output filename
    outputFileName = 'Prog.hack'
    # Try to get the output filename
    try:
        outputFileName = sys.argv[2]
    except IndexError:
        pass
    # Parse the input file
    parser = HackAssemblyParser.parseAssembly(inputFileName)
    # Open the output file for writing
    with open (outputFileName, 'w') as outputFile:
        # Step through the parser and convert each command
        for op in parser:
            print op
            binaryCommand = HackBinaryCode.convertCommand(op)
            print binaryCommand
            outputFile.write(binaryCommand)
            outputFile.write('\n')
    # The output file will be automatically closed upon leaving the 'with' clause


if __name__ == '__main__':
    main()
