import os
import sys

AbsoluteDirectoryPath = os.path.dirname(os.path.abspath(__file__))
if AbsoluteDirectoryPath.endswith(".pyz") or AbsoluteDirectoryPath.endswith(".pyzw"):
    AbsoluteDirectoryPath = os.path.dirname(AbsoluteDirectoryPath)
if sys.path[0] != AbsoluteDirectoryPath:
    sys.path.insert(0, AbsoluteDirectoryPath)

from PyQt5.QtWidgets import QApplication

from Interface.Windows.DiceRollerWindow import DiceRollerWindow
from Interface.Windows.DieClockWindow import DieClockWindow
from Interface.Windows.ModeSelectionWindow import ModeSelectionWindow
from Interface.Windows.WildernessTravelManagerWindow import WildernessTravelManagerWindow
from Build import BuildVariables


def StartApp():
    AppInst = QApplication(sys.argv)

    # Script Name
    ScriptName = BuildVariables["VersionedAppName"]

    # Mode Selection Window
    ModeSelectionWindowInst = ModeSelectionWindow(ScriptName, AbsoluteDirectoryPath)

    # Enter Mode Selection Loop
    AppInst.exec_()

    # Initialize Mode
    Mode = ModeSelectionWindowInst.Mode
    if Mode is not None:
        # Modes Dictionary
        Modes = {}
        Modes["Dice Roller"] = DiceRollerWindow
        Modes["Die Clock"] = DieClockWindow
        Modes["Wilderness Travel Manager"] = WildernessTravelManagerWindow

        # Create Mode Window
        ModeWindowInst = Modes[Mode](ScriptName, AbsoluteDirectoryPath)

        # Enter Mode Loop
        sys.exit(AppInst.exec_())


if __name__ == "__main__":
    StartApp()
