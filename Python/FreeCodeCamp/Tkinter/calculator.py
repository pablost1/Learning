from tkinter import *

main_window = Tk()
main_window.title("Calculator")

input =  Entry(main_window, width=35, borderwidth=5)
input.grid(row=0, column = 0, columnspan=3, padx=10, pady=10 )

# # # Variables # # #
global calc
calc = 0
# # # Functions # # #

def onef():
    input.insert(END, "1")
    return

def twof():
    input.insert(END, "2")
    return

def threef():
    input.insert(END, "3")
    return

def fourf():
    input.insert(END, "4")
    return

def fivef():
    input.insert(END, "5")
    return

def sixf():
    input.insert(END, "6")
    return

def sevenf():
    input.insert(END, "7")
    return

def eightf():
    input.insert(END, "8")
    return

def ninef():
    input.insert(END, "9")
    return

def zerof():
    input.insert(END, "0")
    return

def plusf():
    query = input.get()
    if query == "":
        query = 0
    global calc
    global last_operation
    last_operation = "plus"
    calc = int(query)
    clearf()
    return

def dividef():
    query = input.get()
    if query == "":
        query = 0
    global calc
    global last_operation
    last_operation = "divide"
    calc = int(query)
    clearf()
    return

def subtractf():
    query = input.get()
    if query == "":
        query = 0
    global calc
    global last_operation
    last_operation = "subtract"
    calc = int(query)
    clearf()
    return

def multiplyf():
    query = input.get()
    if query == "":
        query = 0
    global calc
    global last_operation
    last_operation = "multiply"
    calc =int(query)
    clearf()
    return

def clearf():
    input.delete(0, END)
    return

def resultf():
    current = input.get()
    if current == "":
        current = 0
    else:
        current = int(current)
    clearf()
    if last_operation == "plus":
        input.insert(0, calc + current)
    elif last_operation == "subtract":
        input.insert(0, calc - current)
    elif last_operation == "multiply":
        input.insert(0, calc * current)
    elif last_operation == "divide":
        input.insert(0, calc // current)
    return

# # # Buttons # # #

oneb = Button(main_window, padx=40,pady = 20, text = "1", command = onef).grid(row = 3, column = 0)
twob = Button(main_window, padx=40,pady = 20, text = "2", command = twof).grid(row = 3, column = 1)
threeb = Button(main_window, padx=40,pady = 20, text = "3", command = threef).grid(row = 3, column = 2)

fourb = Button(main_window, padx=40,pady = 20, text = "4", command = fourf).grid(row = 2, column = 0)
fiveb = Button(main_window, padx=40,pady = 20, text = "5", command = fivef).grid(row = 2, column = 1)
sixb = Button(main_window, padx=40,pady = 20, text = "6", command = sixf).grid(row = 2, column = 2)

sevenb = Button(main_window, padx=40,pady = 20, text = "7", command = sevenf).grid(row = 1, column = 0)
eightb = Button(main_window, padx=40,pady = 20, text = "8", command = eightf).grid(row = 1, column = 1)
nineb = Button(main_window, padx=40,pady = 20, text = "9", command = ninef).grid(row = 1, column = 2)
zerob = Button(main_window, padx=40,pady = 20, text = "0", command = zerof).grid(row = 4, column = 0)

plusb = Button(main_window, padx=40,pady = 20, text= "+", command = plusf).grid(row = 5, column = 0)
resultb = Button(main_window, padx=91,pady = 20, text = "=", command = resultf).grid(row = 4, column = 1, columnspan=2)
clearb = Button(main_window, padx=81,pady = 20, text = "Clear", command = clearf).grid(row = 5, column = 1, columnspan=2)

subtractb = Button(main_window, padx=40,pady = 20, text = "-", command = subtractf).grid(row = 6, column = 0)
divideb = Button(main_window, padx=40,pady = 20, text = "/", command = dividef).grid(row = 6, column = 1)
multiplyb = Button(main_window, padx=40,pady = 20, text = "*", command = multiplyf).grid(row = 6, column = 2)


# # # ------------- # # #



main_window = mainloop()