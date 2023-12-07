class Livre:
    def __init__(self, titre, auteur, categorie):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.emprunte_par = None

    def disponible(self):
        return self.emprunte_par is None

    def emprunter(self, utilisateur):
        if self.disponible():
            self.emprunte_par = utilisateur
            return True
        else:
            return False

    def retourner(self):
        self.emprunte_par = None

class LivreRomance(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Romance")

class LivreFiction(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Fiction")
    
class LivreNonFiction(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Non-Fiction")

class LivreHorreur(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Horreur")

class LivreBiographie(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Biographie")

class LivreAutobiographie(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Autobiographie")

class LivreScienceFiction(Livre):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur, "Science fiction")
        





class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
class UtilisateurMineur(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.autorisation_parentale = False

class UtilisateurMajeur(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)
        self.autorisation_parentale = True



class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def retirer_livre(self, livre):
        if livre in self.livres:
            self.livres.remove(livre)

    def enregistrer_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)
        
    def livres_par_categorie(self, categorie):
        livres_par_cat = [livre for livre in self.livres if livre.categorie == categorie]
        if livres_par_cat:
            print(f"Liste des livres dans la catégorie '{categorie}':")
            for livre in livres_par_cat:
                print(f"- {livre.titre} par {livre.auteur}")
        else:
            print(f"Aucun livre trouvé dans la catégorie '{categorie}'.")
            
    def emprunter_livre(self, livre, utilisateur):
        if livre.emprunter(utilisateur):
            print(f"L'utilisateur {utilisateur.prenom} {utilisateur.nom} a emprunté le livre {livre.titre} par {livre.auteur}.")
            
        else:
            print(f"Le livre {livre.titre} par {livre.auteur} n'est pas disponible.")
            
    def retourner_livre(self, livre):
        livre.retourner()
    
    def afficher_livres_disponibles(self):
        livres_disponibles = [livre for livre in self.livres if livre.disponible()]
        if livres_disponibles:
            print("Liste des livres disponibles :")
            for i, livre in enumerate(livres_disponibles):
                print(f"{i+1}. {livre.titre} par {livre.auteur}")
        else:
            print("Aucun livre disponible.")
            
    def afficher_livres_empruntes(self):
        livres_empruntes = [livre for livre in self.livres if not livre.disponible()]
        if livres_empruntes:
            print("Liste des livres empruntés :")
            for i, livre in enumerate(livres_empruntes):
                print(f"{i+1}. {livre.titre} par {livre.auteur}")
        else:
            print("Aucun livre emprunté.")
            
    def afficher_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(f"- {utilisateur.prenom} {utilisateur.nom}")

def choisir_categorie():
    print("Choisissez une catégorie :")
    print("1. Fiction")
    print("2. Non-Fiction")
    print("3. Autobiographie")
    print("4. Biographie")
    print("5. Horreur")
    print("6. Romance")
    print("7. Science fiction")
    choix = input("Votre choix : ")
    
    if choix == "1":
        return "Fiction"
    elif choix == "2":
        return "Non-Fiction"
    elif choix == "3":
        return "Autobiographie"
    elif choix == "4":
        return "Biographie"
    elif choix == "5":
        return "Horreur"
    elif choix == "6":
        return "Romance"
    elif choix == "7":
        return "Science fiction"
    else:
        print("Choix invalide !")
        return choisir_categorie()


    # ... d'autres méthodes pour gérer les emprunts, les retours, etc.

# Utilisation d'un dictionnaire pour simuler le "switch"
actions = {
    'ajouter_livre': Bibliotheque.ajouter_livre,
    'retirer_livre': Bibliotheque.retirer_livre,
    'enregistrer_utilisateur': Bibliotheque.enregistrer_utilisateur,
    # Ajoutez d'autres actions ici
}

biblio = Bibliotheque()

while True:
    print("Que voulez-vous faire ?")
    print("1. Ajouter un livre")
    print("2. Retirer un livre")
    print("3. Afficher les livres par catégorie")
    print("4. Enregistrer un utilisateur")
    print("5. Emprunter un livre")
    print("6. Retourner un livre")
    print("7. Quitter")
    choix = input("Votre choix : ")
    
    if choix == "1":
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        categorie = choisir_categorie()  # Appel de la fonction pour choisir la catégorie
        if categorie == "Fiction":
            livre = LivreFiction(titre, auteur)
        elif categorie == "Non-Fiction":
            livre = LivreNonFiction(titre, auteur)
        elif categorie == "Autobiographie":
            livre = LivreAutobiographie(titre, auteur)
        elif categorie == "Biographie":
            livre = LivreBiographie(titre, auteur)
        elif categorie == "Horreur":
            livre = LivreHorreur(titre, auteur)
        elif categorie == "Romance":
            livre = LivreRomance(titre, auteur)
        elif categorie == "Science fiction":
            livre = LivreScienceFiction(titre, auteur)
        else:
            print("Catégorie invalide !")
            continue
        
        biblio.ajouter_livre(livre)  # Ajout du livre créé à la bibliothèque
        print("Livre ajouté !")
        print(f"Nombre de livres de la catégorie {categorie} : {len([livre for livre in biblio.livres if livre.categorie == categorie])}")

    elif choix == "2":
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        categorie = choisir_categorie() 
        if categorie == "Fiction":
            livre = LivreFiction(titre, auteur)
        elif categorie == "Non-Fiction":
            livre = LivreNonFiction(titre, auteur)
        elif categorie == "Autobiographie":
            livre = LivreAutobiographie(titre, auteur)
        elif categorie == "Biographie":
            livre = LivreBiographie(titre, auteur)
        elif categorie == "Horreur":
            livre = LivreHorreur(titre, auteur)
        elif categorie == "Romance":
            livre = LivreRomance(titre, auteur)
        elif categorie == "Science fiction":
            livre = LivreScienceFiction(titre, auteur)
        else:
            print("Catégorie invalide !")
            continue
        biblio.retirer_livre(livre)
        print("Livre retiré !")
    elif choix == "3":
        categorie = choisir_categorie()
        biblio.livres_par_categorie(categorie)
    elif choix == "4":
        nom = input("Nom de l'utilisateur : ")
        prenom = input("Prénom de l'utilisateur : ")
        utilisateur = Utilisateur(nom, prenom)
        biblio.enregistrer_utilisateur(utilisateur)
        print("Utilisateur enregistré !")
    elif choix == "5":
        biblio.afficher_livres_disponibles()
        choix_livre = input("Entrez le numéro du livre que vous souhaitez emprunter : ")
        try:
            choix_livre = int(choix_livre)
            livre_choisi = [livre for livre in biblio.livres if livre.disponible()][choix_livre - 1]
            # Demandez les détails de l'utilisateur pour l'emprunt
            nom = input("Nom de l'utilisateur : ")
            prenom = input("Prénom de l'utilisateur : ")
            utilisateur = Utilisateur(nom, prenom)
            if livre_choisi.emprunter(utilisateur):
                print(f"Vous avez emprunté '{livre_choisi.titre}' par {livre_choisi.auteur}.")
            else:
                print("Ce livre n'est pas disponible pour l'emprunt.")
        except (ValueError, IndexError):
            print("Choix invalide.")
    elif choix == "6":
        biblio.afficher_livres_empruntes()
        choix_livre = input("Entrez le numéro du livre que vous souhaitez retourner : ")
        try:
            choix_livre = int(choix_livre)
            livre_choisi = [livre for livre in biblio.livres if not livre.disponible()][choix_livre - 1]
            livre_choisi.retourner()
            print(f"Vous avez retourné '{livre_choisi.titre}' par {livre_choisi.auteur}.")
        except (ValueError, IndexError):
            print("Choix invalide.")

    elif choix == "7":
        biblio.retourner_livre()
        
    else:
        print("Choix invalide !")
        
        