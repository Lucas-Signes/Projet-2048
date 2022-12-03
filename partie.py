from saisie import * #import les fonctions du fichier sasie 
from grille import *  #import la classe grille du fichier grille 
from classement import * #import les fonctions du fichier classement

def sauvegarde(histo):
    '''
    fonction qui sauvegarde les grilles et les scores dune partie dans un fichier last_games.bk quand elle est appelee
    '''
    with open("last_games.bk" , "w") as fichier:
        fichier.write('[')
        aux = histo.copie()
        fichier.write(str([aux.sommet()[0], aux.sommet()[1]]))
        for i in range (1, histo.taille+1):
          fichier.write(',')
          fichier.write(str([aux.sommet()[0], aux.sommet()[1]]))
          aux.depiler()
        fichier.write(']')
        fichier.close()    

# IMPLANTATION DE PILES (EN OBJET)
class Pile:
    
    def __init__(self):
        self.memoire = []
        self.taille = 0

    def est_vide(self):
        return self.taille == 0

    def empiler(self, x):
        self.memoire.append(x)
        self.taille = self.taille + 1

    def depiler(self):
        """
        Retourne None si la liste est vide
        """
        if not(self.est_vide()):
            self.taille = self.taille - 1
            return self.memoire.pop()

    def copie(self):
        """ Retourne une pile copie de la pile """
        aux = Pile()
        while not(self.est_vide()):
            aux.empiler(self.depiler())
        copie = Pile()
        while not(aux.est_vide()):
            elt = aux.depiler()
            copie.empiler(elt)
            self.empiler(elt)
        return copie

    def afficher(self):
        """ affiche la pile """
        print(self)

    def sommet(self):
        """ Retourne, sans le dépiler, l'élément au sommet de la pile """
        x = self.depiler()
        self.empiler(x)
        return x

    def sous_pile(self):
        """ Retourne la sous-pile, c'est-à-dire la pile sans le sommet """
        p = self.copie()
        p.depiler()
        return p

class Partie:
        
    def start(self):
        '''
        cette methode prend en compte tout les autres fonction et classe dautres fichiers pour fair une boucle qui permet
        la jouabilite et laffichage du 2048
        '''
        joue = True 
        if saisie_rep_partie() == True:
            try:
                with open("last_games.bk", "r") as fichier:
                    lines = fichier.readlines()
                    aux = eval(lines[0])
                    aux2 = Pile()
                    histo = Pile()
                    for i in range (len(aux)):
                        aux2.empiler(aux[i])
                    while not aux2.est_vide():
                        histo.empiler(aux2.depiler())
                    g = Grille(histo.sommet()[0], histo.sommet()[1], len(histo.sommet()[0]))
                    fichier.close()
            except:
                print("\nil n'y a pas de fichier last_games, 'ca marche")
                score = 0
                histo = Pile()
                taille = 5 #La Taille peut etre change par l'utilisateur
                grille = [[ 0 for j in range(taille) ] for i in range(taille)]
                g = Grille(grille, score, taille)
                histo.empiler([g.grille, g.score])
                g.nouvelle_tuile()
                g.nouvelle_tuile()
        
        else:
            score = 0
            histo = Pile()
            taille = 5 #La Taille peut etre change par l'utilisateur
            grille = [[ 0 for j in range(taille) ] for i in range(taille)]
            g = Grille(grille, score, taille)
            histo.empiler([g.grille, g.score])
            g.nouvelle_tuile()
            g.nouvelle_tuile()
        
        if saisie_classement() == True: #demande si vous voulez voir le clssement des meilleurs scores
            voir_classement()
        else:
            pass
        print("*** BIENVENUE AU 2048 DE L'EIB ***")
        while joue != False: #commence la boucle du jeu pour chaque tour 
            print("\nVotre score actuel est de:", g.score) #print le score actuel du joueur pendant la partie
            g.afficher_grille() #affche la grille au debut de chaque tour 
            
            end = g.test_fin() #Ici on test la finalite de la partie pour savoir si elle continue, si l'utilisateur a gagne ou si il a perdu
            if end == 'C': #condition si la partie continue
                histo.empiler([g.grille, g.score])
            elif end == 'P': #condition si on perd
                print('P')
                ask, prenom = saisie_score()
                if ask == True:
                    classement(g, prenom)  #Fonction qui sauvegarde le score et le nom du joueur dans un classement
                else:
                    pass
                if saisie_rejouer() == False:
                    joue = False
                else:
                    self.start()
                    
            elif end == 'G': #condition si on gagne
                print('G')
                if saisie_fin() == True:
                    sauvegarde(histo)
                    pass
                else:
                    pass
                ask, prenom = saisie_score()
                if ask == True:
                    classement(g, prenom) #Fonction qui sauvegarde le score et le nom du joueur dans un classement
                else:
                    pass
                if saisie_rejouer() == False:
                    joue = False
                else:
                    self.start()
            
            com = saisie_commande() # ici on saisit les commandes pour savoir quel mouvement choisit lutilisateur 
            if com == 'a': #condition quand on bouge vers la gauche
                grille = g.mouvement_g()
                g.nouvelle_tuile()
                
            elif com == 'd': #condition quand on bouge vers la droite
                grille = g.mouvement_d()
                g.nouvelle_tuile()
                
            elif com == 'w': #condition quand on bouge vers le haut
                grille = g.mouvement_h()
                g.nouvelle_tuile()
            
            elif com == 's': #condition quand on bouge vers le bas
                grille = g.mouvement_b()
                g.nouvelle_tuile()
                
            elif com == 'm': #condition quand on arrete la partie
                if saisie_fin() == True:
                    sauvegarde(histo)
                else:
                    pass
                ask1, prenom = saisie_score()
                if ask1 == True:
                    classement(g, prenom) #Fonction qui sauvegarde le score et le nom du joueur dans un classement
                else:
                    pass
                if saisie_classement() == True:
                    voir_classement()
                else:
                    pass
                if saisie_rejouer() == False:
                    joue = False
                else:
                    self.start()
            
            elif com == '9': #condition quand on revient a la grille precedente
                histo.depiler()
                g = Grille(histo.sommet()[0], histo.sommet()[1], len(histo.sommet()[0]))

                