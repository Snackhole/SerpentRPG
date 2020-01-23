from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QHeaderView


class PresetRollsTreeWidget(QTreeWidget):
    def __init__(self, DiceRoller):
        super().__init__()

        # Store Parameters
        self.DiceRoller = DiceRoller

        # Header Setup
        self.setHeaderHidden(True)
        self.setRootIsDecorated(False)
        self.header().setSectionResizeMode(QHeaderView.ResizeToContents)

    def FillFromPresetRolls(self):
        self.clear()
        for PresetRollIndex in range(len(self.DiceRoller.PresetRolls)):
            self.invisibleRootItem().addChild(PresetRollsWidgetItem(PresetRollIndex, self.DiceRoller.PresetRolls[PresetRollIndex]))


class PresetRollsWidgetItem(QTreeWidgetItem):
    def __init__(self, Index, PresetRoll):
        super().__init__()

        # Store Parameters
        self.Index = Index
        self.PresetRoll = PresetRoll

        # Set Text
        self.setText(0, self.PresetRoll["Name"])
