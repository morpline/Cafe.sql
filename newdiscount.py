import psycopg2 as pg2
name = input("Name of Discount? - ")
discount = input("Percent discount? - ")
expires = input("Expires? - ")
donewithproducts = False
products = "{"
while(not donewithproducts):
    s = input("Add product id or input SKIP to go onto the next step")
    if(s == "SKIP"):
        donewithproducts = True
    else:
        if not products == "{":
            products +=", "
        if not (int(s)==None):
            products+=f'"{s}"'
        else:
            print("Not a number, try again")
products+="}"
conn = pg2.connect(database='type3',user="postgres",password="ethan",port=19026)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM cafe.discounts")
count = cur.fetchone()[0]
cur.execute(f"INSERT INTO cafe.discounts VALUES ({count+1},'{name}','{discount}','{expires}', '{products}');")
conn.commit()
cur.execute(f"SELECT * FROM cafe.discounts;")
print(cur.fetchall())