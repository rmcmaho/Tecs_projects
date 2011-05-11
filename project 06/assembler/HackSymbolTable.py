
class SymbolTable:

    symbolTable = {"SP"     : 0,
                   "LCL"    : 1,
                   "ARG"    : 2,
                   "THIS"   : 3,
                   "THAT"   : 4,
                   "R0"     : 0,
                   "R1"     : 1,
                   "R2"     : 2,
                   "R3"     : 3,
                   "R4"     : 4,
                   "R5"     : 5,
                   "R6"     : 6,
                   "R7"     : 7,
                   "R8"     : 8,
                   "R9"     : 9,
                   "R10"     : 10,
                   "R11"     : 11,
                   "R12"     : 12,
                   "R13"     : 13,
                   "R14"     : 14,
                   "R15"     : 15,
                   "SCREEN"  : 16384,
                   "KBD"     : 24576}

    nextUnusedAddress = 16

    def addEntry (self, symbol, address = None):
        if (address is None):
            self.symbolTable[symbol] = self.nextUnusedAddress
            self.nextUnusedAddress = self.nextUnusedAddress + 1
        else:
            self.symbolTable[symbol] = address

    def contains (self, symbol):
        try:
            temp = self.symbolTable[symbol]
            return True
        except KeyError:
            return False

    def getAddress (self, symbol):
        return self.symbolTable[symbol]
