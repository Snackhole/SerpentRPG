import math
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QFrame, QTextEdit, QInputDialog, QSizePolicy, QAction, QMessageBox

from Core.DieClock import DieClock
from Core.WildernessTravelManager import WildernessTravelManager
from Interface.Widgets.LineEditMouseWheelExtension import LineEditMouseWheelExtension
from Interface.Windows.Window import Window
from SaveAndLoad.SaveAndOpenMixin import SaveAndOpenMixin


class WildernessTravelManagerWindow(Window, SaveAndOpenMixin):
    def __init__(self, ScriptName, AbsoluteDirectoryPath):
        # Store Absolute Directory Path for SaveAndOpenMixin
        self.AbsoluteDirectoryPath = AbsoluteDirectoryPath

        # Initialize
        super().__init__(ScriptName, AbsoluteDirectoryPath)

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
        self.SpendDaysButton = QPushButton("Spend Days")
        self.SpendDaysButton.clicked.connect(self.SpendDays)
        self.SpendDaysButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)

        # Wilderness Clock Label
        self.WildernessClockLabel = QLabel("Wilderness Clock")
        self.WildernessClockLabel.setStyleSheet(self.LabelStyle)
        self.WildernessClockLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Wilderness Clock Current Value Line Edit
        self.WildernessClockCurrentValueLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyWildernessClockCurrentValue(1 if event.angleDelta().y() > 0 else -1))
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
        self.WildernessClockMaximumValueLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyWildernessClockMaximumValue(1 if event.angleDelta().y() > 0 else -1))
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

        # Wilderness Clock Threshold Label
        self.WildernessClockThresholdLabel = QLabel("Threshold")
        self.WildernessClockThresholdLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Wilderness Clock Threshold Line Edit
        self.WildernessClockThresholdLineEdit = LineEditMouseWheelExtension(lambda event: self.ModifyWildernessClockThreshold(1 if event.angleDelta().y() > 0 else -1))
        self.WildernessClockThresholdLineEdit.setReadOnly(True)
        self.WildernessClockThresholdLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.WildernessClockThresholdLineEdit.setStyleSheet(self.LineEditStyle)
        self.WildernessClockThresholdLineEdit.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockThresholdLineEdit.setFixedWidth(self.PoolAndClockWidth)

        # Wilderness Clock Threshold Buttons
        self.WildernessClockThresholdIncreaseButton = QPushButton("+")
        self.WildernessClockThresholdIncreaseButton.clicked.connect(lambda: self.ModifyWildernessClockThreshold(1))
        self.WildernessClockThresholdIncreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockThresholdIncreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)
        self.WildernessClockThresholdDecreaseButton = QPushButton("-")
        self.WildernessClockThresholdDecreaseButton.clicked.connect(lambda: self.ModifyWildernessClockThreshold(-1))
        self.WildernessClockThresholdDecreaseButton.setSizePolicy(self.ButtonAndLineEditSizePolicy)
        self.WildernessClockThresholdDecreaseButton.setStyleSheet(self.PoolAndClockButtonStyle)

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
        self.TravelActionsLayout.addWidget(self.SpendDaysButton, 2, 0)
        for Row in range(1, 3):
            self.TravelActionsLayout.setRowStretch(Row, 1)
        self.TravelActionsFrame.setLayout(self.TravelActionsLayout)
        self.Layout.addWidget(self.TravelActionsFrame, 0, 0)

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
        self.WildernessClockThresholdFrame = QFrame()
        self.WildernessClockThresholdLayout = QGridLayout()
        self.WildernessClockThresholdLayout.addWidget(self.WildernessClockThresholdLabel, 0, 0, 1, 3)
        self.WildernessClockThresholdLayout.addWidget(self.WildernessClockThresholdDecreaseButton, 1, 0)
        self.WildernessClockThresholdLayout.addWidget(self.WildernessClockThresholdLineEdit, 1, 1)
        self.WildernessClockThresholdLayout.addWidget(self.WildernessClockThresholdIncreaseButton, 1, 2)
        self.WildernessClockThresholdFrame.setLayout(self.WildernessClockThresholdLayout)
        self.WildernessClockLayout.addWidget(self.WildernessClockThresholdFrame, 4, 0, 1, 3)
        self.WildernessClockLayout.setRowStretch(1, 1)
        self.WildernessClockLayout.setRowStretch(2, 2)
        self.WildernessClockLayout.setRowStretch(3, 1)
        self.WildernessClockFrame.setLayout(self.WildernessClockLayout)
        self.Layout.addWidget(self.WildernessClockFrame, 0, 1)

        # Add Wilderness Log Widgets to Layout
        self.WildernessLogFrame = QFrame()
        self.WildernessLogFrame.setFrameStyle(QFrame.Panel | QFrame.Plain)
        self.WildernessLogLayout = QGridLayout()
        self.WildernessLogLayout.addWidget(self.WildernessLogLabel, 0, 0)
        self.WildernessLogLayout.addWidget(self.WildernessLogTextEdit, 1, 0)
        self.WildernessLogFrame.setLayout(self.WildernessLogLayout)
        self.Layout.addWidget(self.WildernessLogFrame, 0, 2)

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
    def ModifyWildernessClockCurrentValue(self, Delta):
        self.WildernessTravelManager.ModifyWildernessClockCurrentValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def ModifyWildernessClockMaximumValue(self, Delta):
        self.WildernessTravelManager.ModifyWildernessClockMaximumValue(Delta)
        self.UpdateUnsavedChangesFlag(True)

    def ModifyWildernessClockThreshold(self, Delta):
        self.WildernessTravelManager.ModifyWildernessClockThreshold(Delta)
        self.UpdateUnsavedChangesFlag(True)

    # Travel Action Methods
    def Move(self):
        TravelTime, OK = QInputDialog.getInt(self, "Travel Time", "Travel time of movement:", 1, 1)
        if OK:
            self.WildernessTravelManager.Move(TravelTime)
            self.UpdateUnsavedChangesFlag(True)

    def SpendDays(self):
        DaysSpent, OK = QInputDialog.getInt(self, "Spend Days", "Days spent:", 1, 1)
        if OK:
            self.WildernessTravelManager.SpendDays(DaysSpent, Log=True)
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
        # Wilderness Clock Display
        self.WildernessClockCurrentValueLineEdit.setText(str(self.WildernessTravelManager.WildernessClock.Value))
        self.WildernessClockMaximumValueLineEdit.setText(str(self.WildernessTravelManager.WildernessClock.MaximumValue))
        self.WildernessClockThresholdLineEdit.setText(str(self.WildernessTravelManager.WildernessClock.ComplicationThreshold))

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
