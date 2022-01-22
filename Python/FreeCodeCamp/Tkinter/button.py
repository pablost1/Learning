from tkinter import * 
global x
x = 0
main = Tk()

text = "Click me!"

def click():
    global x
    x +=1
    label = Label(main, text = "CLICK!", fg = "black", bg= "pink", padx = 50)
    label.grid(row = x, column = 0)
myButton = Button(main, text = text , padx=50, pady=50, fg="pink",bg="#000000", command = click)
myButton.grid(row = 0, column = 0)

exit_button = Button(main, text = "Exit", bg="black", fg="red", command = main.quit)
exit_button.grid(row = 0, column = 1)
main.mainloop()