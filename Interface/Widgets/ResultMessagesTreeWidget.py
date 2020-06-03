from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QHeaderView


class ResultMessagesTreeWidget(QTreeWidget):
    def __init__(self, ResultMessages):
        super().__init__()

        # Store Parameters
        self.ResultMessages = ResultMessages

        # Header Setup
        self.setHeaderHidden(True)
        self.setRootIsDecorated(False)
        self.header().setSectionResizeMode(QHeaderView.ResizeToContents)

    def FillFromResultMessages(self):
        self.clear()
        for Key, Value in sorted(self.ResultMessages.items(), key=lambda x: int(x[0])):
            self.invisibleRootItem().addChild(ResultMessagesWidgetItem(Key, Value))

    def SelectIndex(self, Index):
        DestinationIndex = self.model().index(Index, 0)
        self.setCurrentIndex(DestinationIndex)
        self.scrollToItem(self.currentItem(), self.PositionAtCenter)


class ResultMessagesWidgetItem(QTreeWidgetItem):
    def __init__(self, Result, Message):
        super().__init__()

        # Store Parameters
        self.Result = Result
        self.Message = Message

        # Set Text
        self.setText(0, self.Result + ":  " + self.Message)
