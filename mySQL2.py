import sqlite3

connection = sqlite3.connect("test_database.db")
# c = connection.cursor()
# #connection.commit
# connection = sqlite3.connect(':memory:')
# one time use database
#
# connection.close()

#get person data from User
first_name = input("Enter your first name")
last_name = input("Enter your last name")
age = int(input("Enter your age:"))
person_data = (first_name, last_name, age)

#execure insert statement for supplied person data
with sqlite3.conect("test_database.db") as connection:
    c = connection.cursor()
    ("""
    DROP TABLE IF EXISTS People;
    CREATE TABLE People(FirstName Text, LastName Text, Age Int);
    """)
    people_values = (
        ('Ron', 'Obvious', 42),
        ('Luigi', 'Vercotti', 43),
        ('Arthur', 'Belling', 28)
    )
    c.executemany("INSERT INTO People Values(?,?,?)", people_values)
    c.execute("INSERT INTO People VALUES(?,?,?)", person_data)
    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName = ?", (45, 'Luigi', 'Vercotti'))
