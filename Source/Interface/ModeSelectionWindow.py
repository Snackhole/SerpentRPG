from PyQt5.QtWidgets import QPushButton, QGridLayout, QComboBox, QLabel

from Interface.Window import Window


class ModeSelectionWindow(Window):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Mode Value
        self.Mode = None

    def CreateInterface(self):
        # Mode Label
        self.ModeLabel = QLabel("Mode:")

        # Mode ComboBox
        self.ModeComboBox = QComboBox()
        self.ModeComboBox.addItem("Dice Roller")
        self.ModeComboBox.addItem("Wilderness Travel Manager")
        self.ModeComboBox.setEditable(False)

        # Buttons
        self.OpenButton = QPushButton("Open")
        self.OpenButton.clicked.connect(lambda: self.SelectMode(self.ModeComboBox.currentText()))

        # Create and Set Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.ModeLabel, 0, 0)
        self.Layout.addWidget(self.ModeComboBox, 0, 1)
        self.Layout.addWidget(self.OpenButton, 1, 0, 1, 2)
        self.Frame.setLayout(self.Layout)

    def UpdateWindowTitle(self):
        self.setWindowTitle(self.ScriptName + " Mode Selection")

    def SelectMode(self, Mode):
        self.Mode = Mode
        self.close()
