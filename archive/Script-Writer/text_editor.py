from cgitb import text
from tkinter import *
from tkinter import filedialog
from tkinter import font
# import pyglet

root = Tk()

# Adds custom font
# pyglet.font.add_file("../fonts/Lovelt__.ttf")

root.title('Script Writer')
root.geometry('1200x660')

# Main Frame
frame = Frame(root)
frame.pack(pady=5)

# Text Scroller
scroller = Scrollbar(frame)
scroller.pack(side=RIGHT, fill=Y)

# Text Box
text_box = Text(
    frame,
    width=97,
    height=25,
    font=("Courier", 12),
    # font=("Delius", 12),
    selectbackground='gray',
    selectforeground='black',
    undo=True,
    yscrollcommand=scroller.set,
)
text_box.pack()


# Top-Bar Menu
top_menu = Menu(root)


# File, Edit Button into Menu
file_menu = Menu(top_menu, tearoff=False)
top_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New')
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
### Every edit should save with title + curr time 
### so there is a backlog incase one wants to go back to prior 'commit'
file_menu.add_separator()
file_menu.add_command(label='Close App', command=root.quit)

edit_menu = Menu(top_menu, tearoff=False)
top_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_separator()
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')


# Status Bar
status_bar = Label(root, text='Ready    ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


# Configurations
scroller.config(command=text_box.yview)
root.config(menu=top_menu)



root.mainloop()