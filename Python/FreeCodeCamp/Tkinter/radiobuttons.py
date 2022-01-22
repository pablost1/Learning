from tkinter import * 
from PIL import ImageTk, ImageTk

main_window = Tk()
main_window.title("Radio Buttons")
main_window.iconbitmap("vader.ico")
### Functions

def clicked(value):
    global label
    label.grid_forget()
    label= Label(main_window, text = value)
    label.grid(row=0, column = 0)
    
# # # Variables # # #
#r = IntVar()
option_list = [
    ("Charmander","Fire"),
    ("Squirtle","Water"),
    ("Bulbasaur","Leaf"),
]
element = StringVar()
element.set("")
# # # Declaring Widgets # # #
#a = Radiobutton(main_window, text="Option 1", variable=r, value=1, command= lambda: clicked(r.get()))
#b = Radiobutton(main_window, text="Option 2", variable=r, value=2, command= lambda: clicked(r.get()))
#c = Radiobutton(main_window, text="Option 3", variable=r, value=3, command= lambda: clicked(r.get()))
label= Label(main_window, text= str(element.get()))

exit_button = Button(main_window, text = "Quit", fg= "white", bg = "black", borderwidth = 3, anchor = E, command = main_window.quit)
# # # Deploying Widgets # # #
#a.grid(row=1, column = 0)
#b.grid(row=2, column = 0)
#c.grid(row=3, column = 0)
i = 1
for pokemon, type in option_list:
    Radiobutton(main_window, text=pokemon, variable = element, value = type, command = lambda: clicked(element.get())).grid(row= i, column = 0)
    i+=1

label.grid(row=0, column = 0)

exit_button.grid(row=4, column=1, sticky = E)
###
main_window.mainloop()