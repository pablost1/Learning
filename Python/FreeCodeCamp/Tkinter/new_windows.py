from tkinter import *
from PIL import ImageTk, Image

main_window = Tk()
main_window.title("Main Window")
main_window.iconbitmap("vader.ico")
#  #  # Functions
def second_windows():
    global image1

    top = Toplevel()
    top.title("second windows")
    top.iconbitmap("vader.ico")

    image1 = ImageTk.PhotoImage(Image.open("images\zelda1.png"))
    label1 = Label(top, image= image1).pack()
    second_exit = Button(top, text = "Quit", command = top.destroy)
    second_exit.pack()
    
#  #  # Declaring widgets
image1 = ImageTk.PhotoImage(Image.open("images\zelda1.png"))

open_second = Button(main_window, text = "open second windows", command = second_windows)

exit = Button(main_window, text = "Quit", bg = "black", fg = "white", command = main_window.quit)
#  #  # Deploying widgets
open_second.pack()
exit.pack()
#  #  #
main_window.mainloop()