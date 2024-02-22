from PySide6.QtWidgets import QMainWindow, QPushButton # pip install pyside6

class QTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple GUI")
        self.setGeometry(100, 100, 200, 100)

        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_clicked)  # Connect the button's clicked signal to a method
        self.button.setGeometry(50, 20, 100, 50)
    
    def on_button_clicked(self):
        print("test button out")
