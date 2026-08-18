from pathlib import Path
import sqlite3

# Specify path to directory holding the databases
db_folder = Path("databases")


# "Home" page
def home():
	print("Hello and welcome to my program")
	print("Choose a database to use by entering the number associated with it, or enter 0 to add a new database:")
	db_list = [file.stem for file in db_folder.rglob("*.db")]

	for index, db in enumerate(db_list, start=1):
		print(f"({index}) {db}")

	choose_db = int(input())

	if choose_db == 0:
		new_db = str(input(print("Enter a name for the database:")))
		sqlite3.connect(db_folder + "/" + new_db + ".db")
		print("Successfully created database")
		home()
	else:
		choose_db -= 1
		user_db = sqlite3.connect(str(db_folder) + "/" + db_list[choose_db] + ".db")
		print("Opening " + db_list[choose_db])
	return choose_db

def nextpage(use_db):
#	user_db = sqlite.connect(str(db_folder + "/" + choose_db - 1)
	cursor = user_db.cursor
	print("connected")

nextpage(home())
print("DONE")
