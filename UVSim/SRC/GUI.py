from PySide6.QtWidgets import QAbstractItemView, QMainWindow, QPushButton, QVBoxLayout, \
    QTableWidget, QLabel, QTextEdit, QHBoxLayout, QWidget, QTableWidgetItem, QMenu, QInputDialog, QMessageBox, QWizard, QWizardPage # pip install pyside6
from PySide6.QtCore import Qt
import os

class QTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BasicML Simulator - No File Opened (0/1)")
        self.setGeometry(100, 100, 600, 350)
        self.new_dialog = None
        self.new_dialog_id = ''
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        con = open(os.path.join(self.__location__, "config.ini"))
        lines = con.readlines()
        self.main_theme = lines[0]
        self.off_theme = lines[1]
        self.setStyleSheet(f"background-color: {self.main_theme}; color: {self.off_theme};")
        self.UIsetup()

    def UIsetup(self):
        self.main_layout = QVBoxLayout()
        self.display_layout = QHBoxLayout()

        self.create_menu_bar()
        self.create_memory()
        # self.create_register()
        # self.create_accumulator()
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
        self.register_display.setFixedWidth(50)
        self.register_display.setFixedHeight(50)

        
        buttons_layout = QHBoxLayout()
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("background-color: #dbdbdb;")
        buttons_layout.addWidget(self.reset_button)

    def create_accumulator(self):
        self.accumulator_display = QTextEdit()
        self.accumulator_display.setStyleSheet("background-color: #dbdbdb;")
        self.accumulator_display.setFixedWidth(50)
        self.accumulator_display.setFixedHeight(50)

    def create_console(self):
        self.console = QTextEdit()
        self.console.setStyleSheet("background-color: #dbdbdb;")
        self.console.setFixedHeight(150)
        self.console.setPlaceholderText("Programs will print out to here.")
        self.console.setDisabled(True)
        self.console.setTextColor('#000000')

    def create_textbox(self):
        self.textbox_layout = QVBoxLayout()
        #Register and Accumulator
        self.accumulator_button = QPushButton("Accumulator: NaN")
        self.accumulator_button.setStyleSheet("background-color: #dbdbdb;")
        self.textbox_layout.addWidget(self.accumulator_button)
        self.register_button = QPushButton("Register: NaN")
        self.register_button.setStyleSheet("background-color: #dbdbdb;")
        self.textbox_layout.addWidget(self.register_button)
        self.editor_button = QPushButton("Open Code Editor")
        self.editor_button.setStyleSheet("background-color: #dbdbdb;")
        self.textbox_layout.addWidget(self.editor_button)

        # optional logo placement at eof
        self.textbox_layout.addStretch()
        # self.register_label = QLabel("Register")
        # self.register_label.setStyleSheet("color: #FFFFFF;")
        # self.textbox_layout.addWidget(self.register_label)
        # self.textbox_layout.addWidget(self.register_display)
        # self.accumulator_label = QLabel("Accumulator")
        # self.accumulator_label.setStyleSheet("color: #FFFFFF;")
        # self.textbox_layout.addWidget(self.accumulator_label)
        # self.textbox_layout.addWidget(self.accumulator_display)
        
        self.console_label = QLabel("Console")
        self.console_label.setStyleSheet("color: #FFFFFF;")
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
        self.theme_dialog.setWindowTitle("Change Main Theme")
        self.theme_dialog.setLabelText("Enter a hex value to change the main theme:")

        self.off_theme_dialog = QInputDialog()
        self.off_theme_dialog.setWindowTitle("Change Off Theme")
        self.off_theme_dialog.setLabelText("Enter a hex value to change the off theme:")


        _ = self.theme_dialog.exec_()
        if self.theme_dialog.textValue():
            self.main_theme = self.theme_dialog.textValue()
            self.setStyleSheet(f"background-color: {self.main_theme}; color: {self.off_theme};")

        _ = self.off_theme_dialog.exec_()
        if self.off_theme_dialog.textValue():
            self.off_theme = self.off_theme_dialog.textValue()
            self.setStyleSheet(f"color: {self.off_theme}; ")
            self.setStyleSheet(f"background-color: {self.main_theme}; color: {self.off_theme};")

        con = open(os.path.join(self.__location__, "config.ini"), "w")
        con.write(self.main_theme + "\n")
        con.write(self.off_theme)


    def show_version(self):
        self.version_dialog = QMessageBox()
        
        help_about = open(os.path.join(self.__location__, "about.txt"))
        help_about_lines = help_about.read()

        self.version_dialog.setText(help_about_lines)

        _ = self.version_dialog.exec_()

    def show_help(self):
        self.help_dialog = QMessageBox()
        self.help_dialog.setStyleSheet("QLabel{min-width: 700px; text-align: left;}")
        # change the following to an updated instruction list

        help_doc = open(os.path.join(self.__location__, "DOCS.txt"))
        help_doc_lines = help_doc.read()

        self.help_dialog.setText(help_doc_lines)

        _ = self.help_dialog.exec_()

    def custom_alert(self, title, desc):
        self.new_dialog = QMessageBox()
        self.new_dialog.setStyleSheet("QLabel{min-width: 200px; text-align: left;}")
        # change the following to an updated instruction list
        self.new_dialog.setWindowTitle(title)
        self.new_dialog.setText(desc)

        _ = self.new_dialog.exec_()

    def change_register(self):
        self.new_dialog = QInputDialog()
        self.new_dialog.setWindowTitle("Change Register")
        self.new_dialog.setLabelText("Enter a Register value (TODO):")

        _ = self.new_dialog.exec_()
        try:
            return self.new_dialog.textValue()
        except:
            return None

    def change_accumulator(self):
        self.new_dialog = QInputDialog()
        self.new_dialog.setWindowTitle("Change Accumulator")
        self.new_dialog.setLabelText("Enter an Accumulator value (0-99):")

        _ = self.new_dialog.exec_()
        try:
            return int(self.new_dialog.textValue())
        except:
            return None

    def insert_Read(self):
        self.new_dialog = QInputDialog()
        self.new_dialog.setWindowTitle("Insert Value")
        self.new_dialog.setLabelText("Enter a value for the program:")

        _ = self.new_dialog.exec_()
        try:
            return int(self.new_dialog.textValue())
        except:
            return None
        
    def close_dialog(self):
        self.new_dialog = None
        self.new_dialog_id = ''

    def code_editor(self, code):
        self.new_dialog = QWizard()
        self.new_dialog_id = 'code_editor'
        self.new_dialog.setStyleSheet("QWizard { background-color: #ffffff; }")
        self.new_dialog.setButtonLayout([])
        # self.new_dialog.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint) # no close button
        self.text_editor = QTextEdit()
        self.text_editor.setText(code)

        self.button_layout = QVBoxLayout()
        
        self.wiz_layout = QHBoxLayout()
        self.wiz_layout.addWidget(self.text_editor)

        self.code_load_button = QPushButton("Compile")
        self.code_load_button.setStyleSheet("background-color: #dbdbdb;")
        self.export_button = QPushButton("Save As")
        self.export_button.setStyleSheet("background-color: #dbdbdb;")
        self.save_button = QPushButton("Save")
        self.save_button.setStyleSheet("background-color: #dbdbdb;")
        self.editor_load_button = QPushButton("Open File")
        self.editor_load_button.setStyleSheet("background-color: #dbdbdb;")
    
        self.button_layout.addWidget(self.code_load_button)
        self.button_layout.addWidget(self.export_button)
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.editor_load_button)
        self.wiz_layout.addLayout(self.button_layout)

        # self.new_dialog.finished(self.close_dialog)

        self.new_dialog.setLayout(self.wiz_layout)
        # self.new_dialog.setWindowTitle("Code Editor")
        # self.new_dialog.setLabelText("Enter a Register value (TODO):")

    def name_export(self):
        self.export_name = QInputDialog()
        self.export_name.setWindowTitle("Enter File Name")
        self.export_name.setLabelText("Saves to Current Directory\nFile Name:")
        self.export_name.setOkButtonText("Save")
        _ = self.export_name.exec_()
        try:
            self.file_name =  self.export_name.textValue()
        except:
            return None 

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
