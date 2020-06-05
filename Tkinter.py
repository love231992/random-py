import tkinter as tk
from tkinter import ttk
from PIL import Image 
from tkinter import font  
win =tk.Tk()
win.title('Program')
main_menu = tk.Menu()

new_icon = tk.PhotoImage(file='icons/new.png')
redo_icon = tk.PhotoImage(file='icons/redo.png')
undo_icon = tk.PhotoImage(file='icons/undo.png')
search_icon = tk.PhotoImage(file='icons/search.png')
output_icon = tk.PhotoImage(file='icons/output.png')

file_menu = tk.Menu(main_menu, tearoff=False)
file_menu.add_command(label='New File',compound=tk.LEFT,image=new_icon, accelerator='Ctrl+n')
file_menu.add_command(label='Open file',accelerator='Ctrl+o')

edit = tk.Menu(main_menu, tearoff=False)
edit.add_command(label='Undo',compound=tk.LEFT,image=undo_icon,accelerator='Ctrl+z')
edit.add_command(label='Redo',compound=tk.LEFT,image=redo_icon,accelerator='Ctrl+r')

view = tk.Menu(main_menu, tearoff=False)
view.add_checkbutton(label='Output',compound=tk.LEFT,image=output_icon,accelerator='Ctrl+y')
view.add_command(label='Serach',compound=tk.LEFT,image=search_icon,accelerator='Ctrl+z')


main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)


toolbar =ttk.Label(win)
toolbar.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box= ttk.Combobox(toolbar, width=30, textvariable= font_family, state='readonly')
font_box['values'] = font_tuple
font_box.grid(row=0, column=0, padx=5)
font_box.current(font_tuple.index('Arial Black'))

size_var = tk.IntVar()
font_size =ttk.Combobox(toolbar,width=15,textvariable=size_var, state='readonly')
font_size.grid(row=0, column=1, padx =5)
font_size['values'] = tuple(range(10,100,2))
font_size.current(3)


text_editor = tk.Text(win)
text_editor.config(wrap='word', relief=tk.FLAT)
text_editor.focus_set()
text_editor.configure(font=('Roman', 14))

scroll_bar = tk.Scrollbar(win)
scroll_bar.pack(fill=tk.Y, side=tk.RIGHT)
text_editor.pack(expand=True, fill=tk.BOTH)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

status_bar = ttk.Label(win, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)




win.config(menu=main_menu)
win.mainloop()

