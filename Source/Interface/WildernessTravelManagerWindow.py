import math

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QFrame, QTextEdit, QInputDialog

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
        self.LineEditStyleYellow = "QLineEdit {font-size: 20pt; color: goldenrod;}"
        self.LineEditStyleRed = "QLineEdit {font-size: 20pt; color: red;}"

        # Travel Actions Label
        self.TravelActionsLabel = QLabel("Travel Actions")
        self.TravelActionsLabel.setStyleSheet(self.LabelStyle)
        self.TravelActionsLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Travel Action Buttons
        self.MoveButton = QPushButton("Move")
        self.MoveButton.clicked.connect(self.Move)
        self.ForageButton = QPushButton("Forage")
        self.ForageButton.clicked.connect(self.Forage)
        self.ShortRestButton = QPushButton("Short Rest")
        self.ShortRestButton.clicked.connect(self.ShortRest)
        self.LongRestButton = QPushButton("Long Rest")
        self.LongRestButton.clicked.connect(self.LongRest)
        self.PurchaseSuppliesButton = QPushButton("Purchase Supplies")
        self.PurchaseSuppliesButton.clicked.connect(self.PurchaseSupplies)
        self.SeekShortTermLodgingButton = QPushButton("Seek Short-Term Lodging")
        self.SeekShortTermLodgingButton.clicked.connect(self.SeekShortTermLodging)
        self.SeekLongTermLodgingButton = QPushButton("Seek Long-Term Lodging")
        self.SeekLongTermLodgingButton.clicked.connect(self.SeekLongTermLodging)
        self.SpendSuppliesButton = QPushButton("Spend Supplies")
        self.SpendSuppliesButton.clicked.connect(self.SpendSupplies)
        self.SpendDaysButton = QPushButton("Spend Days")
        self.SpendDaysButton.clicked.connect(self.SpendDays)
        self.SpendSuppliesAndDaysButton = QPushButton("Spend Supplies and Days")
        self.SpendSuppliesAndDaysButton.clicked.connect(self.SpendSuppliesAndDays)

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

        # Wilderness Log Label
        self.WildernessLogLabel = QLabel("Wilderness Log")
        self.WildernessLogLabel.setStyleSheet(self.LabelStyle)
        self.WildernessLogLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Wilderness Log Text Edit
        self.WildernessLogTextEdit = QTextEdit()
        self.WildernessLogTextEdit.setReadOnly(True)

        # Create Layout
        self.Layout = QGridLayout()

        # Travel Action Widgets in Layout
        self.TravelActionsFrame = QFrame()
        self.TravelActionsFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.TravelActionsLayout = QGridLayout()
        self.TravelActionsLayout.addWidget(self.TravelActionsLabel, 0, 0)
        self.TravelActionsLayout.addWidget(self.MoveButton, 1, 0)
        self.TravelActionsLayout.addWidget(self.ForageButton, 2, 0)
        self.TravelActionsLayout.addWidget(self.ShortRestButton, 3, 0)
        self.TravelActionsLayout.addWidget(self.LongRestButton, 4, 0)
        self.TravelActionsLayout.addWidget(self.PurchaseSuppliesButton, 5, 0)
        self.TravelActionsLayout.addWidget(self.SeekShortTermLodgingButton, 6, 0)
        self.TravelActionsLayout.addWidget(self.SeekLongTermLodgingButton, 7, 0)
        self.TravelActionsLayout.addWidget(self.SpendSuppliesButton, 8, 0)
        self.TravelActionsLayout.addWidget(self.SpendDaysButton, 9, 0)
        self.TravelActionsLayout.addWidget(self.SpendSuppliesAndDaysButton, 10, 0)
        self.TravelActionsFrame.setLayout(self.TravelActionsLayout)
        self.Layout.addWidget(self.TravelActionsFrame, 0, 0, 2, 1)

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
        self.Layout.addWidget(self.SupplyPoolFrame, 0, 1)

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
        self.Layout.addWidget(self.WildernessClockFrame, 1, 1)

        # Add Wilderness Log Widgets to Layout
        self.WildernessLogFrame = QFrame()
        self.WildernessLogFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.WildernessLogLayout = QGridLayout()
        self.WildernessLogLayout.addWidget(self.WildernessLogLabel, 0, 0)
        self.WildernessLogLayout.addWidget(self.WildernessLogTextEdit, 1, 0)
        self.WildernessLogFrame.setLayout(self.WildernessLogLayout)
        self.Layout.addWidget(self.WildernessLogFrame, 0, 2, 2, 1)

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

    def Move(self):
        TravelCost, OK = QInputDialog.getInt(self, "Travel Cost", "Travel cost to move:", 1, 1)
        if OK:
            self.WildernessTravelManager.Move(TravelCost)
            self.UpdateDisplay()

    def Forage(self):
        NumberOfSuccesses, OK = QInputDialog.getItem(self, "Forage Success", "Number of party members who succeeded:", ["None", "Half or More", "All"])
        if OK:
            if NumberOfSuccesses == "Half or More":
                HalfSucceeded = True
                AllSucceeded = False
            elif NumberOfSuccesses == "All":
                HalfSucceeded = False
                AllSucceeded = True
            else:
                HalfSucceeded = False
                AllSucceeded = False
            self.WildernessTravelManager.Forage(HalfSucceeded, AllSucceeded)
            self.UpdateDisplay()

    def ShortRest(self):
        self.WildernessTravelManager.ShortRest()
        self.UpdateDisplay()

    def LongRest(self):
        self.WildernessTravelManager.LongRest()
        self.UpdateDisplay()

    def PurchaseSupplies(self):
        self.WildernessTravelManager.PurchaseSupplies()
        self.UpdateDisplay()

    def SeekShortTermLodging(self):
        self.WildernessTravelManager.SeekShortTermLodging()
        self.UpdateDisplay()

    def SeekLongTermLodging(self):
        self.WildernessTravelManager.SeekLongTermLodging()
        self.UpdateDisplay()

    def SpendSupplies(self):
        self.WildernessTravelManager.SpendSupplies(1, Log=True)
        self.UpdateDisplay()

    def SpendDays(self):
        self.WildernessTravelManager.SpendDays(1, Log=True)
        self.UpdateDisplay()

    def SpendSuppliesAndDays(self):
        self.WildernessTravelManager.SpendSuppliesAndDays(1, Log=True)
        self.UpdateDisplay()

    def UpdateDisplay(self):
        # Supply Pool Display
        self.CurrentSupplyPointsLineEdit.setText(str(self.WildernessTravelManager.CurrentSupplyPoints))
        self.SupplyPoolLineEdit.setText(str(self.WildernessTravelManager.SupplyPool))

        # Check Supply Pool Values Too Low
        if self.WildernessTravelManager.CurrentSupplyPoints < 0:
            self.CurrentSupplyPointsLineEdit.setStyleSheet(self.LineEditStyleRed)
        elif self.WildernessTravelManager.CurrentSupplyPoints <= math.floor(0.5 * self.WildernessTravelManager.SupplyPool) and self.WildernessTravelManager.SupplyPool > 0:
            self.CurrentSupplyPointsLineEdit.setStyleSheet(self.LineEditStyleYellow)
        else:
            self.CurrentSupplyPointsLineEdit.setStyleSheet(self.LineEditStyle)
        if self.WildernessTravelManager.SupplyPool < self.WildernessTravelManager.CurrentSupplyPoints or self.WildernessTravelManager.SupplyPool < 0:
            self.SupplyPoolLineEdit.setStyleSheet(self.LineEditStyleRed)
        else:
            self.SupplyPoolLineEdit.setStyleSheet(self.LineEditStyle)

        # Wilderness Clock Display
        self.WildernessClockCurrentValueLineEdit.setText(str(self.WildernessTravelManager.WildernessClock.Value))
        self.WildernessClockMaximumValueLineEdit.setText(str(self.WildernessTravelManager.WildernessClock.MaximumValue))

        # Wilderness Log Display
        WildernessLogString = ""
        for LogEntry in reversed(self.WildernessTravelManager.WildernessLog):
            WildernessLogString += LogEntry + "\n\n---\n\n"
        self.WildernessLogTextEdit.setPlainText(WildernessLogString[:-7])
