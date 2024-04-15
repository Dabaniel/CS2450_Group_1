from UVSim import UVSim, I_UVSim
from GUI import QTGUI
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidgetItem
from PySide6 import QtGui
import sys
from functools import partial
import buffer

class Controller():
    def __init__(self) -> None:
        #Simulation text source
        self.current_file = 0
        self.sim_editors = ['']
        self.file_paths = ['']
        self.buffers = [buffer.Buffer()]
        self.sims = [I_UVSim(UVSim(self.buffers[0]))]
        self.sim_editor = self.sim_editors[self.current_file]
        self.file_path = self.file_paths[self.current_file]
        
        #Simulation interface
        self.buffer = self.buffers[self.current_file]
        self.sim = self.sims[self.current_file] # Create a Interface with a UVSim object using its buffer
        
        # GUI dispaly
        app = QApplication(sys.argv)
        self.gui = QTGUI()
        self.gui.show()
        self.button_activation()

        #Update GUI
        self.update_memory()

        # self.gui = QTGUI()

        # Gui exit handler
        sys.exit(app.exec())

    def button_activation(self):
        """Connect buttons to functions
        """
        # self.gui.load_button.clicked.connect(self.file_load)
        self.gui.halt_button.clicked.connect(self.halt)
        self.gui.run_button.clicked.connect(self.run)
        self.gui.step_button.clicked.connect(self.step)
        # self.gui.reset_button.clicked.connect(self.reset)
        self.gui.accumulator_button.clicked.connect(self.set_accumulator)
        self.gui.register_button.clicked.connect(self.set_register)
        self.gui.next_file_button.clicked.connect(self.next_file)
        self.gui.previous_file_button.clicked.connect(self.prev_file)
        self.gui.editor_button.clicked.connect(self.open_editor)
        self.gui.file_menu.addAction("Open New Page", self.new_file)
        theme = self.gui.edit_menu.addMenu("Change Theme")
        theme.addAction("Main Theme", self.gui.change_main_theme)
        theme.addAction("Off Theme", self.gui.change_off_theme)
        # theme.addAction("Off Theme", self.gui.change_off_theme)
        # theme.addAction("Text Theme", self.gui.change_text_theme)
        
        self.gui.help_menu.addAction("About", self.gui.show_version)
        self.gui.help_menu.addAction("Docs", self.gui.show_help)

    def editor_load(self):
        self.sim.load_list(self.sim_editor.splitlines())
        self.update_memory()
    
    def halt(self):
        if(self.sim.get_accumulator() == -1):
            #unhalt
            self.sim.set_accumulator(0)
        else:
            #halt
            self.sim.halt()

        self.update_memory()

    def save_file(self):
        try:
            with open(self.file_path, 'w') as file:
                file.write(self.sim_editor)
        except:
            self.custom_alert('File Error', 'Invalid directory')

    def next_file(self):
        if(self.current_file < len(self.file_paths) - 1):
            self.current_file += 1
            
            self.buffer = self.buffers[self.current_file]
            self.sim = self.sims[self.current_file]
            self.sim_editor = self.sim_editors[self.current_file]
            self.file_path = self.file_paths[self.current_file]
            if(self.file_path == ''):
                self.gui.setWindowTitle(f"BasicML Simulator - No File Opened ({self.current_file + 1}/{len(self.file_paths)})")
            else:
                self.gui.setWindowTitle(f"BasicML Simulator - {self.file_path.split('/')[-1]} ({self.current_file + 1}/{len(self.file_paths)})")
            self.update_memory()

    def prev_file(self):
        if(0 < self.current_file):
            self.current_file -= 1
            
            self.buffer = self.buffers[self.current_file]
            self.sim = self.sims[self.current_file]
            self.sim_editor = self.sim_editors[self.current_file]
            self.file_path = self.file_paths[self.current_file]
            if(self.file_path == ''):
                self.gui.setWindowTitle(f"BasicML Simulator - No File Opened ({self.current_file + 1}/{len(self.file_paths)})")
            else:
                self.gui.setWindowTitle(f"BasicML Simulator - {self.file_path.split('/')[-1]} ({self.current_file + 1}/{len(self.file_paths)})")
            self.update_memory()

    def new_file(self):
        self.current_file = len(self.file_paths)
        self.sim_editors.append('')
        self.file_paths.append('')
        self.buffers.append(buffer.Buffer())
        self.sims.append(I_UVSim(UVSim(self.buffers[self.current_file])))
        
        self.buffer = self.buffers[self.current_file]
        self.sim = self.sims[self.current_file]
        self.sim_editor = self.sim_editors[self.current_file]
        self.file_path = self.file_paths[self.current_file]
        self.gui.setWindowTitle(f"BasicML Simulator - No File Opened ({self.current_file + 1}/{len(self.file_paths)})")

        self.update_memory()
    
    def remove_file(self):
        if(1 < len(self.file_paths)):
            self.sim_editor.remove(self.current_file)
            self.sims.remove(self.current_file)
            self.buffers.remove(self.current_file)
            self.file_paths.remove(self.current_file)
    
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
            # self.sim.load_list(self.sim_editor)
            if(self.gui.new_dialog_id == 'code_editor'):
                self.gui.text_editor.setText(self.sim_editor)
            self.sim.load_list(contents)
            self.update_memory()
            self.file_path = file_path
            self.gui.setWindowTitle(f"BasicML Simulator - {file_path.split('/')[-1]} ({self.current_file + 1}/{len(self.file_paths)})")
    
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
        self.sim.load_list(self.sim_editor.splitlines())
        self.sim.set_register()
        self.sim.set_accumulator()
        self.clear_console()
        self.update_memory()

    def append_console(self, info: str):
        self.gui.console.append(info)

    def clear_console(self):
        self.gui.console.setText('')

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
        self.gui.code_load_button.clicked.connect(partial(self.sim.load_list, self.sim_editor.splitlines()))
        self.gui.code_load_button.clicked.connect(self.editor_load)
        self.gui.save_button.clicked.connect(self.save_file)
        self.gui.clear_console_button.clicked.connect(self.clear_console)
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
        try:
            with open(self.gui.file_name, "w") as export_file:
                export_file.write(self.sim_editor)
        except:
            self.custom_alert('File Error', 'Invalid directory')

    def set_code(self):
        self.sim_editor = self.gui.text_editor.toPlainText()
    
    def set_sim_editor(self, value):
        self.sim_editor = value
        #TODO detect if QWizard is open, then set text
        if(False):
            pass

    def custom_alert(self, title = "About your input...", desc = "The input provided was not proper!"):
        self.gui.custom_alert(title, desc)

    def update_memory(self):
        stack_memory = self.sim.get_memory()
        for i in range(250):
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
            self.gui.register_button.setEnabled(False)
            self.gui.accumulator_button.setEnabled(False)
            self.gui.step_button.setEnabled(False)
            self.gui.run_button.setEnabled(False)
        else:
            #halt
            self.gui.halt_button.setText("Halt")
            self.gui.register_button.setEnabled(True)
            self.gui.accumulator_button.setEnabled(True)
            self.gui.step_button.setEnabled(True)
            self.gui.run_button.setEnabled(True)

    def update_register(self):
        self.gui.register_button.setText(f"Register: '{self.sim.get_register()}'")

    def update_accumulator(self):
        self.gui.accumulator_button.setText(f"Accumulator: {self.sim.get_accumulator()}")
