from Components.WildernessTravelManager import WildernessTravelManager
from Interface.Window import Window


class WildernessTravelManagerWindow(Window):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Wilderness Travel Manager
        self.WildernessTravelManager = WildernessTravelManager()
