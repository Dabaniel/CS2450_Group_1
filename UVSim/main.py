from UVSim import UVSim
from GUI import QTGUI
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidgetItem
from PySide6 import QtGui
import sys

class Controller():
    def __init__(self) -> None:
        # GUI dispaly
        app = QApplication(sys.argv)
        self.gui = QTGUI()
        self.gui.show()
        self.button_activation()

        # self.gui = QTGUI()
        self.sim = UVSim()

        # Gui exit handler
        sys.exit(app.exec())

    def button_activation(self):
        """Connect buttons to functions
        """
        self.gui.load_button.clicked.connect(self.load)
        self.gui.run_button.clicked.connect(self.run)
        self.gui.step_button.clicked.connect(self.step)
        self.gui.reset_button.clicked.connect(self.reset)
        self.gui.file_menu.addAction("Load", self.load)
        self.gui.edit_menu.addAction("Toggle Theme", self.gui.change_theme)
        self.gui.help_menu.addAction("About", self.gui.show_version)
        self.gui.help_menu.addAction("Docs", self.gui.show_help)


    def load(self):
        file_path, _ = QFileDialog.getOpenFileName(self.gui, "Open file", "", "All Files (*);;Text Files (*.txt)")
        
        if file_path:
            print(f"Selected file: {file_path}")
            self.sim.load_from_text(file_path)
            stack_memory = self.sim.get_memory()
            for i in range(100):
                self.gui.memory_display.setItem(i, 1, QTableWidgetItem(f"{stack_memory[i] if stack_memory[i] is not None else ''}"))
    
    def step(self):
        self.sim.step()
        stack_memory = self.sim.get_memory()
        for i in range(100):
            self.gui.memory_display.setItem(i, 1, QTableWidgetItem(f"{stack_memory[i] if stack_memory[i] is not None else ''}"))
    
    def run(self):
        self.sim.run()
        stack_memory = self.sim.get_memory()
        for i in range(100):
            self.gui.memory_display.setItem(i, 1, QTableWidgetItem(f"{stack_memory[i] if stack_memory[i] is not None else ''}"))
    

    def reset(self):
        # Placeholder for reset function
        print("Reset")

    def update_regacc(self):
        pass

def run_sim(sim, text_file):
    """Runs the sim with the specified text file"""
    sim.load_from_text(text_file)
    while sim.accumulator[0] >= 0:
        if sim.check_if_instruction(sim.memory[sim.accumulator[0]]):
            data = sim.split_data(sim.memory[sim.accumulator[0]])
            sim.case_switch(data[0], data[1])
        else:
            sim.accumulator[0] += 1

def main():
    """Main function"""
    simple_start = Controller()


if __name__ == '__main__':
    main()
