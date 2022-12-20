import sqlite3

# conn = sqlite3.connect(':memory:')

# conn = sqlite3.connect('customer.db')

# Create a cursor
# c = conn.cursor()


# Query the DB and Returns All Records

def show_all():
    #Connect to the database and create cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

# Add a new record to the Table
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    conn.commit()
    conn.close()

#Add MAny Records To Table
def add_many(List):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)",(List))
    conn.commit()
    conn.close()   

#Delete Record from Table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers where rowid = (?)",id)
    conn.commit()
    conn.close()

#LOOKUP with Where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)",(email,))
    items = c.fetchall()
    for item in items:
        print(item)
#commit our connection and close connection
    conn.commit()
    conn.close()







# ----------------1st step---------------------------------
#  Create a Table
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
# )""")

# or----
# c.execute("CREATE TABLE customers (first_name DATATYPE,last_name DATATYPE,email DATATYPE)")


# DATATYPES:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# -----------------------2nd step----------------------------
# many_customers = [
#                     ('Bharti', 'Smriti', 'smriti123@gmail.com'), 
#                     ('Smriti','Modi','modi123@gmail.com'),  
#                     ('misthi','barnwal','bhartismriti56@gmail.com')
#                 ]

# c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)


# ------------------------3rd step---------------------------

# Query The Database


# Update Records

# c.execute("""UPDATE customers SET first_name= "Smriti" 
#             WHERE rowid = 4
# """)

# c.execute("DELETE from customers WHERE  rowid=5")
# conn.commit()




# c.execute("SELECT rowid, * FROM customers")
# c.execute("SELECT * FROM customers WHERE email LIKE '%smriti%'")
# c.execute("SELECT rowid, * FROM customers")
# print(c.fetchone()[1])
# print(c.fetchmany(3))


# c.execute("SELECT rowid, * FROM customers ORDER BY rowid ASC")
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name")
# c.execute("SELECT * FROM customers WHERE first_name LIKE 'Sm%' OR rowid = 4")
#  DROP Table
# c.execute("DROP TABLE customers")
# conn.commit()
#Query the Database
# c.execute("SELECT rowid, * FROM customers")

# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")


# items = c.fetchall()


# ----------------------------4th step------------------------

# print("NAME" + "\t\tlast_name" + "\t\tEmail")
# print("-------" + "\t\t-------" + "\t\t---------------")
# for item in items:
#     print(item[0] + " \t\t "+ item[1]+ " \t\t "+ item[2])

# -----------------------5th step-------------------------------

# for item in items:
#     print(item)





# print("Command execute succesfully....")
# Commit our command
# conn.commit()

# # Close our connection
# conn.close()