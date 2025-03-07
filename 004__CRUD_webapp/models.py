from dataclasses import dataclass

@dataclass
class Transaction:
    type : str
    categorie : str
    montant : float