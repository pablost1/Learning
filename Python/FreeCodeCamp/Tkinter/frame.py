from tkinter import *
from PIL import ImageTk, Image

main_window = Tk()
main_window.title("frames")
main_window.iconbitmap('vader.ico') ### < Put the path here

frame = LabelFrame(main_window, text = "This is my Frame...", padx = 5, pady=5)
frame.pack(padx = 10, pady = 10)

labele = Label(frame, text = "Hello world!")
labele.pack()

main_window.mainloop()