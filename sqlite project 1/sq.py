import sqlite3 as lite
# Functionality of the Database
class DatabaseManagement(object):
    def __init__(self):
        global con
        try:
            con=lite.connect("courses.db")
            with con:
                    cur=con.cursor()
                    cur.execute('''CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,description TEXT,price TEXT NOT NULL,is_private BOOLEAN NOT NULL DEFAULT 1)''')
                    con.commit()
                    print("Database created successfuly")
        except Exception:
            print("Unable to create database")
    #TODO: To insert data to the database
    def insert_data(self,data):
        try:
            con=lite.connect("courses.db")
            with con: #Using context manager so no need to close the database manually
                cur=con.cursor()
                cur.execute('''INSERT INTO course(name,description,price,is_private) VALUES(?,?,?,?)''',data)
                con.commit()
                return True
                #If context manager is not used we need to close the database manually using con.close()
        except Exception:
            return False
    # TODO: To fetch all data from the database
    def fetch_data(self):
        try:
            con=lite.connect("courses.db")
            with con: #Using context manager so we dont need to close the database manually
                cur=con.cursor()
                cur.execute('''SELECT * FROM course''')
                return cur.fetchall()
                #If context manager is not used then we need to close the database using con.close() manually
        except Exception:
            return False
    # TODO: To delete data from the database
    def delete_data(self,id):
        try:
            con=lite.connect("courses.db")
            with con: #Using context manager so we dont need to close the database manually
                cur=con.cursor()
                cur.execute('''DELETE FROM course WHERE id=?''',(id,))
                con.commit()
                return True
                #If context manager is not used then we need to close the database manually using con.close()
        except Exception:
            return False
#User Interface
def main():
    print("#"*40)
    print(":: COURSE MANAGEMENT ::\n")
    print("#"*40)
    print("1 : To insert data to the database\n")
    print("2 : To fetch data from the database\n")
    print("3 : To delete data from the database\n")
    db=DatabaseManagement()
    choice=int(input("Enter your choice: "))
    print("\n")
    if choice==1:
        name=input("Enter the name of thr course: ")
        description=input("Write a small description about your course: ")
        price=input("Enter the price of the course: ")
        is_private=input("Is private True(1) or False(0): ")
        data=(name,description,price,is_private)
        if db.insert_data(data):
            print("Inserted Successfuly")
        else:
            print("Not Inserted Something Went Wrong")
    elif choice==2:
        if db.fetch_data():
            for pos,val in enumerate(db.fetch_data()):
                print("Course id: ",val[0])
                print("Name: ",val[1])
                print("Description: ",val[2])
                print("Price: ",val[3])
                private=True if val[4] else False
                print("Is Private: ",private)
                print("\n")
        else:
            print("Fetching the data is unsuccessful")
    elif choice==3:
        id=int(input("Enter the course id you want to delete: "))
        if db.delete_data(id):
            print("Deleted successfuly")
        else:
            print("Not deleted something went wrong")
    else:
        print("Wrong Choice")
if __name__=="__main__":
    main()
