# Hack assembler

import sys
import HackAssemblyParser


def main():
    fileName = sys.argv[1]
    parser = HackAssemblyParser.parseAssembly(fileName)
    for op in parser:
        print op


if __name__ == '__main__':
    main()
