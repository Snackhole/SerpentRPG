import math
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPushButton, QFrame, QTextEdit, QInputDialog, QSizePolicy, QAction, QMessageBox

from Core.DieClock import DieClock
from Core.WildernessTravelManager import WildernessTravelManager
from Interface.Window import Window
from SaveAndLoad.SaveAndOpenMixin import SaveAndOpenMixin


class WildernessTravelManagerWindow(Window, SaveAndOpenMixin):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Wilderness Travel Manager
        self.WildernessTravelManager = WildernessTravelManager()

        # Set Up Save and Open
        self.SetUpSaveAndOpen(".wildtrvl", "Wilderness Travel Manager", (WildernessTravelManager, DieClock))

        # Update Display
        self.UpdateDisplay()

    def CreateInterface(self):
        # Styles
        self.LabelStyle = "QLabel {font-size: 20pt;}"
        self.LineEditStyle = "QLineEdit {font-size: 20pt;}"
        self.LineEditStyleYellow = "QLineEdit {font-size: 20pt; color: goldenrod;}"
        self.LineEditStyleRed = "QLineEdit {font-size: 20pt; color: red;}"
        self.PoolAndClockButtonStyle = "QPushButton {font-size: 20pt;}"

        # Button and Line Edit Size Policy
        self.ButtonAndLineEditSizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        # Pool and Clock Width
        self.PoolAndClockWidth = 160

        # Travel Actions Label
        self.TravelActionsLabel = QLabel("Travel Actions")
        self.TravelActionsLabel.setStyleSheet(self.LabelStyle)
        self.TravelActionsLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Travel Action Buttons
        self.MoveButton = QPushButton("Move")
        self.MoveButton.clicked.connect(self.Move)
        self.MoveButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.ForageButton = QPushButton("Forage")
        self.ForageButton.clicked.connect(self.Forage)
        self.ForageButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.ShortRestButton = QPushButton("Short Rest")
        self.ShortRestButton.clicked.connect(self.ShortRest)
        self.ShortRestButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.LongRestButton = QPushButton("Long Rest")
        self.LongRestButton.clicked.connect(self.LongRest)
        self.LongRestButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.PurchaseSuppliesButton = QPushButton("Purchase Supplies")
        self.PurchaseSuppliesButton.clicked.connect(self.PurchaseSupplies)
        self.PurchaseSuppliesButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SeekShortTermLodgingButton = QPushButton("Seek Short-Term Lodging")
        self.SeekShortTermLodgingButton.clicked.connect(self.SeekShortTermLodging)
        self.SeekShortTermLodgingButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SeekLongTermLodgingButton = QPushButton("Seek Long-Term Lodging")
        self.SeekLongTermLodgingButton.clicked.connect(self.SeekLongTermLodging)
        self.SeekLongTermLodgingButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SpendSuppliesButton = QPushButton("Spend Supplies")
        self.SpendSuppliesButton.clicked.connect(self.SpendSupplies)
        self.SpendSuppliesButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SpendDaysButton = QPushButton("Spend Days")
        self.SpendDaysButton.clicked.connect(self.SpendDays)
        self.SpendDaysButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SpendSuppliesAndDaysButton = QPushButton("Spend Supplies and Days")
        self.SpendSuppliesAndDaysButton.clicked.connect(self.SpendSuppliesAndDays)
        self.SpendSuppliesAndDaysButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.GainSuppliesButton = QPushButton("Gain Supplies")
        self.GainSuppliesButton.clicked.connect(self.GainSupplies)
        self.GainSuppliesButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)

        # Supply Pool Label
        self.SupplyPoolLabel = QLabel("Supply Pool")
        self.SupplyPoolLabel.setStyleSheet(self.LabelStyle)
        self.SupplyPoolLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Current Supply Points Line Edit
        self.CurrentSupplyPointsLineEdit = QLineEdit()
        self.CurrentSupplyPointsLineEdit.setReadOnly(True)
        self.CurrentSupplyPointsLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentSupplyPointsLineEdit.setStyleSheet(self.LineEditStyle)
        self.CurrentSupplyPointsLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.CurrentSupplyPointsLineEdit.setFixedWidth(self.PoolAndClockWidth)

        # Current Supply Points Buttons
        self.CurrentSupplyPointsIncreaseButton = QPushButton("+")
        self.CurrentSupplyPointsIncreaseButton.clicked.connect(lambda: self.ModifyCurrentSupplyPointsValue(1))
        self.CurrentSupplyPointsIncreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.CurrentSupplyPointsIncreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)
        self.CurrentSupplyPointsDecreaseButton = QPushButton("-")
        self.CurrentSupplyPointsDecreaseButton.clicked.connect(lambda: self.ModifyCurrentSupplyPointsValue(-1))
        self.CurrentSupplyPointsDecreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.CurrentSupplyPointsDecreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)

        # Supply Pool Divider Label
        self.SupplyPoolDividerLabel = QLabel("/")
        self.SupplyPoolDividerLabel.setStyleSheet(self.LabelStyle)
        self.SupplyPoolDividerLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Supply Pool Line Edit
        self.SupplyPoolLineEdit = QLineEdit()
        self.SupplyPoolLineEdit.setReadOnly(True)
        self.SupplyPoolLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.SupplyPoolLineEdit.setStyleSheet(self.LineEditStyle)
        self.SupplyPoolLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SupplyPoolLineEdit.setFixedWidth(self.PoolAndClockWidth)

        # Supply Pool Buttons
        self.SupplyPoolIncreaseButton = QPushButton("+")
        self.SupplyPoolIncreaseButton.clicked.connect(lambda: self.ModifySupplyPoolValue(1))
        self.SupplyPoolIncreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SupplyPoolIncreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)
        self.SupplyPoolDecreaseButton = QPushButton("-")
        self.SupplyPoolDecreaseButton.clicked.connect(lambda: self.ModifySupplyPoolValue(-1))
        self.SupplyPoolDecreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.SupplyPoolDecreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)

        # Wilderness Clock Label
        self.WildernessClockLabel = QLabel("Wilderness Clock")
        self.WildernessClockLabel.setStyleSheet(self.LabelStyle)
        self.WildernessClockLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Wilderness Clock Current Value Line Edit
        self.WildernessClockCurrentValueLineEdit = QLineEdit()
        self.WildernessClockCurrentValueLineEdit.setReadOnly(True)
        self.WildernessClockCurrentValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.WildernessClockCurrentValueLineEdit.setStyleSheet(self.LineEditStyle)
        self.WildernessClockCurrentValueLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockCurrentValueLineEdit.setFixedWidth(self.PoolAndClockWidth)

        # Wilderness Clock Current Value Buttons
        self.WildernessClockCurrentValueIncreaseButton = QPushButton("+")
        self.WildernessClockCurrentValueIncreaseButton.clicked.connect(lambda: self.ModifyWildernessClockCurrentValue(1))
        self.WildernessClockCurrentValueIncreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockCurrentValueIncreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)
        self.WildernessClockCurrentValueDecreaseButton = QPushButton("-")
        self.WildernessClockCurrentValueDecreaseButton.clicked.connect(lambda: self.ModifyWildernessClockCurrentValue(-1))
        self.WildernessClockCurrentValueDecreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockCurrentValueDecreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)

        # Wilderness Clock Divider Label
        self.WildernessClockDividerLabel = QLabel("/")
        self.WildernessClockDividerLabel.setStyleSheet(self.LabelStyle)
        self.WildernessClockDividerLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Wilderness Clock Maximum Value Line Edit
        self.WildernessClockMaximumValueLineEdit = QLineEdit()
        self.WildernessClockMaximumValueLineEdit.setReadOnly(True)
        self.WildernessClockMaximumValueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.WildernessClockMaximumValueLineEdit.setStyleSheet(self.LineEditStyle)
        self.WildernessClockMaximumValueLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockMaximumValueLineEdit.setFixedWidth(self.PoolAndClockWidth)

        # Wilderness Clock Maximum Value Buttons
        self.WildernessClockMaximumValueIncreaseButton = QPushButton("+")
        self.WildernessClockMaximumValueIncreaseButton.clicked.connect(lambda: self.ModifyWildernessClockMaximumValue(1))
        self.WildernessClockMaximumValueIncreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockMaximumValueIncreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)
        self.WildernessClockMaximumValueDecreaseButton = QPushButton("-")
        self.WildernessClockMaximumValueDecreaseButton.clicked.connect(lambda: self.ModifyWildernessClockMaximumValue(-1))
        self.WildernessClockMaximumValueDecreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockMaximumValueDecreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)

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
        self.TravelActionsLayout.addWidget(self.GainSuppliesButton, 11, 0)
        for Row in range(1, 12):
            self.TravelActionsLayout.setRowStretch(Row, 1)
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
        self.SupplyPoolLayout.setRowStretch(1, 1)
        self.SupplyPoolLayout.setRowStretch(2, 2)
        self.SupplyPoolLayout.setRowStretch(3, 1)
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
        self.WildernessClockLayout.setRowStretch(1, 1)
        self.WildernessClockLayout.setRowStretch(2, 2)
        self.WildernessClockLayout.setRowStretch(3, 1)
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

        # Set and Configure Layout
        self.Layout.setColumnStretch(2, 1)
        self.Frame.setLayout(self.Layout)

        # Create Menu Actions
        self.NewAction = QAction("New")
        self.NewAction.setShortcut("Ctrl+N")
        self.NewAction.triggered.connect(self.NewActionTriggered)

        self.OpenAction = QAction("Open")
        self.OpenAction.setShortcut("Ctrl+O")
        self.OpenAction.triggered.connect(self.OpenActionTriggered)

        self.SaveAction = QAction("Save")
        self.SaveAction.setShortcut("Ctrl+S")
        self.SaveAction.triggered.connect(self.SaveActionTriggered)

        self.SaveAsAction = QAction("Save As")
        self.SaveAsAction.setShortcut("Ctrl+Shift+S")
        self.SaveAsAction.triggered.connect(self.SaveAsActionTriggered)

        self.QuitAction = QAction("Quit")
        self.QuitAction.setShortcut("Ctrl+Q")
        self.QuitAction.triggered.connect(self.close)

        self.AddToLogAction = QAction("Add to Log")
        self.AddToLogAction.triggered.connect(self.AddToLog)

        self.RemoveLastLogEntryAction = QAction("Remove Last Log Entry")
        self.RemoveLastLogEntryAction.triggered.connect(self.RemoveLastLogEntry)

        self.ClearLogAction = QAction("Clear Log")
        self.ClearLogAction.triggered.connect(self.ClearLog)

        # Menu Bar
        self.MenuBar = self.menuBar()

        self.FileMenu = self.MenuBar.addMenu("File")
        self.FileMenu.addAction(self.NewAction)
        self.FileMenu.addAction(self.OpenAction)
        self.FileMenu.addSeparator()
        self.FileMenu.addAction(self.SaveAction)
        self.FileMenu.addAction(self.SaveAsAction)
        self.FileMenu.addSeparator()
        self.FileMenu.addAction(self.QuitAction)

        self.LogMenu = self.MenuBar.addMenu("Log")
        self.LogMenu.addAction(self.AddToLogAction)
        self.LogMenu.addAction(self.RemoveLastLogEntryAction)
        self.LogMenu.addAction(self.ClearLogAction)

    # Modify Values Methods
    def ModifySupplyPoolValue(self, Delta):
        self.WildernessTravelManager.ModifySupplyPoolValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def ModifyCurrentSupplyPointsValue(self, Delta):
        self.WildernessTravelManager.ModifyCurrentSupplyPointsValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def ModifyWildernessClockCurrentValue(self, Delta):
        self.WildernessTravelManager.ModifyWildernessClockCurrentValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def ModifyWildernessClockMaximumValue(self, Delta):
        self.WildernessTravelManager.ModifyWildernessClockMaximumValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    # Travel Action Methods
    def Move(self):
        TravelCost, OK = QInputDialog.getInt(self, "Travel Cost", "Travel cost to move:", 1, 1)
        if OK:
            self.WildernessTravelManager.Move(TravelCost)
            self.UpdateUnsavedChangesFlag(True)

    def Forage(self):
        NumberOfSuccesses, OK = QInputDialog.getItem(self, "Forage Success", "Number of party members who succeeded:", ["None", "Half or More", "All"], editable=False)
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
            self.UpdateUnsavedChangesFlag(True)

    def ShortRest(self):
        self.WildernessTravelManager.ShortRest()
        self.UpdateUnsavedChangesFlag(True)

    def LongRest(self):
        self.WildernessTravelManager.LongRest()
        self.UpdateUnsavedChangesFlag(True)

    def PurchaseSupplies(self):
        SupplyPointsGained, OK = QInputDialog.getInt(self, "Purchase Supplies", "Supply points purchased:", 1, 1)
        if OK:
            self.WildernessTravelManager.PurchaseSupplies(SupplyPointsGained)
            self.UpdateUnsavedChangesFlag(True)

    def SeekShortTermLodging(self):
        PaidWithSupplyPoint, OK = QInputDialog.getItem(self, "Short-Term Lodging", "Paid with Supply point or other value:", ["Supply Point", "Other Value"], editable=False)
        if OK:
            self.WildernessTravelManager.SeekShortTermLodging(PaidWithSupplyPoint == "Supply Point")
            self.UpdateUnsavedChangesFlag(True)

    def SeekLongTermLodging(self):
        PaidWithSupplyPoints, OK = QInputDialog.getItem(self, "Long-Term Lodging", "Paid with Supply points or other value:", ["Supply Points", "Other Value"], editable=False)
        if OK:
            self.WildernessTravelManager.SeekLongTermLodging(PaidWithSupplyPoints == "Supply Points")
            self.UpdateUnsavedChangesFlag(True)

    def SpendSupplies(self):
        SupplyPointsSpent, OK = QInputDialog.getInt(self, "Spend Supplies", "Supply points spent:", 1, 1)
        if OK:
            self.WildernessTravelManager.SpendSupplies(SupplyPointsSpent, Log=True)
            self.UpdateUnsavedChangesFlag(True)

    def SpendDays(self):
        DaysSpent, OK = QInputDialog.getInt(self, "Spend Days", "Days spent:", 1, 1)
        if OK:
            self.WildernessTravelManager.SpendDays(DaysSpent, Log=True)
            self.UpdateUnsavedChangesFlag(True)

    def SpendSuppliesAndDays(self):
        SupplyPointsAndDaysSpent, OK = QInputDialog.getInt(self, "Spend Supplies and Days", "Supply points and days spent:", 1, 1)
        if OK:
            self.WildernessTravelManager.SpendSuppliesAndDays(SupplyPointsAndDaysSpent, Log=True)
            self.UpdateUnsavedChangesFlag(True)

    def GainSupplies(self):
        SupplyPointsGained, OK = QInputDialog.getInt(self, "Gain Supplies", "Supply points gained:", 1, 1)
        if OK:
            self.WildernessTravelManager.GainSupplies(SupplyPointsGained, Log=True)
            self.UpdateUnsavedChangesFlag(True)

    # File Menu Action Methods
    def NewActionTriggered(self):
        if self.New(self.WildernessTravelManager):
            self.WildernessTravelManager = WildernessTravelManager()
        self.UpdateDisplay()

    def OpenActionTriggered(self):
        OpenData = self.Open(self.WildernessTravelManager)
        if OpenData is not None:
            self.WildernessTravelManager = OpenData
        self.UpdateDisplay()

    def SaveActionTriggered(self):
        self.Save(self.WildernessTravelManager)
        self.UpdateDisplay()

    def SaveAsActionTriggered(self):
        self.Save(self.WildernessTravelManager, SaveAs=True)
        self.UpdateDisplay()

    # Log Menu Action Methods
    def AddToLog(self):
        LogString, OK = QInputDialog.getText(self, "Add to Log", "Add this to the Wilderness Log:")
        if OK:
            self.WildernessTravelManager.Log(LogString)
            self.UpdateUnsavedChangesFlag(True)

    def RemoveLastLogEntry(self):
        if self.DisplayMessageBox("Are you sure you want to remove the last log entry?  This cannot be undone.", Icon=QMessageBox.Question, Buttons=(QMessageBox.Yes | QMessageBox.No)) == QMessageBox.Yes:
            self.WildernessTravelManager.RemoveLastLogEntry()
            self.UpdateUnsavedChangesFlag(True)

    def ClearLog(self):
        if self.DisplayMessageBox("Are you sure you want to clear the log?  This cannot be undone.", Icon=QMessageBox.Question, Buttons=(QMessageBox.Yes | QMessageBox.No)) == QMessageBox.Yes:
            self.WildernessTravelManager.ClearLog()
            self.UpdateUnsavedChangesFlag(True)

    # Display Update Methods
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

        # Update Window Title
        self.UpdateWindowTitle()

    def UpdateWindowTitle(self):
        CurrentFileTitleSection = " [" + os.path.basename(self.CurrentOpenFileName) + "]" if self.CurrentOpenFileName != "" else ""
        UnsavedChangesIndicator = " *" if self.UnsavedChanges else ""
        self.setWindowTitle("Wilderness Travel Manager - " + self.ScriptName + CurrentFileTitleSection + UnsavedChangesIndicator)

    def UpdateUnsavedChangesFlag(self, UnsavedChanges):
        self.UnsavedChanges = UnsavedChanges
        self.UpdateDisplay()
