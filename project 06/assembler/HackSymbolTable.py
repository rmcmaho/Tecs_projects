
class SymbolTable:
    ''' Class to represent a symbol table'''
    symbolTable = {"SP"     : '0',
                   "LCL"    : '1',
                   "ARG"    : '2',
                   "THIS"   : '3',
                   "THAT"   : '4',
                   "R0"     : '0',
                   "R1"     : '1',
                   "R2"     : '2',
                   "R3"     : '3',
                   "R4"     : '4',
                   "R5"     : '5',
                   "R6"     : '6',
                   "R7"     : '7',
                   "R8"     : '8',
                   "R9"     : '9',
                   "R10"     : '10',
                   "R11"     : '11',
                   "R12"     : '12',
                   "R13"     : '13',
                   "R14"     : '14',
                   "R15"     : '15',
                   "SCREEN"  : '16384',
                   "KBD"     : '24576'}

    nextUnusedAddress = 16

    def addEntry (self, symbol, address = None):
        if (address is None):
            self.symbolTable[symbol] = str(self.nextUnusedAddress)
            self.nextUnusedAddress = self.nextUnusedAddress + 1
        else:
            self.symbolTable[symbol] = str(address)

    def contains (self, symbol):
        try:
            temp = self.symbolTable[symbol]
            return True
        except KeyError:
            return False

    def getAddress (self, symbol):
        return self.symbolTable[symbol]
# END SymbolTable


def generateSymbolTable (inputFileName):
    ''' Function to generate a symbol table from an assembly file '''
    symbolTable = SymbolTable()
    with open(inputFileName) as assemblyFile:
        lineNumber = 0
        for line in assemblyFile:
            # Strip off leading and trailing whitespace
            line = line.strip()
            
            if len(line) == 0:
                # Ignore blank lines
                continue
            elif line.startswith("@"):
                # Increment line number for A commands
                lineNumber += 1
                # Symbol starts after @
                aSymbol = line[1:]
                # If the symbol doesn't already exist
                if (not symbolTable.contains(aSymbol)):
                    # Then add it
                    symbolTable.addEntry(aSymbol)
                    continue
            elif line.startswith("("):
                # Do not increment line number for labels
                pass
                # Label begins after first ( and ends before )
                label = line[1:-1]
                # Remove leading or trailing whitespace from the label
                label = label.strip()
                # If the label doesn't already exist
                if (not symbolTable.contains(label)):
                    # Then add it as the line number
                    symbolTable.addEntry(label, lineNumber)
                    continue
            elif line.startswith("//"):
                # Ignore comments
                continue
            else:
                # Incrememnt line number for C commands
                lineNumber += 1
    return symbolTable
