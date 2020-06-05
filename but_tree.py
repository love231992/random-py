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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(389, 19, 381, 541))
        self.groupBox.setObjectName("groupBox")
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox)
        self.treeWidget.setGeometry(QtCore.QRect(50, 30, 241, 381))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setWhatsThis(0, "")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        item_0.setFont(0, font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(1, brush)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 440, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 470, 47, 13))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 440, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 470, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 510, 201, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.sale)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Customers"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Sales"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "abc"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "path"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def sale(self):
        sum_list= []
        x = datetime.datetime.now()
        a = x.strftime("%B")
        # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        path = r'C:\Users\Lovepreet Singh\OneDrive - Larsen & Toubro'
        userpath = self.lineEdit_2.text()
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
        tarik = self.lineEdit.text()
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
                
                # self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "New Item"))
                self.treeWidget.topLevelItem(i).setText(0, _translate("MainWindow",j[0])) 
        # combi2 = range(0, len(sum_list))    
        for i,j in zip(combi,sum_list):
            if j[1] != '0':
                
                self.treeWidget.topLevelItem(i).setText(1, _translate("MainWindow",j[1]))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
