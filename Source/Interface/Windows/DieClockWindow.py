import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QSizePolicy, QPushButton, QLabel, QGridLayout, QFrame

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
        self.LargeButtonsStyle = "QPushButton {font-size: 20pt;}"
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
        self.DieClockCurrentValueIncreaseButton.setStyleSheet(self.LargeButtonsStyle)
        self.DieClockCurrentValueDecreaseButton = QPushButton("-")
        self.DieClockCurrentValueDecreaseButton.clicked.connect(lambda: self.ModifyDieClockValue(-1))
        self.DieClockCurrentValueDecreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.DieClockCurrentValueDecreaseButton.setStyleSheet(self.LargeButtonsStyle)

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
        self.DieClockMaximumValueIncreaseButton.setStyleSheet(self.LargeButtonsStyle)
        self.DieClockMaximumValueDecreaseButton = QPushButton("-")
        self.DieClockMaximumValueDecreaseButton.clicked.connect(lambda: self.ModifyDieClockMaximumValue(-1))
        self.DieClockMaximumValueDecreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.DieClockMaximumValueDecreaseButton.setStyleSheet(self.LargeButtonsStyle)

        # Increase Clock Button
        self.IncreaseClockButton = QPushButton("Increase Clock")
        self.IncreaseClockButton.clicked.connect(lambda: self.IncreaseClock())
        self.IncreaseClockButton.setSizePolicy(self.InputsSizePolicy)
        self.IncreaseClockButton.setStyleSheet(self.LargeButtonsStyle)

        # Increase Clock By Button
        self.IncreaseClockByButton = QPushButton("Increase Clock By...")
        self.IncreaseClockByButton.clicked.connect(lambda: self.IncreaseClockBy())
        self.IncreaseClockByButton.setSizePolicy(self.InputsSizePolicy)

        # Threshold Label
        self.ThresholdLabel = QLabel("Threshold")
        self.ThresholdLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Threshold Line Edit
        self.ThresholdLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyThreshold(1 if event.angleDelta().y() > 0 else -1))
        self.ThresholdLineEdit.setReadOnly(True)
        self.ThresholdLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ThresholdLineEdit.setStyleSheet(self.LineEditStyle)
        self.ThresholdLineEdit.setSizePolicy(self.InputsSizePolicy)
        self.ThresholdLineEdit.setMinimumWidth(self.LineEntryWidth)

        # Threshold Buttons
        self.ThresholdIncreaseButton = QPushButton("+")
        self.ThresholdIncreaseButton.clicked.connect(lambda: self.ModifyThreshold(1))
        self.ThresholdIncreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.ThresholdIncreaseButton.setStyleSheet(self.LargeButtonsStyle)
        self.ThresholdDecreaseButton = QPushButton("-")
        self.ThresholdDecreaseButton.clicked.connect(lambda: self.ModifyThreshold(-1))
        self.ThresholdDecreaseButton.setSizePolicy(self.InputsSizePolicy)
        self.ThresholdDecreaseButton.setStyleSheet(self.LargeButtonsStyle)

        # Create Layout
        self.Layout = QGridLayout()
        self.ButtonsFrame = QFrame()
        self.ButtonsFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.ButtonsLayout = QGridLayout()
        self.ButtonsLayout.addWidget(self.IncreaseClockButton, 0, 0)
        self.ButtonsLayout.addWidget(self.IncreaseClockByButton, 1, 0)
        self.ButtonsFrame.setLayout(self.ButtonsLayout)
        self.ButtonsLayout.setRowStretch(0, 1)
        self.ButtonsLayout.setRowStretch(1, 1)
        self.Layout.addWidget(self.ButtonsFrame, 0, 0)
        self.ClockFrame = QFrame()
        self.ClockFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.ClockLayout = QGridLayout()
        self.ClockLayout.addWidget(self.DieClockCurrentValueIncreaseButton, 0, 0)
        self.ClockLayout.addWidget(self.DieClockCurrentValueLineEdit, 1, 0)
        self.ClockLayout.addWidget(self.DieClockCurrentValueDecreaseButton, 2, 0)
        self.ClockLayout.addWidget(self.DieClockDividerLabel, 1, 1)
        self.ClockLayout.addWidget(self.DieClockMaximumValueIncreaseButton, 0, 2)
        self.ClockLayout.addWidget(self.DieClockMaximumValueLineEdit, 1, 2)
        self.ClockLayout.addWidget(self.DieClockMaximumValueDecreaseButton, 2, 2)
        self.ClockLayout.setRowStretch(0, 1)
        self.ClockLayout.setRowStretch(1, 2)
        self.ClockLayout.setRowStretch(2, 1)
        self.ClockLayout.setColumnStretch(0, 1)
        self.ClockLayout.setColumnStretch(2, 1)
        self.ThresholdFrame = QFrame()
        self.ThresholdLayout = QGridLayout()
        self.ThresholdLayout.addWidget(self.ThresholdLabel, 0, 0, 1, 3)
        self.ThresholdLayout.addWidget(self.ThresholdDecreaseButton, 1, 0)
        self.ThresholdLayout.addWidget(self.ThresholdLineEdit, 1, 1)
        self.ThresholdLayout.addWidget(self.ThresholdIncreaseButton, 1, 2)
        self.ThresholdFrame.setLayout(self.ThresholdLayout)
        self.ClockLayout.addWidget(self.ThresholdFrame, 3, 0, 1, 3)
        self.ClockFrame.setLayout(self.ClockLayout)
        self.Layout.addWidget(self.ClockFrame, 1, 0)

        # Set and Configure Layout
        self.Frame.setLayout(self.Layout)

    # Clock Methods
    def ModifyDieClockValue(self, Delta):
        self.DieClock.ModifyCurrentValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def ModifyDieClockMaximumValue(self, Delta):
        self.DieClock.ModifyMaximumValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def ModifyThreshold(self, Delta):
        self.DieClock.ModifyComplicationThreshold(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def IncreaseClock(self):
        ClockGoesOff = self.DieClock.IncreaseClock()
        self.UpdateUnsavedChangesFlag(True)
        if ClockGoesOff:
            self.DisplayMessageBox("The clock went off!")

    def IncreaseClockBy(self):
        pass

    # Display Methods
    def UpdateDisplay(self):
        # Die Clock Display
        self.DieClockCurrentValueLineEdit.setText(str(self.DieClock.Value))
        self.DieClockMaximumValueLineEdit.setText(str(self.DieClock.MaximumValue))

        # Threshold Display
        self.ThresholdLineEdit.setText(str(self.DieClock.ComplicationThreshold))

        # Update Window Title
        self.UpdateWindowTitle()

    def UpdateWindowTitle(self):
        CurrentFileTitleSection = " [" + os.path.basename(self.CurrentOpenFileName) + "]" if self.CurrentOpenFileName != "" else ""
        UnsavedChangesIndicator = " *" if self.UnsavedChanges else ""
        self.setWindowTitle("Die Clock - " + self.ScriptName + CurrentFileTitleSection + UnsavedChangesIndicator)

    def UpdateUnsavedChangesFlag(self, UnsavedChanges):
        self.UnsavedChanges = UnsavedChanges
        self.UpdateDisplay()
