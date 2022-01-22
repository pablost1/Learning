from tkinter import *

from PIL import ImageTk,Image

main_window = Tk()
main_window.title('Sliders!')
main_window.iconbitmap('C:\\Users\pablo\\tkinter_learning\\vader.ico')
main_window.geometry('400x400')

### Defining
def resize():
    main_window.geometry('%sx%s' % (horizontal.get(), vertical.get()))
###


vertical = Scale(main_window, from_=400, to=800, bg= 'silver')
vertical.pack(side=RIGHT, fill= Y)

horizontal = Scale(main_window, from_=400, to=800, bg= 'silver', orient=HORIZONTAL)
horizontal.pack(side=BOTTOM, fill= X)



resize_button = Button(main_window, text='Resize it!', command = resize)
resize_button.pack(expand = True, fill=BOTH)

exit = Button(main_window, text='Quit', bg='black',fg='gold', command=main_window.quit)
exit.pack(expand = True, fill=BOTH)

main_window.mainloop()