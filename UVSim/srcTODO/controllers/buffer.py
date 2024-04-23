

class Buffer():
    def __init__(self):
        self._buffer_bit = 0
        self._buffer_location = 0
        self._buffer_message = ''
    
    def set_buffer(self, bit = 0, location = 0, message = ''):
        self.set_buffer_bit(bit)
        self.set_buffer_location(location)
        self.set_buffer_message(message)
    
    def set_buffer_bit(self, bit = 0):
        self._buffer_bit = bit
    
    def set_buffer_location(self, location = 0):
        self._buffer_location = location
    
    def set_buffer_message(self, message = ''):
        self._buffer_message = message
    
    def get_buffer(self):
        return self.get_buffer_bit(), self.get_buffer_location(),  self.get_buffer_message()
    
    def get_buffer_bit(self):
        return self._buffer_bit
    
    def get_buffer_location(self):
        return self._buffer_location
    
    def get_buffer_message(self):
        return self._buffer_message