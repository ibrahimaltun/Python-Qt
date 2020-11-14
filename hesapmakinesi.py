import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,700,700)
        
        self.initUI()

    def initUI(self):
        #        Sayi 1
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı 1 : ')
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)
        
        #        Sayi 2
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayı 2 : ')
        self.lbl_sayi2.move(50,80)
        
        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)
        
        #         İşlem Butonları
        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapla)
        
        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Çıkar')
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.hesapla)
        
        self.btn_carpma = QtWidgets.QPushButton(self)
        self.btn_carpma.setText('Çarp')
        self.btn_carpma.move(150,210)
        self.btn_carpma.clicked.connect(self.hesapla)

        self.btn_bolme = QtWidgets.QPushButton(self)
        self.btn_bolme.setText('Böl')
        self.btn_bolme.move(150,250)
        self.btn_bolme.clicked.connect(self.hesapla)
        
        #             Sonucun Yazılacağı Yer
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText('Sonuç : ')
        self.lbl_sonuc.move(150,290)
    
    def hesapla(self):

        sender = self.sender().text()
        #print(sender.text())
        result = 0
        
        if sender == 'Topla':
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == 'Çıkar':
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == 'Çarp':
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender == 'Böl':
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())

        self.lbl_sonuc.setText('Sonuç : ' + str(result))

    #     Tıklama Sonucunda Yapılacak İşlemler
    #def toplama(self):
     #   result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
      #  self.lbl_sonuc.setText('Sonuç : ' + str(result))

    #def cikarma(self):
     #   result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
      #  self.lbl_sonuc.setText('Sonuç : ' + str(result))

    #def carpma(self):
     #   result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
      #  self.lbl_sonuc.setText('Sonuç : ' + str(result))
    
    #def bolme(self):
     #   result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
      #  self.lbl_sonuc.setText('Sonuç : ' + str(result))

# Uygulama Tanımlama Kısmı
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()