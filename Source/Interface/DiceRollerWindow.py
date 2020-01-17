import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QSizePolicy, QGridLayout, QFrame, QLabel, QPushButton, QTextEdit

from Core.DiceRoller import DiceRollerWithPresetRolls
from Interface.LineEditMouseWheelExtension import LineEditMouseWheelExtension
from Interface.Window import Window
from SaveAndLoad.SaveAndOpenMixin import SaveAndOpenMixin


class DiceRollerWindow(Window, SaveAndOpenMixin):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Dice Roller
        self.DiceRoller = DiceRollerWithPresetRolls()

        # Set up Save and Open
        self.SetUpSaveAndOpen(".presetrolls", "Dice Roller", (DiceRollerWithPresetRolls,))

        # Update Display
        self.UpdateDisplay()

    def CreateInterface(self):
        # Styles
        self.LabelStyle = "QLabel {font-size: 20pt;}"
        self.LineEditStyle = "QLineEdit {font-size: 20pt;}"
        self.RollButtonStyle = "QPushButton {font-size: 20pt;}"

        # Button and Line Edit Size Policy
        self.ButtonAndLineEditSizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Dice Roller Width
        self.DiceRollerWidth = 80

        # Dice Number Line Edit
        self.DiceNumberLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyDiceNumber(1 if event.angleDelta().y() > 0 else -1))
        self.DiceNumberLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.DiceNumberLineEdit.setStyleSheet(self.LineEditStyle)
        self.DiceNumberLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.DiceNumberLineEdit.setFixedWidth(self.DiceRollerWidth)
        self.DiceNumberLineEdit.setText("1")

        # Die Type Label
        self.DieTypeLabel = QLabel("d")
        self.DieTypeLabel.setStyleSheet(self.LabelStyle)
        self.DieTypeLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Die Type Line Edit
        self.DieTypeLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyDieType(1 if event.angleDelta().y() > 0 else -1))
        self.DieTypeLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.DieTypeLineEdit.setStyleSheet(self.LineEditStyle)
        self.DieTypeLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.DieTypeLineEdit.setFixedWidth(self.DiceRollerWidth)
        self.DieTypeLineEdit.setText("20")

        # Modifier Label
        self.ModifierLabel = QLabel("+")
        self.ModifierLabel.setStyleSheet(self.LabelStyle)
        self.ModifierLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Modifier Line Edit
        self.ModifierLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyModifier(1 if event.angleDelta().y() > 0 else -1))
        self.ModifierLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ModifierLineEdit.setStyleSheet(self.LineEditStyle)
        self.ModifierLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.ModifierLineEdit.setFixedWidth(self.DiceRollerWidth)
        self.ModifierLineEdit.setText("0")

        # Roll Button
        self.RollButton = QPushButton("Roll")
        self.RollButton.clicked.connect(self.Roll)
        self.RollButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.RollButton.setStyleSheet(self.RollButtonStyle)

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
        self.DiceRollerInputsLayout.addWidget(self.DiceNumberLineEdit, 0, 0)
        self.DiceRollerInputsLayout.addWidget(self.DieTypeLabel, 0, 1)
        self.DiceRollerInputsLayout.addWidget(self.DieTypeLineEdit, 0, 2)
        self.DiceRollerInputsLayout.addWidget(self.ModifierLabel, 0, 3)
        self.DiceRollerInputsLayout.addWidget(self.ModifierLineEdit, 0, 4)
        self.DiceRollerInputsLayout.addWidget(self.RollButton, 0, 5)
        self.DiceRollerInputsFrame.setLayout(self.DiceRollerInputsLayout)
        self.Layout.addWidget(self.DiceRollerInputsFrame, 0, 0)

        # Results Log Widgets in Layout
        self.ResultsLogFrame = QFrame()
        self.ResultsLogFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.ResultsLogLayout = QGridLayout()
        self.ResultsLogLayout.addWidget(self.ResultsLogLabel, 0, 0)
        self.ResultsLogLayout.addWidget(self.ResultsLogTextEdit, 1, 0)
        self.ResultsLogFrame.setLayout(self.ResultsLogLayout)
        self.Layout.addWidget(self.ResultsLogFrame, 0, 1, 2, 1)

        # Set and Configure Layout
        self.Frame.setLayout(self.Layout)

    # Action Methods
    def Roll(self):
        print("Rolled")

    # Modify Values Methods
    def ModifyDiceNumber(self, Delta):
        print("ModifyDiceNumber:  " + str(Delta))

    def ModifyDieType(self, Delta):
        print("ModifyDieType:  " + str(Delta))

    def ModifyModifier(self, Delta):
        print("ModifyModifier:  " + str(Delta))

    # Display Update Methods
    def UpdateDisplay(self):
        self.UpdateWindowTitle()

    def UpdateWindowTitle(self):
        CurrentFileTitleSection = " [" + os.path.basename(self.CurrentOpenFileName) + "]" if self.CurrentOpenFileName != "" else ""
        UnsavedChangesIndicator = " *" if self.UnsavedChanges else ""
        self.setWindowTitle("Dice Roller - " + self.ScriptName + CurrentFileTitleSection + UnsavedChangesIndicator)

    def UpdateUnsavedChangesFlag(self, UnsavedChanges):
        self.UnsavedChanges = UnsavedChanges
        self.UpdateDisplay()
