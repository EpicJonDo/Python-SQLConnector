from pathlib import Path
import sqlite3

# Specify path to directory holding the databases
db_path = "databases"
def dbpath()
	db_folder = Path(db_path)
	db_list = [file.stem for file in db_folder.rglob("*.db")]
	return db_list

# "Home" page, prints databases from path
# Then asks the user to choose one (or create a new ono)
def showdbs():
	for index, db in enumerate(db_list, start=1):
		print(f"({index}) {db}")

def createdb(new_db):
	sqlite3.connect(str(db_folder) + "/" + new_db + ".db")
	print("Successfully created database\n")

def connectdb(choose_db):
	user_db = sqlite3.connect(str(db_folder) + "/" + db_list[choose_db - 1] + ".db")
	print("Opening " + db_list[choose_db - 1])
	displaydb(user_db)

# Prints all tables from Database
def displaytables(user_db):
	cursor = user_db.cursor()
	cursor.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
	print(cursor.fetchall())

def displayinfo(table)
	cursor.execute("SELECT * FROM {table}")
	table_info = cursor.fetchall()
	return table_info

def maketable(new_table):
	print("Making Table...")
	cursor.execute(f"CREATE TABLE IF NOT EXISTS {new_table} (id INTEGER);")
	cursor.commit
	print("Made Table")

def makecolumn(table, name, value):
	print("Adding column...")
	cursor.execute(f"ALTER TABLE {table} ADD COLUMN {name} {value};")
	cursor.commit()
	print("Added Column")

def deletecolumn(table, column):
	print("Deleting Column...")
	cursor.execute(f"ALTER TABLE {table} DROP COLUMN {column};")
	cursor.commit()
	print("Deleted Column")

print("Hello and welcome to my program")
print("Choose a database to use by entering the number associated with it, or enter 0 to add a new database:")
showdbs()

db = int(input(">>"))

if db == 0:
	createdb(str(input("Enter a name for the new database:\n>>")))
else:
	connectdb(db)
