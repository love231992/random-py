# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtWidgets
import pandas as pd
import os.path
import pdb
import datetime
from datetime import date

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        sum_list =[]
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro\SALE DETAIL SHEET OCTOBER 2019.xlsx'
        # abc = os.path.join(path, userpath+'.xlsx')
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
        data1= [['asian', '183.51'], ['asian fine', '671.36'], ['utcl roorkee', '495.81'], ['utcl bagheri', '296.82'], ['utcl panipat', 0], ['amnuja nalagargh', 0]]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(100, 10, 200, 400))
        self.treeWidget.setObjectName("treeWidget")
        for i in range(len(sum_list)):
            # if j[1] != '0':
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        # item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Customer"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Sale Qty (MT)"))
        # self.treeWidget.headerItem().setText(2, _translate("MainWindow", "b"))
        # self.treeWidget.headerItem().setText(3, _translate("MainWindow", "c"))
        # self.treeWidget.headerItem().setText(4, _translate("MainWindow", "d"))

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        sum_list= []
        x = datetime.datetime.now()
        a = x.strftime("%B")
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
        userpath = input('give path : ')
        if userpath =='' :
            userpath = f'SALE DETAIL SHEET {a.upper()} 2019'
        else:  
            userpath = userpath
        # userpath = f'SALE DETAIL SHEET {a} 2019' # 'SALE DEATIL SHEET+' '+a+2019'
        # path = r'C:\Users\20035128\OneDrive - Larsen & Toubro\SALE DETAIL SHEET OCTOBER 2019.xlsx'
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
        print(sum_list)    
        # combi = range(0,len(customers1))
        # combi = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]
        
        # combi = [[0,],[1,1],[2,1]]
        data1= [['asian', '183.51'], ['asian fine', '671.36'], ['utcl roorkee', '495.81'], ['utcl bagheri', '296.82'], ['utcl panipat', '0'], ['amnuja nalagargh', '0']]
        combi = range(0, len(sum_list))
        # pdb.set_trace()
        for i,j in zip(combi,sum_list):
            if j[1] != '0':
                self.treeWidget.topLevelItem(i).setText(0, _translate("MainWindow",j[0])) 
            # a= self.treeWidget.topLevelItem(i[0])
            # a.setText(i[1], _translate("MainWindow", j[0]))
        # combi2 = [[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],[7,1]]
        combi2 = range(0, len(data1))    
        for i,j in zip(combi,sum_list):
            if j[1] != '0':
                self.treeWidget.topLevelItem(i).setText(1, _translate("MainWindow",j[1]))
            # a= self.treeWidget.topLevelItem(i[0])
            # a.setText(i[1], _translate("MainWindow", j[1]))
            # self.treeWidget.topLevelItem(i[0]).setText((i[1]+1), _translate("MainWindow", j[1]))
        # for i,j in zip(combi,data1):    
            # self.treeWidget.topLevelItem(i).setText(1, _translate("MainWindow", j[1]))
            # self.treeWidget.topLevelItem(i).setText(0, _translate("MainWindow", j[0]))
        # self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow", "2"))
        # self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "z"))
        # self.treeWidget.topLevelItem(2).setText(1, _translate("MainWindow", "3"))
        # self.treeWidget.topLevelItem(1).setText(4, _translate("MainWindow", "Hey"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)





#     sum_list= []
#     customers1 = [20,31,28,27,17,13,15,14,37,100125,100051,100062,100087,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
#     customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund sahib','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC']
#     customers2_length = range(0,len(customers2))
#     tarik = input('enter data')
#     df = pd.read_excel(open(r'Z:\Ash\FY 2019-20\Sale detail sheet\SALE DETAIL SHEET NOVEMBER 2019.xlsx',"rb"), index_col=None, header=  None)
#     for (i,j) in zip(customers1, customers2_length):
#         ab = df[df[2] == i]
#         a= (ab[ab[6]== tarik][8]).sum()
#         b = round(a,2)
#         i = customers2[j]
#         sum_list.append([i, str(b)])
#     # app = QtWidgets.QApplication(sys.argv)
#     # win = QtWidgets.QWidget()    
#     layout =QtWidgets.QVBoxLayout(MainWindow)
# # data1= [['asian', '183.51'], ['asian fine', '671.36'], ['utcl roorkee', '495.81'], ['utcl bagheri', '296.82'], ['utcl panipat', '0'], ['amnuja nalagargh', '0']]
#     t = QtWidgets.QTreeWidget()
#     t.setGeometry(400, 100, 200, 191)
#     t.setHeaderLabels(['Customers','Sales (MT)'])
#     t.setAlternatingRowColors(True)
#     for i in sum_list:
#         if i[1] != '0' :
#             cg =QtWidgets.QTreeWidgetItem(t,i)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())