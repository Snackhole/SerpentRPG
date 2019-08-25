import os
import sys

from PyQt5.QtWidgets import QApplication

from Interface.ModeSelectionWindow import ModeSelectionWindow

if __name__ == "__main__":
    AppInst = QApplication(sys.argv)

    # Main Window Interface
    ScriptName = os.path.splitext(os.path.basename(__file__))[0]
    MainWindowInst = ModeSelectionWindow(ScriptName)

    # Enter Main Loop
    sys.exit(AppInst.exec_())
