import mariadb
import sys

import tkinter as tk
from tkinter import ttk

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

# Class
class Anrede:
    def __init__(self, id, bezeichnung):
        self.id = id
        self.bezeichnung = bezeichnung
    def values(self):
        return (self.id, self.bezeichnung)
 
#get cursor
 
abfrage = conn.cursor()
abfrage.execute("SELECT * FROM anrede;")

anrede_liste = []
for row in abfrage:
    anrede = Anrede(*row)
    anrede_liste.append(anrede.values())

# Functions
def anrede_hinzufügen():
    id_anrede = anrede_liste[-1][0]
    id_anrede += 1
    anrede = str(entry_anrede.get())
    abfrage.execute("INSERT INTO anrede (ID_Anrede, Anrede) VALUES (%s, %s)",(id_anrede, anrede,))
    conn.commit()
    abfrage.execute("SELECT * FROM anrede;")
    for row in abfrage:
        anrede = Anrede(*row)
        anrede_liste.append(anrede.values())
    tree.insert("", "end", values = anrede.values())


# Tkinter

root = tk.Tk()
root.title("Anrede hinzufügen")
root.geometry("500x600")

label_anrede = tk.Label(root, text = "Neue Anrede:")
label_anrede.pack()

entry_anrede = ttk.Entry(root)
entry_anrede.pack()
anrede = str(entry_anrede.get())

button_filtern = ttk.Button(
    root,
    text = "Hinzufügen",
    command = anrede_hinzufügen
)
button_filtern.pack()

columns = ("ID_Anrede", "Anrede")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)  
    tree.column(col, anchor="center", width=140)
    abfrage = conn.cursor()
abfrage.execute("SELECT * FROM anrede;")

anrede_liste = []
for row in abfrage:
    anrede = Anrede(*row)
    anrede_liste.append(anrede.values())
    level1= tree.insert("", "end", values = anrede.values())

tree.pack(expand=True, fill="both")

root.mainloop()