# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tree_button.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os.path
import pdb
import datetime
from datetime import date



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(455, 50, 281, 431))
        self.treeWidget.setObjectName("treeWidget")
        sum_list =[]
        # path = r'C:\Users\20035128\OneDrive - Larsen & Toubro\SALE DETAIL SHEET OCTOBER 2019.xlsx'
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\SALE DETAIL SHEET OCTOBER 2019.xlsx'
        customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
        customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
        customers2_length = range(0,len(customers2))
        tarik = '10-10-2019'
        df = pd.read_excel(open(path,"rb"), index_col=None, header=  None)
        for (i,j) in zip(customers1, customers2_length):
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b = round(a,2)
            i = customers2[j]
            if b != 0:
                sum_list.append([i, str(b)])
        for i in range(len(sum_list)):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.headerItem().setText(0, "1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 510, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.sale_detail)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ash Solutions"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Customer"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Sale Qty (MT)"))

    def sale_detail(self):
        pdb.set_trace()
        sum_list= []
        x = datetime.datetime.now()
        a = x.strftime("%B")
        # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
        userpath = input('give path : ')
        if userpath =='' :
            userpath = f'SALE DETAIL SHEET {a.upper()} 2019'
        else:  
            userpath = userpath
        abc = os.path.join(path, userpath+'.xlsx')
        customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
        customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
        customers2_length = range(0,len(customers2))
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        tarik = input('enter date : ')
        if tarik == '':
            tarik = d1
        else :
            tarik = tarik
        
        df = pd.read_excel(open(abc,"rb"), index_col=None, header=  None)
        for (i,j) in zip(customers1, customers2_length):
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b = round(a,2)
            i = customers2[j]
            if b != 0:
                sum_list.append([i, str(b)])

        combi = range(0, len(sum_list))
        # pdb.set_trace()
        for i,j in zip(combi,sum_list):
            if j[1] != '0':
                self.treeWidget.topLevelItem(i).setText(0, _translate("MainWindow",j[0])) 
        combi2 = range(0, len(sum_list))    
        for i,j in zip(combi,sum_list):
            if j[1] != '0':
                self.treeWidget.topLevelItem(i).setText(1, _translate("MainWindow",j[1])) 

        # __sortingEnabled = self.treeWidget.isSortingEnabled()
        # self.treeWidget.setSortingEnabled(False)               
        # self.treeWidget.setSortingEnabled(__sortingEnabled)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
