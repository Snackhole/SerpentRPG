from PyQt5.QtWidgets import QLineEdit


class LineEditMouseWheelExtension(QLineEdit):
    def __init__(self, MouseWheelEventCallback):
        # Initialize QLineEdit
        super().__init__()

        # Store Parameters
        self.MouseWheelEventCallback = MouseWheelEventCallback

    def wheelEvent(self, event):
        self.MouseWheelEventCallback(event)
        event.accept()
