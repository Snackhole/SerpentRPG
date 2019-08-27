from PyQt5.QtWidgets import QPushButton, QGridLayout

from Interface.Window import Window


class ModeSelectionWindow(Window):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Mode Value
        self.Mode = None

    def CreateInterface(self):
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

    def UpdateWindowTitle(self):
        self.setWindowTitle(self.ScriptName + " Mode Selection")

    def SelectMode(self, Mode):
        self.Mode = Mode
        self.close()
