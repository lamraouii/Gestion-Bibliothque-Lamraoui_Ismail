from Livre import Livre
from Membre import Membre
from Bibliotheque import Bibliotheque

maktaba= Bibliotheque()
bendamo= Membre(1,"smail")
bendam= Membre(2,"mehdi")
benda= Membre(3,"amine")

kessa= Livre(20,"iran","adro3i","chi3i",2000)
kes= Livre(10,"sran","abde","chi3i",2000)
ktab= Livre(30,"sran","abde","chi3i",2000)

# maktaba.AjouterLivre(kessa)

# maktaba.AjouterLivre(ktab)
# maktaba.AjouterMembre(bendamo)
# maktaba.AjouterMembre(bendam)
# maktaba.AjouterMembre(benda)
# maktaba.Emprunter_livre(bendamo,kessa)
try:
    maktaba.AjouterLivre(kes)
    # maktaba.Rendre_livre(bendamo,kes)
except ValueError as e:
    print(f"0 {e}")
