from UVSim import UVSim
from GUI import QTGUI
from PySide6.QtWidgets import QApplication
import sys
import threading

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
    sim1 = UVSim()
    thread_sim = threading.Thread(target=run_sim, args=(sim1, 'test1.txt'))
    thread_sim.start()
    
    app = QApplication(sys.argv)
    window = QTGUI()
    window.show()
    thread_gui = threading.Thread(target=sys.exit, args=(app.exec()))
    thread_gui.start

    


if __name__ == '__main__':
    main()