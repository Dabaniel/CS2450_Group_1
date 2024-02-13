#Global variables
memory = [0] * 100
register = ""

#Simple function that gets user input as a string.
def GetUserInput():
    userInput = str(input(" "))
    return userInput

#Splits the input into a tuple: case, and memory location. Has built in check for correct input length and correct sign.
def SplitData(input):
    if (input.length > 5 or input.length < 5):
        return ValueError
    data = input[:3], input[3:]
    if (data[0][0] != "+"):
        return None
    return data

#Switches cases based on the sign and first two integers of the input. This has already been split in the SplitData function
def CaseSwitch(case, memoryLocation):
    if (case == "+10"):
        pass
        #TODO
        Read(memoryLocation)
    elif (case == "+11"):
        pass
        #TODO
        Write(memoryLocation)
    elif (case == "+20"):
        pass
        #TODO
        Load(memoryLocation)
    elif (case == "+21"):
        pass
        #TODO
        Store(memoryLocation)
    elif (case == "+30"):
        pass
        #TODO
        Add(memoryLocation)
    elif (case == "+31"):
        pass
        #TODO
        Subtract(memoryLocation)
    elif (case == "+32"):
        pass
        #TODO
        Divide(memoryLocation)
    elif (case == "+33"):
        pass
        #TODO
        Multiply(memoryLocation)
    elif (case == "+40"):
        pass
        #TODO
        Branch(memoryLocation)
    elif (case == "+41"):
        pass
        #TODO
        BranchNeg(memoryLocation)
    elif (case == "+42"):
        pass
        #TODO
        BranchZero(memoryLocation)
    elif (case == "+43"):
        pass
        #TODO
        Halt(memoryLocation)
    else:
        return ValueError
"""
TODO - All of the functions below still need definitions. -Dan
"""

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
    userInput = GetUserInput()
    while userInput != "":
        inputData = SplitData(userInput)

if __name__ == '__main__':
    main()