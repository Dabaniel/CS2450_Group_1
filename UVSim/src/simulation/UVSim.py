"""Module that contains and runs the UVSim Virtual machine"""
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import simulation.operations as operations
import controllers.buffer as buffer

def check_if_instruction(user_input):
    """Checks an input for sign, if sign detected returns True"""
    if user_input[0] == '+' or user_input[0] == '-':
        return True
    return False

def check_if_non_instruction(user_input):
    return user_input[0] == '&'

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
                    self._operator.Nothing()
                    return True
            except:
                self._operator.Nothing()
                return True
            
            try:
                data = self.split_data(self._memory[self.get_accumulator()])
                self._operator.case_switch(data[0], data[1])
            except:
                print(f"Something went wrong at line {self.get_accumulator()}. The simulation will now halt.")
                self._buffer.set_buffer(1, self.get_accumulator(), f"Something went wrong at line {self.get_accumulator()}. The simulation will now halt.")
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
            if(0 < len(content)):
                if (self.set_command_length is False):
                    if(check_if_instruction(content)):
                        if(len(content) == 5):
                            self._command_length = 5
                            self.set_command_length = True
                        if(len(content) == 7):
                            self._command_length = 7
                            self.set_command_length = True
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
        else:
            #TODO give a valid error for when code exceeds memory limit
            raise ValueError('your code too long :(')
        self.Halt()

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

    def Halt(self, memory_location = '00'):
        """Stops the sim"""
        self._operator.Halt(memory_location)
    
    def Reset(self):
        """Reset the registers"""
        self._accumulator = [0, '0']

    def Reboot(self):
        """Reboot the simulation"""
        self._accumulator = [0, '0']
        self._memory = [''] * self.get_memory_size()

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

    def load_list(self, text):
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