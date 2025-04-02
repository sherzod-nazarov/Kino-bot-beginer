from sqlite3 import Error, connect


def AddFilm(name, description, url):
    try:
        c = connect("kino.db")
        cursor = c.cursor()
        cursor.execute("""
            insert into Kinolar(name, discription, url) values(?, ?, ?)
                """, (name, description, url))
        c.commit()
        return "bajarildi"
    except (Error, Exception) as eror:
        print("eror: ", eror)
    finally:
        if c:
            cursor.close()
            c.close()

# print(AddFilm(name="Talsa Qiroli ", description="""👑 Talsa Qiroli 

# 🎬  2 fasl 5 qism 
# 🇺🇿 Tarjima - Oʻzbek 
# 🎥 Sifati - HD 720 p
# 🗓 Sanasi - 2024 yil""", url="https://t.me/Javlon6ek/1243"))


def ReadFilm(id):
    try:
        c = connect("kino.db")
        cursor = c.cursor()
        cursor.execute("""
            select * from kinolar where id = ?
            """, (id))
        malumot = cursor.fetchone()
        return malumot
    except (Error, Exception) as eror:
        print("eror: ", eror)
    finally:
        if c:
            cursor.close()
            c.close()




def BarchaKinolar():
    try:
        c = connect("kino.db")
        cursor = c.cursor()
        cursor.execute("""
            select id from kinolar
            """)
        malumot = cursor.fetchall()
        kino_idlar = []
        for i in malumot:
            kino_idlar.append(str(i[0]))
        return kino_idlar
    except (Error, Exception) as eror:
        print("eror: ", eror)
    finally:
        if c:
            cursor.close()
            c.close()




# try:
#     c = connect("kino.db")
#     cursor = c.cursor()
#     cursor.execute("""
#         Create table Kinolar(
#                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                    NAME TEXT NOT NULL, 
#                    DISCRIPTION TEXT NOT NULL,
#                    URL TEXT NOT NULL
#                    );
#             """)
#     c.commit()
# except (Error, Exception) as eror:
#     print("eror: ", eror)
# finally:
#     if c:
#         cursor.close()
#         c.close()
    
