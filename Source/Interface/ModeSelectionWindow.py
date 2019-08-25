from Interface.Window import Window


class ModeSelectionWindow(Window):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

    def CreateInterface(self):
        pass

    def UpdateWindowTitle(self):
        self.setWindowTitle(self.ScriptName + " Mode Selection")
