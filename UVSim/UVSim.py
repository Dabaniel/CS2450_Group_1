class UVSim:
    def __init__(self) -> None:
        self.memory = [0] * 100
        self.accumulator = 0 #
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


    #Simple function that gets user input as a string.
    def GetUserInput(self):
        userInput = str(input(" "))
        return userInput

    #Splits the input into a tuple: case, and memory location. Has built in check for correct input length and correct sign.
    def SplitData(self, input):
        if (len(input) > 5 or len(input) < 5):
            return ValueError
        data = input[:3], input[3:]
        if (data[0][0] != "+"):
            return None
        return data

    #Switches cases based on the sign and first two integers of the input. This has already been split in the SplitData function
    def CaseSwitch(self, case, memoryLocation):
        try:
            self.operations[case](memoryLocation)
        except:
            print('CaseSwitch(): something went horribly wrong!!!')
            return ValueError
        # if (case == "+10"):
        #     self.Read(int(memoryLocation))
        # elif (case == "+11"):
        #     self.Write(memoryLocation)
        # elif (case == "+20"):
        #     self.Load(int(memoryLocation))
        # elif (case == "+21"):
        #     self.Store(int(memoryLocation))
        # elif (case == "+30"):
        #     pass
        #     #TODO
        #     Add(memoryLocation)
        # elif (case == "+31"):
        #     pass
        #     #TODO
        #     Subtract(memoryLocation)
        # elif (case == "+32"):
        #     pass
        #     #TODO
        #     Divide(memoryLocation)
        # elif (case == "+33"):
        #     pass
        #     #TODO
        #     Multiply(memoryLocation)
        # elif (case == "+40"):
        #     pass
        #     #TODO
        #     Branch(memoryLocation)
        # elif (case == "+41"):
        #     pass
        #     #TODO
        #     BranchNeg(memoryLocation)
        # elif (case == "+42"):
        #     pass
        #     #TODO
        #     BranchZero(memoryLocation)
        # elif (case == "+43"):
        #     pass
        #     #TODO
        #     Halt(memoryLocation)
        # else:
        #     return ValueError

    #I/O operators
    def Read(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Read: Bad input')
            return ValueError
        user_in = input('Insert value to Read: ')
        self.memory[memoryLocation] = user_in

    def Write(self, memoryLocation):
        print(self.memory[int(memoryLocation)])

    #Load/Store operators
    def Load(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Load: Bad input')
            return ValueError
        self.accumulator = self.memory[memoryLocation]

    def Store(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
       self.memory[memoryLocation] = self.accumulator
    
    #Arithmatic operators
    #TODO
    def Add(self, memoryLocation):
        #ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
        self.accumulator = self.accumulator + memoryLocation 
        return self.accumulator

    #TODO
    def Subtract(memoryLocation):
        #Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
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


"""
TODO - All of the functions below still need definitions. -Dan
     - Add each function as method to class. -Anthony
"""

#Arithmatic operators
#TODO
def Add(self, memoryLocation):
    #ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
    self.accumulator = self.accumulator + memoryLocation 
    return self.accumulator

#TODO
def Subtract(memoryLocation):
    #Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
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
    sim = UVSim()
    userInput = sim.GetUserInput()
    while userInput != "":
        inputData = sim.SplitData(userInput)
        sim.CaseSwitch(inputData[0], inputData[1])
        userInput = sim.GetUserInput()

if __name__ == '__main__':
    main()
