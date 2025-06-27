from Livre import Livre
from Membre import Membre
from Livre import Status
import json
from datetime import datetime #hadi dual curent date
from Exceptions import *
import matplotlib.pyplot as plt
# definitha brra ???? bch nst3mlha west llclass kima bghit 



class Bibliotheque:
    def __init__(self):
        self.__listLivres={}
        self.__listMembres={}

    def AjouterLivre(self,livre):
        if livre._isbn not in self.__listLivres:
            self.__listLivres[livre._isbn]=livre
            # print(livre)
            # print(self.__listLivres)
        else: return 1
        
    
    def AjouterMembre(self,membre):
        if membre._id not in self.__listMembres:
            self.__listMembres[membre._id]=membre
            # print(membre)
            # print(self.__listMembres)
        else: return 1

    def Save_historique(self,date,livre,membre,action): # hadi function machi methode ghtst3mel ghir hna west les fcts lkhren
        data=[date,str(livre._isbn),str(membre._id),action]
        with  open(r"C:\Users\ismai\DevProjects\BibPython\data\historique.csv","a") as historique_file: #hadik r bhal \\n bach myw93ch ghalat flcode
            historique_file.writelines(";".join(data)+"\n") # ;.join ktjm3 binathum b ";"
        # historique_file.close()

    def Emprunter_livre(self,membre,livre):
        # check lmembre wach kayen
        if membre._id not in self.__listMembres:
            raise MembreInexistantError("the following membre doesnt exist:",membre._id,membre._nom )
        # livre wach kayen
        elif  livre._isbn not in self.__listLivres:
            raise LivreInexistantError("the following livre doesnt exist", livre._isbn,livre._titre)
        #wach dispo
        elif not livre.is_dispo():
            raise LivreIndisponibleError("the following livre isn't dispo fr the mmnt", livre._isbn,livre._titre) 
        #wach lmmbre i9dr ykri
        elif not membre.PeutEmprunte():
            raise QuotaEmpruntDepasseError("the following membre cant emprunt", membre._id)
        
        #### if all is good 
        else:
            livre._status=Status.NotDispo  #hadi enum ghir bach nbsst
            membre._livres_empruntes.append(livre)
            self.Save_historique(datetime.now().strftime("%Y-%m-%d"),livre,membre,"emprunte")
            # print("lktab tzad")

    def Rendre_livre(self,membre,livre):
        if membre._id not in self.__listMembres:
            raise MembreInexistantError("the following membre doesnt exist:",membre._id,membre._nom )
        # livre wach kayen
        elif  livre._isbn not in self.__listLivres:
            raise LivreInexistantError("the following livre doesnt exist", livre._isbn,livre._titre)
        
        elif livre not in membre._livres_empruntes:
            raise LivreInexistantError("the following livre doesnt exist in the membre list empuntes", livre._isbn,livre._titre)
        
        else:
            livre._status=Status.Dispo  #redinah dispo
            membre._livres_empruntes.remove(livre)
            self.Save_historique(datetime.now().strftime("%Y-%m-%d"),livre,membre,"Rendu")
            # print("lktab t7yed") 

    def charger_data(self):
        with open(r"C:\Users\ismai\DevProjects\BibPython\data\livre.json","r") as f:
            livrdata= json.load(f)
            for i in livrdata:
                temp_livre= Livre(i["isbn"], i["titre"],i["auteur"],i["genre"],i["annee"],i["status"])
                self.__listLivres[i["isbn"]]=temp_livre
        
        with open(r"C:\Users\ismai\DevProjects\BibPython\data\membre.json","r") as f:
            membrdata= json.load(f)
            for i in membrdata:
                temp_membre= Membre(i["id"],i["nom"])
                for j in i["livres_empruntes"]: # j represent alors le isbn
                    # var=i["livres_empruntes"][j] ///false cz i[livre_emprnt] machi dict its a list 
                    livre1= self.__listLivres[j]
                    temp_membre._livres_empruntes.append(livre1)
                


    def sauvegarder_data(self):
        with open(r"C:\Users\ismai\DevProjects\BibPython\data\livre.json","w") as f:
            livre_data=[]
            for i in self.__listLivres:
                temp_livre= self.__listLivres[i]
                data={
                    "isbn":temp_livre._isbn,
                      "titre":temp_livre._titre,
                      "auteur":temp_livre._auteur,
                      "genre":temp_livre._genre,
                      "annee":temp_livre._annee,
                      "status":temp_livre._status
                      }
                livre_data.append(data)
            json.dump(livre_data,f,indent=2)

        with open(r"C:\Users\ismai\DevProjects\BibPython\data\membre.json","w") as f:
            membre_data=[]
            for i in self.__listMembres:
                temp_membre= self.__listMembres[i]
                emprunts_isbn=[] # bach ncollectiw only isbns of livre
                for lvr_empr in temp_membre._livres_empruntes:
                    emprunts_isbn.append(lvr_empr._isbn)
                data={
                      "id":temp_membre._id,
                      "nom":temp_membre._nom,
                      "livres_empruntes": emprunts_isbn
                      }
                membre_data.append(data)
            json.dump(membre_data,f,indent=2)



    def genre_stats(self):
        genres_analyseur={}
        for livre in self.__listLivres.values():
            if livre.genre not in genres_analyseur:
                genres_analyseur[livre.genre]=1
            else:
                genres_analyseur[livre.genre] +=1
        values= list(genres_analyseur.values())
        keys=list(genres_analyseur.keys())
        # it would be better ila sortitu(rtebto)
        plt.pie(values,labels=keys,autopct='%2.1f%%') 
        # autocapts ky3te this exmpl 18.2%
        plt.title(r"% de livres par genre")
        plt.show()

    # def top_10_authors(self):
    #     all_authors={}
    #     with open (r"C:\Users\ismai\DevProjects\BibPython\data\historique.csv","r") as f:
    #         for lines in 
    #         data=f.readline()
    #         if 

        
        
        
        

        