import psycopg2 as pg2
import os
import dotenv
dotenv.load_dotenv()
inputs = {}
def take_inputs (data_name):
    inputs[data_name]=input(f"Input {data_name} - ")
data_needed = [
    "name",
    "customerid"
]
for f in data_needed:
    take_inputs(f)
donewithproducts = False
products = []
pstring = "{"
while(not donewithproducts):
    s = input("Add product id or press enter to go onto the next step")
    if(s == ""):
        donewithproducts = True
    else:
        print("s", s, int(s))
        if not pstring == "{":
            pstring +=", "
        if not (int(s)==None):
            products.append(int(s))
            pstring+=f'{s}'
        else:
            print("Not a number, try again")
pstring+="}"
print(pstring, products)
cost = 0
conn = pg2.connect(os.environ.get("database"),os.environ.get("username"),os.environ.get("password"),os.environ.get("port"))
cur = conn.cursor()
discounts = []
dstring = "{"
for p in products:
    print("product in list ",type(p),p)
    if (type(p).is_integer ):
        cur.execute(f"SELECT price FROM cafe.menu WHERE _id={p};")
        q = cur.fetchone()
        print(q[0])
        c = float(q[0])
        cur.execute(f"SELECT type, _id FROM cafe.discounts WHERE NOT (items#{p} = 0);")
        d = cur.fetchall()
        print(d)
        for discount in d:
            if not dstring == "{":
                dstring +=", "
            c*=((100-float(discount[0]))/100)
            dstring+=str(discount[1])
        cost+=c
dstring+="}"
print("dstring",dstring)
cur.execute("SELECT COUNT(*) FROM cafe.orders")
count = cur.fetchone()[0]
query = f"INSERT INTO cafe.orders VALUES ({count+1},'{inputs["name"]}',{inputs["customerid"]},'{pstring}','{dstring}',{cost});"
cur.execute(query)
conn.commit()
if not(inputs["customerid"] == ""):
    cur.execute(f"SELECT rewardpoints FROM cafe.customers WHERE _id = {inputs["customerid"]}")
    points = cur.fetchone()[0] + cost
    cur.execute(f"UPDATE cafe.customers SET rewardpoints = {int(points*100)} WHERE _id = {inputs["customerid"]}")
    conn.commit()
