from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton

from Core.WildernessTravelManager import WildernessTravelManager
from Interface.Window import Window


class WildernessTravelManagerWindow(Window):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Wilderness Travel Manager
        self.WildernessTravelManager = WildernessTravelManager()

        # Update Display
        self.UpdateDisplay()

    def CreateInterface(self):
        # Supply Pool Styles
        self.SupplyPoolStyle = "QLabel {font-size: 20pt;} QLineEdit {font-size: 20pt;}"
        self.SupplyPoolStyleRed = "QLineEdit {font-size: 20pt; color: red}"

        # Supply Pool Label
        self.SupplyPoolLabel = QLabel("Supply Pool")
        self.SupplyPoolLabel.setStyleSheet(self.SupplyPoolStyle)
        self.SupplyPoolLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Current Supply Points Line Edit
        self.CurrentSupplyPointsLineEdit = QLineEdit()
        self.CurrentSupplyPointsLineEdit.setReadOnly(True)
        self.CurrentSupplyPointsLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentSupplyPointsLineEdit.setStyleSheet(self.SupplyPoolStyle)
        self.CurrentSupplyPointsLineEdit.setMaximumWidth(80)

        # Current Supply Points Buttons
        self.CurrentSupplyPointsIncreaseButton = QPushButton("+")
        self.CurrentSupplyPointsIncreaseButton.clicked.connect(lambda: self.ModifyCurrentSupplyPointsValue(1))
        self.CurrentSupplyPointsDecreaseButton = QPushButton("-")
        self.CurrentSupplyPointsDecreaseButton.clicked.connect(lambda: self.ModifyCurrentSupplyPointsValue(-1))

        # Supply Pool Divider Label
        self.SupplyPoolDividerLabel = QLabel("/")
        self.SupplyPoolDividerLabel.setStyleSheet(self.SupplyPoolStyle)
        self.SupplyPoolDividerLabel.setMaximumWidth(10)

        # Supply Pool Line Edit
        self.SupplyPoolLineEdit = QLineEdit()
        self.SupplyPoolLineEdit.setReadOnly(True)
        self.SupplyPoolLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SupplyPoolLineEdit.setStyleSheet(self.SupplyPoolStyle)
        self.SupplyPoolLineEdit.setMaximumWidth(80)

        # Supply Pool Buttons
        self.SupplyPoolIncreaseButton = QPushButton("+")
        self.SupplyPoolIncreaseButton.clicked.connect(lambda: self.ModifySupplyPoolValue(1))
        self.SupplyPoolDecreaseButton = QPushButton("-")
        self.SupplyPoolDecreaseButton.clicked.connect(lambda: self.ModifySupplyPoolValue(-1))

        # Create Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.SupplyPoolLabel, 0, 0, 1, 3)
        self.Layout.addWidget(self.CurrentSupplyPointsIncreaseButton, 1, 0)
        self.Layout.addWidget(self.SupplyPoolIncreaseButton, 1, 2)
        self.Layout.addWidget(self.CurrentSupplyPointsLineEdit, 2, 0)
        self.Layout.addWidget(self.SupplyPoolDividerLabel, 2, 1)
        self.Layout.addWidget(self.SupplyPoolLineEdit, 2, 2)
        self.Layout.addWidget(self.CurrentSupplyPointsDecreaseButton, 3, 0)
        self.Layout.addWidget(self.SupplyPoolDecreaseButton, 3, 2)
        self.Frame.setLayout(self.Layout)

    def ModifySupplyPoolValue(self, Delta):
        self.WildernessTravelManager.ModifySupplyPoolValue(Delta)
        self.UpdateDisplay()

    def ModifyCurrentSupplyPointsValue(self, Delta):
        self.WildernessTravelManager.ModifyCurrentSupplyPointsValue(Delta)
        self.UpdateDisplay()

    def UpdateDisplay(self):
        # Supply Pool Display
        self.CurrentSupplyPointsLineEdit.setText(str(self.WildernessTravelManager.CurrentSupplyPoints))
        self.SupplyPoolLineEdit.setText(str(self.WildernessTravelManager.SupplyPool))

        # Check Supply Pool Values Too Low
        self.CurrentSupplyPointsLineEdit.setStyleSheet(self.SupplyPoolStyleRed if self.WildernessTravelManager.CurrentSupplyPoints < 0 else self.SupplyPoolStyle)
        self.SupplyPoolLineEdit.setStyleSheet(
            self.SupplyPoolStyleRed if self.WildernessTravelManager.SupplyPool < self.WildernessTravelManager.CurrentSupplyPoints or self.WildernessTravelManager.SupplyPool < 0 else self.SupplyPoolStyle)
