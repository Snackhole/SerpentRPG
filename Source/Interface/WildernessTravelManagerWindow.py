from PyQt5 import QtCore
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QLineEdit, QGridLayout, QLabel, QSpinBox

from Core.WildernessTravelManager import WildernessTravelManager
from Interface.Window import Window


class WildernessTravelManagerWindow(Window):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Wilderness Travel Manager
        self.WildernessTravelManager = WildernessTravelManager()

    def CreateInterface(self):
        # Current Supply Points Label
        self.CurrentSupplyPointsLabel = QLabel("Supply Points")
        self.CurrentSupplyPointsLabel.setMaximumWidth(70)

        # Current Supply Points Line Edit
        self.CurrentSupplyPointsLineEdit = QSpinBox()
        self.CurrentSupplyPointsLineEdit.setMaximumWidth(40)

        # Supply Pool Label
        self.SupplyPoolLabel = QLabel("Supply Pool")
        self.SupplyPoolLabel.setMaximumWidth(70)

        # Supply Pool Line Edit
        self.SupplyPoolLineEdit = QSpinBox()
        self.SupplyPoolLineEdit.setMaximumWidth(40)

        # Create Layout
        self.Layout = QGridLayout()
        self.Layout.addWidget(self.CurrentSupplyPointsLabel, 0, 0)
        self.Layout.addWidget(self.CurrentSupplyPointsLineEdit, 0, 1)
        self.Layout.addWidget(self.SupplyPoolLabel, 1, 0)
        self.Layout.addWidget(self.SupplyPoolLineEdit, 1, 1)
        self.Frame.setLayout(self.Layout)
