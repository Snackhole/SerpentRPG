from PyQt5.QtWidgets import QPushButton, QGridLayout, QFrame

from Interface.Window import Window


class ModeSelectionWindow(Window):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Initialize Mode
        self.Mode = None

    def CreateInterface(self):
        # Frame
        self.Frame = QFrame()

        # Buttons Style
        self.ButtonsStyle = "QPushButton {font-size: 20pt;}"

        # Buttons
        self.WildernessTravelManagerModeButton = QPushButton("Wilderness Travel Manager")
        self.WildernessTravelManagerModeButton.setStyleSheet(self.ButtonsStyle)
        self.WildernessTravelManagerModeButton.clicked.connect(lambda: self.SelectMode("Wilderness Travel Manager"))

        # Create and Set Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.WildernessTravelManagerModeButton)
        self.Frame.setLayout(self.Layout)

        # Set Frame as Central Widget
        self.setCentralWidget(self.Frame)

    def UpdateWindowTitle(self):
        self.setWindowTitle(self.ScriptName + " Mode Selection")

    def SelectMode(self, Mode):
        self.Mode = Mode
        self.close()
