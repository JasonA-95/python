valeur1 = int(input("Saisir la première valeur : "))
valeur2 = int(input("Saisir la deuxième valeur : "))

if valeur1 < valeur2:
    print(valeur1)
else: 
    print(valeur2)

chaine1 = input("Saisir la première chaîne de caractères : ")
chaine2 = input("Saisir la deuxième chaîne de caractères : ")   

if len(chaine1) > len(chaine2):
    print(chaine1)
else:
    print(chaine2)





taux_euro_dollar = 1.1  # taux de change euro vers dollar

devise = input("Saisir la devise ('E' pour euros, '$' pour dollars) : ")
montant = float(input("Entrez le montant : "))

if devise == "E" or devise == "e":
    dollars = montant * taux_euro_dollar
    print(f"{montant} € = {dollars:.2f} $")
elif devise == "$":
    euros = montant / taux_euro_dollar
    print(f"{montant} $ = {euros:.2f} €")
else:
    print("Devise inconnue ! Veuillez entrer 'E' ou '$'.")




studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Julie"

if name in studentsTuring:
    print("Vous êtes sur la liste de Turing")
else:
    print("Vous ne faites pas partie du groupe Turing")




rayon = 10

import math 
volume = (4/3) * math.pi * rayon**3
print("Le volume de la sphère de rayon {} est de {:.2f}".format(rayon, volume))