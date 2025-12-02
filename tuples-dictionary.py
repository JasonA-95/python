dictionnaire = {"apple":"pomme", "strawberry":"fraise", "grape":"raisin", "watermelon":"pastèque", "peach":"pêche"} 
dictionnaire["cherry"] = "cerise"
print(dictionnaire)



liste_mots = "Je suis le maitre du monde".split()
print(liste_mots)


chaine = "Le_nombre_universel_est_42"
nouvelle_chaine = chaine.replace("_"," ")
print(nouvelle_chaine)




héros = {"Superman": "Clark Kent", "Batman": "Bruce Wayne", "Spiderman": "Peter Parker"}
valeurs = héros.values()
print(valeurs)



prix_produits = {"épée laser": 229.00 ,"Mitendo DX": 127.30 ,"Coussin Linux": 74.50 ,"Slip Goldorak": 29.90 , "Station Nextpresso": 184.60 }
del prix_produits["Slip Goldorak"]
prix_total = sum(prix_produits.values())
print(prix_total)