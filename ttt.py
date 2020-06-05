# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os.path

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(410, 40, 361, 481))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 420, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 450, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 420, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 450, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(250, 430, 91, 20))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 256, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.sale_detail)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "date"))
        self.label_2.setText(_translate("MainWindow", "path"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "cust"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "qty"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def sale_detail(self):
        # pdb.set_trace()
        sum_list= []
        # x = datetime.datetime.now()
        # a = x.strftime("%B")
        # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
        # userpath = input('give path : ')
        userpath = self.lineEdit_2.text()
        # if userpath =='' :
        #     userpath = f'SALE DETAIL SHEET {a.upper()} 2019'
        # else:  
        #     userpath = userpath
        abc = os.path.join(path, userpath+'.xlsx')
        customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
        customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
        customers2_length = range(0,len(customers2))
        # today = date.today()
        # d1 = today.strftime("%d-%m-%Y")
        # tarik = input('enter date : ')
        # if tarik == '':
        #     tarik = d1
        # else :
        #     tarik = tarik
        tarik = self.lineEdit.text()
        df = pd.read_excel(open(abc,"rb"), index_col=None, header=  None)
        for (i,j) in zip(customers1, customers2_length):
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b = round(a,2)
            i = customers2[j]
            if b != 0:
                sum_list.append([i, str(b)])

        combi = range(0, len(sum_list))
        
        # self.tableWidget.setRowCount(len(sum_list))
        for (i,j) in zip(combi,sum_list):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(j[0]))
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(j[1]))
            # item = self.tableWidget.item(i, 0)
            # item.setText(_translate("MainWindow", j[0]))
            # item = self.tableWidget.item(i, 1)
            # item.setText(_translate("MainWindow", j[1]))




        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
