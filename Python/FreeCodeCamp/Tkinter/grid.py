from tkinter import *

window = Tk()

window.title("Let's get going")
window.configure(background="black")
'''photo1 = PhotoImage(file = "C:\\Users\\pablo_hhwi4\\Downloads\\14234327479080.png")
Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=W)'''
label1 = Label(window, text = "How are ya?\n\n\n")
label2 = Label(window, text = "Let's get going!\n\n\n")

# # # --- # # #
label1.grid(row=0, column =0)
label2.grid(row=1, column =1)
label2.grid(row=2, column =0)


# # # Main loop # # #
window.mainloop()
