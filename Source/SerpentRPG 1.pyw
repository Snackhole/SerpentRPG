import os
import sys

from PyQt5.QtWidgets import QApplication

from Interface.ModeSelectionWindow import ModeSelectionWindow
from Interface.WildernessTravelManagerWindow import WildernessTravelManagerWindow

if __name__ == "__main__":
    AppInst = QApplication(sys.argv)

    # Script Name
    ScriptName = os.path.splitext(os.path.basename(__file__))[0]

    # Mode Selection Window
    ModeSelectionWindowInst = ModeSelectionWindow(ScriptName)

    # Enter Mode Selection Loop
    AppInst.exec_()

    # Initialize Mode
    Mode = ModeSelectionWindowInst.Mode
    if Mode is not None:
        # Modes Dictionary
        Modes = {}
        Modes["Wilderness Travel Manager"] = WildernessTravelManagerWindow

        # Create Mode Window
        ModeWindowInst = Modes[Mode](ScriptName)

        # Enter Mode Loop
        sys.exit(AppInst.exec_())
