from tkinter import * 
from tkinter import messagebox

main_window = Tk()
main_window.title("Vader")
main_window.iconbitmap("vader.ico")
#  #  #  Functions
def popup():
        pop = messagebox.askyesno("This is my pop up", "Hello World")
        if pop == 1:
            Label(main_window, text="You Clicked Yes!").pack()
        else:
            Label(main_window,text = "You Clicked No!").pack()
#  #  # Declaring Widget

Button(main_window, text = "pop-up", command = popup).pack()

#  #  #

main_window.mainloop()