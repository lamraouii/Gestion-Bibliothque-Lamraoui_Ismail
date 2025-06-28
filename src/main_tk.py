import tkinter as tk
from  tkinter import messagebox, ttk
from Bibliotheque import Bibliotheque


Makataba= Bibliotheque()
Makataba.charger_data()

root= tk.Tk()
root.title("emprunter!")
root.geometry("400x300")
# root.state("zoomed")

id_label= tk.Label(root,text="Your Id:")
id_label.grid(row=0, column=0, padx=10, pady=10)

id_entry= tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=10)

isbn_label= tk.Label(root,text="book isbn:")
isbn_label.grid(row=1, column=0, padx=10, pady=10)

isbn_entry= tk.Entry(root)
isbn_entry.grid(row=1, column=1, padx=10, pady=10)

def emprunter_action():
    id_val= id_entry.get()
    isbn_val=isbn_entry.get()
    try:
        Makataba.Emprunter_livre(Makataba.getMembbres(int(id_val)),Makataba.getLivres(str(isbn_val)))
        messagebox.showinfo("well done","livre emprunte")
        Makataba.sauvegarder_data()
    except Exception as e:
        messagebox.showerror("Erreur",f"Couldn't emprunte {str(e)}")

emprunt_butn=tk.Button(root,text="Emprunter",command=emprunter_action)
emprunt_butn.grid(row=2,column=2, columnspan=2, pady=10)

#####################rendre#################
def rendre_action():
    id_val=id_entry.get()
    isbn_val=isbn_entry.get()
    try:
        Makataba.Rendre_livre(Makataba.getMembbres(int(id_val)),Makataba.getLivres(str(isbn_val)))
        messagebox.showinfo("well Done","the book returned sccflly")
        Makataba.sauvegarder_data()
    except Exception as e:
        messagebox.showerror("Erreur",f"failed to return {str(e)}")


retourner_btn= tk.Button(root,text="Rendre",command=rendre_action)
retourner_btn.grid(row=2,column=1,pady=10)


########################## affiche livres##########

def affiche_lvr_action():
    for row in lvr_table.get_children():
        lvr_table.delete(row)
    for book in Makataba._Bibliotheque__listLivres.values():
        lvr_table.insert("","end",values=(
            book._isbn,
            book._titre,
            book._auteur,
            book._genre,
            book._annee,
            book._status.value
        ))# insert ktdkhel ftable

affich_livrs= tk.Button(root,text="Afficher Livres",command=affiche_lvr_action)
affich_livrs.grid(row=3, column=1, pady=10)

lvr_table= ttk.Treeview(root,columns=("ISBN", "Titre", "Auteur", "Genre", "Année", "Statut"), show="headings")
#cmya dles columns and show:"headings" 
lvr_table.grid(row=4,column=0,columnspan=2, padx=10,pady=10)
for col in ("ISBN", "Titre", "Auteur", "Genre", "Année", "Statut"):
    lvr_table.heading(col, text=col)
    lvr_table.column(col, width=100)


root.mainloop()