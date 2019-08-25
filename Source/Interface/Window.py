from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    def __init__(self, ScriptName):
        super().__init__()

        # Store Parameters
        self.ScriptName = ScriptName

        # Window Icon and Title
        self.WindowIcon = QIcon("Assets/SerpentRPG Icon.png")
        self.setWindowIcon(self.WindowIcon)
        self.UpdateWindowTitle()

        # Create Interface
        self.CreateInterface()
        self.Center()
        self.show()

    def CreateInterface(self):
        pass

    def UpdateWindowTitle(self):
        self.setWindowTitle(self.ScriptName)

    # Window Management Methods
    def Center(self):
        FrameGeometryRectangle = self.frameGeometry()
        DesktopCenterPoint = QApplication.primaryScreen().availableGeometry().center()
        FrameGeometryRectangle.moveCenter(DesktopCenterPoint)
        self.move(FrameGeometryRectangle.topLeft())
