import os
import sqlite3
dbAddress = "example.db"
# ---- creating a table, if not exists
if not os.path.exists("example.db"): 
    try: 
        os.remove(dbAddress)
    except Exception:
        print "file does not exist to remove"
    conn = sqlite3.connect(dbAddress)
    c = conn.cursor()
    c.execute('create table Persons (id int, name text, city text)')
else:
    os.remove(dbAddress)
    conn = sqlite3.connect(dbAddress)
    c = conn.cursor()
    c.execute('create table Persons (id int, name text, city text)')


names = ["behzad", "molly", "amir", "khoda", "others"]
city = ["ramsar", "portland", "kerman", "homeless", "world"]
ltableInfo = zip(range(len(names)), names,city)


for element in ltableInfo:
    c.execute('insert into Persons VALUES '+ str(element))
conn.commit()
conn.close()

