import database

#add a record to the database
# database.add_one("Reena","Modi","rinamodi@gmail.com")

#delete a record 
# database.delete_one('6')

# LOOKUP Email Address Record
database.email_lookup("ABC@gmail.com")

#Add MAny Records

# stuff = [
# ('Ajay','Kumar','ajaykr@gmail.com'),
# ('Rina','Modi','reenamodi@gmail.com')
# ]

# database.add_many(stuff)

#show all the records
# database.show_all()
