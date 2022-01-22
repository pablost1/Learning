from tkinter import * 
import sqlite3

main_window = Tk()
main_window.title('Drop Down Boxes!')
main_window.iconbitmap('C:\\Users\pablo\\tkinter_learning\\vader.ico')
main_window.geometry('400x400')

### defy

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')


# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")


# Commit changes
conn.commit()

# Close connection
conn.close()
### deploy


exitb = Button(main_window,text="QUIT", bg = "black", fg = "gold", command= main_window.quit)
exitb.pack(side=BOTTOM)
main_window.mainloop()