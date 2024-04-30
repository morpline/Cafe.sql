import psycopg2 as pg2
name = input("Full name? - ")
phone = input("Phone Number? - ")
email = input("Email Address? - ")
import os
import dotenv
dotenv.load_dotenv()

conn = pg2.connect(os.environ.get("database"),os.environ.get("username"),os.environ.get("password"),os.environ.get("port"))
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM cafe.customers")
count = cur.fetchone()[0]
cur.execute(f"INSERT INTO cafe.customers VALUES ({count+1},'{name}','{email}','{phone}',0);")
conn.commit()
cur.execute(f"SELECT * FROM cafe.customers;")
print(cur.fetchall())