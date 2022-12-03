import random #on import random pour etre utilise dans laffichage

class Grille():
   
    def __init__(self, L, score, taille):
        '''
        methode qui initialise la grille en tant que liste de liste, le score du joueur et la taile de la grille et ???
        '''
        self.grille = L       # on attribut la grille
        self.score = score    # on attribut le score
        self.taille = taille  #on attribut la taille
       
    def afficher_grille(self):
        '''
        methode qui affiche la grille en prenant la taille de la grille et fesant un carre qui change par rapport a la taille donné et la quntite des nombres a linterieur
        '''
        t_max = 0                 # on calcule la taille du plus grand caractere
       
        for i in range(0, len(self.grille)):
           
            for j in range(0, len(self.grille[i])):
               
                if len(str(self.grille[i][j])) > t_max:
                   
                    t_max = len(str(self.grille[i][j]))    # t_max est a la fin la taille du plus grand caractere
                   
        print( "", "_" * (8*len(self.grille) + 8 * (t_max -1)))
        for i in range(0, len(self.grille)):
            print("|", end="")
            for esp in range (len(self.grille)):
              print( " " * ((t_max - (len(str(self.grille[i][j]))-1)// 2)), " " * len(str(self.grille[i][j])) ," " * ((t_max - len(str(self.grille[i][j]))// 2)+1), "|" , end="")
            for j in range (0, len(self.grille[i])):
               
                if j == 0:
                   
                    print("\n|", " " * ((t_max - ((len(str(self.grille[i][j])))-1)// 2)), self.grille[i][j], " " * ((t_max - len(str(self.grille[i][j]))// 2)), "|", end='')              
       
                else:

                    print( " " * ((t_max - (len(str(self.grille[i][j]))-1)// 2)+1), self.grille[i][j], " " * ((t_max - len(str(self.grille[i][j]))// 2)),"|" ,  end='')
                   
            print("\n|", end="")
            for esp in range (len(self.grille)):
              print( " " * ((t_max - (len(str(self.grille[i][j]))-1)// 2)), " " * len(str(self.grille[i][j])) ," " * ((t_max - len(str(self.grille[i][j]))// 2)+1), "|" , end="")
            print( "\n", "_" * (8*len(self.grille) + 8 * (t_max -1)))
        
    def reverse_horz(self):
        '''
        methode de reverse horizontale qui fait un nouvelle grille et parcours la grille originale de la gauche vers la droite et pour chaque element ajoute 
        la valeur a la nouvelle grille de la droite vers la gauche donc a l'envers
        '''
        n_grille = [[ 0 for j in range(self.taille) ] for i in range(self.taille)]
        for i in range(self.taille):
            for j in range(self.taille):
                n_grille[i][j] = self.grille[i][self.taille-1-j] #Atrribut toute valeur de la grille a la nouvelle grille mais en la parcourant dans le sens inverse
        self.grille = n_grille

    def reverse_vert(self):
        '''
        methode de reverse verticale qui fait un nouvelle grille et parcours la grille originale de la gauche vers la droite et pour chaque element ajoute 
        la valeur a la nouvelle grille du haut vers le bas ce qui la retourne a 90 degres
        '''
        n_grille = [[ 0 for j in range(self.taille) ] for i in range(self.taille)]
        for i in range(self.taille):
            for j in range(self.taille):
                n_grille[i][j] = self.grille[j][i] #Atrribut toute valeur de la grille a la nouvelle grille mais en la parcourant du haut vers le bas
        self.grille = n_grille
    
    def deplacement_g(self):
        '''
        methode qui creer une nouvelle liste et en parcourant la liste de la gauche vers la droite tout element superieur a 0 est 
        decale vers la gauche dans la nouvelle grille
        '''
        n_grille = [[ 0 for j in range(self.taille)] for i in range(self.taille)]
        for i in range(self.taille):
            aux = 0
            for j in range(self.taille):
                if self.grille[i][j] > 0:
                    n_grille[i][aux] = self.grille[i][j] #Traverse la grille et on attribut toute valeur au dessus de 0 a cette nouvelle grille
                    aux += 1
        self.grille = n_grille
    
    def fusion(self):
        '''
        methode qui parcours la liste et verifie si 2 elements qui sont a cote sont les memes alors il fusent et la valeur de la 
        premiere double et lautre devient 0
        '''
        for i in range(self.taille):
            for j in range(self.taille - 1):
                if self.grille[i][j] > 0 and self.grille[i][j] == self.grille[i][j+1]: #Si il ya 2 tuiles pareils alors elle fusionnent
                    self.grille[i][j] = self.grille[i][j] * 2
                    self.grille[i][j+1] = 0
                    self.score += self.grille[i][j]
     
    def mouvement_g(self):
        '''
        methode qui gere le mouvement vers la gauche en deplacent tout les elements vers la gauche, faire une fusion et redeplacer 
        tout les elements vers la gauche
        '''
        self.deplacement_g()
        self.fusion()
        self.deplacement_g()
     
     
    def mouvement_d(self):
        '''
        methode qui gere le mouvement vers la droite qui reverse la liste horizontalement puis appel le mouvement vers la gauche 
        et reverse encore une fois la liste vers la droite
        '''
        self.reverse_horz()
        self.mouvement_g()
        self.reverse_horz()
             
    def mouvement_h(self):
        '''
        methode  pour effecture le mouvement vers le haut qui retourne la grille de 90 degres puis effectue le mouvement g et retourne encore une fois la grille de 90 degres 
        '''
        self.reverse_vert()
        self.mouvement_g()
        self.reverse_vert()
        
        #return n_grille, score
     
    def mouvement_b(self):
        '''
        methode pour effecture le mouvement vers le bas qui retourne la grille de 90 degres puis la effectue le mouvement vers la droite 
        et retourne encore une fois de 90 degres
        '''
        self.reverse_vert()
        self.mouvement_d()
        self.reverse_vert()
        

    def nouvelle_tuile(self):
        '''
        methode qui place une nouvelle tuile dans un case au hasard de la grille sauf si celle si est deja occupe et elle en choisit une autre 
        '''
        rep = False
        for i in range(self.taille):
            for j in range(self.taille):
                if self.grille[i][j] == 0: #on parcours la liste pour savoir si il ya une place libre pour une nouvelle tuile sinon on en ajoute pas
                    rep = True
        if rep == True:
            i = random.randint(0, 3)
            j = random.randint(0, 3)
            while self.grille[i][j] != 0: #Place la tuile dasn un endroit random
                i = random.randint(0, 3)
                j = random.randint(0, 3) 
            r = random.randint(0,4)
            if r == 4:
                self.grille[i][j] = 4
            else:
                self.grille[i][j] = 2
        else:
            pass

 
    def test_fin(self):
        '''
        methode qui test si la partie est fini dabord en parcourant la grille pour verifier si il ya un 2048 pr que la partie sois gagne puis 
        verifie si il ya un 0 ou 2 tuiles qui peuvent fusioner et la partie continue et sinon la partiie est perdu
        '''
        for i in range(4):
            for j in range(4):
                if self.grille[i][j] == 2048:
                    return 'G' #si il ya un 2048 retourne G pour gagne 
        for i in range(4):
             for j in range(4):
                 if self.grille[i][j] == 0:
                     return 'C' #si il ya un 0 dans la grille on retourne C pour continue 
        for i in range(3):
            for j in range(3):
                if self.grille[i][j] == self.grille[i+1][j] or self.grille[i][j] == self.grille[i][j+1]:
                    return 'C' #si il ya 2 tuiles qui peuvent etre fusionne on retourne C pour continue 
        return 'P' #Pour tout autre cas la partie est perdue
    
grille = [[0,2,0,0],[2,0,0,0],[0,2,0,4],[0,0,0,0]]
g = Grille(grille, score=0, taille=4)
g.mouvement_d
g.afficher_grille