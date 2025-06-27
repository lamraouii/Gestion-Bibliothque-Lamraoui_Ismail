

class LivreIndisponibleError (Exception) :
    def __init__(self, message,isbn=None, titre=None):
        super().__init__(message)
        self.Isbn=isbn
        self.Titre=titre

    
class QuotaEmpruntDepasseError (Exception):
    def __init__(self, message,id=None, titre=None):
        super().__init__(message)
        self.Id=id
        self.Titre=titre


class MembreInexistantError (Exception):
    def __init__(self, message,id=None, nom=None):
        super().__init__(message)
        self.Id=id
        self.Titre=nom


class LivreInexistantError (Exception):
    pass
    



























# import os

# print(os.getcwd())
# print(os.path.abspath(__file__))
# ISBN.strip().lower()          /// strip: t7yeed espace---lower: ktrd miniscule kolshi
#datetime.now().strftime("%Y-%m-%d")     ////   datetime import  --  .now Ñactuell -- strftime(format): katsayeb lformat mzyaan
# print(r"\n")
# date="fff"
# b="dddd"
# data=[date,b+"\n"]
# historique_fil = open("..\data\livre.txt","a")
# historique_fil.writelines(data)
# historique_fil.close()

# import json

# with open(r"C:\Users\ismai\DevProjects\BibPython\data\livre.json","r") as f:
#     moonvar= json.load(f)
#     f.close()
# with open(r"C:\Users\ismai\DevProjects\BibPython\data\membre.json","w") as f:
#     dt=[
#   {
#     "isbn": "978123456",
#     "titre": "saheh",
#     "auteur": "ana",
#     "annee": 2040,
#     "genre": "fiqh",
#     "statut": "disponible"
#   },
#   {
#     "isbn": "9787891011",
#     "titre": "rasa2il",
#     "auteur": "farid",
#     "annee": 2003,
#     "genre": "dini",
#     "statut": "emprunte"
#   }
# ]

#     json.dump(dt,f,indent=2)
