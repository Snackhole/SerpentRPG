from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class PresetRollsTreeWidget(QTreeWidget):
    def __init__(self, DiceRoller):
        super().__init__()

        # Store Parameters
        self.DiceRoller = DiceRoller

        # Header Setup
        self.setHeaderHidden(True)

    def FillFromPresetRolls(self):
        for PresetRollIndex in range(len(self.DiceRoller.PresetRolls)):
            pass


class PresetRollsWidgetItem(QTreeWidgetItem):
    def __init__(self, Title, Index):
        super().__init__()

        # Store Parameters
        self.Title = Title
        self.Index = Index

        # Set Text
        self.setText(0, self.Title)
