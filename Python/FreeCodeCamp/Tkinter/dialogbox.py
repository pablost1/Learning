from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

main_window = Tk()
main_window.title("Dialog Box")
main_window.iconbitmap("vader.ico")
#  #  # Data

main_window.filename = filedialog.askopenfilename(initialdir= ".\\images", title = "Select a File", filetypes=(("png files", "*.png"),("all files","*.*")))

#  #  #  Declaring Widgets

label = Label(main_window, text = main_window.filename)
image1 = ImageTk.PhotoImage(Image.open(main_window.filename))
label2 = Label(main_window, image = image1)

#  #  #  Deploying Widgets

label.pack()
label2.pack()

#  #  #
main_window.mainloop()