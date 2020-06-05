# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import xlwings
import os.path
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 781, 121))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../icons&pics/sompic.png"))
        self.photo.setScaledContents(True)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(20, 160, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.date_label.setFont(font)
        self.date_label.setAutoFillBackground(True)
        self.date_label.setWordWrap(False)
        self.date_label.setObjectName("date_label")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(20, 190, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 160, 141, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 190, 141, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 240, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.photo.raise_()
        self.label2.raise_()
        self.date_label.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.submitbtn)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.date_label.setText(_translate("MainWindow", "Enter the date (DD-MM-YYYY) "))
        self.label2.setText(_translate("MainWindow", "Enter the file path"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))

    def submitbtn(self):
        userdate_date= self.lineEdit.text()
        userpath = self.lineEdit_2.text()
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
        userpath1 = f'SALE DETAIL SHEET {userpath.upper()} 2019'
        abc = os.path.join(path, userpath1+'.xlsx')
        customers1 = [20,31,28,27,17,13,15,14,37,100125]
        customers2 = [100051,100062,100087,100071,100070]
        customers3 = [100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
        df = pd.read_excel(open(abc, "rb"), sheet_name="OCTOBER",index_col=None, header=  None)
        tarik = userdate_date
#  program for sumifs and countifs for customers1 and appending data to Dpr
        sum_list1 = []
        count_list1 =[]
        for i in customers1:
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b= (ab[ab[6]== tarik][8]).count()
            sum_list1.append(round(a,2))
            count_list1.append(b)
        wb = xlwings.Book(r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\DAILY REPORT FORMAT.xlsx')
        xlwings.App().visible=False
        ws = wb.sheets['DPR']
        ws.range('E7').options(transpose=True).value = count_list1
        ws.range('F7').options(transpose=True).value = sum_list1
        print(sum_list1)
        print(count_list1)
#  program for sumifs and countifs for customers2 and appending data to Dpr
        sum_list2 = []
        count_list2 =[]
        for i in customers2:
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b= (ab[ab[6]== tarik][8]).count()
            sum_list2.append(round(a,2))
            count_list2.append(b)
# wb = xlwings.Book('dpr.xlsx')
# xlwings.App().visible=False
# ws = wb.sheets['DPR']
        ws.range('E18').options(transpose=True).value = count_list2
        ws.range('F18').options(transpose=True).value = sum_list2
        print(sum_list2)
        print(count_list2)
#  program for sumifs and countifs for customers3 and appending data to Dpr
        sum_list3 = []
        count_list3 =[]
        for i in customers3:
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b= (ab[ab[6]== tarik][8]).count()
            sum_list3.append(round(a,2))
            count_list3.append(b)
# wb = xlwings.Book('dpr.xlsx')
# xlwings.App().visible=False
# ws     = wb.sheets['DPR']
        ws.range('F24').options(transpose=True).value = sum_list3
        ws.range('E24').options(transpose=True).value = count_list3
        print(sum_list3)
        print(count_list3)

        dict1= {
            'F7' : 'E45',
            'F8' : 'E46',
            'F9' : 'E47',
            'F10' : 'E48',
            'F11' : 'E49',
            'F12': 'E50',
            'F13' : 'E51',
            'F14' : 'E52',
            'F15' : 'E53',
            'F16' : 'E54',
    
         }

        for i,j in dict1.items():
            num1 = 0
            num1_new = ws.range(i).value 
            num2 = ws.range(j).value 
            ws.range(j).value = (num2+(num1_new - num1))
    # num1 = num1_new

        dict2= {
            'F18' : 'E56',
            'F19' : 'E57',
            'F20' : 'E59',
            'F21' : 'E60',
            'F22' : 'E61', 
        }

        for i,j in dict2.items():
            num1 = 0
            num1_new = ws.range(i).value 
            num2 = ws.range(j).value 
            ws.range(j).value = (num2+(num1_new - num1))
    # num1 = num1_new

        dict3= {
            'F24' : 'E63',
            'F25' : 'E64',
            'F26' : 'E65',
            'F27' : 'E66',
            'F28' : 'E67',
            'F29':  'E68',
            'F30' : 'E70',
            'F31' : 'E71',
            'F32' : 'E72',
            'F33' : 'E73',
            'F34' : 'E74',
            'F35' : 'E75',
            'F36' : 'E76',
            'F37' : 'E77',
    
        }

        for i,j in dict3.items():
            num1 = 0
            num1_new = ws.range(i).value 
            num2 = ws.range(j).value 
            ws.range(j).value = (num2+(num1_new - num1))
    # num1 = num1_new
        msg = QMessageBox()
        msg.setWindowTitle("Submitted")
        msg.setText('DPR Generated successfully')
        msg.setIcon(QMessageBox.Information)
        x= msg.exec_()   

        wb.save()
        wb.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
