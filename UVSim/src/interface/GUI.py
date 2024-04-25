from PySide6.QtWidgets import QAbstractItemView, QMainWindow, QPushButton, QVBoxLayout, \
    QTableWidget, QLabel, QTextEdit, QHBoxLayout, QWidget, QTableWidgetItem, QMenu, QInputDialog, QMessageBox, QDialog, QHeaderView, QScrollArea, QScrollBar # pip install pyside6
from PySide6.QtCore import Qt
import os

class QTGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BasicML Simulator - No File Opened (1/1)")
        self.setGeometry(100, 100, 700, 500)
        self.new_dialog = None
        self.new_dialog_id = ''
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.styles = []
        try:
            con = open(os.path.join(self.__location__, "config.ini"))
            self.styles = con.readlines()
            for i in range(len(self.styles)):
                self.styles[i].strip()
            self.styles[3]
        except:
            self.styles = ["#4C721D", "#eeeeee", "#006600", "#dddddd"]
        self.UIsetup()

        self.reset_style()

    def UIsetup(self):
        self.main_layout = QVBoxLayout()
        self.display_layout = QHBoxLayout()

        self.create_menu_bar()
        self.create_memory()
        self.create_console()
        self.create_console_side()
        self.display_main()

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def create_memory(self):
        self.memory_display = QTableWidget(250, 3)
        self.memory_display.setColumnCount(3)
        # self.reset_style(self.memory_display)
        self.memory_display.setHorizontalHeaderLabels(["##", "Value", "A"])
        self.memory_display.setMinimumWidth(300)
        header = self.memory_display.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.memory_layout = QVBoxLayout()
        self.memory_label = QLabel("Memory")
        self.memory_layout.addWidget(self.memory_label)
        self.memory_layout.addWidget(self.memory_display)

        #Buttons
        button_split = QHBoxLayout()
        self.accumulator_button = QPushButton("Accumulator: NaN")
        button_split.addWidget(self.accumulator_button)
        self.register_button = QPushButton("Register: NaN")
        button_split.addWidget(self.register_button)
        self.halt_button = QPushButton("----")
        button_split.addWidget(self.halt_button)
        self.memory_layout.addLayout(button_split)
        
        button_split = QHBoxLayout()
        self.run_button = QPushButton("Run")
        button_split.addWidget(self.run_button)
        self.step_button = QPushButton("Step")
        button_split.addWidget(self.step_button)
        # self.reset_button = QPushButton("Reset")
        # button_split.addWidget(self.reset_button)
        self.memory_layout.addLayout(button_split)


        labels = []
        for i in range(250):
            self.memory_display.setItem(i, 0, QTableWidgetItem(f"{i:03d}"))
            labels.append("")
        self.memory_display.setVerticalHeaderLabels(labels)
        # immutable table
        self.memory_display.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def create_console(self):
        self.console = QTextEdit()
        self.console.setPlaceholderText("Programs will print out to here.")
        self.console.setReadOnly(True)

    def create_console_side(self):
        """Creates buttons for textbox side of GUI"""
        self.textbox_layout = QVBoxLayout()
        
        #Page navigation buttons
        page_navigation = QHBoxLayout()
            #Set page button
        # self.change_page_button = QPushButton("TODO Page: --")
        # page_navigation.addWidget(self.change_page_button)
            #Previous page
        self.previous_file_button = QPushButton("Previous")
        page_navigation.addWidget(self.previous_file_button)
            #Next page
        self.next_file_button = QPushButton("Next")
        page_navigation.addWidget(self.next_file_button)
        self.textbox_layout.addLayout(page_navigation)
        
        #Add editor button underneath
        self.editor_button = QPushButton("Open Code Editor")
        self.textbox_layout.addWidget(self.editor_button)
        
        #Add Console control buttons underneath
        button_split = QHBoxLayout()
            #Copy from console
        # self.copy_console_button = QPushButton("TODO Copy Console")
        # button_split.addWidget(self.copy_console_button)
            #Clear console content
        self.clear_console_button = QPushButton("Clear Console")
        button_split.addWidget(self.clear_console_button)
        self.textbox_layout.addLayout(button_split)
        
        #Add console and its label underneath all buttons
        self.console_label = QLabel("Console")
        self.textbox_layout.addWidget(self.console_label)
        self.textbox_layout.addWidget(self.console)

    def display_main(self):
        self.display_layout.addLayout(self.memory_layout)
        self.display_layout.addLayout(self.textbox_layout)
        self.main_layout.addLayout(self.display_layout)
    
    def create_menu_bar(self):
        menu_bar = self.menuBar()
        self.file_menu = QMenu("&File", self)
        menu_bar.addMenu(self.file_menu)

        self.edit_menu = QMenu("&Edit", self)
        menu_bar.addMenu(self.edit_menu)

        self.help_menu = QMenu("&Help", self)
        menu_bar.addMenu(self.help_menu)

    def reset_style(self, value = None):
        #QTGUI Style
        style_string = "QMainWindow {" + f"background-color: {self.styles[0]}; color: {self.styles[1]};" + "}"
        if(value == None):
            value = self
            #border: 1px solid orange;
            #Table Style
            self.memory_display.setStyleSheet(f"background-color: {self.styles[3]}; color: {self.styles[2]};")
            self.console.setStyleSheet(f"background-color: {self.styles[3]}; color: {self.styles[2]};")
            #Menu Style
            self.menuBar().setStyleSheet(f"background-color: {self.styles[3]}; color: {self.styles[2]}")
            #Label Style
            style_string += "QLabel {" + f"color: {self.styles[1]};" + "}"
        elif(type(value) == type(QMessageBox())):
            #Label Style
            style_string += "QLabel {" + f"color: {self.styles[2]};" + "}"
        style_string += "QScrollArea{min-width:300 px; min-height: 400px}"
        #QDialog Style
        style_string += "QDialog {" + f"background-color: {self.styles[0]}; color: {self.styles[1]};" + "}"
        #QMessageBox Style
        style_string += "QMessageBox {" + f"background-color: {self.styles[3]}; color: {self.styles[2]};" + "}"
        #QInputDialog Style
        style_string += "QInputDialog {" + f"background-color: {self.styles[3]}; color: {self.styles[2]};" + "}" + "QInputDialog > QLabel {" + f"color: {self.styles[2]};" + "}"
        #QMenu Style
        style_string += "QMenu {" + f"background-color: {self.styles[3]}; color: {self.styles[2]};" + "} QMenu::item:selected {" + f"background-color: {self.styles[2]}; color: {self.styles[3]};" +"}"
        #QTextEdit Style
        style_string += "QTextEdit {" + f"background-color: {self.styles[3]}; color: {self.styles[2]};" + "}"
        #QPushButton Style
        style_string += """QPushButton {
""" + f"""
background-color: {self.styles[1]};
border-color: {self.styles[1]};
border-width: 4px;
font-size: 12px;
border: 2px solid {self.styles[1]};
border-radius: 10px;
height: 20px;
min-width: 40px;
color: {self.styles[0]};
""" + """}
""" + """QPushButton:hover {
""" + f"""
background-color: {self.styles[0]};
color: {self.styles[1]};
""" + """}
""" + """QPushButton:disabled {
""" + f"""
background-color: {self.styles[0]};
color: {self.styles[1]};
""" + """}
"""
        value.setStyleSheet(style_string)
    
    def change_theme(self, which):
        self.theme_dialog = QInputDialog()
        self.theme_dialog.setWindowTitle("Change Main Theme")
        self.theme_dialog.setLabelText("Enter a hex value to change the main theme:")


        _ = self.theme_dialog.exec_()
        if self.theme_dialog.textValue():
            self.styles[which] = self.theme_dialog.textValue()

        con = open(os.path.join(self.__location__, "config.ini"), "w")
        for i in self.styles:
            con.write(i.strip() + '\n')
        # con.write(f"{self.styles[0].strip()}\n{self.styles[1].strip()}\n{self.styles[2].strip()}\n{self.styles[3].strip()}")
        # con.write(f"{self.styles[which].strip()}\n{self.styles[2].strip()}\n{self.styles[1].strip()}")

        self.reset_style()

    def change_main_theme(self):
        self.theme_dialog = QInputDialog()
        self.theme_dialog.setWindowTitle("Change Main Theme")
        self.theme_dialog.setLabelText("Enter a hex value to change the main theme:")


        _ = self.theme_dialog.exec_()
        if self.theme_dialog.textValue():
            self.styles[0] = self.theme_dialog.textValue()

        con = open(os.path.join(self.__location__, "config.ini"), "w")
        con.write(f"{self.styles[0].strip()}\n{self.styles[1].strip()}\n{self.styles[2].strip()}\n{self.styles[3].strip()}")

        self.reset_style()

    def change_off_theme(self):
        self.theme_dialog = QInputDialog()
        self.theme_dialog.setWindowTitle("Change Off Theme")
        self.theme_dialog.setLabelText("Enter a hex value to change the off theme:")


        _ = self.theme_dialog.exec_()
        if self.theme_dialog.textValue():
            self.styles[1] = self.theme_dialog.textValue()

        con = open(os.path.join(self.__location__, "config.ini"), "w")
        con.write(f"{self.styles[0].strip()}\n{self.styles[2].strip()}\n{self.styles[1].strip()}")

        self.reset_style()
        
    def show_version(self):
        self.version_dialog = QMessageBox()
        self.reset_style(self.version_dialog)
        
        help_about = open(os.path.join(self.__location__, "about.txt"))
        help_about_lines = help_about.read()

        self.version_dialog.setText(help_about_lines)

        _ = self.version_dialog.exec_()

    def show_help(self):
        self.help_dialog = QDialog()
        self.help_dialog.setMinimumWidth(500)
        self.help_dialog.setMinimumHeight(400)
        layout = QVBoxLayout()
        # self.help_dialog.layout()

        help_doc = open(os.path.join(self.__location__, "DOCS.txt"))
        help_doc_lines = help_doc.read()

        textBox = QTextEdit()
        textBox.setText(help_doc_lines)
        textBox.setReadOnly(True)

        layout.addWidget(textBox)
        self.reset_style(self.help_dialog)

        # help_doc = open(os.path.join(self.__location__, "DOCS.txt"))
        # help_doc_lines = help_doc.read()

        # self.help_dialog.setText(help_doc_lines)

        self.help_dialog.setLayout(layout)

        _ = self.help_dialog.exec_()

    def custom_alert(self, title, desc):
        self.new_dialog = QMessageBox()
        self.reset_style(self.new_dialog)
        # .setStyleSheet("QLabel{min-width: 200px; text-align: left;}")
        # change the following to an updated instruction list
        self.new_dialog.setWindowTitle(title)
        self.new_dialog.setText(desc)

        _ = self.new_dialog.exec_()

    def change_register(self):
        self.new_dialog = QInputDialog()
        self.reset_style(self.new_dialog)
        self.new_dialog.setWindowTitle("Change Register")
        self.new_dialog.setLabelText("Enter a Register value:") # (todo)

        _ = self.new_dialog.exec_()
        try:
            return self.new_dialog.textValue()
        except:
            return None

    def change_accumulator(self):
        self.new_dialog = QInputDialog()
        self.reset_style(self.new_dialog)
        self.new_dialog.setWindowTitle("Change Accumulator")
        self.new_dialog.setLabelText("Enter an Accumulator value (0-249):")

        _ = self.new_dialog.exec_()
        try:
            return int(self.new_dialog.textValue())
        except:
            return None

    def insert_Read(self):
        self.new_dialog = QInputDialog()
        self.reset_style(self.new_dialog)
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
        self.new_dialog = QDialog()
        self.new_dialog_id = 'code_editor'
        self.reset_style(self.new_dialog)
        self.new_dialog.setWindowTitle('UVSim Code Editor')
        self.new_dialog.setGeometry(150, 150, 600, 400)
        self.text_editor = QTextEdit()
        self.text_editor.setText(code)

        self.button_layout = QVBoxLayout()
        
        self.wiz_layout = QHBoxLayout()
        self.wiz_layout.addWidget(self.text_editor)

        self.code_load_button = QPushButton("Compile")
        self.export_button = QPushButton("Save As")
        self.save_button = QPushButton("Save")
        self.editor_load_button = QPushButton("Open File")
    
        self.button_layout.addWidget(self.code_load_button)
        self.button_layout.addWidget(self.export_button)
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.editor_load_button)
        self.wiz_layout.addLayout(self.button_layout)

        # self.new_dialog.finished(self.close_dialog)

        self.new_dialog.setLayout(self.wiz_layout)

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
