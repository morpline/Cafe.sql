import psycopg2 as pg2
name = input("Full name? - ")
phone = input("Phone Number? - ")
email = input("Email Address? - ")
conn = pg2.connect(database='type3',user="postgres",password="ethan",port=19026)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM cafe.customers")
count = cur.fetchone()[0]
cur.execute(f"INSERT INTO cafe.customers VALUES ({count+1},'{name}','{email}','{phone}',0);")
conn.commit()
cur.execute(f"SELECT * FROM cafe.customers;")
print(cur.fetchall())