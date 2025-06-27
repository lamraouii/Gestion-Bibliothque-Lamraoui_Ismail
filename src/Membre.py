from Livre import Livre

class Membre:
    
    def __init__(self,ID,nom,livres_empruntes=[]):
        self._id=ID
        self._nom=nom
        self._livres_empruntes=livres_empruntes
        
    def nombreLivre(self):
        return len(self._livres_empruntes)
    
    def PeutEmprunte (self):
        if self.nombreLivre() <=5:
            return True
        else: return False

    def __str__(self):
        return f"the membre {self._nom}"