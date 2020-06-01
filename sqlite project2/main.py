import sqlite3 as lite

# Functionality


class DatabaseManagement(object):
    def __init__(self):
        global con
        try:
            con = lite.connect("Youtube.db")
            with con:  # Using context manager so no need to close the database manually
                cur = con.cursor()
                cur.execute(
                    '''CREATE TABLE IF NOT EXISTS youtube_videos(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,description TEXT,tags TEXT,is_private BOOLEAN NOT NULL DEFAULT 0)''')
                con.commit()
                # If context manager is not used then we have to close the database manually using con.close()
        except Exception:
            print("Unable to create database")
    # To insert data to the database

    def insert_data(self, name, description, tags, is_private):
        try:
            con = lite.connect("Youtube.db")
            with con:  # Using context manager so no need to close the database manually
                cur = con.cursor()
                cur.execute(
                    '''INSERT INTO youtube_videos(name,description,tags,is_private) VALUES(?,?,?,?)''', (name, description, tags, is_private))
                con.commit()
                # If context manager is not used then we have to close the database manually using con.close()
                return True
        except Exception:
            return False
    # To fetch all the data from the database

    def fetch_data(self):
        try:
            con = lite.connect("Youtube.db")
            with con:  # Using context manager so no need to close the database manually
                cur = con.cursor()
                cur.execute('''SELECT * FROM youtube_videos''')
                con.commit()
                # If context manager is not used then we have to close the database manually using con.close()
                return cur.fetchall()
        except Exception:
            return False
    # To update data into the database

    def update_data(self, name, description, tags, is_private, id):
        try:
            con = lite.connect("Youtube.db")
            with con:  # Using context manager so no need to close the database manually
                cur = con.cursor()
                cur.execute('''UPDATE youtube_videos SET name = ?, description = ?,tags = ?,is_private = ? WHERE id = ?''', (
                    name, description, tags, is_private, id))
                con.commit()
                # If context manager is not used then we have to close the database manually using con.close()
                return True
        except Exception:
            return False
    # To delete data from the database

    def delete_data(self, id):
        try:
            con = lite.connect("Youtube.db")
            with con:  # Using context manager so no need to close the database manually
                cur = con.cursor()
                cur.execute('''DELETE FROM youtube_videos WHERE id=?''', (id,))
                con.commit()
                # If context manager is not used then we have to close the database manually using con.close()
                return True
        except Exception:
            return False

# User Interface


def main():
    print("#"*40)
    print("\n")
    print(":: Video Management ::")
    print("\n")
    print("#"*40)
    print("\n")
    db = DatabaseManagement()
    print("1: To insert data to the database\n")
    print("2: To fetch all data from the database\n")
    print("3: To update data into the database\n")
    print("4: To delete data from the database\n")
    print("5: To exit")
    while True:
        choice = int(input("Enter a choice: "))
        print("\n")
        if choice == 1:
            name = input("Enter the name: ")
            description = input("Type a small description of the video: ")
            tags = str(input("Enter the tags separated by spaces: ").split(" "))
            is_private = int(input("Private-->0(False) or 1(True): "))
            #data = [name, description, str_tags, is_private]
            if db.insert_data(name, description, tags, is_private):
                print("Inserted Successfuly")
            else:
                print("Not inserted somethig went wrong")
        elif choice == 2:
            if db.fetch_data():
                for val in db.fetch_data():
                    print("Video id: ", val[0])
                    print("name: ", val[1])
                    print("description: ", val[2])
                    print("tags: ", val[3])
                    private = True if val[4] else False
                    print("Private: ", private)
                    print("\n")
            else:
                print("Can not fetch data something is wrong")
        elif choice == 3:
            id = int(input("Enter the video id which you want to update: "))
            name = input("Enter the name: ")
            description = input("Type a small description of the video: ")
            tags = str(input("Enter the tags separated by spaces: ").split(" "))
            is_private = int(input("Enter 0(False) or 1(True): "))
            if db.update_data(name, description, tags, is_private, id):
                print("Updated Successfuly")
            else:
                print("Update Failed")
        elif choice == 4:
            id = int(input("Enter the video id which you want to delete: "))
            if db.delete_data(id):
                print("Deleted Successfuly")
            else:
                print("Failed to delete")
        elif choice==5:
            break
        else:
            print("Wrong Choice")


if __name__ == "__main__":
    main()
