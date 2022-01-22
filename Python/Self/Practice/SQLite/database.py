import sqlite3

database_con =  sqlite3.connect('trivia.db')

cursor = database_con.cursor()

'''
cursor.execute("""CREATE TABLE MCU (
        question text,
        answer text
        )""")

database_con.execute("INSERT INTO MCU VALUES (:question, :answer)",
        {
            'question': '12',
            'answer': '12',
        }
)
'''
# cursor.execute("SELECT COUNT(*), FROM MCU")
number = 2
cursor.execute(f"SELECT *, oid From MCU")

all_records = cursor.fetchall()
 
for question_tuple in all_records:
        print(question_tuple)
database_con.commit()
database_con.close()
