# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DPR_final.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# Fix qt import error
# Include this file before import PyQt5 

import fix_qt_import_error
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import xlwings
import os.path
from PyQt5.QtWidgets import QMessageBox
import datetime
from datetime import date
import babel.numbers
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1900, 870)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("truck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1380, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("new.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.groupBox_dpr = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dpr.setGeometry(QtCore.QRect(20, 170, 311, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_dpr.setFont(font)
        self.groupBox_dpr.setAutoFillBackground(False)
        self.groupBox_dpr.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_dpr.setFlat(False)
        self.groupBox_dpr.setCheckable(False)
        self.groupBox_dpr.setObjectName("groupBox_dpr")
        self.label_date_dpr = QtWidgets.QLabel(self.groupBox_dpr)
        self.label_date_dpr.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_date_dpr.setObjectName("label_date_dpr")
        self.label_dpr_file = QtWidgets.QLabel(self.groupBox_dpr)
        self.label_dpr_file.setGeometry(QtCore.QRect(10, 100, 141, 21))
        self.label_dpr_file.setObjectName("label_dpr_file")
        self.lineEdit_dpr_date = QtWidgets.QLineEdit(self.groupBox_dpr)
        self.lineEdit_dpr_date.setGeometry(QtCore.QRect(160, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dpr_date.setFont(font)
        self.lineEdit_dpr_date.setWhatsThis("")
        self.lineEdit_dpr_date.setObjectName("lineEdit_dpr_date")
        self.lineEdit_dpr_file = QtWidgets.QLineEdit(self.groupBox_dpr)
        self.lineEdit_dpr_file.setGeometry(QtCore.QRect(160, 100, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_dpr_file.setFont(font)
        self.lineEdit_dpr_file.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_dpr_file.setObjectName("lineEdit_dpr_file")
        self.pushButton_dpr = QtWidgets.QPushButton(self.groupBox_dpr)
        self.pushButton_dpr.setGeometry(QtCore.QRect(90, 170, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_dpr.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("2185917.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_dpr.setIcon(icon1)
        self.pushButton_dpr.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_dpr.setObjectName("pushButton_dpr")
        self.groupBox_sale = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_sale.setGeometry(QtCore.QRect(360, 170, 421, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_sale.setFont(font)
        self.groupBox_sale.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_sale.setObjectName("groupBox_sale")
        self.tableWidget_sale = QtWidgets.QTableWidget(self.groupBox_sale)
        self.tableWidget_sale.setGeometry(QtCore.QRect(10, 20, 256, 471))
        self.tableWidget_sale.setAutoFillBackground(False)
        self.tableWidget_sale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_sale.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_sale.setAutoScrollMargin(16)
        self.tableWidget_sale.setAlternatingRowColors(True)
        self.tableWidget_sale.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget_sale.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_sale.setObjectName("tableWidget_sale")
        self.tableWidget_sale.setColumnCount(2)
        self.tableWidget_sale.setRowCount(25)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sale.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sale.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_sale.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_sale.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_sale.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_sale.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sale.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sale.setItem(1, 1, item)

        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox_sale)
        self.pushButton_1.setGeometry(QtCore.QRect(290, 420, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        icon_2 = QtGui.QIcon()
        icon_2.addPixmap(QtGui.QPixmap("clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_1.setIcon(icon_2)
        self.pushButton_1.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_sale = QtWidgets.QPushButton(self.groupBox_sale)
        self.pushButton_sale.setGeometry(QtCore.QRect(290, 370, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_sale.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("click.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sale.setIcon(icon2)
        self.pushButton_sale.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_sale.setObjectName("pushButton_sale")
        self.pushButton_1.setObjectName("pushButton_1")

        self.widget = QtWidgets.QWidget(self.groupBox_sale)
        self.widget.setGeometry(QtCore.QRect(280, 30, 131, 52))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sale_date = QtWidgets.QLabel(self.widget)
        self.label_sale_date.setObjectName("label_sale_date")
        self.verticalLayout.addWidget(self.label_sale_date)
        self.lineEdit_sale_date = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sale_date.setFont(font)
        self.lineEdit_sale_date.setObjectName("lineEdit_sale_date")
        self.verticalLayout.addWidget(self.lineEdit_sale_date)
        self.widget1 = QtWidgets.QWidget(self.groupBox_sale)
        self.widget1.setGeometry(QtCore.QRect(276, 200, 141, 52))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_sale_file = QtWidgets.QLabel(self.widget1)
        self.label_sale_file.setObjectName("label_sale_file")
        self.verticalLayout_2.addWidget(self.label_sale_file)
        self.lineEdit_sale_file = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_sale_file.setFont(font)
        self.lineEdit_sale_file.setObjectName("lineEdit_sale_file")
        self.verticalLayout_2.addWidget(self.lineEdit_sale_file)
        self.groupBox__balance = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox__balance.setGeometry(QtCore.QRect(850, 170, 411, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox__balance.setFont(font)
        self.groupBox__balance.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox__balance.setObjectName("groupBox__balance")
        self.tableWidget_balance = QtWidgets.QTableWidget(self.groupBox__balance)
        self.tableWidget_balance.setGeometry(QtCore.QRect(10, 20, 256, 471))
        self.tableWidget_balance.setAlternatingRowColors(True)
        self.tableWidget_balance.setObjectName("tableWidget_balance")
        self.tableWidget_balance.setColumnCount(2)
        self.tableWidget_balance.setRowCount(25)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_balance.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_balance.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_balance.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_balance.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_balance.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_balance.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_balance.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_balance.setItem(1, 1, item)
        self.pushButton_balance = QtWidgets.QPushButton(self.groupBox__balance)
        self.pushButton_balance.setGeometry(QtCore.QRect(270, 220, 131, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_balance.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("tap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_balance.setIcon(icon3)
        self.pushButton_balance.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_balance.setObjectName("pushButton_balance")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
     # ************************* Push buttons signals *****************************************   
        self.pushButton_dpr.clicked.connect(self.daily_report)
        self.pushButton_balance.clicked.connect(self.balance)
        self.pushButton_sale.clicked.connect(self.sale_detail)
        self.pushButton_1.clicked.connect(self.clear)
        # self.pushButton_1.clicked.connect(self.clear)
# **********************************************************************************************8

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASH SOLUTION"))
        self.groupBox_dpr.setTitle(_translate("MainWindow", "Daily Progress Report"))
        self.label_date_dpr.setText(_translate("MainWindow", "Enter the date"))
        self.label_dpr_file.setText(_translate("MainWindow", "Enter the file name"))
        self.lineEdit_dpr_date.setPlaceholderText(_translate("MainWindow", "DD-MM-YYYY"))
        self.lineEdit_dpr_file.setPlaceholderText(_translate("MainWindow", "Month from file name"))
        self.pushButton_dpr.setText(_translate("MainWindow", "Generate DPR"))
        self.groupBox_sale.setTitle(_translate("MainWindow", "Sale Quantity"))
        item = self.tableWidget_sale.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_sale.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_sale.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CUSTOMER"))
        item = self.tableWidget_sale.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "QTY (MT)"))
        __sortingEnabled = self.tableWidget_sale.isSortingEnabled()
        self.tableWidget_sale.setSortingEnabled(False)
        # item = self.tableWidget_sale.item(0, 0)
        # item.setText(_translate("MainWindow", "ABC"))
        # item = self.tableWidget_sale.item(0, 1)
        # item.setText(_translate("MainWindow", "ZXC"))
        # item = self.tableWidget_sale.item(1, 0)
        # item.setText(_translate("MainWindow", "zxc"))
        # item = self.tableWidget_sale.item(1, 1)
        # item.setText(_translate("MainWindow", "qw"))
        self.tableWidget_sale.setSortingEnabled(__sortingEnabled)
        self.pushButton_sale.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton_1.setText(_translate("MainWindow", "Clear"))
        # self.pushButton_sale.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.label_sale_date.setText(_translate("MainWindow", "Enter the date"))
        self.lineEdit_sale_date.setPlaceholderText(_translate("MainWindow", "DD-MM-YYYY"))
        self.label_sale_file.setText(_translate("MainWindow", "Enter the file name"))
        self.lineEdit_sale_file.setPlaceholderText(_translate("MainWindow", "Month from file"))
        self.groupBox__balance.setTitle(_translate("MainWindow", "Customer Balance"))
        item = self.tableWidget_balance.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_balance.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_balance.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CUSTOMER"))
        item = self.tableWidget_balance.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BALANCE"))
        __sortingEnabled = self.tableWidget_balance.isSortingEnabled()
        self.tableWidget_balance.setSortingEnabled(False)
        # item = self.tableWidget_balance.item(0, 0)
        # item.setText(_translate("MainWindow", "ASD"))
        # item = self.tableWidget_balance.item(0, 1)
        # item.setText(_translate("MainWindow", "10"))
        # item = self.tableWidget_balance.item(1, 0)
        # item.setText(_translate("MainWindow", "ZXC"))
        # item = self.tableWidget_balance.item(1, 1)
        # item.setText(_translate("MainWindow", "20"))
        self.tableWidget_balance.setSortingEnabled(__sortingEnabled)
        self.pushButton_balance.setText(_translate("MainWindow", "SHOW"))



# ************************************DPR creation starts****************************************
    def daily_report(self):
        userdate_date= self.lineEdit_dpr_date.text()
        userpath = self.lineEdit_dpr_file.text()

        path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        userpath1 = f'SALE DETAIL SHEET {userpath.upper()} 2020'
        abc = os.path.join(path, userpath1+'.xlsx')
        customers1 = [20,31,28,27,17,46,18,13,15,14,37,100125]
        customers2 = [100051,100062,100072,100087,100071,100070]
        customers3 = [100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165,100180]
        x = datetime.datetime.now()
        month = x.strftime("%B")
        df = pd.read_excel(open(abc, "rb"), sheet_name= 'JANUARY' ,index_col=None, header=  None)
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
        wb = xlwings.Book(r'\\10.9.32.2\adm\Ash\FY 2019-20\DAILY REPORT\DAILY REPORT FORMAT.xlsx')
        xlwings.App().visible=False
        ws = wb.sheets['DPR']
        ws.range('E7').options(transpose=True).value = count_list1
        ws.range('F7').options(transpose=True).value = sum_list1
        
#  program for sumifs and countifs for customers2 and appending data to Dpr
        sum_list2 = []
        count_list2 =[]
        for i in customers2:
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b= (ab[ab[6]== tarik][8]).count()
            sum_list2.append(round(a,2))
            count_list2.append(b)

        ws.range('E20').options(transpose=True).value = count_list2
        ws.range('F20').options(transpose=True).value = sum_list2
        
#  program for sumifs and countifs for customers3 and appending data to Dpr
        sum_list3 = []
        count_list3 =[]
        for i in customers3:
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b= (ab[ab[6]== tarik][8]).count()
            sum_list3.append(round(a,2))
            count_list3.append(b)

        ws.range('F27').options(transpose=True).value = sum_list3
        ws.range('E27').options(transpose=True).value = count_list3
        # print(sum_list3)
        # print(count_list3)

        dict1= {
            'F7' : 'E49',
            'F8' : 'E50',
            'F9' : 'E51',
            'F10' : 'E52',
            'F11' : 'E53',
            'F12' : 'E54',
            'F13' : 'E55',
            'F14' : 'E56',
            'F15' : 'E57',
            'F16' : 'E58',
            'F17' : 'E59',
            'F18' : 'E60',
            
    
         }

        for i,j in dict1.items():
            num1 = 0
            num1_new = ws.range(i).value 
            num2 = ws.range(j).value 
            ws.range(j).value = (num2+(num1_new - num1))
    

        dict2= {
            'F20' : 'E62',
            'F21' : 'E63',
            'F22' : 'E64',
            'F23' : 'E65', 
            'F24' : 'E66', 
            'F25' : 'E67', 
        }

        for i,j in dict2.items():
            num1 = 0
            num1_new = ws.range(i).value 
            num2 = ws.range(j).value 
            ws.range(j).value = (num2+(num1_new - num1))
    

        dict3= {
            'F27' : 'E69',
            'F28' : 'E70',
            'F29' : 'E71',
            'F30':  'E72',
            'F31' : 'E73',
            'F32' : 'E74',
            'F33' : 'E76', ##
            'F34' : 'E77',
            'F35' : 'E78',
            'F36' : 'E79',
            'F37' : 'E80',
            'F38' : 'E81',
            'F39' : 'E82',
            'F40' : 'E83',
            'F41' : 'E84',
    
        }

        for i,j in dict3.items():
            num1 = 0
            num1_new = ws.range(i).value 
            num2 = ws.range(j).value 
            ws.range(j).value = (num2+(num1_new - num1))
   
        msg = QMessageBox()
        msg.setWindowTitle("Submitted")
        msg.setText('Report Generated Successfully')
        msg.setIcon(QMessageBox.Information)
        x= msg.exec_()   

        wb.save()
        wb.close()
#                  *********************** dpr creation ends **************************
#                   *********************  Balance starts **********************************
    def balance(self):
        app = xlwings.App(visible=False)
        wb = app.books.open(r'\\10.9.32.2\adm\Ash\FY 2019-20\DAILY REPORT\DAILY REPORT FORMAT.xlsx')
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
        yester_bal = []
        for i,j in dict1.items():
            b = ws.range(j). value
            c = b
            yester_bal.append(c)  
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        x = datetime.datetime.now()
        month = x.strftime("%B")
        path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        userpath = f'SALE DETAIL SHEET {month.upper()} 2020' 
        abc = os.path.join(path, userpath+'.xlsx')
        df = pd.read_excel(open(abc,"rb"),sheet_name= month.upper(), index_col=None, header=  None)
        tarik = d1
        customers = [100051,100070,100071,100062,100072,100087,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165,100180]
        today_sale = []
        for i in customers:
            ab = df[df[2] == i]
            amount = (ab[ab[6]== tarik][19]).sum()
            today_sale.append(amount)

        net_bal = []   
        for (i, j) in zip(yester_bal,today_sale):
            final = round(i - j)
            # x = babel.numbers.format_currency(( final ), "INR")
            net_bal.append(final)
        
        cust_name =[]
        for (i,j) in dict1.items():
            b = ws.range(i). value
            cust_name.append(b)

        bal= list(zip(cust_name, net_bal))
        combi = range(0, len(bal))
        for (i,j) in zip(combi,bal):
            self.tableWidget_balance.setItem(i,0,QtWidgets.QTableWidgetItem(j[0]))
            self.tableWidget_balance.setItem(i,1,QtWidgets.QTableWidgetItem(str(j[1])))

        wb.close()
# ***************************************** balance ends ****************************************************
# **************************************** Sale QTy Start *************************************************
    def sale_detail(self):
        self.tableWidget_sale.setRowCount(25)
        sum_list= []
        x = datetime.datetime.now()
        month = x.strftime("%B")
        # path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        path = r'\\10.9.32.2\adm\Ash\FY 2019-20\Sale detail sheet'
        userpath = self.lineEdit_sale_file.text()
        if userpath =='' :
            userpath = f'SALE DETAIL SHEET {month.upper()} 2020'
        else:  
            userpath = userpath
        abc = os.path.join(path, userpath+'.xlsx')
        customers1 = [20,31,28,27,17,46,18,13,15,14,37,100125,100051,100062,100087,100072,100071,100070,100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165,100180]
        customers2 = [ 'Asian Cements','Asian Fine', 'UTCL Roorkee', 'UTCL Bagheri','UTCL Panipat','UTCL Sikandrabad','UTCL Bathinda','Ambuja Nalagargh','Ambuja Ropar','Ambuja Roorkee','Ambuja Dadri','ACC LTD','Fateh','Everest','Hemkund Sahib','Rakesh kumar','Amritsaria','Jai Shiv shankar','Ramjee','Paras','Manju','Sachin','R.S.Green','BTS','S.A.Bricks','Royal','M.M. Concrete','Fairmont','Aniket','A One','ONS','NTC','Guru Teg Bhadar']
        customers2_length = range(0,len(customers2))
        today = date.today()
        d1 = today.strftime("%d-%m-%Y")
        tarik = self.lineEdit_sale_date.text()
        if tarik == '':
            tarik = d1
        else :
            tarik = tarik       
        df = pd.read_excel(open(abc,"rb"),sheet_name= month.upper(), index_col=None, header=  None)
        for (i,j) in zip(customers1, customers2_length):
            ab = df[df[2] == i]
            a= (ab[ab[6]== tarik][8]).sum()
            b = round(a,2)
            i = customers2[j]
            if b != 0:
                sum_list.append([i, str(b)])

        combi = range(0, len(sum_list))
        for (i,j) in zip(combi,sum_list):
            self.tableWidget_sale.setItem(i,0,QtWidgets.QTableWidgetItem(j[0]))
            self.tableWidget_sale.setItem(i,1,QtWidgets.QTableWidgetItem(j[1]))    
        # QtCore.QTimer.singleShot(5, self.sale_detail)


# **************************************** sale ends *****************************************
######################################### Clear starts ##################################
    # def clear(self):
    #     self.tableWidget_sale.setRowCount(0)
    def clear(self):
        self.tableWidget_sale.setRowCount(0)

######################################### Clear ends ##################################





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
