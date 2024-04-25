#OPERATIONS CLASS

class Operator:
    def __init__(self, memory_getter, memory_setter, acc_getter, acc_setter, reg_getter, reg_setter, buff) -> None:
        self._get_memory = memory_getter
        self._set_memory = memory_setter
        self._get_accumulator = acc_getter
        self._set_accumulator = acc_setter
        self._get_register = reg_getter
        self._set_register = reg_setter
        self._buffer = buff

        self._operations = {            
            "+10": self.Read,
            "+010": self.Read,
            "+11": self.Write,
            "+011": self.Write,
            "+20": self.Load,
            "+020": self.Load,
            "+21": self.Store,
            "+021": self.Store,
            "+30": self.Add,
            "+030": self.Add,
            "+31": self.Subtract,
            "+031": self.Subtract,
            "+32": self.Divide,
            "+032": self.Divide,
            "+33": self.Multiply,
            "+033": self.Multiply,
            "+40": self.Branch,
            "+040": self.Branch,
            "+41": self.BranchNeg,
            "+041": self.BranchNeg,
            "+42": self.BranchZero,
            "+042": self.BranchZero,
            "+43": self.Halt,
            "+043": self.Halt
        }
    
    def _add_acc(self, add = 1):
        self._set_accumulator(self._get_accumulator() + add)
    
    def case_switch(self, case, memory_location):
        """Switches cases based on the sign and first two integers of the input."""
        try:
            self._operations[case](memory_location)
        except ValueError:
            print('_case_switch(): something went horribly wrong!!!')
            self.Halt()
            return ValueError
    
    def Nothing(self):
        """Placeholder"""
        self._add_acc()

    #I/O operators
    def Read(self, memory_location):
        """Reads input from the keyboard and stores in specifed memory location"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Read: Bad input')
            return ValueError
        if(type(self._buffer) == None):
            user_in = input('Insert value to Read: ')
            self._set_memory(mem_loc, user_in)
        else:
            self._buffer.set_buffer(1, mem_loc, '')
        self._add_acc()
    
    def Write(self, memory_location):
        """Writes word stored at memory location to console"""
        if(type(self._buffer) == None):
            print(self._memory[int(memory_location)])
        else:
            self._buffer.set_buffer(1, int(memory_location), str(self._get_memory()[int(memory_location)]))
        self._add_acc()

    #Load/Store operators
    def Load(self, memory_location):
        """Loads word from memory loaction into accumulator"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Load: Bad input')
            return ValueError
        self._set_register(self._get_memory()[mem_loc])
        self._add_acc()

    def Store(self, memory_location):
        """Stores word from accumulator into specified memory location"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        self._set_memory(mem_loc, self._get_register())
        self._add_acc()

    #Arithmatic operators
    def Add(self, memory_location):
        """Add a word from a specific location in memory to the word in the accumulator"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Add: Bad input')
            return ValueError
        if self._get_register() is None:
            self._set_register(int(self._get_memory()[mem_loc]))
        else:
            self._set_register(int(self._get_register()) + int(self._get_memory()[mem_loc]))
        self._add_acc()

    def Subtract(self, memory_location):
        """Subtract a word from a specific location in memory from the word in the accumulator"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Subtract: Bad input')
            return ValueError
        if self._get_register() is None:
            self._set_register(0 - int(self._get_memory()[mem_loc]))
        else:
            self._set_register(int(self._get_register()) - int(self._get_memory()[mem_loc]))
        self._add_acc()
        
    def Divide(self, memory_location):
        """Divide the word in the accumilator by the word stored in the specified memory location"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Divide: Bad input')
            return ValueError
        if self._get_register() is None:
            self._set_register(0)
        else:
            self._set_register(int(self._get_register()) / int(self._get_memory()[mem_loc]))
        self._add_acc()
        
    def Multiply(self, memory_location):
        """Multiply word in the accumilator by the word stored in the specified memory location"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Multiply: Bad input')
            return ValueError
        if self._get_register() is None:
            self._set_register(0)
        else:
            self._set_register(int(self._get_register()) * int(self._get_memory()[mem_loc]))
        self._add_acc()

    #Control operators
    #TODO
    def Branch(self, memory_location):
        """Branches to the specified memory location"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('Branch: Bad input')
            return ValueError
        self._set_accumulator(mem_loc)

    def BranchNeg(self, memory_location):
        """Branches to the specified memory location if accumulator is negative"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('BranchNeg: Bad input')
            return ValueError
        try:
            if int(self._get_register()) < 0:
                self._set_accumulator(mem_loc)
            else:
                self._add_acc()
        except ValueError:
            print('BranchNeg: Bad input')
            return ValueError

    def BranchZero(self, memory_location):
        """Branches to the specified memory location if accumulator is zero"""
        mem_loc = 0
        try:
            mem_loc = int(memory_location)
        except ValueError:
            print('BranchZero: Bad input')
            return ValueError
        try:
            if int(self._get_register()) == 0:
                self._set_accumulator(mem_loc)
            else:
                self._add_acc()
        except ValueError:
            print('BranchZero: Bad input')
            return ValueError

    def Halt(self, memory_location = '00'):
        """Stops the sim"""
        self._set_accumulator(-1)
        self._set_register(memory_location)

def main():
    pass

if __name__ == '__main__':
    main()
