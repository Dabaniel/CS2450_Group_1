"""Module that contains and runs the UVSim Virtual machine"""

class UVSim:
    """Class for UVSim Virtual Machine"""
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

    def load_from_text(self, filename):
        """Opens a text file and parses the content into memory by line"""
        with open(filename, 'r', encoding="utf-8") as file:
            contents = file.read().splitlines()
            for i, content in enumerate(contents):
                self.memory[i] = content

    def get_user_input(self):
        """Simple function that gets user input as a string."""
        user_input = str(input(" "))
        return user_input

    def split_data(self, user_input):
        """Splits the input into a tuple: case, and memory location."""
        if (len(user_input) > 5 or len(user_input) < 5):
            return ValueError
        data = user_input[:3], user_input[3:]
        if data[0][0] != "+":
            return None
        return data

    def check_if_instruction(self, user_input):
        """Checks an input for sign, if sign detected returns True"""
        if user_input[0] == '+':
            return True
        return False

    def case_switch(self, case, memory_location):
        """Switches cases based on the sign and first two integers of the input."""
        try:
            self.operations[case](memory_location)
        except ValueError:
            print('case_switch(): something went horribly wrong!!!')
            return ValueError

    #I/O operators
    def Read(self, memory_location):
        """Reads input from the keyboard and stores in specifed memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Read: Bad input')
            return ValueError
        user_in = input('Insert value to Read: ')
        self.memory[memory_location] = user_in
        self.accumulator[0] += 1

    def Write(self, memory_location):
        """Writes word stored at memory location to console"""
        print(self.memory[int(memory_location)])
        self.accumulator[0] += 1

    #Load/Store operators
    def Load(self, memory_location):
        """Loads word from memory loaction into accumulator"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Load: Bad input')
            return ValueError
        self.accumulator[1] = self.memory[memory_location]
        self.accumulator[0] += 1

    def Store(self, memory_location):
        """Stores word from accumulator into specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        self.memory[memory_location] = self.accumulator[1]
        self.accumulator[0] += 1

    #Arithmatic operators
    def Add(self, memory_location):
        """Add a word from a specific location in memory to the word in the accumulator"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] is None:
            self.accumulator[1] = int(self.memory[memory_location])
        else:
            self.accumulator[1] = int(self.accumulator[1]) + int(self.memory[memory_location])
        self.accumulator[0] += 1

    def Subtract(self, memory_location):
        """Subtract a word from a specific location in memory from the word in the accumulator"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] is None:
            self.accumulator[1] = 0 - int(self.memory[memory_location])
        else:
            self.accumulator[1] = int(self.accumulator[1]) - int(self.memory[memory_location])
        self.accumulator[0] += 1

    def Divide(self, memory_location):
        """Divide the word in the accumilator by the word stored in the specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] is None:
            self.accumulator[1] = 0
        else:
            self.accumulator[1] = int(self.accumulator[1]) / int(self.memory[memory_location])
        self.accumulator[0] += 1

    def Multiply(self, memory_location):
        """Multiply word in the accumilator by the word stored in the specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] is None:
            self.accumulator[1] = 0
        else:
            self.accumulator[1] = int(self.accumulator[1]) * int(self.memory[memory_location])
        self.accumulator[0] += 1

    #Control operators
    def Branch(self, memory_location):
        """Branches to the specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        self.accumulator[0] = memory_location

    def BranchNeg(self, memory_location):
        """Branches to the specified memory location if accumulator is negative"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] < 0:
            self.accumulator[0] = memory_location
        else:
            self.accumulator[0] += 1

    def BranchZero(self, memory_location):
        """Branches to the specified memory location if accumulator is zero"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self.accumulator[1] == 0:
            self.accumulator[0] = memory_location

    def Halt(self, memory_location):
        """Stops the sim"""
        self.accumulator[0] = -1
        self.accumulator[1] = memory_location
