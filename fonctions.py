def hello(nom = "Anonyme"):
    return f"Bonjour {nom}"



students = [["Jean","Alice","Edwige","Peter","James"],
            ["Redouane","Justine","Adrien","Nicolas","Pierre"]]

def sum_of_students(students):
    total = 0
    for student_list in students:   
        total += len(student_list)
    return total                    

print(sum_of_students(students))


def is_divisible(n,x,y):
    if n <= 0 or x <= 0 or y <= 0:
        return False
    return n % x == 0 and n % y == 0

print(is_divisible(10,2,5)) # True
print(is_divisible(10,2,3)) # False


name = "Jean Dupont"
words = name.split(" ")
first = words[0][0]
second = words[1][0]
initials = first + "." + second
print(initials)




nombres = [10, -20, 17, 24, 32]
def positive_sum(nombres):
    total = 0
    for nombre in nombres:
        if nombre > 0:
            total += nombre
    return total

print(positive_sum(nombres))




nombres = [7, -12, 23, -4, 13, 8]
def mixed_sum(nombres):
    total = 0
    for nombre in nombres:
        if nombre:
            total += int(nombre)
    return total

print(mixed_sum(nombres))




jours_dict = {1:"Lundi", 2:"Mardi", 3:"Mercredi", 4:"Jeudi", 5:"Vendredi", 6:"Samedi", 7:"Dimanche"}
def what_day(nombre):
    return jours_dict[nombre] if nombre in jours_dict else None

while True:
    try:
        saisie = int(input("Entrez un nombre entre 1 et 7: "))
        jour = what_day(saisie)
        if jour:  # nombre correct
            print(f"Le jour correspondant est : {jour}")
            break
        else:     # nombre incorrect
            print("Incorrect, veuillez entrer un nombre entre 1 et 7. Essayez encore.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")




total = 0
i = 1
saisie = int(input("Entrez un nombre entier positif: "))
while i <= saisie:
    total += i
    i += 1
print(total)




def compter_moutons(nombres):
    resultat = ""
    for i in range(1, nombres + 1):
        resultat += f"{i} mouton{'s' if i > 1 else ''}...\n"
    return resultat.strip()
saisie = int(input("Entrez le nombre de moutons: "))
print(compter_moutons(saisie))




