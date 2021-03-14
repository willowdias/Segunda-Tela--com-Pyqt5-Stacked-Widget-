import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from main import*
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
import time
from urllib.request import urlretrieve
from abrir import *
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

class sistema(QMainWindow,QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("icone_pagina-.png"))#colocar icone
         # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page1))
        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page2))
        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pagina3))
        #icone
        #Imagens:::
        self.ui.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.ui.btnRedimensionar.clicked.connect(self.redimensionar)
        self.ui.btnSalvar.clicked.connect(self.salvar)
        self.ui.ver_link_2.clicked.connect(self.abrir_imagem_pagina3)#abrir imagen
        
        #
        self.ui.baixa_link.clicked.connect(self.baixar)#baixa
        self.ui.baixa_link.clicked.connect(self.opcao)#opcao
        self.ui.ver_link_2.clicked.connect(self.box)# ver imagen
        
        
    
    def box (self):#seta combox
        item= self.ui.comboBox.currentText()
        self.ui.label_page2.setText(item)
        
    def baixar(self):# baixa foto
        baixa= self.ui.caixa_link_2.text()
        try:
            baixa==urlretrieve(baixa,"foto.png")
            time.sleep(1)
            self.ui.tela_2.setText("baixando")
            time.sleep(2)
            self.ui.caixa_link_2.setText("")
            self.ui.tela_2.setText("")#limpar
        except:
            self.ui.tela_2.setText("   Erro  ")
            QMessageBox.about(self, "Title", "Tente Novamente")
            time.sleep(1)
            self.ui.tela_2.setText("")
  
    def opcao(self):#selecionar opcao
        if self.ui.radioButton_image.isChecked():#baixa image
            time.sleep(2)
            QMessageBox.about(self, "Title", "Imagen")
            self.sistema=Imagen()
            self.sistema.show()
        if self.ui.radioButton_musica.isChecked():#baixa musica 
            QMessageBox.about(self, "Title", "Musica")
        if self.ui.radioButton_video_2.isChecked():
            QMessageBox.about(self, "Title", "Video")
        else:#falho
            self.ui.tela_2.setText("Nada Selecionada")
            time.sleep(2)
            self.ui.tela_2.setText("")    
    ###############################################
    def abrir_imagem(self):#imagens
        imagem, _ = QFileDialog.getOpenFileName(
            self.ui.centralwidget,
            'Abrir imagem',
            r'/home/luizotavio/Imagens/',
            options=QFileDialog.DontUseNativeDialog
        )
        self.ui.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.ui.labelImg.setPixmap(self.original_img)
        self.ui.inputLargura.setText(str(self.original_img.width()))
        self.ui.inputAltura.setText(str(self.original_img.height()))
        
    def redimensionar(self):#imagens
        largura = int(self.ui.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.ui.labelImg.setPixmap(self.nova_imagem)
        self.ui.inputLargura.setText(str(self.nova_imagem.width()))
        self.ui.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):#imagens
        imagem, _ = QFileDialog.getSaveFileName(
            self.ui.centralwidget,
            'Salvar imagem',
            r'/home/luizotavio/Desktop/',
            options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')
    ############################################## 
    def abrir_imagem_pagina3(self):#imagens pagina 3
        imagem, _ = QFileDialog.getOpenFileName(
            self.ui.centralwidget,
            'Ver Imagen',
            r'/home/luizotavio/Imagens/',
            options=QFileDialog.DontUseNativeDialog
        )
        self.ui.inputAbrirArquivo_2.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.ui.Open_pagina2.setPixmap(self.original_img)
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = sistema()
    window.show()
    app.exec_()