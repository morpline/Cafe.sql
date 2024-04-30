import psycopg2 as pg2
import os
import dotenv
dotenv.load_dotenv()

conn = pg2.connect(os.environ.get("database"),os.environ.get("username"),os.environ.get("password"),os.environ.get("port"))
cur = conn.cursor()
with open("./cafe-setup.sql") as sql:
    s = sql.read()
    print(s)
    cur.execute(s)
    conn.commit()
if input("Add data y/n :") == "y":
    with open("./addmenu.sql") as sql:
        s = sql.read()
        print(s)
        cur.execute(s)
        conn.commit()