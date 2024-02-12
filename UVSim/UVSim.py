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
        Read(memoryLocation)
    elif (case == "+11"):
        Write(memoryLocation)
    elif (case == "+20"):
        Load(memoryLocation)
    elif (case == "+21"):
        Store(memoryLocation)
    elif (case == "+30"):
        Add(memoryLocation)
    elif (case == "+31"):
        Subtract(memoryLocation)
    elif (case == "+32"):
        Divide(memoryLocation)
    elif (case == "+33"):
        Multiply(memoryLocation)
    elif (case == "+40"):
        Branch(memoryLocation)
    elif (case == "+41"):
        BranchNeg(memoryLocation)
    elif (case == "+42"):
        BranchZero(memoryLocation)
    elif (case == "+43"):
        Halt(memoryLocation)
    else:
        return ValueError
"""
TODO - All of the functions below still need definitions. -Dan
"""
#I/O operators
def Read(memoryLocation):
    
def Write(memoryLocation):

#Load/Store operators
def Load(memoryLocation):
def Store(memoryLocation):

#Arithmatic operators
def Add(memoryLocation):
def Subtract(memoryLocation):
def Divide(memoryLocation):
def Multiply(memoryLocation):

#Control operators
def Branch(memoryLocation):
def BranchNeg(memoryLocation):
def BranchZero(memoryLocation):
def Halt():

def main():
    userInput = GetUserInput()
    while userInput != "":
        inputData = SplitData(userInput)

main()