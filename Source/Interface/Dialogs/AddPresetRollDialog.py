from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QGridLayout, QPushButton, QSpinBox, QSizePolicy, QMessageBox

from Interface.Widgets.DieTypeSpinBox import DieTypeSpinBox
from Interface.Widgets.ResultMessagesTreeWidget import ResultMessagesTreeWidget


class AddPresetRollDialog(QDialog):
    def __init__(self, DiceRollerWindow):
        super().__init__(parent=DiceRollerWindow)

        # Store Parameters
        self.DiceRollerWindow = DiceRollerWindow

        # Variables
        self.ResultMessages = {}
        self.Data = None
        self.Confirm = False

        # Inputs Size Policy
        self.InputsSizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Labels
        self.PromptLabel = QLabel("Add preset roll?")
        self.PromptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLabel = QLabel("Name:")
        self.DieTypeLabel = QLabel("d")
        self.ModifierLabel = QLabel("+")
        self.ResultMessagesLabel = QLabel("Result Messages:")
        self.ResultMessagesLabel.setAlignment(QtCore.Qt.AlignCenter)

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

        # Result Messages Tree Widget
        self.ResultMessagesTreeWidget = ResultMessagesTreeWidget(self.ResultMessages)

        # Buttons
        self.AddResultMessageButton = QPushButton("+")
        self.AddResultMessageButton.clicked.connect(self.AddResultMessage)
        self.AddResultMessageButton.setSizePolicy(self.InputsSizePolicy)
        self.DeleteResultMessageButton = QPushButton("-")
        self.DeleteResultMessageButton.clicked.connect(self.DeleteResultMessage)
        self.DeleteResultMessageButton.setSizePolicy(self.InputsSizePolicy)
        self.EditResultMessageButton = QPushButton("Edit")
        self.EditResultMessageButton.clicked.connect(self.EditResultMessage)
        self.EditResultMessageButton.setSizePolicy((self.InputsSizePolicy))
        self.CopyResultMessageButton = QPushButton("Copy")
        self.CopyResultMessageButton.clicked.connect(self.CopyResultMessage)
        self.CopyResultMessageButton.setSizePolicy((self.InputsSizePolicy))
        self.AddButton = QPushButton("Add")
        self.AddButton.clicked.connect(self.Add)
        self.AddButton.setDefault(True)
        self.AddButton.setAutoDefault(True)
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
        self.ResultMessagesLayout = QGridLayout()
        self.ResultMessagesLayout.addWidget(self.ResultMessagesLabel, 0, 0)
        self.ResultMessagesLayout.addWidget(self.ResultMessagesTreeWidget, 1, 0, 4, 1)
        self.ResultMessagesLayout.addWidget(self.AddResultMessageButton, 1, 1)
        self.ResultMessagesLayout.addWidget(self.DeleteResultMessageButton, 2, 1)
        self.ResultMessagesLayout.addWidget(self.EditResultMessageButton, 3, 1)
        self.ResultMessagesLayout.addWidget(self.CopyResultMessageButton, 4, 1)
        self.ResultMessagesLayout.setRowStretch(1, 1)
        self.ResultMessagesLayout.setRowStretch(2, 1)
        self.ResultMessagesLayout.setRowStretch(3, 1)
        self.ResultMessagesLayout.setRowStretch(4, 1)
        self.Layout.addLayout(self.ResultMessagesLayout, 3, 0, 1, 2)
        self.Layout.addWidget(self.AddButton, 4, 0)
        self.Layout.addWidget(self.CancelButton, 4, 1)
        self.setLayout(self.Layout)

        # Set Window Title and Icon
        self.setWindowTitle(self.DiceRollerWindow.ScriptName)
        self.setWindowIcon(self.DiceRollerWindow.WindowIcon)

        # Edit Hook
        self.EditHook()

        # Update Display
        self.UpdateDisplay()

        # Execute Dialog
        self.exec_()

    def Add(self):
        if self.ValidInput():
            self.Data = {}
            self.Data["Name"] = self.NameLineEdit.text()
            self.Data["DiceNumber"] = self.DiceNumberSpinBox.value()
            self.Data["DieType"] = self.DieTypeSpinBox.value()
            self.Data["Modifier"] = self.ModifierSpinBox.value()
            self.Data["ResultMessages"] = self.ResultMessages
            self.Confirm = True
            self.close()

    def Cancel(self):
        self.close()

    def ValidInput(self):
        if self.NameLineEdit.text() == "":
            self.DiceRollerWindow.DisplayMessageBox("Preset rolls must have a name.", Icon=QMessageBox.Warning, Parent=self)
            return False
        return True

    def AddResultMessage(self):
        AddResultMessageDialogInst = AddResultMessageDialog(self, self.ResultMessages, self.DiceRollerWindow)
        if AddResultMessageDialogInst.Confirm:
            Result = AddResultMessageDialogInst.Result
            Message = AddResultMessageDialogInst.Message
            self.ResultMessages[Result] = Message
            self.UpdateDisplay()
            SortedKeys = sorted(self.ResultMessages.keys(), key=lambda x: int(x))
            for KeyIndex in range(0, len(SortedKeys)):
                if Result == SortedKeys[KeyIndex]:
                    self.ResultMessagesTreeWidget.SelectIndex(KeyIndex)
                    break

    def DeleteResultMessage(self):
        CurrentSelection = self.ResultMessagesTreeWidget.selectedItems()
        if len(CurrentSelection) > 0:
            if self.DiceRollerWindow.DisplayMessageBox("Are you sure you want to delete this result message?  This cannot be undone.", Icon=QMessageBox.Question, Buttons=(QMessageBox.Yes | QMessageBox.No)) == QMessageBox.Yes:
                CurrentResultMessage = CurrentSelection[0]
                CurrentResult = CurrentResultMessage.Result
                CurrentResultInt = int(CurrentResult)
                del self.ResultMessages[CurrentResult]
                self.UpdateDisplay()
                ResultMessagesLength = len(self.ResultMessages)
                if ResultMessagesLength > 0:
                    self.ResultMessagesTreeWidget.SelectIndex(CurrentResultInt if CurrentResultInt < ResultMessagesLength else ResultMessagesLength - 1)

    def EditResultMessage(self):
        CurrentSelection = self.ResultMessagesTreeWidget.selectedItems()
        if len(CurrentSelection) > 0:
            CurrentResultMessage = CurrentSelection[0]
            CurrentResult = CurrentResultMessage.Result
            EditResultMessageDialogInst = EditResultMessageDialog(CurrentResult, self, self.ResultMessages, self.DiceRollerWindow)
            if EditResultMessageDialogInst.Confirm:
                NewResult = EditResultMessageDialogInst.Result
                Message = EditResultMessageDialogInst.Message
                self.ResultMessages[NewResult] = Message
                if CurrentResult != NewResult:
                    del self.ResultMessages[CurrentResult]
                self.UpdateDisplay()
                SortedKeys = sorted(self.ResultMessages.keys(), key=lambda x: int(x))
                for KeyIndex in range(0, len(SortedKeys)):
                    if NewResult == SortedKeys[KeyIndex]:
                        self.ResultMessagesTreeWidget.SelectIndex(KeyIndex)
                        break

    def CopyResultMessage(self):
        CurrentSelection = self.ResultMessagesTreeWidget.selectedItems()
        if len(CurrentSelection) > 0:
            CurrentResultMessage = CurrentSelection[0]
            CopyResultMessageDialogInst = CopyResultMessageDialog(self, self.ResultMessages, self.DiceRollerWindow)
            if CopyResultMessageDialogInst.Confirm:
                Floor = CopyResultMessageDialogInst.RangeFloor
                Ceiling = CopyResultMessageDialogInst.RangeCeiling
                for Result in range(Floor, Ceiling + 1):
                    self.ResultMessages[str(Result)] = CurrentResultMessage.Message
                self.UpdateDisplay()

    def UpdateDisplay(self):
        self.ResultMessagesTreeWidget.FillFromResultMessages()

    def EditHook(self):
        pass


class AddResultMessageDialog(QDialog):
    def __init__(self, AddPresetRollDialog, ResultMessages, DiceRollerWindow):
        super().__init__(parent=AddPresetRollDialog)

        # Store Parameters
        self.AddPresetRollDialog = AddPresetRollDialog
        self.DiceRollerWindow = DiceRollerWindow
        self.ResultMessages = ResultMessages

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

        # Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.PromptLabel, 0, 0, 1, 2)
        self.Layout.addWidget(self.ResultLabel, 1, 0)
        self.Layout.addWidget(self.ResultSpinBox, 1, 1)
        self.Layout.addWidget(self.MessageLabel, 2, 0)
        self.Layout.addWidget(self.MessageLineEdit, 2, 1)
        self.ButtonsLayout = QGridLayout()
        self.ButtonsLayout.addWidget(self.AddButton, 0, 0)
        self.ButtonsLayout.addWidget(self.CancelButton, 0, 1)
        self.Layout.addLayout(self.ButtonsLayout, 3, 0, 1, 2)
        self.setLayout(self.Layout)

        # Set Window Title and Icon
        self.setWindowTitle(self.DiceRollerWindow.ScriptName)
        self.setWindowIcon(self.DiceRollerWindow.WindowIcon)

        # Edit Hook
        self.EditHook()

        # Execute Dialog
        self.exec_()

    def Add(self):
        if self.ValidInput():
            self.Result = str(self.ResultSpinBox.value())
            self.Message = self.MessageLineEdit.text()
            self.Confirm = True
            self.close()

    def Cancel(self):
        self.close()

    def ValidInput(self):
        if self.MessageLineEdit.text() == "":
            self.DiceRollerWindow.DisplayMessageBox("Result message cannot be blank.", Icon=QMessageBox.Warning, Parent=self)
            return False
        if str(self.ResultSpinBox.value()) in self.ResultMessages.keys():
            self.DiceRollerWindow.DisplayMessageBox("Result already has an associated message.  Please choose another result.", Icon=QMessageBox.Warning, Parent=self)
            return False
        return True

    def EditHook(self):
        pass


class EditPresetRollDialog(AddPresetRollDialog):
    def __init__(self, PresetRoll, DiceRollerWindow):
        # Store Parameters
        self.PresetRoll = PresetRoll

        # Initialize AddPresetRollDialog
        super().__init__(DiceRollerWindow)

    def EditHook(self):
        # Update Prompt and Button
        self.PromptLabel.setText("Edit preset roll?")
        self.AddButton.setText("Done")

        # Update Data
        self.NameLineEdit.setText(self.PresetRoll["Name"])
        self.DiceNumberSpinBox.setValue(self.PresetRoll["DiceNumber"])
        self.DieTypeSpinBox.setValue(self.PresetRoll["DieType"])
        self.ModifierSpinBox.setValue(self.PresetRoll["Modifier"])
        self.ResultMessages = self.PresetRoll["ResultMessages"].copy()
        self.ResultMessagesTreeWidget.ResultMessages = self.ResultMessages


class EditResultMessageDialog(AddResultMessageDialog):
    def __init__(self, CurrentResult, AddPresetRollDialog, ResultMessages, DiceRollerWindow):
        # Store Parameters
        self.CurrentResult = CurrentResult

        # Initialize AddResultMessageDialog
        super().__init__(AddPresetRollDialog, ResultMessages, DiceRollerWindow)

    def EditHook(self):
        # Update Prompt and Button
        self.PromptLabel.setText("Edit result message?")
        self.AddButton.setText("Done")

        # Update Data
        self.ResultSpinBox.setValue(int(self.CurrentResult))
        self.MessageLineEdit.setText(self.ResultMessages[self.CurrentResult])

    def ValidInput(self):
        if self.MessageLineEdit.text() == "":
            self.DiceRollerWindow.DisplayMessageBox("Result message cannot be blank.", Icon=QMessageBox.Warning, Parent=self)
            return False
        ResultValue = str(self.ResultSpinBox.value())
        if ResultValue in self.ResultMessages.keys() and ResultValue != self.CurrentResult:
            self.DiceRollerWindow.DisplayMessageBox("Result already has an associated message.  Please choose another result.", Icon=QMessageBox.Warning, Parent=self)
            return False
        return True


class CopyResultMessageDialog(QDialog):
    def __init__(self, AddPresetRollDialog, ResultMessages, DiceRollerWindow):
        super().__init__(parent=AddPresetRollDialog)

        # Store Parameters
        self.AddPresetRollDialog = AddPresetRollDialog
        self.ResultMessages = ResultMessages
        self.DiceRollerWindow = DiceRollerWindow

        # Variables
        self.RangeFloor = None
        self.RangeCeiling = None
        self.Confirm = False

        # Inputs Size Policy
        self.InputsSizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Prompt Label
        self.PromptLabel = QLabel("Copy result message to result range:")
        self.PromptLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Floor Spin Box
        self.FloorSpinBox = QSpinBox()
        self.FloorSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.FloorSpinBox.setSizePolicy(self.InputsSizePolicy)
        self.FloorSpinBox.setButtonSymbols(self.FloorSpinBox.NoButtons)
        self.FloorSpinBox.setRange(-1000000000, 1000000000)
        self.FloorSpinBox.setValue(1)

        # Range Label
        self.RangeLabel = QLabel("to")
        self.RangeLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Ceiling Spin Box
        self.CeilingSpinBox = QSpinBox()
        self.CeilingSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CeilingSpinBox.setSizePolicy(self.InputsSizePolicy)
        self.CeilingSpinBox.setButtonSymbols(self.CeilingSpinBox.NoButtons)
        self.CeilingSpinBox.setRange(-1000000000, 1000000000)
        self.CeilingSpinBox.setValue(1)

        # Buttons
        self.CopyButton = QPushButton("Copy")
        self.CopyButton.clicked.connect(self.Copy)
        self.CopyButton.setSizePolicy(self.InputsSizePolicy)
        self.CancelButton = QPushButton("Cancel")
        self.CancelButton.clicked.connect(self.Cancel)
        self.CancelButton.setSizePolicy(self.InputsSizePolicy)

        # Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.PromptLabel, 0, 0, 1, 3)
        self.Layout.addWidget(self.FloorSpinBox, 1, 0)
        self.Layout.addWidget(self.RangeLabel, 1, 1)
        self.Layout.addWidget(self.CeilingSpinBox, 1, 2)
        self.ButtonsLayout = QGridLayout()
        self.ButtonsLayout.addWidget(self.CopyButton, 0, 0)
        self.ButtonsLayout.addWidget(self.CancelButton, 0, 1)
        self.Layout.addLayout(self.ButtonsLayout, 2, 0, 1, 3)
        self.Layout.setRowStretch(1, 1)
        self.Layout.setRowStretch(2, 1)
        self.Layout.setColumnStretch(0, 1)
        self.Layout.setColumnStretch(2, 1)
        self.setLayout(self.Layout)

        # Set Window Title and Icon
        self.setWindowTitle(self.DiceRollerWindow.ScriptName)
        self.setWindowIcon(self.DiceRollerWindow.WindowIcon)

        # Execute Dialog
        self.exec_()

    def Copy(self):
        if self.ValidInput():
            self.Confirm = True
            self.RangeFloor = self.FloorSpinBox.value()
            self.RangeCeiling = self.CeilingSpinBox.value()
            self.close()

    def Cancel(self):
        self.close()

    def ValidInput(self):
        Floor = self.FloorSpinBox.value()
        Ceiling = self.CeilingSpinBox.value()
        if Floor > Ceiling:
            self.DiceRollerWindow.DisplayMessageBox("The floor of the range cannot be greater than the ceiling.")
            return False
        for Result in range(Floor, Ceiling + 1):
            if str(Result) in self.ResultMessages:
                self.DiceRollerWindow.DisplayMessageBox("Cannot copy.  At least one result in this range already has a message associated with it")
                return False
        return True
