"""Module that contains and runs the UVSim Virtual machine"""

import UVSim
import operations
import buffer

def check_if_instruction(user_input):
    """Checks an input for sign, if sign detected returns True"""
    if user_input[0] == '+' or user_input[0] == '-':
        return 4 < len(user_input)
    return False

def check_if_non_instruction(user_input):
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
    def __init__(self, uvsim: UVSim) -> None:
        self.uvsim = uvsim

    ## GETTERS ##
    def get_accumulator(self):
        return self.uvsim.get_accumulator()
    
    def get_register(self):
        return self.uvsim.get_register()
    
    def get_memory(self):
        return self.uvsim.get_memory()
    
    def get_buffer_bit(self):
        return self.uvsim.get_buffer_bit()
    
    def get_buffer_message(self):
        return self.uvsim.get_buffer_message()
    
    def get_buffer_location(self):
        return self.uvsim.get_buffer_location()
    
    def get_memory_size(self):
        return self.uvsim.get_memory_size()

    ## SETTERS ##
    def set_accumulator(self, value = 0):
        return self.uvsim.set_accumulator(value)
    
    def set_register(self, value = '00'):
        self.uvsim.set_register(value)
    
    def set_data_at_location(self, position, value):
        self.uvsim.set_position_in_memory(position, value)

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
    def __init__(self, buff = None, memory_size = 250) -> None:
        self._memory_size = memory_size
        self._memory = [''] * memory_size
        self._command_length = 5 #3 + len(str(memory_size - 1))
        self.set_command_length = False
        
        self._buffer = buff

        self._operator = operations.Operator(self.get_memory, self.set_position_in_memory, self.get_accumulator, self.set_accumulator, self.get_register, self.set_register, self._buffer)
        
        self._accumulator = [-1, "000"] #First is next memory location, second is register content
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

    ## CALLED ##
    def step(self):
        """Performs the current spot in memory, and proceeds the accumulator"""
        if(self.get_accumulator() < 0):
            #Test to see if program has been halted
            # self.set_accumulator()
            self.Halt()
            return False
        
        if(self._memory[self.get_accumulator()] == '-99999' or self._memory_size - 1 <= self.get_accumulator()):
            #Test to see if program should end
            self.Halt()
            return False
        else:
            #Test to see if correct format to execute
            try:
                if(self._memory[self.get_accumulator()][0] != '+'):
                    self.Nothing()
                    return True
            except:
                self.Nothing()
                return True
            
            try:
                data = self.split_data(self._memory[self.get_accumulator()])
                self._case_switch(data[0], data[1]) #soon to be depreciated
                #TODO, FINISH ALL FUNCTIONS IN OPERATOR
                # self._operator.case_switch(data[0], data[1])
            except:
                print(f"Something went wrong at line {self.get_accumulator()}. The simulation will now halt.")
                self.Halt()
                return False
            
        return True

    def run(self):
        """Runs the rest of the program"""
        # if(self.get_accumulator() < 0):
        #     self.set_accumulator()
        while -1 < self.get_accumulator():
            self.step()

    def load_from_string(self, text):
        """parses the content of a string into memory by line"""
        contents = text
        placeCnt = 0
        load_buffer = []
        for i, content in enumerate(contents):
            #Checks the first detected instruction for length and 
            if (self.set_command_length  is False):
                if(check_if_instruction(content)):
                    if(len(content) == 5):
                        self._command_length = 5
                        self.set_command_length = True
                    if(len(content) == 7):
                        self._command_length = 7
                        self.set_command_length = True
            if(0 < len(content)):
                if(self.check_if_non_instruction(content)):
                    load_buffer.append(content[1:].replace('\\n', '\n'))
                    placeCnt += 1
                content = content.split()[0]
                if(self.check_if_instruction(content)):
                    if self._command_length == 7 and len(content) != 7 and content != "-99999":
                        lengthened_string = content[0] + "0" + content[1:]
                        lengthened_string = lengthened_string[:4] + "0" + lengthened_string[4:]
                        content = lengthened_string
                    load_buffer.append(content)
                    placeCnt += 1
        if(len(load_buffer) < self._memory_size):
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
    
    def get_accumulator(self):
        """Getter for accumulator"""
        return self._accumulator[0]
    
    def get_register(self):
        """Getter for accumulator"""
        return self._accumulator[1]
    
    def get_memory_size(self):
        return self._memory_size
    
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
        self._buffer.set_buffer_bit(value)
    
    def set_buffer_location(self, value = 0):
        """Setter for the buffer bit"""
        self._buffer.set_buffer_location(value)
    
    def set_buffer_message(self, value = ''):
        """Setter for the buffer bit"""
        self._buffer.set_buffer_message(value)

    ## 
    def split_data(self, user_input):
        """Splits the input into a tuple: case, and memory location."""
        if (not len(user_input) == self._command_length):
            return ValueError
        splitpoint = int((len(user_input) + 1) / 2)
        data = user_input[:splitpoint], user_input[splitpoint:]
        if data[0][0] != "+":
            return None
        return data

    def check_if_instruction(self, user_input):
        """Checks an input for sign, if sign detected returns True"""
        if user_input[0] == '+' or user_input[0] == '-':
            return True
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
        if(type(self._buffer) == None):
            user_in = input('Insert value to Read: ')
            self._memory[memory_location] = user_in
        else:
            self._buffer.set_buffer(1, memory_location, '')
        self.add_acc()

    def Write(self, memory_location):
        """Writes word stored at memory location to console"""
        if(type(self._buffer) == None):
            print(self._memory[int(memory_location)])
        else:
            self._buffer.set_buffer(1, memory_location, str(self._memory[int(memory_location)]))
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

    def Halt(self, memory_location = '00'):
        """Stops the sim"""
        self.set_accumulator(-1)
        self._accumulator[1] = memory_location
    
    def Reset(self):
        """Reset the registers"""
        self._accumulator = [0, '0']

    def Reboot(self):
        """Reboot the simulation"""
        self._accumulator = [0, '0']
        self._memory = [''] * self.get_memory_size()

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
