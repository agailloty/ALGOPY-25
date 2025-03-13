import sqlite3
import queries
from models import Eleve

DB_NAME = "ecole.db"

def init_database():
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute(queries.CREATE_TABLE_ELEVE)
        conn.commit()


def create_eleve(eleve : Eleve):
    with sqlite3.connect(DB_NAME) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO eleves (nom, prenom, date_naissance, adresse, telephone, email, classe) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                  (eleve.nom, eleve.prenom, eleve.date_naissance, 
                   eleve.adresse, eleve.telephone, eleve.email, eleve.classe))
        conn.commit()

def read_all_eleve() -> list[Eleve]:
    with sqlite3.connect("ecole.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM eleves")
        res = c.fetchall()

        all_eleves = []

        for line in res:
            eleve = Eleve(
                nom = line[1],
                prenom= line[2],
                date_naissance= line[3],
                classe = line[4],
                adresse= line[5],
                email= line[6],
                telephone= line[7],
                photo= None
            )
            all_eleves.append(eleve)
    return all_eleves

def read_eleve(id : int) -> Eleve:
    pass


def update_eleve(eleve : Eleve):
    pass

def delete_eleve(id : int):
    pass