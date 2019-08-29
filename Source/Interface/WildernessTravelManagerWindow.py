from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QFrame

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
        # Styles
        self.LabelStyle = "QLabel {font-size: 15pt;}"
        self.LineEditStyle = "QLineEdit {font-size: 20pt;}"
        self.LineEditStyleRed = "QLineEdit {font-size: 20pt; color: red;}"

        # Supply Pool Label
        self.SupplyPoolLabel = QLabel("Supply Pool")
        self.SupplyPoolLabel.setStyleSheet(self.LabelStyle)
        self.SupplyPoolLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Current Supply Points Line Edit
        self.CurrentSupplyPointsLineEdit = QLineEdit()
        self.CurrentSupplyPointsLineEdit.setReadOnly(True)
        self.CurrentSupplyPointsLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentSupplyPointsLineEdit.setStyleSheet(self.LineEditStyle)
        self.CurrentSupplyPointsLineEdit.setMaximumWidth(80)

        # Current Supply Points Buttons
        self.CurrentSupplyPointsIncreaseButton = QPushButton("+")
        self.CurrentSupplyPointsIncreaseButton.clicked.connect(lambda: self.ModifyCurrentSupplyPointsValue(1))
        self.CurrentSupplyPointsDecreaseButton = QPushButton("-")
        self.CurrentSupplyPointsDecreaseButton.clicked.connect(lambda: self.ModifyCurrentSupplyPointsValue(-1))

        # Supply Pool Divider Label
        self.SupplyPoolDividerLabel = QLabel("/")
        self.SupplyPoolDividerLabel.setStyleSheet(self.LineEditStyle)
        self.SupplyPoolDividerLabel.setMaximumWidth(10)

        # Supply Pool Line Edit
        self.SupplyPoolLineEdit = QLineEdit()
        self.SupplyPoolLineEdit.setReadOnly(True)
        self.SupplyPoolLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SupplyPoolLineEdit.setStyleSheet(self.LineEditStyle)
        self.SupplyPoolLineEdit.setMaximumWidth(80)

        # Supply Pool Buttons
        self.SupplyPoolIncreaseButton = QPushButton("+")
        self.SupplyPoolIncreaseButton.clicked.connect(lambda: self.ModifySupplyPoolValue(1))
        self.SupplyPoolDecreaseButton = QPushButton("-")
        self.SupplyPoolDecreaseButton.clicked.connect(lambda: self.ModifySupplyPoolValue(-1))

        # Wilderness Clock Label
        self.WildernessClockLabel = QLabel("Wilderness Clock")
        self.WildernessClockLabel.setStyleSheet(self.LabelStyle)
        self.WildernessClockLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Wilderness Clock Current Value Line Edit
        self.WildernessClockCurrentValueLineEdit = QLineEdit()
        self.WildernessClockCurrentValueLineEdit.setReadOnly(True)
        self.WildernessClockCurrentValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.WildernessClockCurrentValueLineEdit.setStyleSheet(self.LineEditStyle)
        self.WildernessClockCurrentValueLineEdit.setMaximumWidth(80)

        # Wilderness Clock Current Value Buttons
        self.WildernessClockCurrentValueIncreaseButton = QPushButton("+")
        self.WildernessClockCurrentValueIncreaseButton.clicked.connect(lambda: self.ModifyWildernessClockCurrentValue(1))
        self.WildernessClockCurrentValueDecreaseButton = QPushButton("-")
        self.WildernessClockCurrentValueDecreaseButton.clicked.connect(lambda: self.ModifyWildernessClockCurrentValue(-1))

        # Wilderness Clock Divider Label
        self.WildernessClockDividerLabel = QLabel("/")
        self.WildernessClockDividerLabel.setStyleSheet(self.LineEditStyle)
        self.WildernessClockDividerLabel.setMaximumWidth(10)

        # Wilderness Clock Maximum Value Line Edit
        self.WildernessClockMaximumValueLineEdit = QLineEdit()
        self.WildernessClockMaximumValueLineEdit.setReadOnly(True)
        self.WildernessClockMaximumValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.WildernessClockMaximumValueLineEdit.setStyleSheet(self.LineEditStyle)
        self.WildernessClockMaximumValueLineEdit.setMaximumWidth(80)

        # Wilderness Clock Maximum Value Buttons
        self.WildernessClockMaximumValueIncreaseButton = QPushButton("+")
        self.WildernessClockMaximumValueIncreaseButton.clicked.connect(lambda: self.ModifyWildernessClockMaximumValue(1))
        self.WildernessClockMaximumValueDecreaseButton = QPushButton("-")
        self.WildernessClockMaximumValueDecreaseButton.clicked.connect(lambda: self.ModifyWildernessClockMaximumValue(-1))

        # Create Layout
        self.Layout = QGridLayout()

        # Supply Pool Widgets in Layout
        self.SupplyPoolFrame = QFrame()
        self.SupplyPoolFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.SupplyPoolLayout = QGridLayout()
        self.SupplyPoolLayout.addWidget(self.SupplyPoolLabel, 0, 0, 1, 3)
        self.SupplyPoolLayout.addWidget(self.CurrentSupplyPointsIncreaseButton, 1, 0)
        self.SupplyPoolLayout.addWidget(self.SupplyPoolIncreaseButton, 1, 2)
        self.SupplyPoolLayout.addWidget(self.CurrentSupplyPointsLineEdit, 2, 0)
        self.SupplyPoolLayout.addWidget(self.SupplyPoolDividerLabel, 2, 1)
        self.SupplyPoolLayout.addWidget(self.SupplyPoolLineEdit, 2, 2)
        self.SupplyPoolLayout.addWidget(self.CurrentSupplyPointsDecreaseButton, 3, 0)
        self.SupplyPoolLayout.addWidget(self.SupplyPoolDecreaseButton, 3, 2)
        self.SupplyPoolFrame.setLayout(self.SupplyPoolLayout)
        self.Layout.addWidget(self.SupplyPoolFrame, 0, 0)

        # Add Wilderness Clock Widgets to Layout
        self.WildernessClockFrame = QFrame()
        self.WildernessClockFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.WildernessClockLayout = QGridLayout()
        self.WildernessClockLayout.addWidget(self.WildernessClockLabel, 0, 0, 1, 3)
        self.WildernessClockLayout.addWidget(self.WildernessClockCurrentValueIncreaseButton, 1, 0)
        self.WildernessClockLayout.addWidget(self.WildernessClockCurrentValueLineEdit, 2, 0)
        self.WildernessClockLayout.addWidget(self.WildernessClockCurrentValueDecreaseButton, 3, 0)
        self.WildernessClockLayout.addWidget(self.WildernessClockDividerLabel, 2, 1)
        self.WildernessClockLayout.addWidget(self.WildernessClockMaximumValueIncreaseButton, 1, 2)
        self.WildernessClockLayout.addWidget(self.WildernessClockMaximumValueLineEdit, 2, 2)
        self.WildernessClockLayout.addWidget(self.WildernessClockMaximumValueDecreaseButton, 3, 2)
        self.WildernessClockFrame.setLayout(self.WildernessClockLayout)
        self.Layout.addWidget(self.WildernessClockFrame)

        # Set Layout
        self.Frame.setLayout(self.Layout)

    def ModifySupplyPoolValue(self, Delta):
        self.WildernessTravelManager.ModifySupplyPoolValue(Delta)
        self.UpdateDisplay()

    def ModifyCurrentSupplyPointsValue(self, Delta):
        self.WildernessTravelManager.ModifyCurrentSupplyPointsValue(Delta)
        self.UpdateDisplay()

    def ModifyWildernessClockCurrentValue(self, Delta):
        self.WildernessTravelManager.ModifyWildernessClockCurrentValue(Delta)
        self.UpdateDisplay()

    def ModifyWildernessClockMaximumValue(self, Delta):
        self.WildernessTravelManager.ModifyWildernessClockMaximumValue(Delta)
        self.UpdateDisplay()

    def UpdateDisplay(self):
        # Supply Pool Display
        self.CurrentSupplyPointsLineEdit.setText(str(self.WildernessTravelManager.CurrentSupplyPoints))
        self.SupplyPoolLineEdit.setText(str(self.WildernessTravelManager.SupplyPool))

        # Check Supply Pool Values Too Low
        self.CurrentSupplyPointsLineEdit.setStyleSheet(self.LineEditStyleRed if self.WildernessTravelManager.CurrentSupplyPoints < 0 else self.LineEditStyle)
        self.SupplyPoolLineEdit.setStyleSheet(
            self.LineEditStyleRed if self.WildernessTravelManager.SupplyPool < self.WildernessTravelManager.CurrentSupplyPoints or self.WildernessTravelManager.SupplyPool < 0 else self.LineEditStyle)

        # Wilderness Clock Display
        self.WildernessClockCurrentValueLineEdit.setText(str(self.WildernessTravelManager.WildernessClock.Value))
        self.WildernessClockMaximumValueLineEdit.setText(str(self.WildernessTravelManager.WildernessClock.MaximumValue))
