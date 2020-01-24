from Core.DieClock import DieClock
from Interface.Windows.Window import Window
from SaveAndLoad.SaveAndOpenMixin import SaveAndOpenMixin


class DieClockWindow(Window, SaveAndOpenMixin):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Die Clock
        self.DieClock = DieClock()

        # Set Up Dave and open
        self.SetUpSaveAndOpen(".dieclock", "Die Clock", (DieClock,))

        # Update Display
        self.UpdateDisplay()

    def CreateInterface(self):
        pass

    def UpdateDisplay(self):
        pass
