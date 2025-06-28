from enum import Enum
class Status(Enum):
    Dispo="disponible"
    NotDispo="emprunte"


class Livre :

    def __init__ (self,ISBN,titre,auteur,genre,annee,status=Status.Dispo):
        self._isbn=str(ISBN)   
        self._titre=titre
        self._auteur=auteur
        self._genre=genre
        self._status=status
        if annee < 0 :
            annee=0
        self._annee=annee
        
        

    def is_dispo(self):
        if self._status ==Status.Dispo:
            return True
        else: return False
    
    def __str__(self):
        return f"book: {self._titre}"


