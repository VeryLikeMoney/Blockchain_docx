import typing
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class MyWorker(QThread):
    

    def __init__(self, func, *args) -> None:
        self.func = func
        self.args = args
        super().__init__()

    def run(self):
        # Это место, где выполняется фоновая задача
        # Например, длительные вычисления
        while True:
            self.func(*self.args)
            