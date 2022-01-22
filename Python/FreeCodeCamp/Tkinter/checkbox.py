from tkinter import *

from PIL import ImageTk,Image

main_window = Tk()
main_window.title('Checkboxes !')
main_window.iconbitmap('C:\\Users\pablo\\tkinter_learning\\vader.ico')
main_window.geometry('400x400')

### Defining
var = StringVar()
mylabel = Label(main_window, text = str(var.get())).pack()
def show():
    global mylabel
    mylabel = Label(main_window, text = str(var.get())).pack()
    return



###

show_button = Button(main_window, text = 'show the variable', command=show)
show_button.deselect()
show_button.pack()

check = Checkbutton(main_window, text='This is a text, yeah.', variable = var, onvalue='yeah', offvalue='oh no')
check.pack()

exit = Button(main_window, text='Quit', bg='black',fg='gold', command=main_window.quit)
exit.pack(expand = True, fill=BOTH)

main_window.mainloop()