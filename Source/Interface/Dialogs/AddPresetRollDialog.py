from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QGridLayout, QPushButton, QSpinBox

from Interface.Widgets.DieTypeSpinBox import DieTypeSpinBox


class AddPresetRollDialog(QDialog):
    def __init__(self, DiceRollerWindow):
        super().__init__(parent=DiceRollerWindow)

        # Store Parameters
        self.DiceRollerWindow = DiceRollerWindow

        # Variables
        self.ResultMessages = {}
        self.Data = None
        self.Confirm = False

        # Labels
        self.PromptLabel = QLabel("Add preset roll?")
        self.PromptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabel = QLabel("Name:")
        self.DieTypeLabel = QLabel("d")
        self.ModifierLabel = QLabel("+")

        # Roll Inputs
        self.NameLineEdit = QLineEdit()

        self.DiceNumberSpinBox = QSpinBox()
        self.DiceNumberSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.DiceNumberSpinBox.setButtonSymbols(self.DiceNumberSpinBox.NoButtons)
        self.DiceNumberSpinBox.setRange(1, 1000000000)
        self.DiceNumberSpinBox.setValue(1)

        self.DieTypeSpinBox = DieTypeSpinBox()
        self.DieTypeSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.DieTypeSpinBox.setButtonSymbols(self.DieTypeSpinBox.NoButtons)
        self.DieTypeSpinBox.setRange(1, 1000000000)
        self.DieTypeSpinBox.setValue(20)

        self.ModifierSpinBox = QSpinBox()
        self.ModifierSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ModifierSpinBox.setButtonSymbols(self.ModifierSpinBox.NoButtons)
        self.ModifierSpinBox.setRange(-1000000000, 1000000000)
        self.ModifierSpinBox.setValue(0)

        # Buttons
        self.AddButton = QPushButton("Add")
        self.AddButton.clicked.connect(self.Add)
        self.CancelButton = QPushButton("Cancel")
        self.CancelButton.clicked.connect(self.Cancel)

        # Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.PromptLabel, 0, 0, 1, 2)
        self.NameLayout = QGridLayout()
        self.NameLayout.addWidget(self.NameLabel, 0, 0)
        self.NameLayout.addWidget(self.NameLineEdit, 0, 1)
        self.NameLayout.setColumnStretch(1, 1)
        self.Layout.addLayout(self.NameLayout, 1, 0, 1, 2)
        self.DiceInputsLayout = QGridLayout()
        self.DiceInputsLayout.addWidget(self.DiceNumberSpinBox, 0, 0)
        self.DiceInputsLayout.addWidget(self.DieTypeLabel, 0, 1)
        self.DiceInputsLayout.addWidget(self.DieTypeSpinBox, 0, 2)
        self.DiceInputsLayout.addWidget(self.ModifierLabel, 0, 3)
        self.DiceInputsLayout.addWidget(self.ModifierSpinBox, 0, 4)
        self.DiceInputsLayout.setColumnStretch(0, 1)
        self.DiceInputsLayout.setColumnStretch(2, 1)
        self.DiceInputsLayout.setColumnStretch(4, 1)
        self.Layout.addLayout(self.DiceInputsLayout, 2, 0, 1, 2)
        self.Layout.addWidget(self.AddButton, 4, 0)
        self.Layout.addWidget(self.CancelButton, 4, 1)
        self.setLayout(self.Layout)

        # Set Window Title and Icon
        self.setWindowTitle(self.DiceRollerWindow.ScriptName)
        self.setWindowIcon(self.DiceRollerWindow.WindowIcon)

        # Execute Dialog
        self.exec_()

    def Add(self):
        if self.ValidInput():
            self.Data = {}
            self.Data["Name"] = self.NameLineEdit.text()
            self.Data["DiceNumber"] = self.DiceNumberSpinBox.value()
            self.Data["DieType"] = self.DieTypeSpinBox.value()
            self.Data["Modifier"] = self.ModifierSpinBox.value()
            self.Confirm = True
            self.close()

    def Cancel(self):
        self.close()

    def ValidInput(self):
        Valid = True
        if self.NameLineEdit.text() == "":
            Valid = False
            return Valid
        return Valid


class AddResultMessageDialog(QDialog):
    def __init__(self, AddPresetRollDialog):
        super().__init__(parent=AddPresetRollDialog)

        # Store Parameters
        self.AddPresetRollDialog = AddPresetRollDialog

        # Variables
        self.Result = None
        self.Message = None
        self.Confirm = False

        # Labels
        self.PromptLabel = QLabel("Add result message to preset roll?")
        self.PromptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultLabel = QLabel("Result:")
        self.MessageLabel = QLabel("Message:")

        # Inputs
        self.ResultSpinBox = QSpinBox()
        self.ResultSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultSpinBox.setButtonSymbols(self.ResultSpinBox.NoButtons)
        self.ResultSpinBox.setRange(-1000000000, 1000000000)
        self.ResultSpinBox.setValue(1)
        self.MessageLineEdit = QLineEdit()

        # Buttons
        self.AddButton = QPushButton("Add")
        self.AddButton.clicked.connect(self.Add)
        self.CancelButton = QPushButton("Cancel")
        self.CancelButton.clicked.connect(self.Cancel)

        # Set Window Title and Icon
        self.setWindowTitle(self.DiceRollerWindow.ScriptName)
        self.setWindowIcon(self.DiceRollerWindow.WindowIcon)

        # Execute Dialog
        self.exec_()

    def Add(self):
        if self.ValidInput():
            self.Result = self.ResultSpinBox.value()
            self.Message = self.MessageLineEdit.text()
            self.Confirm = True
            self.close()

    def Cancel(self):
        self.close()

    def ValidInput(self):
        Valid = True
        if self.NewResultMessage.text() == "":
            Valid = False
            return Valid
        return Valid
