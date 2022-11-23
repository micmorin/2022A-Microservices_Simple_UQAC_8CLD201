def calcul(calcul):
    #Fonction qui calcule le résultat d'un calcul simple
    result = eval(str(calcul))
    return result

# demande à l'utilisateur de saisir un calcul et affiche le résultat
if __name__ == "__main__":
    enter = input("Entrez un calcul : ")
    print(calcul(enter))