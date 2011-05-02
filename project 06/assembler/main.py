# Hack assembler

import sys


class A_Command:
    def __init__(self, symbol):
        self.symbol = symbol
    def __repr__(self):
        return "A_COMMAND: @"+self.symbol

class L_Command:
    def __init__(self, symbol, lineNumber=0):
        self.symbol = symbol
        self.lineNumber = lineNumber
    def __repr__(self):
        return "L_COMMAND: ("+self.symbol+") = "+self.lineNumber

class C_Command:
    def __init__(self, line):
        self.dest, self.comp, self.jmp = self.parseCommand(line)

    def __repr__(self):
        output = "C_COMMAND: "
        if self.dest != None:
            output += self.dest + "="
        if self.comp != None:
            output += self.comp
        if self.jmp != None:
            output += ";"+self.jmp
        return output
        
    def parseJmp(self,line):
        parsingJmp = line.split(";",1)
        if(len(parsingJmp) == 1):
            return (parsingJmp[0], None)
        else:
            return (parsingJmp[0], parsingJmp[1])

    def parseDest(self,line):
        parsingDest = line.split("=",1)
        if(len(parsingDest) == 1):
            return (None, parsingDest[0])
        else:
            return (parsingDest[0], parsingDest[1])

    def parseCommand(self,line):
        dest, compAndJmp = self.parseDest(line)
        comp, jmp = self.parseJmp(compAndJmp)
        return dest, comp, jmp

def parseAssembly(fileName):
    assemblyFile = file(fileName)
    lineNumber = 0
    for line in assemblyFile:
        lineNumber += 1
        line = line.strip()

        if len(line) == 0:
            continue
        elif line.startswith("@"):
            yield A_Command(line[1:])
            continue
        elif line.startswith("("):
            yield L_Command(line[1:-1], lineNumber)
            continue
        elif line.startswith("//"):
            continue
        else:
            yield C_Command(line)


def main():
    fileName = sys.argv[1]
    parser = parseAssembly(fileName)
    for op in parser:
        print op


if __name__ == '__main__':
    main()
