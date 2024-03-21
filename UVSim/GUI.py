from PySide6.QtWidgets import QAbstractItemView, QMainWindow, QPushButton, QVBoxLayout, QTableWidget, QLabel, QTextEdit, QHBoxLayout, QWidget, QTableWidgetItem # pip install pyside6
from PySide6.QtGui import QPixmap
import os

class QTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BasicML Simulator")
        self.setGeometry(100, 100, 600, 350)
        self.UIsetup()

    def UIsetup(self):
        main_layout = QVBoxLayout()
        display_layout = QHBoxLayout()

        # Memory display
        self.memory_display = QTableWidget(100, 2)
        self.memory_display.setHorizontalHeaderLabels(["Address", "Value"])
        self.memory_display.setFixedWidth(227)
        self.memory_display.setFixedHeight(300)
        memory_layout = QVBoxLayout()
        memory_layout.addWidget(QLabel("Memory"))
        memory_layout.addWidget(self.memory_display)

        labels = []
        for i in range(100):
            self.memory_display.setItem(i, 0, QTableWidgetItem(f"{i:02d}"))
            labels.append("")
        self.memory_display.setVerticalHeaderLabels(labels)
        # immutable table
        self.memory_display.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Registers display
        self.register_display = QTextEdit()
        self.register_display.setFixedWidth(400)
        self.register_display.setFixedHeight(50)

        # Accumulator display
        self.accumulator_display = QTextEdit()
        self.accumulator_display.setFixedWidth(400)
        self.accumulator_display.setFixedHeight(50)


        # Console
        self.console = QTextEdit()
        self.console.setFixedHeight(100)

        # Textbox Layout
        textbox_layout = QVBoxLayout()
        # optional logo placement at eof
        textbox_layout.addStretch()
        textbox_layout.addWidget(QLabel("Register"))
        textbox_layout.addWidget(self.register_display)
        textbox_layout.addWidget(QLabel("Accumulator"))
        textbox_layout.addWidget(self.accumulator_display)
        textbox_layout.addWidget(QLabel("Console"))
        textbox_layout.addWidget(self.console)

        # Setup layout
        display_layout.addLayout(memory_layout)
        display_layout.addStretch()
        display_layout.addLayout(textbox_layout)
        main_layout.addLayout(display_layout)
        main_layout.addStretch()

        # Control buttons
        buttons_layout = QHBoxLayout()
        self.load_button = QPushButton("Load")
        self.run_button = QPushButton("Run")
        self.step_button = QPushButton("Step")
        self.reset_button = QPushButton("Reset")
        buttons_layout.addWidget(self.load_button)
        buttons_layout.addWidget(self.run_button)
        buttons_layout.addWidget(self.step_button)
        buttons_layout.addWidget(self.reset_button)

        main_layout.addLayout(buttons_layout)

        # Setting the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

"""
This is optional if logo image is wanted
self.logo = QLabel(self)
textbox_layout.addWidget(self.logo)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
self.image = QPixmap(os.path.join(__location__, "uvu.png"))
self.image = self.image.scaled(250, 250)
self.logo.setPixmap(self.image)
"""
