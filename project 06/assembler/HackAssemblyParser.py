# HackAssemblyParser module

# Encapsulates access to the input code. Reads an assembly language
# command, parses it, and provides convenient access to the command's
# components (fields and symbols). In addition, removes all white space
# and comments.

import HackSymbolTable

class A_Command:
    ''' For @Xxx where Xxx is either a symbol or a decimal number '''
    # Either a symbol or a decimal number
    symbol = None
    
    def __init__(self, symbol):
        self.symbol = symbol
    def __repr__(self):
        return "A_COMMAND: @"+self.symbol

class L_Command:
    ''' For (Xxx) where Xxx is a symbol '''
    # Either a symbol or a decimal number
    symbol = None
    # A decimal number indicating label location
    lineNumber = None
    
    def __init__(self, symbol, lineNumber=0):
        self.symbol = symbol
        self.lineNumber = lineNumber
    def __repr__(self):
        return "L_COMMAND: ("+self.symbol+") = "+str(self.lineNumber)

class C_Command:
    ''' For dest=comp;jump '''
    # Location to store result
    dest = None
    # Operation to compute
    comp = None
    # Jump condition
    jump = None
    
    def __init__(self, line):
        self.dest, self.comp, self.jump = self.parseCommand(line)

    def __repr__(self):
        output = "C_COMMAND: "
        if self.dest != None:
            output += self.dest + "="
        if self.comp != None:
            output += self.comp
        if self.jump != None:
            output += ";"+self.jump
        return output
        
    def parseJmp(self,line):
        ''' Returns the jump mnemonic in the current C-command (8 possibilities) '''
        parsingJmp = line.split(";",1)
        if(len(parsingJmp) == 1):
            return (parsingJmp[0], None)
        else:
            jmp = parsingJmp[1]
            restOfCommand = parsingJmp[0]
            # Assert the jump is one of the possible values
            if(jmp == "JGT" or jmp == "JEQ" or
               jmp == "JGE" or jmp == "JLT" or
               jmp == "JNE" or jmp == "JLE" or
               jmp == "JMP"):
                return (restOfCommand, jmp)
            else:
                return (None, None)

    def parseDest(self,line):
        ''' Returns the dest mnemonic in the current C-command (8 possibilities) '''
        parsingDest = line.split("=",1)
        if(len(parsingDest) == 1):
            return (None, parsingDest[0])
        else:
            dest = parsingDest[0]
            restOfCommand = parsingDest[1]
            # Assert the dest is one of the possible values
            if(dest == "M" or dest == "D" or
               dest == "MD" or dest == "A" or
               dest == "AM" or dest == "AD" or
               dest == "AMD"):
                return (dest, restOfCommand)
            else:
                return (None, None)

    def removeComment(self, line):
        lineWithoutComments = line.split("//",1)
        return lineWithoutComments[0].strip()

    def parseCommand(self,line):
        ''' Returns the comp mnemonic in the C-command (28 possibilities)
        along with the dest and jmp components if they exist'''
        command = self.removeComment(line)
        dest, compAndJmp = self.parseDest(command)
        comp, jmp = self.parseJmp(compAndJmp)
        return dest, comp, jmp

def parseAssembly(fileName, symbolTable):
    assemblyFile = file(fileName)
    lineNumber = 0
    for line in assemblyFile:
        lineNumber += 1
        line = line.strip()

        if len(line) == 0:
            continue
        elif line.startswith("@"):
            symbol = line[1:]
            address = symbolTable.getAddress(symbol)
            yield A_Command(address)
            continue
        elif line.startswith("("):
            symbol = line[1:-1]
            address = symbolTable.getAddress(symbol)
            yield L_Command(symbol, address)
            continue
        elif line.startswith("//"):
            continue
        else:
            yield C_Command(line)
