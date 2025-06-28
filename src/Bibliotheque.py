from Livre import Livre
from Membre import Membre
from Livre import Status
import json
from Exceptions import *
from datetime import datetime,timedelta
from matplotlib import pyplot as plt


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
            self.Save_historique(datetime.now().strftime("%Y-%m-%d"),livre,membre,"emprunt")
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
            if livre._genre not in genres_analyseur:
                genres_analyseur[livre._genre]=1
            else:
                genres_analyseur[livre._genre] +=1
        values= list(genres_analyseur.values())
        keys=list(genres_analyseur.keys())
        # it would be better ila sortitu(rtebto)
        plt.pie(values,labels=keys,autopct='%2.1f%%') 
        # autocapts ky3te this exmpl 18.2%
        plt.title(r"% de livres par genre")
        plt.show()

    def top_10_authors(self):
        all_authors={}
        with open (r"C:\Users\ismai\DevProjects\BibPython\data\historique.csv","r") as f:
            line =f.readline()
            while line:
                elem= line.split(";") # lines mfar9in b ;
                if len(elem) != 4 and elem[3].strip() != "emprunt":    # bach n assuriw bli kayni 4 dles champs
                    line =f.readline()
                    continue
                else:
                    temp_isbn=elem[1]
                author=self.__listLivres[temp_isbn]._auteur
                if author not in all_authors:
                    all_authors[author]=1
                else: 
                    all_authors[author] +=1
                line =f.readline()
        top_authors=sorted(all_authors.items(), key=lambda x: x[1], reverse= True) #return a list of tupels not a dict 
        # lamda x:x[1] bach nsortiw b lvalues machi bnames d authors
        top_authors=top_authors[:10]
        ky,vl=zip(*top_authors)   # unzip the list 
        plt.bar(ky,vl)
        # plt.xticks(rotation=45)  the plot in rotated (i9der ikono smawat twal)
        plt.title("Top 10 des auteurs les plus populaires")
        plt.show()
            
    def stats_30_days (self):
        today= datetime.today()
        last_30_days=[]
        for i in range(0,30):
            temp_day= today - timedelta(days=i)
            last_30_days.append(temp_day.strftime("%Y-%m-%d"))
        with open(r"C:\Users\ismai\DevProjects\BibPython\data\historique.csv","r") as f :
            line=f.readline()
            last_30_day={d: 0 for d in last_30_days} # bach ta ila kan nhar khawi ikon fih 0
            while line:
                elem= line.split(";")

                if elem[3].strip() != "emprunt" or elem[0] not in last_30_days :
                    line = f.readline()# to read thenext line before going to next iteration
                    continue
                else:
                    if elem[0] not in last_30_day:
                        last_30_day[elem[0]]=1
                    else:
                        last_30_day[elem[0]] +=1

                line=f.readline()
        plt.figure()
        plt.plot(last_30_days,[last_30_day[d] for d in last_30_days])
        plt.xticks(rotation=45)
        plt.title("Activité des emprunts (30 derniers jours)")
        plt.show()

