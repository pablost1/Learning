from tkinter import * 


main_window = Tk()
main_window.title('Drop Down Boxes!')
main_window.iconbitmap('C:\\Users\pablo\\tkinter_learning\\vader.ico')
main_window.geometry('400x400')

### defy
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set("Choose something")
drop = OptionMenu(main_window, clicked, *options)

### deploy
drop.pack()


exitb = Button(main_window,text="QUIT", bg = "black", fg = "gold", command= main_window.quit)
exitb.pack(side=BOTTOM)
main_window.mainloop()