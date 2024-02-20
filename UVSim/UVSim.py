class UVSim:
    def __init__(self) -> None:
        self.memory = [None] * 100
        self.accumulator = [0, "0"] #First is next memory location, second is register content
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
    def LoadFromText(self, filename):
        with open(filename, 'r') as file:
            content = file.read().splitlines()
            for i in range(len(content)):
                self.memory[i] = content[i]

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

    def CheckIfInstruction(self, input):
        if input[0] == '+':
            return True
        return False

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
        self.accumulator[0] += 1

    def Write(self, memoryLocation):
        print(self.memory[int(memoryLocation)])
        self.accumulator[0] += 1

    #Load/Store operators
    def Load(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Load: Bad input')
            return ValueError
        self.accumulator[1] = self.memory[memoryLocation]
        self.accumulator[0] += 1

    def Store(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        self.memory[memoryLocation] = self.accumulator[1]
        self.accumulator[0] += 1
    
    #Arithmatic operators
    def Add(self, memoryLocation):
        #ADD = 30 Add a word from a specific location in memory to the word in the accumulator (leave the result in the accumulator)
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] == None:
            self.accumulator[1] = int(self.memory[memoryLocation])
        else:
            self.accumulator[1] = int(self.accumulator[1]) + int(self.memory[memoryLocation])
        self.accumulator[0] += 1

    def Subtract(self, memoryLocation):
        #Subtract a word from a specific location in memory from the word in the accumulator (leave the result in the accumulator)
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] == None:
            self.accumulator[1] = 0 - int(self.memory[memoryLocation])
        else:
            self.accumulator[1] = int(self.accumulator[1]) - int(self.memory[memoryLocation])
        self.accumulator[0] += 1

    def Divide(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] == None:
            self.accumulator[1] = 0
        else:
            self.accumulator[1] = int(self.accumulator[1]) / int(self.memory[memoryLocation])
        self.accumulator[0] += 1

    def Multiply(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] == None:
            self.accumulator[1] = 0
        else:
            self.accumulator[1] = int(self.accumulator[1]) * int(self.memory[memoryLocation])
        self.accumulator[0] += 1

    #Control operators
    def Branch(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        self.accumulator[0] = memoryLocation

    def BranchNeg(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] < 0:
            self.accumulator[0] = memoryLocation

    def BranchZero(self, memoryLocation):
        try:
            memoryLocation = int(memoryLocation)
        except:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] == 0:
            self.accumulator[0] = memoryLocation

    def Halt(self, memoryLocation):
        self.accumulator[0] = -1

def main():
    sim = UVSim()
    sim.LoadFromText('test2.txt')
    while sim.accumulator[0] >= 0:
        if sim.CheckIfInstruction(sim.memory[sim.accumulator[0]]):
            data = sim.SplitData(sim.memory[sim.accumulator[0]])
            sim.CaseSwitch(data[0], data[1])
        else:
            sim.accumulator[0] += 1
        
    #userInput = sim.GetUserInput()
    #while userInput != "":
    #    inputData = sim.SplitData(userInput)
    #    sim.CaseSwitch(inputData[0], inputData[1])
    #    userInput = sim.GetUserInput()

if __name__ == '__main__':
    main()
