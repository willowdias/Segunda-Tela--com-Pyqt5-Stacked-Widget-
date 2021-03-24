from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel

from PyQt5.QtGui import QPixmap


class Imagen(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Imagen'
        self.left = 50
        self.top = 50
        self.width = 400
        self.height = 400
        self.initUI()
    
    def initUI(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))#colocar icone
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('foto.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()
#import sys    
#if __name__ == '__main__':
 #   app = QApplication(sys.argv)
 #   ex = Imagen()
  #  sys.exit(app.exec_())