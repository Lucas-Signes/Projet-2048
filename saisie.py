def saisie_commande0(): 
    '''
    Fonction qui demande un input et verifie que lutilisateur saisie un mouvement ou une commande pendant une partie et retourne cette valeur ( fonction non utilise)
    '''
    rep = False
    while rep != True:
        m = input("Voici les commandes : \n 'W' or 'w' : Bouger vers le haut \n 'S' or 's' : Bouger vers le Bas \n 'A' or 'a' : Bouger vers le la gauche \n 'D' or 'd' : Bouger vers la droite \n 'M' or 'm' : arreter la partie \n '9' : efface le dernier coup (impossible d'effacer le dernier coup plusieurs fois d'affiler) \n Dans quel direction souhaiter vous bouger le tableau: ")  
        if m == 'W' or m == 'w':
            rep = True                            # pour que la saisie accepte minuscule et majuscule
            return 'w'
        elif m == 'S' or m == 's':
            rep = True
            return 's'
        elif m == 'A' or m == 'a':
            rep = True
            return 'a'
        elif m == 'D' or m == 'd':
            rep = True
            return 'd'
        elif m == 'M' or m == 'm':
            rep = True
            return 'm'
        elif m == '9':
            rep = True
            return '9'

def saisie_commande():
    '''
    Fonction qui demande un input et verifie que lutilisateur saisie un mouvement ou une commande pendant une partie et retourne cette valeur ( fonction non utilise)
    '''
    liste_caracteres_autorises = ["a", "d", "w", "s", "m", "9"]    # CHANGER LA LISTE DES CARACTERES AUTORISES
    print("Voici les commandes : \n 'W' or 'w' : Bouger vers le haut \n 'S' or 's' : Bouger vers le Bas \n 'A' or 'a' : Bouger vers le la gauche \n 'D' or 'd' : Bouger vers la droite \n 'M' or 'm' : arreter la partie \n '9' : efface le dernier coup (impossible d'effacer le dernier coup plusieurs fois d'affiler) \n Dans quel direction souhaiter vous bouger le tableau: " , end = "")
    char = saisir(liste_caracteres_autorises)
    while char != "a" or "d" or "w" or "s" or "m" or "9":
        if char == "a" or char == "A":         # pour que la saisie accepte minuscule et majuscule
            return 'a'
        elif char == "d" or char =="D":
            return 'd'
        elif char == "w" or char == "W":
            return 'w'
        elif char == "s" or char =="S":
            return 's'
        elif char == "m" or char == "M":
            return 'm'
        elif char == "9":
            return '9'
        

def saisie_fin():     # permet de demander ce que le joueur veut a la fin de la partie
    '''
    fonction qui demande un input et retourne un boolean pour savoir si lutilisateur veut sauvegarder la partie
    '''
    rep = False
    while rep != True:
        part = input("\nLa partie est finit voulez vous sauvegarder votre partie? (repondez avec oui ou non) : ")
        if part == 'Oui' or part == "oui" or part == 'OUI':
            rep = True
            return True
        elif part == 'Non' or part == 'non' or part == 'NON':
            rep = True
            return False

def saisie_score():    # permet de savoir si le joueur veut sauvegarder son score
    '''
    fonction qui demande un input et retourne un boolen pour savoir si lutilisateur veut enregistrez son score, et si cest Vrai il demande a lutilisateur un prenom a enregistrer 
    '''
    rep = False
    while rep != True:
        score = input("\nVoulez vous enregistrez votre score? (reponder par oui ou par non) : ")
        if score == 'Oui' or score == "oui" or score == 'OUI':
            prenom = "            "
            while len(prenom) > 10:
                prenom = input("Saisissez votre prenom (10 caracteres maximum): ")
            rep = True
            return True, prenom
        elif score == 'Non' or score == 'non' or score == 'NON':
            rep = True
            return False, None
        
def saisie_rejouer():   # demande si le joueur veut rejouer
    '''
    fonction qui demande a lutilisateur un input pour savoir ce quil veut faire apres que la partie est finie 
    '''
    rep = False
    while rep != True:
        part = input("\nQue voulez vous faire? \n 1 - rejouer \n 2 - quitter \n Que voulez vous faire (saisissez 1 ou 2) : ")
        if part == '1':
            rep = True
            return True
        elif part == '2':
            rep = True
            return False
        
def saisie_rep_partie():
    '''
    fonction qui demande un input et retourne un boolean pour savoir si lutilisateur veut sauvegarder la partie
    '''
    rep = False
    while rep != True:
        part = input("\nVoulez vous reprendre une ancienne partie? (repondez avec oui ou non) : ")
        if part == 'Oui' or part == "oui" or part == 'OUI':
            rep = True
            return True
        elif part == 'Non' or part == 'non' or part == 'NON':
            rep = True
            return False
        
def saisie_classement():
    '''
    fonction qui demande un input et retourne un boolen pour savoir si l'utilisateur veut voir les meilleurs scores enregistres (pas plus que les 10 meilleurs)
    '''
    rep = False
    while rep != True:
        part = input("\nVoulez vous voir le score? (repondez avec oui ou non) : ")
        if part == 'Oui' or part == "oui" or part == 'OUI':
            rep = True
            return True
        elif part == 'Non' or part == 'non' or part == 'NON':
            rep = True
            return False

##########################################

try:
    from msvcrt import getch    # la librairie msvcrt n'existe que sous windows et contient la fonction getch de saisie clavier d'un caractère
except ImportError:             # si la librairie n'existe pas (cas de systèmes UNIX), on crée la fonction getch
    def getch():
        """
        Fonction de détection et de récupération d'une seule touche clavier depuis l'entrée standard (STDIO)
        """
        import sys          # module de fonctions système
        import tty          # module (nécessitant le module termios) de fonctions de gestion du terminal
        import termios      # module de fonctions bas niveau et d'interface UNIX pour le terminal
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def saisir_caractere_en_ligne():
    """
    Fonction de détection et de récupération d'une touche clavier frappée, à partir des deux cas possibles (système windows ou système UNIX)
    """
    caractere_saisi = getch()
    if isinstance(caractere_saisi, bytes):  # si caractere_saisi est de type bytes (cas du getch windows) :
        caractere_saisi = getch().decode()  # il faut utiliser decode() pour en faire une chaine de un caractère
    return caractere_saisi                  # sinon (cas UNIX) : caractere_saisi est déjà de type string


def saisir(L_choix):
    """
    Fonction de saisie en ligne d'un caractère figurant dans la liste des choix autorisés
    Attention : ne permet de saisir qu'un seul caractère, sans appuyer sur entrée
    """
    while True:
        caractere_saisi = saisir_caractere_en_ligne()   # ne permet de saisir qu'un seul caractère, sans valider avec la touche entrée
        try :
            assert caractere_saisi in L_choix           # le caractère saisi doit être dans la liste des caractères autorisés donnée en argument
#            assert condition                            # possibilité de rajouter d'autres assertions : entier dans une plage de valeurs, booléen, etc
            break
        except ValueError:         # exception en cas de mauvaise valeur (utile dans le cas ou on attend un entier, un booléen ou un autre type en particulier)
            pass
        except AssertionError:     # exception si le caractère saisi n'est pas dans la liste (exception provenant de l'instruction assert)
            pass
    return caractere_saisi




