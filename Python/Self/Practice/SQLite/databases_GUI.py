from tkinter import *
import sqlite3

main_window = Tk()
main_window.title('Databases GUI!')
main_window.iconbitmap('C:\\Users\\pablo_iectaxb\\tkinter_learning\\vader.ico')
#main_window.geometry('450x400')

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''

# Commit changes
conn.commit()

# Close connection
conn.close()

### FUNCTION

def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    #c = conn.cursor()

    # insert into table
    conn.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
            {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get()})

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
    return
    
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()
    
    # Query database
    c.execute("SELECT *, oid FROM addresses")
    global records
    records = c.fetchall()
    #print(records)
    
    print_records = ''
    for record in records:
        print_records += ' - '.join([str(x) for x in record])
        print_records+='\n'
    
    record_window = Tk()
    record_window.title('Records')
    record_window.iconbitmap('C:\\Users\\pablo_iectaxb\\tkinter_learning\\vader.ico')
    #record_window.geometry('400x400')
    
    record_label = Label(record_window, text=print_records)
    record_label.grid(row=0, column=0, columnspan=2)
    
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
    
    return

def delete():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()
    
    # Query database
    c.execute("DELETE from addresses WHERE oid=%s" % (str(select_entry.get())))
    select_entry.delete(0, END)
    
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
    
    return

def edit():
    global edit_window
    
    edit_window = Tk()
    edit_window.title('Edit the record')
    edit_window.iconbitmap('C:\\Users\\pablo_iectaxb\\tkinter_learning\\vader.ico')
    edit_window.geometry('450x400')
        
    ### DEFINE

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
        # # # Entries
        
    f_name_editor = Entry(edit_window, width=30)
    l_name_editor = Entry(edit_window, width=30)
    address_editor = Entry(edit_window, width=30)
    city_editor = Entry(edit_window, width=30)
    state_editor = Entry(edit_window, width=30)
    zipcode_editor = Entry(edit_window, width=30)  

        # # # Labels
        
    f_label_editor = Label(edit_window, text = "First name")
    l_label_editor = Label(edit_window, text = "Last name")
    address_label_editor = Label(edit_window, text = "Address")
    city_label_editor = Label(edit_window, text = "City")
    state_label_editor = Label(edit_window, text = "State")
    zipcode_label_editor = Label(edit_window, text = "Zipcode")

        # # # Buttons
        
    update_btn = Button(edit_window, text = "Save changes", command = update)
    
    
    ### DEPLOY

        # # # Entries

    f_name_editor.grid(row=1, column=0, padx=20, pady=5)
    l_name_editor.grid(row=1, column=1, padx=20, pady=5)
    address_editor.grid(row=3, column=0, padx=20, pady=5)
    city_editor.grid(row=3, column=1, padx=20, pady=5)
    state_editor.grid(row=5, column=0, padx=20, pady=5)
    zipcode_editor.grid(row=5, column=1, padx=20, pady=5)


        # # # Labels
        
    f_label_editor.grid(row=0, column=0)
    l_label_editor.grid(row=0, column=1)
    address_label_editor.grid(row=2, column=0)
    city_label_editor.grid(row=2, column=1)
    state_label_editor.grid(row=4, column=0)
    zipcode_label_editor.grid(row=4, column=1)
    
        # # # Buttons
    
    update_btn.grid(row=6, column=1, pady=10, ipadx= 60 ,stick=S)
    
    #   #   #    #    #    #    #    #    #    #

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    record_id = select_entry.get()
    # Query the database
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])    
    
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    return
    
def update():
        # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()
    
    record_id = select_entry.get()
    c.execute('''UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :adress,
        city = :city,
        state = :state,
        zipcode = :zipcode
    
        WHERE oid = :oid''',
        {'first': f_name_editor.get(),
        'last': l_name_editor.get(),
        'adress': address_editor.get(),
        'city': city_editor.get(),
        'state': state_editor.get(),
        'zipcode': zipcode_editor.get(),
        'oid': record_id
        })
    
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()
    edit_window.destroy()
    return
    
### DEFINE

    # # # Entries
    
f_name = Entry(main_window, width=30)
l_name = Entry(main_window, width=30)
address = Entry(main_window, width=30)
city = Entry(main_window, width=30)
state = Entry(main_window, width=30)
zipcode = Entry(main_window, width=30)  
select_entry = Entry(main_window, width=30)

    # # # Labels
    
f_label = Label(main_window, text = "First name")
l_label = Label(main_window, text = "Last name")
address_label = Label(main_window, text = "Address")
city_label = Label(main_window, text = "City")
state_label = Label(main_window, text = "State")
zipcode_label = Label(main_window, text = "Zipcode")
select_label = Label(main_window, text= "Enter the Record ID")

    # # # Buttons
    
submit_btn = Button(main_window, text="Submit", command=submit)
delete_btn = Button(main_window, text="Delete", command= delete)
edit_btn = Button(main_window, text="Edit", command = edit)
query_btn = Button(main_window, text="Show Records", command = query)

### DEPLOY

    # # # Entries

f_name.grid(row=1, column=0, padx=20, pady=5)
l_name.grid(row=1, column=1, padx=20, pady=5)
address.grid(row=3, column=0, padx=20, pady=5)
city.grid(row=3, column=1, padx=20, pady=5)
state.grid(row=5, column=0, padx=20, pady=5)
zipcode.grid(row=5, column=1, padx=20, pady=5)
select_entry.grid(row=9, column=0, columnspan=2, pady=5)

    # # # Labels
    
f_label.grid(row=0, column=0)
l_label.grid(row=0, column=1)
address_label.grid(row=2, column=0)
city_label.grid(row=2, column=1)
state_label.grid(row=4, column=0)
zipcode_label.grid(row=4, column=1)
select_label.grid(row=8, column=0, columnspan=2)

    # # # Buttons

submit_btn.grid(row=6, column=0, columnspan=2,pady=5, ipadx=153)
query_btn.grid(row=7, column=0, columnspan=2,pady=5, ipadx=135)
edit_btn.grid(row=10, column=0, columnspan=2,pady=5, ipadx=163)
delete_btn.grid(row=11, column=0, columnspan=2,pady=5, ipadx=157)

###

exitb = Button(main_window,text="QUIT", bg = "black", fg = "gold", command= main_window.quit, anchor = S)
exitb.grid(row=12, column = 0, columnspan=2,pady=5, ipadx=161)
main_window.mainloop()