import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "fxizz<1>", host = "localhost", port = "5432")
print("Connected Successfully")

cur = conn.cursor()
cur.execute('''create table CAR
            (Company    TEXT    NOT NULL,
            Name    TEXT    NOT NULL,
            price   INT NOT NULL)''')
print("Table create successfully")
conn.commit()
conn.close()