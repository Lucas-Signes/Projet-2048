# Projet-2048
Projet 2048 - Lucas et Conrad

repartition du travail:
Instruction 0 - Conrad
Instruction 1 - Conrad
Instruction 2 - Lucas 
Instruction 3 - Lucas
Instruction 4 - Lucas
Instruction 5 - Conrad
Instruction 6 - Lucas
Instruction 7 - Lucas
Instruction 8 - Conrad
Instruction 9 - Lucas

Aborescence:
partie.py - Il contient la classe Pile pour le fichier last_games.bk, la fonction pour sauvegarder et la class Partie
pour le deroulement du jeu et de l'affichage
grille.py - Il contient la classe grille qui a comme methode l'affichage de la grille, les methodes pour le fonctionnement
du mouvement, la methode pour ajouter de nouvelles tuiles et la methode pour tester la fin d'une partie
saisie.py - Il contient toute les fonctions permettant toutes les saisies clavier
nécessaires au déroulement du jeu
classement.py - Il contient les fonctions pour sauvegarder son score et le joueur dans un fichier classement.txt et afficher 
les 10 meilleurs scores 
2048.py - Il import tout les autres fichiers et appel la fonction start dans la class Partie pour le deroulement du jeu

Explications:
- Pour lancer le jeu il faut ouvrir le fichier 2048.py et le lancer
- Pour changer la taille de la grille il faut ouvrir le fichier partie.py et au debut de la methode Start trouver le parametre 
  taille et le changer a sa guise dans le fichier Partie.py (Ne marche que pour des entier naturel strictement postitif sauf 1)
- Pour saisir sa commande de mouvement, d'annulation de partie ou de retour en arriere il faut appuyer 2 fois sur la touche
  requise (Ceci est un mesure pour eviter que l'utilisateur saisi la mauvaise touche)
- On ne peut pas retourner en arriere plusieurs fois d'affiler (sinon ca serai trop facile) 
- le nombre de personnes maximum dans le classement est modifiable dans la fonction classement dans le fichier classement.py
- Le fichier dans lequel sont sauvegarder les 10 meilleurs scores est nomme: classement.txt
