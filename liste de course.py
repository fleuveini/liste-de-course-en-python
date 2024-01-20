liste_de_course=[]

print("comment voulez vous agir sur votre liste de course?")
print("tapez '1' pour ajouté un élément")
print("tapez '2' pour retirer un élément")
print("tapez '3' pour afficher la liste un élément")
print("tapez '4' pour ajouté un élément")
print("tapez '5' pour quitter le programme")

choix=int(input("quel chiffre choisiez vous?"))
while choix!="infini": 
    if choix==1:
        nb_ajout=int(input("combien d'élément voulez vous ajouter?"))
        for i in range(nb_ajout):
            liste_de_course.append(input("quel object voulez vous ajouter a votre liste de course? "))
    elif choix==2:
        element_supprime=input("quel élément voulez vous suprimer?")
        if element_supprime in liste_de_course:
            liste_de_course.remove(element_supprime)
        else:
            print("cet élément n'etais pas dans la liste")
    elif choix==3:
        print(liste_de_course)
    elif choix==4:
        liste_de_course=[]
    elif choix==5:
        break
    else:
        print("veuillez entrer un nombre valide")
    choix=int(input("quel chiffre choisiez vous?"))

print("vous avez quitter le programme")