# Hack assembler

import sys
import HackAssemblyParser
import HackBinaryCode

def main():
    fileName = sys.argv[1]
    parser = HackAssemblyParser.parseAssembly(fileName)
    for op in parser:
        print op
        print HackBinaryCode.convertCommand(op)


if __name__ == '__main__':
    main()
