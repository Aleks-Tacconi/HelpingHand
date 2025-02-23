from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QDialog, QLineEdit, QLabel, QFormLayout, QDialogButtonBox

class KeybindDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Keybind")
        self.setGeometry(100, 100, 300, 150)

        self.keybind = ""

        layout = QFormLayout()
        self.label = QLabel("Enter a new keybind:")
        self.keybindInput = QLineEdit()
        self.keybindInput.textChanged.connect(self.update_keybind)

        # Add confirmation button
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout.addRow(self.label, self.keybindInput)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

    def update_keybind(self, text):
        self.keybind = text

    def accept(self):
        # Save the keybind to a file when the dialog is accepted
        with open("keybind.txt", "w") as file:
            file.write(self.keybind)
        super().accept()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Wiki Companion")
        icon = QtGui.QIcon("Assets/icon.png")
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create a layout for positioning
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 0, 0)  # Add padding (left, top, right, bottom)

        # Create the keybind button
        self.keybindMenu = QPushButton("Keybinds")
        self.keybindMenu.setFixedSize(200, 100)
        self.layout.addWidget(self.keybindMenu)

        self.centralwidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralwidget)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.keybindMenu.clicked.connect(self.open_keybind_dialog)
        self.current_keybind = "k"

    def open_keybind_dialog(self):
        dialog = KeybindDialog()
        if dialog.exec():
            self.current_keybind = dialog.keybind
            print(dialog.keybind)


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()
app.exec()
