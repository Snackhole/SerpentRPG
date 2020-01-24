from PyQt5 import QtCore
from PyQt5.QtWidgets import QSizePolicy, QPushButton, QLabel, QGridLayout

from Core.DieClock import DieClock
from Interface.Widgets.LineEditMouseWheelExtension import LineEditMouseWheelExtension
from Interface.Windows.Window import Window
from SaveAndLoad.SaveAndOpenMixin import SaveAndOpenMixin


class DieClockWindow(Window, SaveAndOpenMixin):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Die Clock
        self.DieClock = DieClock()

        # Set Up Dave and open
        self.SetUpSaveAndOpen(".dieclock", "Die Clock", (DieClock,))

        # Update Display
        self.UpdateDisplay()

    def CreateInterface(self):
        # Styles
        self.LineEditStyle = "QLineEdit {font-size: 20pt;}"
        self.ClockButtonsStyle = "QPushButton {font-size: 20pt;}"
        self.LabelStyle = "QLabel {font-size: 20pt;}"

        # Inputs Size Policy
        self.InputsSizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Line Entry Width
        self.LineEntryWidth = 160

        # Die Clock Current Value Line Edit
        self.DieClockCurrentValueLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyDieClockValue(1 if event.angleDelta().y() > 0 else -1))
        self.DieClockCurrentValueLineEdit.setReadOnly(True)
        self.DieClockCurrentValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.DieClockCurrentValueLineEdit.setStyleSheet(self.LineEditStyle)
        self.DieClockCurrentValueLineEdit.setSizePolicy(self.InputsSizePolicy)
        self.DieClockCurrentValueLineEdit.setMinimumWidth(self.LineEntryWidth)

        # Die Clock Current Value Buttons
        self.DieClockCurrentValueIncreaseButton = QPushButton("+")
        self.DieClockCurrentValueIncreaseButton.clicked.connect(lambda: self.ModifyDieClockValue(1))
        self.DieClockCurrentValueIncreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.DieClockCurrentValueIncreaseButton.setStyleSheet(self.ClockButtonsStyle)
        self.DieClockCurrentValueDecreaseButton = QPushButton("-")
        self.DieClockCurrentValueDecreaseButton.clicked.connect(lambda: self.ModifyDieClockValue(-1))
        self.DieClockCurrentValueDecreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.DieClockCurrentValueDecreaseButton.setStyleSheet(self.ClockButtonsStyle)

        # Die Clock Divider Label
        self.DieClockDividerLabel = QLabel("/")
        self.DieClockDividerLabel.setStyleSheet(self.LabelStyle)
        self.DieClockDividerLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Die Clock Maximum Value Line Edit
        self.DieClockMaximumValueLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyDieClockMaximumValue(1 if event.angleDelta().y() > 0 else -1))
        self.DieClockMaximumValueLineEdit.setReadOnly(True)
        self.DieClockMaximumValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.DieClockMaximumValueLineEdit.setStyleSheet(self.LineEditStyle)
        self.DieClockMaximumValueLineEdit.setSizePolicy(self.InputsSizePolicy)
        self.DieClockMaximumValueLineEdit.setMinimumWidth(self.LineEntryWidth)

        # Die Clock Maximum Value Buttons
        self.DieClockMaximumValueIncreaseButton = QPushButton("+")
        self.DieClockMaximumValueIncreaseButton.clicked.connect(lambda: self.ModifyDieClockMaximumValue(1))
        self.DieClockMaximumValueIncreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.DieClockMaximumValueIncreaseButton.setStyleSheet(self.ClockButtonsStyle)
        self.DieClockMaximumValueDecreaseButton = QPushButton("-")
        self.DieClockMaximumValueDecreaseButton.clicked.connect(lambda: self.ModifyDieClockMaximumValue(-1))
        self.DieClockMaximumValueDecreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.DieClockMaximumValueDecreaseButton.setStyleSheet(self.ClockButtonsStyle)

        # Increase Clock Button
        self.IncreaseClockButton = QPushButton("Increase Clock")
        self.IncreaseClockButton.clicked.connect(lambda: self.IncreaseClock())

        # Increase Clock By Button
        self.IncreaseClockByButton = QPushButton("Increase Clock By...")
        self.IncreaseClockByButton.clicked.connect(lambda: self.IncreaseClockBy())

        # Create Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.DieClockCurrentValueIncreaseButton, 0, 0)
        self.Layout.addWidget(self.DieClockCurrentValueLineEdit, 1, 0)
        self.Layout.addWidget(self.DieClockCurrentValueDecreaseButton, 2, 0)
        self.Layout.addWidget(self.DieClockDividerLabel, 1, 1)
        self.Layout.addWidget(self.DieClockMaximumValueIncreaseButton, 0, 2)
        self.Layout.addWidget(self.DieClockMaximumValueLineEdit, 1, 2)
        self.Layout.addWidget(self.DieClockMaximumValueDecreaseButton, 2, 2)
        self.Layout.addWidget(self.IncreaseClockButton, 3, 0)
        self.Layout.addWidget(self.IncreaseClockByButton, 3, 2)

        # Set and Configure Layout
        self.Layout.setRowStretch(0, 1)
        self.Layout.setRowStretch(1, 1)
        self.Layout.setRowStretch(2, 1)
        self.Layout.setColumnStretch(0, 1)
        self.Layout.setColumnStretch(2, 1)
        self.Frame.setLayout(self.Layout)

    # Clock Methods
    def ModifyDieClockValue(self, Delta):
        pass

    def ModifyDieClockMaximumValue(self, Delta):
        pass

    def IncreaseClock(self):
        pass

    def IncreaseClockBy(self):
        pass

    # Display Methods
    def UpdateDisplay(self):
        pass
