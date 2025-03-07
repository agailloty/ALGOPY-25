import sqlite3
import pandas as pd
import models

def init_database():
    with sqlite3.connect("budget.db") as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS budget (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT,
                    categorie TEXT,
                    montant REAL)''')
        conn.commit()

# Charger les données depuis la base de données
def load_data():
    with sqlite3.connect("budget.db") as conn:
        return pd.read_sql("SELECT * FROM budget", conn)

def save_data(transaction : models.Transaction):
    with sqlite3.connect("budget.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO budget (type, categorie, montant) VALUES (?, ?, ?)", (transaction.type, transaction.categorie, transaction.montant))
        conn.commit()

def delete_item(id : int):
    with sqlite3.connect("budget.db") as conn:
        c = conn.cursor()
        c.execute(f"DELETE FROM budget WHERE id = {id}")
        conn.commit()

# Importer les données depuis un fichier CSV
def import_csv(file):
    return pd.read_csv(file)