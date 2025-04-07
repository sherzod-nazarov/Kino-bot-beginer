from sqlite3 import connect, Error

def ReadAdmins():
    try:
        c = connect("kino.db")
        cursor = c.cursor()
        cursor.execute("""
            select * from admins;
            """,)
        malumot = cursor.fetchall()
        return malumot
    except (Error, Exception) as eror:
        print("eror: ", eror)
    finally:
        if c:
            cursor.close()
            c.close()



def AddAdmins(id):
    try:
        c = connect("kino.db")
        cursor = c.cursor()
        cursor.execute("""
            insert into admins(user_id) values(?)
                """, (id,))
        c.commit()
        return "bajarildi"
    except (Error, Exception) as eror:
        print("eror: ", eror)
    finally:
        if c:
            cursor.close()
            c.close()

# try:
#     c = connect("../kino.db")
#     cursor = c.cursor()
#     cursor.execute("""
#         Create table Admins(
#                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     user_id integer not null
#                    );
#             """)
#     c.commit()
# except (Error, Exception) as eror:
#     print("eror: ", eror)
# finally:
#     if c:
#         cursor.close()
#         c.close()

