from PySide6.QtWidgets import QAbstractItemView, QMainWindow, QPushButton, QVBoxLayout, \
    QTableWidget, QLabel, QTextEdit, QHBoxLayout, QWidget, QTableWidgetItem, QMenu, QInputDialog, QMessageBox # pip install pyside6

class QTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BasicML Simulator")
        self.setGeometry(100, 100, 600, 350)
        self.theme = "#4C721D"
        self.setStyleSheet(f"background-color: {self.theme};")
        self.UIsetup()

    def UIsetup(self):
        self.main_layout = QVBoxLayout()
        self.display_layout = QHBoxLayout()

        self.create_menu_bar()
        self.create_memory()
        self.create_register()
        self.create_accumulator()
        self.create_console()
        self.create_textbox()
        self.display_main()
        self.create_buttons()

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def create_memory(self):
        self.memory_display = QTableWidget(100, 2)
        self.memory_display.setStyleSheet("background-color: #dbdbdb;")
        self.memory_display.setHorizontalHeaderLabels(["Address", "Value"])
        self.memory_display.setFixedWidth(227)
        self.memory_display.setFixedHeight(300)
        self.memory_layout = QVBoxLayout()
        self.memory_label = QLabel("Memory")
        self.memory_label.setStyleSheet("color: #FFFFFF;")
        self.memory_layout.addWidget(self.memory_label)
        self.memory_layout.addWidget(self.memory_display)

        labels = []
        for i in range(100):
            self.memory_display.setItem(i, 0, QTableWidgetItem(f"{i:02d}"))
            labels.append("")
        self.memory_display.setVerticalHeaderLabels(labels)
        # immutable table
        self.memory_display.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def create_register(self):
        self.register_display = QTextEdit()
        self.register_display.setStyleSheet("background-color: #dbdbdb;")
        self.register_display.setFixedWidth(400)
        self.register_display.setFixedHeight(50)

    def create_accumulator(self):
        self.accumulator_display = QTextEdit()
        self.accumulator_display.setStyleSheet("background-color: #dbdbdb;")
        self.accumulator_display.setFixedWidth(400)
        self.accumulator_display.setFixedHeight(50)

    def create_console(self):
        self.console = QTextEdit()
        self.console.setStyleSheet("background-color: #dbdbdb;")
        self.console.setFixedHeight(100)

    def create_textbox(self):
        self.textbox_layout = QVBoxLayout()
        # optional logo placement at eof
        self.textbox_layout.addStretch()
        self.register_label = QLabel("Register")
        self.register_label.setStyleSheet("color: #FFFFFF;")
        self.textbox_layout.addWidget(self.register_label)
        self.textbox_layout.addWidget(self.register_display)
        self.accumulator_label = QLabel("Accumulator")
        self.accumulator_label.setStyleSheet("color: #FFFFFF;")
        self.textbox_layout.addWidget(self.accumulator_label)
        self.textbox_layout.addWidget(self.accumulator_display)
        
        self.console_label = QLabel("Console")
        self.console_label.setStyleSheet("color: #FFFFFF;")
        self.textbox_layout.addWidget(self.console_label)
        self.textbox_layout.addWidget(self.console_label)
        self.textbox_layout.addWidget(self.console)

    def display_main(self):
        self.display_layout.addLayout(self.memory_layout)
        self.display_layout.addStretch()
        self.display_layout.addLayout(self.textbox_layout)
        self.main_layout.addLayout(self.display_layout)
        self.main_layout.addStretch()
    
    def create_buttons(self):
        buttons_layout = QHBoxLayout()
        self.load_button = QPushButton("Load")
        self.run_button = QPushButton("Run")
        self.step_button = QPushButton("Step")
        self.reset_button = QPushButton("Reset")
        self.load_button.setStyleSheet("background-color: #dbdbdb;")
        self.run_button.setStyleSheet("background-color: #dbdbdb;")
        self.step_button.setStyleSheet("background-color: #dbdbdb;")
        self.reset_button.setStyleSheet("background-color: #dbdbdb;")
        buttons_layout.addWidget(self.load_button)
        buttons_layout.addWidget(self.run_button)
        buttons_layout.addWidget(self.step_button)
        buttons_layout.addWidget(self.reset_button)

        self.main_layout.addLayout(buttons_layout)
    
    def create_menu_bar(self):
        menu_bar = self.menuBar()
        self.file_menu = QMenu("&File", self)
        self.file_menu.setStyleSheet("QMenu{background-color: lightgray;} QMenu::item:selected {color: darkgray;}")
        menu_bar.addMenu(self.file_menu)

        self.edit_menu = QMenu("&Edit", self)
        self.edit_menu.setStyleSheet("QMenu{background-color: lightgray;} QMenu::item:selected {color: darkgray;}")
        menu_bar.addMenu(self.edit_menu)

        self.help_menu = QMenu("&Help", self)
        self.help_menu.setStyleSheet("QMenu{background-color: lightgray;} QMenu::item:selected {color: darkgray;}")
        menu_bar.addMenu(self.help_menu)
    
    def change_theme(self):
        self.theme_dialog = QInputDialog()
        self.theme_dialog.setWindowTitle("Change Theme")
        self.theme_dialog.setLabelText("Enter a hex value to change the theme:")

        _ = self.theme_dialog.exec_()
        if self.theme_dialog.textValue():
            self.setStyleSheet(f"background-color: {self.theme_dialog.textValue()};")

    def show_version(self):
        self.version_dialog = QMessageBox()
        self.version_dialog.setText("Version 0.1.0\nThanks For using UVSim (〃￣︶￣)")

        _ = self.version_dialog.exec_()

    def show_help(self):
        self.help_dialog = QMessageBox()
        self.help_dialog.setStyleSheet("QLabel{min-width: 700px; text-align: left;}")
        # change the following to an updated instruction list
        self.help_dialog.setText("Use the terminal to input commands. The first three characters will be '+XX', where XX is a code for an operation.\ni.e."
                                 "'+11' is WRITE. The next two characters will be a memory address '+XXxx', where xx is the memory address.\n\nEX:"
                                 "Write value in memory location '00' into console: '+1100'\n\nWorking commands:\n\nREAD    / '+10XX': Read the following"
                                 "console input into memory location 'XX'.\n\WRITE   / '+11XX': Write value at memory location 'XX' into console.\nLOAD    /"
                                 "'+20XX': \nSTORE   / '+21XX': \n\nHit enter to close the program")

        _ = self.help_dialog.exec_()

"""
This is optional if logo image is wanted
from PySide6.QtGui import QPixmap
import os
self.logo = QLabel(self)
textbox_layout.addWidget(self.logo)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
self.image = QPixmap(os.path.join(__location__, "uvu.png"))
self.image = self.image.scaled(250, 250)
self.logo.setPixmap(self.image)
"""
