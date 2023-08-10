import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="fxizz<1>", host="localhost", port="5432")

print("Successfully connected to the database")
cur = conn.cursor()

cur.execute("INSERT INTO CAR (Company, Name, price) VALUES ('lamborghini', 'lamborghini_sto', 350000)")
cur.execute("INSERT INTO CAR (Company, Name, price) VALUES ('ford', 'ford_raptor', 100000)")
cur.execute("INSERT INTO CAR (Company, Name, price) VALUES ('bugatti', 'bugatti_hiron', 5000000)")
cur.execute("INSERT INTO CAR (Company, Name, price) VALUES ('koenigsegg', 'koenigsegg_jesko', 4000000)")

conn.commit()
print("Records created successfully")
conn.close()