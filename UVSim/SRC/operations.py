#OPERATIONS CLASS

class Operations:
    def __init__(self) -> None:
        self.operations = {
            "+10": self.Read,
            "+11": self.Write,
            "+20": self.Load,
            "+21": self.Store,
            "+30": self.Add,
            "+31": self.Subtract,
            "+32": self.Divide,
            "+33": self.Multiply,
            "+40": self.Branch,
            "+41": self.BranchNeg,
            "+42": self.BranchZero,
            "+43": self.Halt
        }
    #I/O operators
    #TODO
    def Read(memoryLocation):
        pass
        
    #TODO
    def Write(memoryLocation):
        pass

    #Load/Store operators
    #TODO
    def Load(memoryLocation):
        pass

    #TODO
    def Store(memoryLocation):
        pass

    #Arithmatic operators
    #TODO
    def Add(memoryLocation):
        pass

    #TODO
    def Subtract(memoryLocation):
        pass

    #TODO
    def Divide(memoryLocation):
        pass

    #TODO
    def Multiply(memoryLocation):
        pass

    #Control operators
    #TODO
    def Branch(memoryLocation):
        pass

    #TODO
    def BranchNeg(memoryLocation):
        pass

    #TODO
    def BranchZero(memoryLocation):
        pass

    #TODO
    def Halt():
        pass

def main():
    pass

if __name__ == '__main__':
    main()
