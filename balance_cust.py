# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_MainWindow(object):

#     def abc(self):
#         a = self.lineEdit.text()
#         b = self.lineEdit_2.text()
#         self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", a))
#         self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", b))
        



#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
#         self.groupBox.setGeometry(QtCore.QRect(410, 40, 361, 481))
#         self.groupBox.setObjectName("groupBox")
#         self.treeWidget = QtWidgets.QTreeWidget(self.groupBox)
#         self.treeWidget.setGeometry(QtCore.QRect(30, 30, 256, 371))
#         self.treeWidget.setObjectName("treeWidget")
#         item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
#         self.label = QtWidgets.QLabel(self.groupBox)
#         self.label.setGeometry(QtCore.QRect(40, 420, 47, 13))
#         self.label.setObjectName("label")
#         self.label_2 = QtWidgets.QLabel(self.groupBox)
#         self.label_2.setGeometry(QtCore.QRect(50, 450, 47, 13))
#         self.label_2.setObjectName("label_2")
#         self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
#         self.lineEdit.setGeometry(QtCore.QRect(120, 420, 113, 20))
#         self.lineEdit.setObjectName("lineEdit")
#         self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
#         self.lineEdit_2.setGeometry(QtCore.QRect(120, 450, 113, 20))
#         self.lineEdit_2.setObjectName("lineEdit_2")
#         self.pushButton = QtWidgets.QPushButton(self.groupBox)
#         self.pushButton.setGeometry(QtCore.QRect(250, 430, 91, 20))
#         self.pushButton.setObjectName("pushButton")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#         self.pushButton.clicked.connect(self.abc)
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
#         self.treeWidget.headerItem().setText(0, _translate("MainWindow", "cust"))
#         self.treeWidget.headerItem().setText(1, _translate("MainWindow", "qty"))
#         __sortingEnabled = self.treeWidget.isSortingEnabled()
#         self.treeWidget.setSortingEnabled(False)
#         self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "abc"))
#         self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "10"))
#         self.treeWidget.setSortingEnabled(__sortingEnabled)
#         self.label.setText(_translate("MainWindow", "date"))
#         self.label_2.setText(_translate("MainWindow", "path"))
#         self.pushButton.setText(_translate("MainWindow", "PushButton"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os.path
import xlwings
import datetime
from datetime import date
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
        self.tableWidget.setRowCount(25)
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
        self.pushButton.clicked.connect(self.balance)

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

    # def sale_detail(self):
    #     # pdb.set_trace()
    #     sum_list= []
    #     # x = datetime.datetime.now()
    #     # a = x.strftime("%B")
    #     # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
    #     path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
    #     # userpath = input('give path : ')
    #     userpath = self.lineEdit_2.text()
    #     # if userpath =='' :
    #     #     userpath = f'SALE DETAIL SHEET {a.upper()} 2019'
    #     # else:  
    #     #     userpath = userpath
    #     abc = os.path.join(path, userpath+'.xlsx')
    #     customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
    #     customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
    #     customers2_length = range(0,len(customers2))
    #     # today = date.today()
    #     # d1 = today.strftime("%d-%m-%Y")
    #     # tarik = input('enter date : ')
    #     # if tarik == '':
    #     #     tarik = d1
    #     # else :
    #     #     tarik = tarik
    #     tarik = self.lineEdit.text()
    #     df = pd.read_excel(open(abc,"rb"), index_col=None, header=  None)
    #     for (i,j) in zip(customers1, customers2_length):
    #         ab = df[df[2] == i]
    #         a= (ab[ab[6]== tarik][8]).sum()
    #         b = round(a,2)
    #         i = customers2[j]
    #         if b != 0:
    #             sum_list.append([i, str(b)])

    #     combi = range(0, len(sum_list))
    #     for (i,j) in zip(combi,sum_list):
    #         self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(j[0]))
    #         self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(j[1]))

            # item = self.tableWidget.item(i, 0)
            # item.setText(_translate("MainWindow", j[0]))
            # item = self.tableWidget.item(i, 1)
            # item.setText(_translate("MainWindow", j[1]))
    def balance(self):
# wb = xlwings.Book(r'\\10.9.32.2\adm\Ash\FY 2019-20\DAILY REPORT\DAILY REPORT FORMAT.xlsx')
        wb = xlwings.Book(r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\DAILY REPORT FORMAT.xlsx')
        xlwings.App().visible=False
        ws = wb.sheets['advance tracking sheet']
        dict1= {
        'C191' : 'J191',
        'C192' : 'J192',
        'C193' : 'J193',
        'C195' : 'J195',
        'C196' : 'J196',
        'C199' : 'J199',
        'C204' : 'J204',
        'C208' : 'J208',
        'C209' : 'J209',
        'C210' : 'J210',
        'C212' : 'J212',
        'C213' : 'J213',
        'C215' : 'J215',
        'C216' : 'J216',
        'C217' : 'J217',
        'C218' : 'J218',
        'C219' : 'J219',
        'C220' : 'J220',
        'C221' : 'J221',
        'C222' : 'J222',
        'C223' : 'J223',
        'C224' : 'J224',
        'C225' : 'J225',
        }
        list_amount = []
        for i,j in dict1.items():
            b = ws.range(j). value
            c = b
            list_amount.append(c)
# print(list_amount)   
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        x = datetime.datetime.now()
        a = x.strftime("%B")
    # print(d1)
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
    # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        userpath = f'SALE DETAIL SHEET OCTOBER 2019'
        abc = os.path.join(path, userpath+'.xlsx')
        df = pd.read_excel(open(abc,"rb"), index_col=None, header=  None)
        tarik = d1
    # customer_list = []
    # for i in dict1.items():
    #     z = ws.range(i).value
    #     customer_list.append(a)
    # print(customer_list)
        customers2 = [100051,100070,100071,100062,100072,100087,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
        store = []
        for i in customers2:
            ab = df[df[2] == i]
            amount = (ab[ab[6]== tarik][19]).sum()
            store.append(amount)

        final_list = []   
        for (i, j) in zip(list_amount,store):
            final = round(i - j)
            final_list.append(final)

        final_bal = []   
        for (i, j) in zip(list_amount,store):
            final = round(i - j)
            final_bal.append(final)

        cust_name =[]
        for (i,j) in dict1.items():
            b = ws.range(i). value
            cust_name.append(b)

        bal= list(zip(cust_name, final_bal))
        combi = range(0, len(bal))
        for (i,j) in zip(combi,bal):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(j[0]))
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(j[1])))

        wb.close()
                          ##########################################################################




        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
