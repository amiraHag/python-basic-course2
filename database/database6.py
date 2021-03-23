# ----------------------------------------------
# -- Databases => SQLite => Update and Delete --
# ----------------------------------------------

# Import SQLite Module
import sqlite3

# Create Database And Connect
db = sqlite3.connect("app.db")

# Setting Up The Cursor
cr = db.cursor()

#Inserting Data
#cr.execute("insert into users(user_id, name) values(1, 'Amira')")
#cr.execute("insert into users(user_id, name) values(2, 'Ahmed')")
#cr.execute("insert into users(user_id, name) values(3, 'Sara')")
#cr.execute("insert into users(user_id, name) values(4, 'Omar')")

# Update Data
#cr.execute("update users set name = 'Amira MI' where user_id = 1")
#cr.execute("update users set name = 'Ahmed Hag' where user_id = 2")
#cr.execute("update users set name = 'Sara MI' where user_id = 3")

# Delete Data
cr.execute("delete from users where user_id = 4")

# Fetch Data
cr.execute("select * from users")

print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())

# Save (Commit) Changes
db.commit()

# Close Database
db.close()
