"""Module that contains and runs the UVSim Virtual machine"""

import UVSim

def check_if_instruction( user_input ):
    """Checks an input for sign, if sign detected returns True"""
    if user_input[0] == '+' or user_input[0] == '-':
        return 4 < len(user_input)
    return False

def check_if_non_instruction( user_input ):
    return user_input[0] == '&'

class I_UVSim():
    """
        Interface for UVSim
            This is an interface for the UVSim class. Here are the interface's capabilities:
        -- METHODS --
        Getters:
            get_accumulator()
            get_register()
            get_memory()

        Setters:
            set_accumulator(value)
            set_register(value)
            set_data_at_location(position, value)
            load_text_file(file)
            load_string(text)
            step()
            run()
            halt()
            reboot()
    """
    def __init__( self, uvsim: UVSim ) -> None:
        self.uvsim = uvsim

    ## GETTERS ##
    def get_accumulator( self ):
        return self.uvsim.get_acc()[0]
    
    def get_register( self ):
        return self.uvsim.get_acc()[1]
    
    def get_memory( self ):
        return self.uvsim.get_memory()
    
    def get_buffer_bit( self ):
        return self.uvsim.get_buffer_bit()
    
    def get_buffer_message( self ):
        return self.uvsim.get_buffer_message()
    
    def get_buffer_location( self ):
        return self.uvsim.get_buffer_location()

    ## SETTERS ##
    def set_accumulator(self, value = 0):
        return self.uvsim.set_accumulator(value)
    
    def set_register(self, value = '00'):
        self.uvsim.set_register(value)
    
    def set_data_at_location(self, position, value):
        self.uvsim.set_position_in_memory(position, value)
    
    def set_buffer_bit(self, value = 0):
        self.uvsim.set_buffer_bit(value)
    
    def set_buffer_message(self, value = '' ):
        self.uvsim.set_buffer_message(value)
    
    def set_buffer_location(self, value = '' ):
        self.uvsim.set_buffer_location(value)

    def load_text_file(self, file):
        """Load code from a .txt file"""
        self.uvsim.load_from_text(file)

    def load_string(self, text):
        """Load code from a string"""
        self.uvsim.load_from_string(text)

    def step(self):
        self.uvsim.step()

    def run(self):
        self.uvsim.run()

    def halt(self):
        self.uvsim.Halt()

    def reboot(self):
        self.uvsim.Reboot()

class UVSim:
    """Class for UVSim Virtual Machine"""
    def __init__(self, using_buffer = False) -> None:
        self._default_memory = [None] * 100
        self._memory = []
        self._using_buffer = using_buffer
        self._buffer = [0, 0, ''] #First is the buffer bit, second is the buffer contents
        for i in self._default_memory:
            self._memory.append(i)
        self._accumulator = [0, "00"] #First is next memory location, second is register content
        self._step_limit = 90 #The last possible point to leave an operation before the memory for the operations start
        self._operations = {
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

    ## CALLED ##
    def step(self):
        """Performs the current spot in memory, and proceeds the accumulator"""
        if(self.get_acc()[0] < 0):
            #Test to see if program has been halted
            self.set_accumulator()
        
        if(self._memory[self.get_acc()[0]] == '-99999' or self._step_limit - 1 <= self.get_acc()[0]):
            #Test to see if program should end
            self.Halt()
            return False
        else:
            #Test to see if correct format to execute
            try:
                if(self._memory[self.get_acc()[0]][0] != '+'):
                    self.Nothing()
                    return True
            except:
                self.Nothing()
                return True
            
            try:
                data = self.split_data(self._memory[self.get_acc()[0]])
                self._case_switch(data[0], data[1])
            except:
                print(f"Something went wrong at line {self.get_acc()[0]}. The simulation will now halt.")
                self.Halt()
                return False
            
        return True

    def run(self):
        """Runs the rest of the program"""
        if(self.get_acc()[0] < 0):
            self.set_accumulator()
        while -1 < self.get_acc()[0]:
            self.step()

    def load_from_string(self, text):
        """parses the content of a string into memory by line"""
        contents = text.splitlines()
        placeCnt = 0
        load_buffer = []
        for i, content in enumerate(contents):
            if(0 < len(content)):
                if(self.check_if_non_instruction(content)):
                    load_buffer.append(content[1:].replace('\\n', '\n'))
                    placeCnt += 1
                content = content.split()[0]
                if(self.check_if_instruction(content)):
                    load_buffer.append(content)
                    placeCnt += 1
        if(len(load_buffer) < self._step_limit):
            for i, content in enumerate(load_buffer):
                self._memory[i] = content

    def load_from_text(self, filename):
        """Opens a text file and parses the content into memory by line"""
        with open(filename, 'r', encoding="utf-8") as file:
            self.load_from_string(file.read())

    ## GETTERS/SETTERS ##
    
    def get_memory(self):
        """Getter for memory"""
        return self._memory
    
    def get_acc(self):
        """Getter for accumulator"""
        return self._accumulator
    
    def get_buffer_bit( self ):
        """Setter for the buffer bit"""
        return self._buffer[0]
    
    def get_buffer_location( self ):
        """Setter for the buffer bit"""
        return self._buffer[1]
    
    def get_buffer_message( self ):
        """Setter for the buffer bit"""
        return self._buffer[2]
    
    def set_accumulator(self, a = 0):
        """Setter for accumulator"""
        self._accumulator[0] = int(a)
    
    def set_register(self, a):
        """Setter for accumulator"""
        self._accumulator[1] = a
    
    def add_acc(self, a = 1):
        self._accumulator[0] += a
    
    def set_position_in_memory(self, position, value):
        """Setter for memory"""
        self._memory[position] = value
    
    def set_buffer_bit(self, value = 0):
        """Setter for the buffer bit"""
        self._buffer[0] = value
    
    def set_buffer_location(self, value = ''):
        """Setter for the buffer bit"""
        self._buffer[1] = value
    
    def set_buffer_message(self, value = ''):
        """Setter for the buffer bit"""
        self._buffer[2] = value

    ## 
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
        if user_input[0] == '+' or user_input[0] == '-':
            return 4 < len(user_input)
        return False

    def check_if_non_instruction(self, user_input):
        return user_input[0] == '&'

    def _case_switch(self, case, memory_location):
        """Switches cases based on the sign and first two integers of the input."""
        try:
            self._operations[case](memory_location)
        except ValueError:
            print('_case_switch(): something went horribly wrong!!!')
            self.Halt()
            return ValueError

    #I/O operators
    def Nothing(self):
        """Placeholder"""
        self.add_acc()

    def Read(self, memory_location):
        """Reads input from the keyboard and stores in specifed memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Read: Bad input')
            return ValueError
        #TODO: get this input to communicate with main.py to open up an input dialog
        if(not self._using_buffer):
            user_in = input('Insert value to Read: ')
            self._memory[memory_location] = user_in
        else:
            self.set_buffer_bit(1)
            self.set_buffer_message('')
            self.set_buffer_location(memory_location)
        self.add_acc()

    def Write(self, memory_location):
        """Writes word stored at memory location to console"""
        if(not self._using_buffer):
            print(self._memory[int(memory_location)])
        else:
            self.set_buffer_bit(1)
            self.set_buffer_message(str(self._memory[int(memory_location)]))
            self.set_buffer_location(memory_location)
        self.add_acc()

    #Load/Store operators
    def Load(self, memory_location):
        """Loads word from memory loaction into accumulator"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Load: Bad input')
            return ValueError
        self._accumulator[1] = self._memory[memory_location]
        self.add_acc()

    def Store(self, memory_location):
        """Stores word from accumulator into specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        self._memory[memory_location] = self._accumulator[1]
        self.add_acc()

    #Arithmatic operators
    def Add(self, memory_location):
        """Add a word from a specific location in memory to the word in the accumulator"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self._accumulator[1] is None:
            self._accumulator[1] = int(self._memory[memory_location])
        else:
            self._accumulator[1] = int(self._accumulator[1]) + int(self._memory[memory_location])
        self.add_acc()

    def Subtract(self, memory_location):
        """Subtract a word from a specific location in memory from the word in the accumulator"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self._accumulator[1] is None:
            self._accumulator[1] = 0 - int(self._memory[memory_location])
        else:
            self._accumulator[1] = int(self._accumulator[1]) - int(self._memory[memory_location])
        self.add_acc()

    def Divide(self, memory_location):
        """Divide the word in the accumilator by the word stored in the specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self._accumulator[1] is None:
            self._accumulator[1] = 0
        else:
            self._accumulator[1] = int(self._accumulator[1]) / int(self._memory[memory_location])
        self.add_acc()

    def Multiply(self, memory_location):
        """Multiply word in the accumilator by the word stored in the specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self._accumulator[1] is None:
            self._accumulator[1] = 0
        else:
            self._accumulator[1] = int(self._accumulator[1]) * int(self._memory[memory_location])
        self.add_acc()

    #Control operators
    def Branch(self, memory_location):
        """Branches to the specified memory location"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        self.set_accumulator(memory_location)

    def BranchNeg(self, memory_location):
        """Branches to the specified memory location if accumulator is negative"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self._accumulator[1] < 0:
            self.set_accumulator(memory_location)
        else:
            self.add_acc()

    def BranchZero(self, memory_location):
        """Branches to the specified memory location if accumulator is zero"""
        try:
            memory_location = int(memory_location)
        except ValueError:
            print('Store: Bad input')
            return ValueError
        if self._accumulator[1] == 0:
            self.set_accumulator(memory_location)

    def Halt(self, memory_location = '0'):
        """Stops the sim"""
        self.set_accumulator(-1)
        self._accumulator[1] = memory_location
    
    def Reset(self):
        """Reset the registers"""
        self._accumulator = [0, '0']

    def Reboot(self):
        """Reboot the simulation"""
        self._accumulator = [0, '0']
        self._memory = []
        for i in self._default_memory:
            self._memory.append(i)

def main():
    test_the_sim = UVSim()
    test_the_sim.load_from_string("""
//Test operations Read, Write, Load, Store, Add

+1112 //print "This is a really..."
+1010 //take in first value
+1113 //print "Value 2:"
+1011 //take in second value
+2011 //load second into register
+3010 //add register with first value
+2111 //stores output
+1114 //print closing message
+1111 //print addition
+4300 //End program
&
&
&This is a really dumb calculator. Insert two values to add them together.\nValue one: 
&Value 2: 
&Your value is:
-99999""")
    print(test_the_sim.get_memory())

    test_sim = I_UVSim(UVSim())
    test_input = 'h'
    while True:
        if(test_input[0] == 'm'):
            print(f'Memory: {test_sim.get_memory()}')
        elif(test_input[0] == 'a'):
            print(f'Accumulator: {test_sim.get_accumulator()}\nRegister: {test_sim.get_register()}')
        elif(test_input[0] == 's'):
            test_sim.step()
        elif(test_input[0] == 'r'):
            test_sim.run()
        elif(test_input[0] == 'i'):
            pass
            while True:
                position = input('--Type the desired position in memory (0-99): ')
                if(position == 'q'):
                    break
                try:
                    position = int(position)
                    test_sim.set_data_at_location(position, input('--List the desired value to insert: '))
                    break
                except:
                    print('Invalid Input.')
        elif(test_input[0] == 'f'):
            try:
                test_sim.load_text_file(input('--Share the name of the file you want to pass into the simulation: '))
            except:
                print('Huh. Something went wrong with UVSim -> load_from_text()')
        elif(test_input[0] == 't'):
            test_sim.halt()
            test_sim.reboot()
        elif(test_input[0] == 'p'):
            test_sim.set_accumulator(input('Value for accumulator: '))
        elif(test_input[0] == 'c'):
            test_memory = test_sim.get_memory()
            buffer_memory = []
            for i in test_memory:
                if(type(i) == type(None)):
                    buffer_memory.append('')
                else:
                    i = str(i)
                    if(len(i) == 0):
                        buffer_memory.append('&')
                    else:
                        buffer_memory.append('&' * (not check_if_instruction(i)) + i.replace('\n', '\\n'))
                    for i in buffer_memory:
                        print(i)
                    buffer_memory = []
        elif(test_input[0] == 'h'):
            print('\nRunning a console version of UVSim. Here are the commands:\nm/memory = print memory\na/accumulator = print registers\ns/step = step\nr/run = run\nt/terminate = halt program\np/point = set accumulator\ni/insert = insert command at memory location\nc/copy = copy code from memory\nh/help = help dialogue\nq/quit = quit')
        elif(test_input[0] == 'q'):
            print('The script will now terminate. Have a day.\n')
            break
        else:
            print("That didn't seem to match any existing commands. Type \"h\" or \"help\" for the list of valid commands.")
        
        test_input = input('\n  --Next course of action: ')

if __name__ == '__main__':
    main()