from pathlib import Path
import sqlite3

# Specify path to directory holding the databases
db_folder = Path("databases")

# Global Variables
db_list = [file.stem for file in db_folder.rglob("*.db")]

# "Home" page, prints databases from path
# Then asks the user to choose one (or create a new ono)
def homepage():
	print("Hello and welcome to my program")
	print("Choose a database to use by entering the number associated with it, or enter 0 to add a new database:")

	for index, db in enumerate(db_list, start=1):
		print(f"({index}) {db}")

	choose_db = int(input(">>"))

	if choose_db == 0:
		new_db = str(input("Enter a name for the database:\n>>"))
		sqlite3.connect(str(db_folder) + "/" + new_db + ".db")
		print("Successfully created database\n")
	else:
		user_db = sqlite3.connect(str(db_folder) + "/" + db_list[choose_db - 1] + ".db")
		print("Opening " + db_list[choose_db - 1])
	return choose_db

# Prints all tables from Database
def displaydb(use_db):
	user_db = sqlite3.connect(str(db_folder) + "/" + db_list[use_db - 1] + ".db")
	cursor = user_db.cursor()
	cursor.execute("SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
	print(cursor.fetchall())
	print("done")

displaydb(homepage())
print("DONE")
