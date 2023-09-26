from PyQt5.QtWidgets import QApplication
from GUI.gui_main import MyWindow


if __name__ == "__main__":
    import sys
    
    apps = QApplication(sys.argv)

    window = MyWindow()
    window.show()
    #window.stop_server()
    sys.exit(apps.exec())