import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QSizePolicy, QGridLayout, QFrame, QLabel, QPushButton, QTextEdit, QSpinBox

from Core.DiceRoller import DiceRollerWithPresetRolls
from Interface.Widgets.DieTypeSpinBox import DieTypeSpinBox
from Interface.Widgets.PresetRollsTreeWidget import PresetRollsTreeWidget
from Interface.Windows.Window import Window
from SaveAndLoad.SaveAndOpenMixin import SaveAndOpenMixin


class DiceRollerWindow(Window, SaveAndOpenMixin):
    def __init__(self, ScriptName):
        # Create Dice Roller
        self.DiceRoller = DiceRollerWithPresetRolls()

        # Initialize Window and SaveAndOpenMixin
        super().__init__(ScriptName)

        # Set up Save and Open
        self.SetUpSaveAndOpen(".dicerolls", "Dice Roller", (DiceRollerWithPresetRolls,))

        # Update Display
        self.UpdateDisplay()

    def CreateInterface(self):
        # Styles
        self.LabelStyle = "QLabel {font-size: 20pt;}"
        self.SpinBoxStyle = "QSpinBox {font-size: 20pt;}"
        self.RollButtonStyle = "QPushButton {font-size: 20pt;}"

        # Inputs Size Policy
        self.InputsSizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Dice Roller Width
        self.DiceRollerWidth = 80

        # Dice Number Line Edit
        self.DiceNumberSpinBox = QSpinBox()
        self.DiceNumberSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.DiceNumberSpinBox.setStyleSheet(self.SpinBoxStyle)
        self.DiceNumberSpinBox.setSizePolicy(self.InputsSizePolicy)
        self.DiceNumberSpinBox.setFixedWidth(self.DiceRollerWidth)
        self.DiceNumberSpinBox.setButtonSymbols(self.DiceNumberSpinBox.NoButtons)
        self.DiceNumberSpinBox.setRange(1, 1000000000)
        self.DiceNumberSpinBox.setValue(1)

        # Die Type Label
        self.DieTypeLabel = QLabel("d")
        self.DieTypeLabel.setStyleSheet(self.LabelStyle)
        self.DieTypeLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Die Type Line Edit
        self.DieTypeSpinBox = DieTypeSpinBox()
        self.DieTypeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.DieTypeSpinBox.setStyleSheet(self.SpinBoxStyle)
        self.DieTypeSpinBox.setSizePolicy(self.InputsSizePolicy)
        self.DieTypeSpinBox.setFixedWidth(self.DiceRollerWidth)
        self.DieTypeSpinBox.setButtonSymbols(self.DieTypeSpinBox.NoButtons)
        self.DieTypeSpinBox.setRange(1, 1000000000)
        self.DieTypeSpinBox.setValue(20)

        # Modifier Label
        self.ModifierLabel = QLabel("+")
        self.ModifierLabel.setStyleSheet(self.LabelStyle)
        self.ModifierLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Modifier Line Edit
        self.ModifierSpinBox = QSpinBox()
        self.ModifierSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ModifierSpinBox.setStyleSheet(self.SpinBoxStyle)
        self.ModifierSpinBox.setSizePolicy(self.InputsSizePolicy)
        self.ModifierSpinBox.setFixedWidth(self.DiceRollerWidth)
        self.ModifierSpinBox.setButtonSymbols(self.ModifierSpinBox.NoButtons)
        self.ModifierSpinBox.setRange(-1000000000, 1000000000)
        self.ModifierSpinBox.setValue(0)

        # Roll Button
        self.RollButton = QPushButton("Roll")
        self.RollButton.clicked.connect(lambda: self.Roll())
        self.RollButton.setSizePolicy(self.InputsSizePolicy)
        self.RollButton.setStyleSheet(self.RollButtonStyle)

        # Preset Rolls Label
        self.PresetRollsLabel = QLabel("Preset Rolls")
        self.PresetRollsLabel.setStyleSheet(self.LabelStyle)
        self.PresetRollsLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Preset Rolls Tree Widget
        self.PresetRollsTreeWidget = PresetRollsTreeWidget(self.DiceRoller)

        # Preset Rolls Buttons
        self.PresetRollsRollButton = QPushButton("Roll")
        self.PresetRollsRollButton.clicked.connect(self.RollPresetRoll)
        self.PresetRollsRollButton.setSizePolicy(self.InputsSizePolicy)

        self.PresetRollsAddButton = QPushButton("+")
        self.PresetRollsAddButton.clicked.connect(self.AddPresetRoll)
        self.PresetRollsAddButton.setSizePolicy(self.InputsSizePolicy)

        self.PresetRollsDeleteButton = QPushButton("-")
        self.PresetRollsDeleteButton.clicked.connect(self.DeletePresetRoll)
        self.PresetRollsDeleteButton.setSizePolicy(self.InputsSizePolicy)

        self.PresetRollsMoveUpButton = QPushButton("\u2191")
        self.PresetRollsMoveUpButton.clicked.connect(self.MovePresetRollUp)
        self.PresetRollsMoveUpButton.setSizePolicy(self.InputsSizePolicy)

        self.PresetRollsMoveDownButton = QPushButton("\u2193")
        self.PresetRollsMoveDownButton.clicked.connect(self.MovePresetRollDown)
        self.PresetRollsMoveDownButton.setSizePolicy(self.InputsSizePolicy)

        # Results Log Label
        self.ResultsLogLabel = QLabel("Results Log")
        self.ResultsLogLabel.setStyleSheet(self.LabelStyle)
        self.ResultsLogLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Results Log Text Edit
        self.ResultsLogTextEdit = QTextEdit()
        self.ResultsLogTextEdit.setReadOnly(True)

        # Create Layout
        self.Layout = QGridLayout()

        # Dice Roller Inputs in Layout
        self.DiceRollerInputsFrame = QFrame()
        self.DiceRollerInputsFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.DiceRollerInputsLayout = QGridLayout()
        self.DiceRollerInputsLayout.addWidget(self.DiceNumberSpinBox, 0, 0)
        self.DiceRollerInputsLayout.addWidget(self.DieTypeLabel, 0, 1)
        self.DiceRollerInputsLayout.addWidget(self.DieTypeSpinBox, 0, 2)
        self.DiceRollerInputsLayout.addWidget(self.ModifierLabel, 0, 3)
        self.DiceRollerInputsLayout.addWidget(self.ModifierSpinBox, 0, 4)
        self.DiceRollerInputsLayout.addWidget(self.RollButton, 0, 5)
        self.DiceRollerInputsLayout.setColumnStretch(0, 1)
        self.DiceRollerInputsLayout.setColumnStretch(2, 1)
        self.DiceRollerInputsLayout.setColumnStretch(4, 1)
        self.DiceRollerInputsFrame.setLayout(self.DiceRollerInputsLayout)
        self.Layout.addWidget(self.DiceRollerInputsFrame, 0, 0)

        # Preset Rolls in Layout
        self.PresetRollsFrame = QFrame()
        self.PresetRollsFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.PresetRollsLayout = QGridLayout()
        self.PresetRollsLayout.addWidget(self.PresetRollsLabel, 0, 0, 1, 2)
        self.PresetRollsLayout.addWidget(self.PresetRollsTreeWidget, 1, 0, 5, 1)
        self.PresetRollsLayout.addWidget(self.PresetRollsRollButton, 1, 1)
        self.PresetRollsLayout.addWidget(self.PresetRollsAddButton, 2, 1)
        self.PresetRollsLayout.addWidget(self.PresetRollsDeleteButton, 3, 1)
        self.PresetRollsLayout.addWidget(self.PresetRollsMoveUpButton, 4, 1)
        self.PresetRollsLayout.addWidget(self.PresetRollsMoveDownButton, 5, 1)
        for Row in range(1, 6):
            self.PresetRollsLayout.setRowStretch(Row, 1)
        self.PresetRollsFrame.setLayout(self.PresetRollsLayout)
        self.Layout.addWidget(self.PresetRollsFrame, 1, 0)

        # Results Log Widgets in Layout
        self.ResultsLogFrame = QFrame()
        self.ResultsLogFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.ResultsLogLayout = QGridLayout()
        self.ResultsLogLayout.addWidget(self.ResultsLogLabel, 0, 0)
        self.ResultsLogLayout.addWidget(self.ResultsLogTextEdit, 1, 0)
        self.ResultsLogFrame.setLayout(self.ResultsLogLayout)
        self.Layout.addWidget(self.ResultsLogFrame, 0, 1, 2, 1)

        # Set and Configure Layout
        self.Layout.setColumnStretch(1, 1)
        self.Frame.setLayout(self.Layout)

    # Button Methods
    def Roll(self):
        DiceNumber = self.DiceNumberSpinBox.value()
        DieType = self.DieTypeSpinBox.value()
        Modifier = self.ModifierSpinBox.value()
        self.DiceRoller.RollAndLog(DiceNumber, DieType, Modifier)
        self.UpdateDisplay()

    def AddPresetRoll(self):
        pass

    def DeletePresetRoll(self):
        pass

    def MovePresetRollUp(self):
        pass

    def MovePresetRollDown(self):
        pass

    def RollPresetRoll(self):
        pass

    # Display Update Methods
    def UpdateDisplay(self):
        # Results Log Display
        ResultsLogString = ""
        for LogEntry in reversed(self.DiceRoller.ResultsLog):
            ResultsLogString += LogEntry + "\n\n---\n\n"
        self.ResultsLogTextEdit.setPlainText(ResultsLogString[:-7])

        # Update Window Title
        self.UpdateWindowTitle()

    def UpdateWindowTitle(self):
        CurrentFileTitleSection = " [" + os.path.basename(self.CurrentOpenFileName) + "]" if self.CurrentOpenFileName != "" else ""
        UnsavedChangesIndicator = " *" if self.UnsavedChanges else ""
        self.setWindowTitle("Dice Roller - " + self.ScriptName + CurrentFileTitleSection + UnsavedChangesIndicator)

    def UpdateUnsavedChangesFlag(self, UnsavedChanges):
        self.UnsavedChanges = UnsavedChanges
        self.UpdateDisplay()