from tkinter import * 

main = Tk()

text = "Click me!"

def click():
    label = Label(main,borderwidth = 5, text = en.get(), fg = "black", bg= "pink", padx = 50)
    label.pack()
    return

en = Entry(main, borderwidth = 5, bg = "skyblue", fg= "white")
en.pack()
en.insert(0, "type something")
 
myButton = Button(main, text = text, borderwidth = 10, padx=50, pady=50, fg="pink",bg="#000000", command = click)
myButton.pack()


main.mainloop()