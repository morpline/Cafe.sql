import psycopg2 as pg2
import os
import sys
conn = pg2.connect(database='type3',user="postgres",password="ethan",port=19026)
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