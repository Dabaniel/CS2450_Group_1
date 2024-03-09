from PySide6.QtWidgets import QAbstractItemView, QMainWindow, QPushButton, QVBoxLayout, QTableWidget, QLabel, QTextEdit, QHBoxLayout, QWidget, QTableWidgetItem # pip install pyside6

class QTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BasicML Simulator")
        self.setGeometry(100, 100, 800, 600)
        self.UIsetup()

    def UIsetup(self):
        main_layout = QVBoxLayout()

        # Memory display
        self.memory_display = QTableWidget(100, 2)
        self.memory_display.setHorizontalHeaderLabels(["Address", "Value"])
        main_layout.addWidget(QLabel("Memory"))
        main_layout.addWidget(self.memory_display)

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

        main_layout.addWidget(QLabel("Register"))
        main_layout.addWidget(self.register_display)

        # Accumulator display
        self.accumulator_display = QTextEdit()
        self.accumulator_display.setFixedWidth(400)
        self.accumulator_display.setFixedHeight(50)

        main_layout.addWidget(QLabel("Accumulator"))
        main_layout.addWidget(self.accumulator_display)

        # Console
        self.console = QTextEdit()
        self.console.setFixedHeight(100)
        main_layout.addWidget(QLabel("Console"))
        main_layout.addWidget(self.console)

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

        

    
    # Move button functions and self.uvsim to facade in main.py

    # def load(self):
    #     file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "All Files (*);;Text Files (*.txt)")
        
    #     if file_path:
    #         print(f"Selected file: {file_path}")
    #         stack_memory = self.sim.get_memory()
    #         print(stack_memory)
    #         for i in range(100):
    #             self.memory_display.setItem(i, 1, QTableWidgetItem(f"{stack_memory[i]}")) # add ternary to remove Nones

    # def step(self):
    #     pass

    # def run(self):
    #     # Placeholder for run function
    #     print("Run")

    # def reset(self):
    #     # Placeholder for reset function
    #     print("Reset")
    
    # def on_button_clicked(self):
    #     print("test button out")
