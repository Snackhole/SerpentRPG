from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class ResultMessagesTreeWidget(QTreeWidget):
    def __init__(self, ResultMessages):
        super().__init__()

        # Store Parameters
        self.ResultMessages = ResultMessages

        # Header Setup
        self.setHeaderHidden(True)

    def FillFromResultMessages(self):
        pass


class ResultMessagesWidgetItem(QTreeWidgetItem):
    def __init__(self, Title):
        super().__init__()

        # Store Parameters
        self.Title = Title

        # Set Text
        self.setText(0, self.Title)
