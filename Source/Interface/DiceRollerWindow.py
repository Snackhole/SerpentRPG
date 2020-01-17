import os

from Core.DiceRoller import DiceRollerWithPresetRolls
from Interface.Window import Window
from SaveAndLoad.SaveAndOpenMixin import SaveAndOpenMixin


class DiceRollerWindow(Window, SaveAndOpenMixin):
    def __init__(self, ScriptName):
        super().__init__(ScriptName)

        # Create Dice Roller
        self.DiceRoller = DiceRollerWithPresetRolls()

        # Set up Save and Open
        self.SetUpSaveAndOpen(".presetrolls", "Dice Roller", (DiceRollerWithPresetRolls,))

        # Update Display
        self.UpdateDisplay()

    def CreateInterface(self):
        pass

    # Display Update Methods
    def UpdateDisplay(self):
        self.UpdateWindowTitle()

    def UpdateWindowTitle(self):
        CurrentFileTitleSection = " [" + os.path.basename(self.CurrentOpenFileName) + "]" if self.CurrentOpenFileName != "" else ""
        UnsavedChangesIndicator = " *" if self.UnsavedChanges else ""
        self.setWindowTitle("Dice Roller - " + self.ScriptName + CurrentFileTitleSection + UnsavedChangesIndicator)

    def UpdateUnsavedChangesFlag(self, UnsavedChanges):
        self.UnsavedChanges = UnsavedChanges
        self.UpdateDisplay()
