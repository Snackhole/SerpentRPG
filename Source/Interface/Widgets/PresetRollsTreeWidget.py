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
        for PresetRoll in self.DiceRoller.PresetRolls:
            self.invisibleRootItem().addChild(PresetRollsWidgetItem(PresetRoll))


class PresetRollsWidgetItem(QTreeWidgetItem):
    def __init__(self, PresetRoll):
        super().__init__()

        # Store Parameters
        self.PresetRoll = PresetRoll

        # Set Text
        self.setText(0, self.PresetRoll["Name"])
