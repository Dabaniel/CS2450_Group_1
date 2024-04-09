from UVSim import UVSim, I_UVSim
from GUI import QTGUI
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidgetItem
from PySide6 import QtGui
import sys
from functools import partial
import buffer

class Controller():
    def __init__( self ) -> None:
        #Simulation interface
        self.buffer = buffer.Buffer()
        self.sim = I_UVSim( UVSim( self.buffer ) ) # Create a Interface with a UVSim object using its buffer

        #Simulation text source
        self.sim_editor = ''
        self.text_check = ''
        self.file_path = ''

        # GUI dispaly
        app = QApplication( sys.argv )
        self.gui = QTGUI()
        self.gui.show()
        self.button_activation()

        #Update GUI
        self.update_memory()

        # self.gui = QTGUI()

        # Gui exit handler
        sys.exit(app.exec())

    def button_activation( self ):
        """Connect buttons to functions
        """
        # self.gui.load_button.clicked.connect(self.file_load)
        self.gui.halt_button.clicked.connect(self.halt)
        self.gui.run_button.clicked.connect(self.run)
        self.gui.step_button.clicked.connect(self.step)
        self.gui.reset_button.clicked.connect(self.reset)
        self.gui.accumulator_button.clicked.connect(self.set_accumulator)
        self.gui.register_button.clicked.connect(self.set_register)
        self.gui.editor_button.clicked.connect(self.open_editor)
        self.gui.file_menu.addAction("Open New File", self.file_load)
        self.gui.edit_menu.addAction("Toggle Theme", self.gui.change_theme)
        self.gui.help_menu.addAction("About", self.gui.show_version)
        self.gui.help_menu.addAction("Docs", self.gui.show_help)

    def editor_load(self):
        self.sim.load_string(self.sim_editor)
        self.update_memory()
    
    def halt(self):
        if(self.sim.get_accumulator() == -1):
            #unhalt
            self.sim.set_accumulator(0)
        else:
            #halt
            self.sim.halt()

        self.update_memory()

    def file_load(self):
        """
            This function holds the "Load" button and "Load" file menu's functionality:
                Import a file which contains a script for UVSim
            Default to showing only *.txt files, but allow for other types of files to be imported
        """
        file_path, _ = QFileDialog.getOpenFileName(self.gui, "Open file", "", "Text Files (*.txt);;All Files (*)")

        #Confirm a file path was garnered, then insert the file into memory
        if file_path:
            print(f"Selected file: {file_path}")
            with open(file_path, 'r', encoding="utf-8") as file:
                contents = file.read().splitlines()
                new_code = ''
                for i in contents:
                    new_code += i + '\n'
            self.set_sim_editor(new_code)
            # self.sim.load_string(self.sim_editor)
            if(self.gui.new_dialog_id == 'code_editor'):
                self.gui.text_editor.setText(self.sim_editor)
            # self.update_memory()
            self.file_path = file_path
            self.gui.setWindowTitle(f"BasicML Simulator - {file_path.split('/')[-1]} (1/1)")
    
    def step(self, in_run = False):
        """Increment the simulation by one step"""
        self.sim.step()
        if(self.buffer.get_buffer_bit()):
            self.buffer.set_buffer_bit()
            buffer = self.buffer.get_buffer_message()
            if(len(buffer)):
                self.append_console(buffer)
            else:
                ret = self.gui.insert_Read()
                self.sim.set_data_at_location(self.buffer.get_buffer_location(), ret)
                self.append_console(str(ret))
            if(in_run):
                self.update_memory()
        if(not in_run):
            self.update_memory()
    
    def run(self):
        while -1 < self.sim.get_accumulator():
            self.step(True)
        self.update_memory()

    def reset(self):
        self.sim.load_string(self.sim_editor)
        self.sim.set_register()
        self.sim.set_accumulator()
        self.clear_console()
        self.update_memory()

    def append_console(self, info: str):
        self.gui.console.append(info)

    def clear_console(self):
        self.gui.console.setText()

    def set_register(self):
        ret = self.gui.change_register()
        if(False):
            self.custom_alert()
        else:
            self.sim.set_register(ret)
            self.update_register()

    def set_accumulator(self):
        ret = self.gui.change_accumulator()
        if(ret < 0 or len(self.sim.get_memory()) <= ret):
            self.custom_alert()
        else:
            self.sim.set_accumulator(ret)
            self.update_accumulator()
    
    def open_editor(self):
        self.gui.code_editor(self.sim_editor)
        
        self.gui.text_editor.textChanged.connect(self.set_code)
        self.gui.code_load_button.clicked.connect(partial(self.sim.load_string, self.sim_editor))
        self.gui.code_load_button.clicked.connect(self.editor_load)
        self.gui.export_button.clicked.connect(self.gui.name_export)
        self.gui.export_button.clicked.connect(self.export_code)
        self.gui.editor_load_button.clicked.connect(self.file_load)

        _ = self.gui.new_dialog.exec()
        if(False):
            self.custom_alert()
        else:
            try:
                self.set_sim_editor(self.gui.text_editor.toPlainText())
            except:
                self.custom_alert('Compiler Error', 'Code did not compile properly')
        self.gui.close_dialog()
    
    # def change_code_editor(self):
    #     self.change_code_editor() # ret = 
    #     try:
    #         return self.gui.text_editor.toPlainText()
    #     except:
    #         return None
    
    def export_code(self):
        with open(self.gui.file_name, "w") as export_file:
            export_file.write(self.sim_editor)
    
    def set_code(self):
        self.sim_editor = self.gui.text_editor.toPlainText()
        self.text_check = self.gui.text_editor.toPlainText()
    
    def set_sim_editor(self, value):
        self.sim_editor = value
        #TODO detect if QWizard is open, then set text
        if(False):
            pass

    def custom_alert(self, title = "About your input...", desc = "The input provided was not proper!"):
        self.gui.custom_alert(title, desc)

    def update_memory(self):
        stack_memory = self.sim.get_memory()
        for i in range(100):
            self.gui.memory_display.setItem(i, 1, QTableWidgetItem(f"{stack_memory[i] if stack_memory[i] is not None else ''}"))
            self.gui.memory_display.setItem(i, 2, QTableWidgetItem(""))
        cnt = self.sim.get_accumulator()
        if(0 <= cnt and cnt < len(stack_memory)):
            self.gui.memory_display.setItem(cnt, 2, QTableWidgetItem(f"<- {cnt}"))
        self.update_register()
        self.update_accumulator()
        if(self.sim.get_accumulator() == -1):
            #unhalt
            self.gui.halt_button.setText("Unhalt")
        else:
            #halt
            self.gui.halt_button.setText("Halt")

    def update_register(self):
        self.gui.register_button.setText(f"Register: '{self.sim.get_register()}'")

    def update_accumulator(self):
        self.gui.accumulator_button.setText(f"Accumulator: {self.sim.get_accumulator()}")
