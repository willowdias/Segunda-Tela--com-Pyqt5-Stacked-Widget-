import sys 
from PyQt5.QtWidgets import QDialog, QApplication
from app import*


if __name__ == '__main__':
    
    app = QApplication([sys.argv])
    window = app_sistema()
    window.show()
    sys.exit(app.exec_())

    