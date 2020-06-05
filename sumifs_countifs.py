import pandas as pd
import xlwings
# customers defining and reading sale detail sheet
customers1 = [20,31,28,27,17,13,15,14,37,100125]
customers2 = [100051,100062,100087,100071,100070]
customers3 = [100057,100056,100066,100068,100086,100091,100103,100126,100131,100145,100150,100152,100140,100165]
df = pd.read_excel(open(r"Z:\Ash\FY 2019-20\Sale detail sheet\SALE DETAIL SHEET OCTOBER 2019.xlsx", "rb"), sheet_name="OCTOBER",index_col=None, header=  None)
tarik = input("please enter the date(dd-mm-yyyy) : ")
#  program for sumifs and countifs for customers1 and appending data to Dpr
sum_list1 = []
count_list1 =[]
for i in customers1:
    ab = df[df[2] == i]
    a= (ab[ab[6]== tarik][8]).sum()
    b= (ab[ab[6]== tarik][8]).count()
    sum_list1.append(round(a,2))
    count_list1.append(b)
wb = xlwings.Book('Z:\Ash\FY 2019-20\DAILY REPORT\DAILY REPORT FORMAT.xlsx')
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
# ws = wb.sheets['DPR']
ws.range('E24').options(transpose=True).value = count_list3
ws.range('F24').options(transpose=True).value = sum_list3
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


wb.save()
wb.close()
