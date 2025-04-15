import mariadb
import sys
 
#connect mariadb
 
try:
    conn = mariadb.connect(
        user = "na_ng",
        password = "botanical",
        host = "127.0.0.1",
        port = 3307,
        database = "schlumpfshop3")
 
except mariadb.Error as e:
    print(f"Error connecting to MariaDB PLatform: {e}")
    sys.exit(1)
 
#get cursor
 
cur = conn.cursor()

id_anrede = 3

print("Geben Sie 'x' ein, wenn Sie mit der Eingabe fertig sind.")
anrede = input("Bitte geben Sie eine neue Anrede ein: ")

while anrede != "x":
    anrede = input("Bitte geben Sie eine neue Anrede ein: ")
    cur.execute("INSERT INTO anrede (ID_Anrede, Anrede) VALUES (%s, %s)",(id_anrede, anrede,))
    id_anrede += 1
    conn.commit()