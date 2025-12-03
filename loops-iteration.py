étudiants = ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphael", "Axel", "Mathieu", "Adrien"]
étudiants.sort()
print(étudiants)
for étudiant in étudiants:
    if étudiant[0] == "M":
        print(étudiant)


i = 1
for i in range(15):
    print(i)


i = 1 
for i in range(1, 11):
    if i > 5:
        break
    print(i)


i = 1 
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


nombres = [17, 38, 10, 25, 72]
print(sorted(nombres))
nombres.append(12)
print(nombres)
nombres.reverse()
print(nombres)
print(nombres.index(17))
nombres.remove(38)
print(nombres)
print(nombres[1:3])
print(nombres[0:2])
print(nombres[3:])
print(nombres[:])
print(nombres[-1])



nombre = int(input("saisir un nombre: "))
for i in range(nombre, -1, -1):
    print(i)



price = 5

def trouver_prix():
    while True: # boucle jusqua se que le prix soit trouvé 
        number = int(input("Entrez le prix: "))
        if number > price:
            print("C'est moins cher")
        elif number < price:
            print("C'est plus cher")
        else:
            print("Bravo, vous avez gagné!")
            break
# Appel de la fonction
trouver_prix()
# Fin du programme


