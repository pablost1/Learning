from tkinter import *
from numpy import *
from PIL import ImageTk, Image

main_window = Tk()
main_window.title("Icons n' Images")
main_window.iconbitmap('vader.ico') ### < Put the path here
###

first_image = ImageTk.PhotoImage(Image.open("sciencecraft.jpg"))
label1 = Label(image = first_image)
label1.pack()

###
exit_button = Button(main_window, text = "Quit", fg= "white", bg = "black", command = main_window.quit)
exit_button.pack()
main_window.mainloop()