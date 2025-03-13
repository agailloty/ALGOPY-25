CREATE_TABLE_ELEVE = """
CREATE TABLE IF NOT EXISTS eleves (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    date_naissance DATE NOT NULL,
    classe TEXT NOT NULL,
    adresse TEXT,
    email TEXT UNIQUE,
    telephone TEXT,
    photo BLOB
);
"""