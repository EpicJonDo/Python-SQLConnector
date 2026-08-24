from pathlib import Path
import sqlite3

# Specify path to directory holding the databases
db_folder = Path("databases")

# Global Variables
db_list = [file.stem for file in db_folder.rglob("*.db")]

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
def displaydb(user_db):
	cursor = user_db.cursor()
	cursor.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
	print(cursor.fetchall())
	print("Choose a table, or enter 0 to add a new table:\n")
	choose_table = int(input(">>"))

	if choose_table == 0:
		new_table = str(input("ID column will be made by defult. Enter a name for the new table: "))
		columns = int(input("How many more columns would you like to add?: "))
		print("Making table...")
		make_table = f"CREATE TABLE IF NOT EXISTS {new_table} (id INTEGER);"
		cursor.execute(make_table)
		for i in range(columns):
			column_name = str(input("Enter column name: "))
			column_type = str(input("Enter column datatype: "))
			makecolumn(new_table, column_name, column_type)
	else:
		pass

	print("Successfully added table!")

def makecolumn(table, name, value):
	print("Adding column...")
	cursor.execute(f"ALTER TABLE {table} ADD COLUMN {name} {value};")
	cursor.commit()
	print("Added Column")

print("Hello and welcome to my program")
print("Choose a database to use by entering the number associated with it, or enter 0 to add a new database:")
showdbs()

db = int(input(">>"))

if db == 0:
	createdb(str(input("Enter a name for the new database:\n>>")))
else:
	connectdb(db)
