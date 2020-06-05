import tkinter as tk
from tkinter import ttk

def show():

    # tempList = [[20, 0], [31, 664.17], [28, 270.02], [27, 503.42], [17, 0], [13, 0], [15, 962.79], [14, 0], [37, 64.46], [100125, 449.84]]
    tempList = [['Fateh Business House Pvt. Ltd.', 303991], ['JAI SHIV SHANKAR TRANSPORT CO.  ', 240769], [' AMRITSARIA MAL STONE CRUSHER     ', 270146], ['Everest Industries Ltd.', 319180], ['RAKESH KUMAR CONTRACTOR', 195937], ['HEMKUND SAHIB TRADING COMPANY', 113270], ['Ramjee concrete Pvt Ltd.', 84861], ['Paras Construction', 145460], ['Manju concrete fabriactors & developers Pvt. Ltd.', 64782], ['Sachin builders & contractors', 33938], ['R.S. Green Infra (India) Private limited ', 92576], ['BRICK TECHNOLOGY SUPPLIERS ', 45380], ['Tayal Building Material', 26209], ['S A Bricks Enterprises LLP', 9408], ['Royal Bricks Industries', 28237], ['M.M Concrete Products', 80189], ['Fairmont constructions', 95734], ['ANIKET CONSTRUCTION', 89855], ['A One Bricks', 34124], ['ONS Eco Bricks Industries', 20318], ['NTC Tiles LLP', 27805]]

    for name, score in tempList:
        if score > 0:
            listBox.insert("", "end", values=( name, score))

scores = tk.Tk() 
label = tk.Label(scores, text="Sale detail ", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ( 'Customer', 'Quantity(MT)')
listBox = ttk.Treeview(scores, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)    
listBox.grid(row=1, column=0, columnspan=2)

showScores = tk.Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
closeButton = tk.Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

scores.mainloop()