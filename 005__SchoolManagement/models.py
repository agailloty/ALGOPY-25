from dataclasses import dataclass
from datetime import datetime

@dataclass
class Eleve:
    id : int
    nom : str
    prenom : str
    date_naissance : datetime
    adresse : str
    classe : str
    telephone : str
    email : str
    photo : bytes
    
