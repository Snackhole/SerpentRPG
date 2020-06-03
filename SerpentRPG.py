import sys
import os

sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from Interface.Windows.DiceRollerWindow import DiceRollerWindow
from Interface.Windows.DieClockWindow import DieClockWindow
from Interface.Windows.ModeSelectionWindow import ModeSelectionWindow
from Interface.Windows.WildernessTravelManagerWindow import WildernessTravelManagerWindow
from Build import VersionedAppName

if __name__ == "__main__":
    AppInst = QApplication(sys.argv)

    # Script Name
    ScriptName = VersionedAppName

    # Mode Selection Window
    ModeSelectionWindowInst = ModeSelectionWindow(ScriptName)

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
        ModeWindowInst = Modes[Mode](ScriptName)

        # Enter Mode Loop
        sys.exit(AppInst.exec_())
