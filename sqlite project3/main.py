import sqlite3 as lite

# Managing the Database and the CRUD(Create,Retrieve,Update and Delete) operations


class Database_Management():
    # TODO: Connecting to the database and creating the Table
    def __init__(self):
        global con
        try:
            con = lite.connect("sqlite.db")
            with con:
                cur = con.cursor()
                cur.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, roll INTEGER NOT NULL UNIQUE, dept TEXT NOT NULL, year INTEGER NOT NULL, subjects TEXT NOT NULL, under_grad BOOLEAN NOT NULL DEFAULT 1)''')
                con.commit()
                print("Database successfully created")
        except Exception:
            print("Oops Something Went Wrong")
    # TODO: Insertion of data into the database

    def insert_data(self, data):
        try:
            con = lite.connect("sqlite.db")
            with con:
                cur = con.cursor()
                cur.execute(
                    '''INSERT INTO students (name,roll,dept,year,subjects,under_grad) VALUES (?,?,?,?,?,?);''', data)
                con.commit()
                return True
        except Exception:
            return False
    # TODO: Update the data into the database

    def update_data(self, id, data):
        try:
            con = lite.connect("sqlite.db")
            with con:
                cur = con.cursor()
                cur.execute(
                    '''UPDATE students set roll= ?,dept= ?, year= ?, subjects= ?,under_grad= ? where id = ?''', (data[0], data[1], data[2], data[3], data[4], id))
                con.commit()
                return True
        except Exception:
            return False
    # TODO: Fetch data from the database by id

    def fetch_by_id(self, id):
        try:
            con = lite.connect("sqlite.db")
            with con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM students WHERE id = ?''', (id,))
                con.commit()
                record = cur.fetchall()
                return record
        except Exception:
            return False
    # TODO: Fetch all the data from the database

    def fetch_data(self):
        try:
            con = lite.connect("sqlite.db")
            with con:
                cur = con.cursor()
                cur.execute('''SELECT * FROM students''')
                con.commit()
                records = cur.fetchall()
                return records
        except Exception:
            return False
    # TODO: Delete data from the database

    def delete_data(self, id):
        try:
            con = lite.connect("sqlite.db")
            with con:
                cur = con.cursor()
                cur.execute('''DELETE FROM students WHERE id = ?''', [id])
                con.commit()
                return True
        except Exception:
            return False

# User Interface


def main():
    db = Database_Management()
    print("#"*40)
    print("\n")
    print(":: Student Management ::]\n")
    print("#"*40)
    print("\n")
    print("1: To Insert Data Into the Database\n")
    print("2: To Update Data In the Database\n")
    print("3: To Fetch Data from the Database by id\n")
    print("4: To Delete Data from the Database\n")
    print("5: To Fetch all the data from the database\n")
    print("6: To Quit Managing the Database\n")

    while True:
        command = int(input("Command --> "))
        print("\n")
        if command == 1:
            print("You can't change your Name later\n")
            name = input("Name: ")
            roll = int(input("Roll: "))
            dept = input("Dept: ")
            year = int(input("Year: "))
            subjects = input(
                "Enter Your Sunjects Separated by Commas: ").split(",")
            under_grad = int(input("Under_Grad --> 1 For Yes and 0 For No: "))
            data = [name, roll, dept, year, str(subjects), under_grad]
            if db.insert_data(data):
                print("Data Inserted Successfully\n")
            else:
                print("Data can't be inserted properly\n")
        elif command == 2:
            id = int(input("Enter the id whose data you want to update: "))
            print("\n")
            roll = int(input("Roll: "))
            dept = input("Dept: ")
            year = int(input("Year: "))
            subjects = input(
                "Enter Your Sunjects Separated by Spaces: ").split(" ")
            under_grad = int(input("1 For Yes and 0 For No: "))
            data = [roll, dept, year, str(subjects), under_grad]
            if db.update_data(id, data):
                print("Data Updated Successfully\n")
            else:
                print("Data Not Updated Something Went Wrong\n")
        elif command == 3:
            id = int(input("Enter the id whose data you want to fetch: "))
            print("\n")
            if db.fetch_by_id(id):
                record = db.fetch_by_id(id)
                for val in record:
                    print(f"Id: {val[0]}")
                    print(f"Name: {val[1]}")
                    print(f"Roll: {val[2]}")
                    print(f"Dept: {val[3]}")
                    print(f"Year: {val[4]}")
                    print(f"Subjects: {val[5]}")
                    Under_Grad = 'Yes' if val[6] == 1 else 'No'
                    print(f"Under_Grad: {Under_Grad}")
                    print("\n")
            else:
                print("Can't Fetch data")
        elif command == 4:
            id = int(input("Enter the id whose data you want to delete: "))
            print("\n")
            if db.delete_data(id):
                print("Successfully Deleted\n")
            else:
                print("Not Deleted\n")
        elif command == 5:
            if db.fetch_data():
                for pos, val in enumerate(db.fetch_data()):
                    print(f"Id: {val[0]}")
                    print(f"Name: {val[1]}")
                    print(f"Roll: {val[2]}")
                    print(f"Dept: {val[3]}")
                    print(f"Year: {val[4]}")
                    print(f"Subjects: {val[5]}")
                    Under_Grad = 'Yes' if val[6] == 1 else 'No'
                    print(f"Under_Grad: {Under_Grad} \n")

            else:
                print("Fetching all the data can't be done")
        elif command == 6:
            return False
        else:
            print("Wrong Choice")


if __name__ == "__main__":
    main()
