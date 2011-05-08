# Hack assembler

import sys
import HackAssemblyParser
import HackBinaryCode

def main():
    inputFileName = sys.argv[1]
    outputFileName = 'a.out'
    try:
        outputFileName = sys.argv[2]
    except IndexError:
        pass
    outputFile = open (outputFileName, 'w')
    parser = HackAssemblyParser.parseAssembly(inputFileName)
    for op in parser:
        print op
        binaryCommand = HackBinaryCode.convertCommand(op)
        print binaryCommand
        outputFile.write(binaryCommand)
        outputFile.write('\n')


if __name__ == '__main__':
    main()
