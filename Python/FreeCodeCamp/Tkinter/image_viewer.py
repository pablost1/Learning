from tkinter import *
from PIL import ImageTk, Image

main_window = Tk()
main_window.title("Image Viewer v0.7.26022020")
main_window.iconbitmap('vader.ico') ### < Put the path here
### Variables
image_number = 1

### image access
img1 = ImageTk.PhotoImage(Image.open("images\\sciencecraft.jpg"))
img2 = ImageTk.PhotoImage(Image.open("images\\john.jpg"))
img3 = ImageTk.PhotoImage(Image.open("images\\zelda1.png"))
img4 = ImageTk.PhotoImage(Image.open("images\\zelda2.png"))
img5 = ImageTk.PhotoImage(Image.open("images\\zelda3.jfif"))
all_img = [img1, img2, img3, img4, img5]

### Functions
def forward(image_number):
    global label1
    global forward_button
    global back_button
    global progress_bar
    
    label1.grid_forget()
    forward_button.grid_forget()
    back_button.grid_forget()
    progress_bar.grid_forget()
    
    label1 = Label(image = all_img[image_number-1])
    progress_bar = Label(text = "%s image of %s" % (image_number, len(all_img)), bd=1, relief=SUNKEN, anchor=E)

    if image_number == len(all_img):
        forward_button = Button(main_window, text = ">>", state = DISABLED)
    else:
        forward_button = Button(main_window, text = ">>" , bg = "silver", borderwidth = 3, command = lambda: forward(image_number+1))
        
    back_button = Button(main_window, text = "<<", bg = "silver", borderwidth = 3, command = lambda: back(image_number-1))
    label1.grid(row = 0, column = 0, columnspan=3)
    
    back_button.grid(row = 1, column = 0)
    forward_button.grid(row=1, column = 2)
    
    progress_bar.grid(row=2, column = 0, columnspan=3, sticky = W+E)

def back(image_number):
    global label1
    global forward_button
    global back_button
    global progress_bar
    
    label1.grid_forget()
    forward_button.grid_forget()
    back_button.grid_forget()
    progress_bar.grid_forget()
    
    label1 = Label(image = all_img[image_number-1])
    progress_bar = Label(text = "%s image of %s" % (image_number, len(all_img)), bd=1, relief=SUNKEN, anchor=E)
    
    if image_number == 1:
        back_button = Button(main_window, text = "<<", state = DISABLED)
    else:
        back_button = Button(main_window, text = "<<", borderwidth = 3, command = lambda : back(image_number-1))
        
    forward_button = Button(main_window, text = ">>", borderwidth = 3, command = lambda : forward(image_number+1))
    label1.grid(row = 0, column = 0, columnspan=3)
    
    back_button.grid(row = 1, column = 0)
    forward_button.grid(row=1, column = 2)
    
    progress_bar.grid(row=2, column = 0, columnspan=3, sticky = W+E)

### Declaring Widgets

first_image = ImageTk.PhotoImage(Image.open("images\\sciencecraft.jpg"))
label1 = Label(image = all_img[0])

back_button = Button(main_window, text = "<<", bg = "silver", borderwidth = 3, state = DISABLED)
forward_button = Button(main_window, text = ">>", bg = "silver", borderwidth = 3, command = lambda : forward(2))

progress_bar = Label(text = "image 1 of %s" % (len(all_img)), bd=1, relief=SUNKEN, anchor=E)
exit_button = Button(main_window, text = "Quit", fg= "white", bg = "black", borderwidth = 3, command = main_window.quit)

### Deploying Widgets

label1.grid(row = 0, column = 0, columnspan=3)

back_button.grid(row = 1, column = 0, pady = 10)
exit_button.grid(row = 1, column = 1, pady = 10)
forward_button.grid(row=1, column = 2)

progress_bar.grid(row=2, column = 0, columnspan=3, sticky = W+E)
###

main_window.mainloop()