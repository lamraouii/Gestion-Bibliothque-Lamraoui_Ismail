from Livre import Livre
from Membre import Membre
from Bibliotheque import Bibliotheque
from Exceptions import *
maktaba= Bibliotheque()
# smail= Membre(1,"smail")
# mehdi= Membre(2,"mehdi")
# amine= Membre(3,"amine")

# kessa= Livre("20","iran","adro3i","chi3i",2000)
# kes= Livre(10,"sran","abde","chi3i",2000)
# ktab= Livre("30","sran","abde","chi3i",2000)

# maktaba.AjouterLivre(kessa)
# maktaba.AjouterLivre(ktab)
# maktaba.AjouterLivre(kes)

# maktaba.AjouterMembre(smail)
# maktaba.AjouterMembre(mehdi)
# maktaba.AjouterMembre(amine)
# maktaba.Emprunter_livre(bendamo,kessa)

try:
    # maktaba.AjouterLivre(kes)
    maktaba.charger_data()
    # print(maktaba.getLivres("60"))
    # maktaba.Emprunter_livre(maktaba.getMembbres(4),maktaba.getLivres(10))
    maktaba.Emprunter_livre(maktaba.getMembbres(4),maktaba.getLivres("30"))
    maktaba.Emprunter_livre(maktaba.getMembbres(1),maktaba.getLivres("10"))
    maktaba.Emprunter_livre(maktaba.getMembbres(2),maktaba.getLivres("50"))
    maktaba.Emprunter_livre(maktaba.getMembbres(3),maktaba.getLivres("20"))
    maktaba.sauvegarder_data()
    # maktaba.Emprunter_livre(maktaba.getMembbres(5),)
    # maktaba.genre_stats()

    maktaba.stats_30_days()   


    # maktaba.stats_30_days()
    
    # maktaba.Rendre_livre(bendamo,kes)
    # maktaba.sauvegarder_data()
except Exception as e:
    print(f"0 {e}")
