import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="fxizz<1>",
    host="localhost",
    port="5432",
)
print("Connected Successfully")

cur = conn.cursor()
cur.execute("SELECT * FROM CAR;")
rows = cur.fetchall()

for row in rows:
    print(f"Company: {row[0]}\n" f"Name: {row[1]}\n" f"Price: {row[2]}\n")
