#THIS FILE WAS USED TO TEST A 2D LIST AGAINST PYTHON'S DICTIONARY
#THE PYTHON DICTIONARY IS SLIGHTLY FASTER

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

#('code name', function)
test_dict = {
    "+10": Read,
    "+11": Write,
    "+20": Load,
    "+21": Store,
    "+30": Add,
    "+31": Subtract,
    "+32": Divide,
    "+33": Multiply,
    "+40": Branch,
    "+41": BranchNeg,
    "+42": BranchZero,
    "+43": Halt
}

test_list = [
    [Read, Write],
    [Load, Store],
    [Add, Subtract, Divide, Multiply],
    [Branch, BranchNeg, BranchZero, Halt]
]

def accessList(opcode):
    return test_list[int(opcode[1]) - 1][int(opcode[2])]

def main():
    print(accessList('+10'))
    print(test_dict['+10'])

if __name__ == '__main__':
    main()