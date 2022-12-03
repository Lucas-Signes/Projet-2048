def classement(g, prenom):
    '''
    Fonction qui prend en parametres la grille g et le prenom du joueur et le sauvegarde le score dans un fichier classements.txt 
    et enregistre le 10 meilleur scores avec les prenoms des joueurs quanf elle est appelee
    '''
    try:
        with open("highscores.txt", "r") as fichier:  # on ouvre le fichier avec les scores
            #print("test")
            lines = fichier.readlines()
            aux = eval(lines[0])                      # aux prend en valeur la liste des scores
            fichier.close()
        with open('highscores.txt', 'w') as fichier:
              nv = [prenom, g.score]
              nb_max = 10                              # le nombre de personnes maximum dans le classement est modifiable 
              if nb_max > len(aux)+1: 
                  nb_max = len(aux)+1
              for i in range (nb_max+1):               # on fait un tri pour introduire le nom et le score de la nouvelle personne
                  if i < len(aux):
                    if aux[i][1] < nv[1]:
                        aux2 = aux[i]
                        aux[i] = nv
                        nv = aux2
                  elif i > len(aux):
                        aux.append(nv)
                        
              fichier.write(str(aux))
              fichier.close()
                       
    except:
        with open('highscores.txt', 'w') as fichier:   # si le fichier n'existe pas on le creer
            fichier.write(str([[prenom, g.score]]))
            fichier.close()
            
            
def voir_classement():
    '''
    fonction qui affiche le classement des 10 meilleurs score et le prenom du joueur
    '''
    try:
        with open("highscores.txt", "r") as fichier:
            lines = fichier.readlines()
            aux = eval(lines[0])
            for i in range (len(aux)):
                print(i+1, ".", aux[i][0], "avec un score de :", aux[i][1])
            fichier.close()
    except:
        print("il n'a pas de classement")