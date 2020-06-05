# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_qt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pdb
import mysql.connector

class Ui_MainWindow(object):

    # def loaddata(self):
    #     conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'Qwerty@@1234')
    #     cursor = conn.cursor()
    #     query = 'show databases'
    #     cursor.execute(query)
    #     query = 'use dpr'
    #     cursor.execute(query)
    #     query = 'show tables'
    #     cursor.execute(query)
    #     query = 'select* from sale'
    #     a = cursor.execute(query)
    #     self.tableWidget.setRowCount(0)
    #     for row_number, row_data in enumerate(a):
    #         self.tableWidget.insertRow(row_number)
    #         for column_number, data in enumerate(row_data):
    #             self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
    #     conn.close    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 130, 381, 221))
        self.tableWidget.setMinimumSize(QtCore.QSize(10, 10))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 400, 131, 31))
        self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.loaddata)

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
        self.tableWidget.setSortingEnabled(False)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        combi = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1]]
         
        combi = [[0,0],[1,0],[2,0]]#,[3,0]]#,[4,0],[5,0]]
        combi2 = [[0,1],[1,1],[2,1]]#,[3,1]]#,[4,1],[5,1]]
        data1= [['asian', '183.51'], ['asian fine', '671.36'], ['utcl roorkee', '495.81'], ['utcl bagheri', '296.82'], ['utcl panipat', 0], ['amnuja nalagargh', 0]]
        # combi = range(0,len(data1)) 
        for (i,j) in zip(combi,data1):
            item = self.tableWidget.item(i[0], 0)
            item.setText(_translate("MainWindow", j[0]))
        # pdb.set_trace()    
        for (i,j) in zip(combi2,data1):    
            item = self.tableWidget.item(i[0], 1)
            item.setText(_translate("MainWindow", j[1]))
        # item = self.tableWidget.item(3, 0)
        # item.setText(_translate("MainWindow", "acc"))
        # item = self.tableWidget.item(4, 1)
        # item.setText(_translate("MainWindow", "5"))
        # item = self.tableWidget.item(2, 0)
        # item.setText(_translate("MainWindow", "ambuj"))
        # item = self.tableWidget.item(2, 1)
        # item.setText(_translate("MainWindow", "70"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
