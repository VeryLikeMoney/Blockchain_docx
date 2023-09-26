from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from GUI.ui.node_win import Ui_Node_Form
from GUI.ui.whoami_win import Ui_Form
from GUI.ui.sender_win import Ui_Sender_Form

from function_blockchain.server import start_server


class Node_Form(QWidget):

    def __init__(self) -> None:
        super(Node_Form, self).__init__()

        self.ui = Ui_Node_Form()
        self.ui.setupUi(self)

class Whoami_Form(QWidget):

    def __init__(self) -> None:
        super(Whoami_Form, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

class Sender_Form(QWidget):

    def __init__(self) -> None:
        super(Sender_Form, self).__init__()

        self.ui = Ui_Sender_Form()
        self.ui.setupUi(self)

            
            

