from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QGridLayout, QPushButton


class AddPresetRollDialog(QDialog):
    def __init__(self, DiceRollerWindow):
        super().__init__(parent=DiceRollerWindow)

        # Store Parameters
        self.DiceRollerWindow = DiceRollerWindow

        # Variables
        self.Confirm = False

        # Labels
        self.NameLabel = QLabel("Name:")
        self.DieTypeLabel = QLabel("d")
        self.ModifierLabel = QLabel("+")

        # Line Edits
        self.NameLineEdit = QLineEdit()

        self.DiceNumberLineEdit = QLineEdit()
        self.DiceNumberLineEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.DieTypeLineEdit = QLineEdit()
        self.DieTypeLineEdit.setAlignment(QtCore.Qt.AlignCenter)

        self.ModifierLineEdit = QLineEdit()
        self.ModifierLineEdit.setAlignment(QtCore.Qt.AlignCenter)

        # Buttons
        self.DoneButton = QPushButton("Done")
        self.DoneButton.clicked.connect(self.Done)
        self.CancelButton = QPushButton("Cancel")
        self.CancelButton.clicked.connect(self.Cancel)

        # Layout
        self.Layout = QGridLayout()
        self.NameLayout = QGridLayout()
        self.NameLayout.addWidget(self.NameLabel, 0, 0)
        self.NameLayout.addWidget(self.NameLineEdit, 0, 1)
        self.NameLayout.setColumnStretch(1, 1)
        self.Layout.addLayout(self.NameLayout, 0, 0, 1, 2)
        self.DiceInputsLayout = QGridLayout()
        self.DiceInputsLayout.addWidget(self.DiceNumberLineEdit, 0, 0)
        self.DiceInputsLayout.addWidget(self.DieTypeLabel, 0, 1)
        self.DiceInputsLayout.addWidget(self.DieTypeLineEdit, 0, 2)
        self.DiceInputsLayout.addWidget(self.ModifierLabel, 0, 3)
        self.DiceInputsLayout.addWidget(self.ModifierLineEdit, 0, 4)
        self.DiceInputsLayout.setColumnStretch(0, 1)
        self.DiceInputsLayout.setColumnStretch(2, 1)
        self.DiceInputsLayout.setColumnStretch(4, 1)
        self.Layout.addLayout(self.DiceInputsLayout, 1, 0, 1, 2)
        self.Layout.addWidget(self.DoneButton, 3, 0)
        self.Layout.addWidget(self.CancelButton, 3, 1)
        self.setLayout(self.Layout)

        # Set Window Title and Icon
        self.setWindowTitle(self.DiceRollerWindow.ScriptName)
        self.setWindowIcon(self.DiceRollerWindow.WindowIcon)

        # Execute Dialog
        self.exec_()

    def Done(self):
        pass

    def Cancel(self):
        pass
