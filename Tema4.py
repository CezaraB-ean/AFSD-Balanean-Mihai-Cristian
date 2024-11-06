# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

for i in progres:
    print(i, end="")
print("")
cuvant2 = cuvant_de_ghicit
print("Doresti sa iti incerci norocul? \nda SAU nu")
raspuns = input()
if raspuns == "da":
    print("Foarte bine. Ai o singura incercare pentru a ghici cuvantul complet! Succes!")
    raspuns = input()
    if(raspuns == cuvant_de_ghicit):
        print("Excelent! Insa ai avut noroc! Doresti sa mai incerci odata? \nda SAU nu")
        raspuns = input()
        if(raspuns == "da"):
            print("Pacat, am ramas fara cuvinte. Poate daca as fi avut un creator mai putin lenes am fi putut sa ne jucam...")
        else:
            print("Foarte bine! Oricum nu mai ghiceai din nou! HaHaHa!!!")
    else:
        print("HAHAHA! Chiar ai crezut ca o sa fie atat de usor?! Ai gresit, muritorule!!!")
else:
    print("Pff! Foarte bine. Ai 6 incercari.")
    while incercari_ramase > 0 and progres.count("_") >= 1:
        litera = input()
        while len(litera) > 1 :
            print("Introduce-ti o SINGURA litera")
            litera = input()
        while litera.isalpha() != 1 :
            print("Introduce-ti o LITERA! o_o")
            litera = input()
        while litere_incercate.count(litera) != 0 :
            print("Introduce-ti o litera NOUA >:(")
            litera = input()
        litere_incercate.append(litera)
        cuvant_de_ghicit = list(cuvant_de_ghicit)
        if cuvant_de_ghicit.count(litera):
            while cuvant_de_ghicit.count(litera):
                for i in range(0,len(cuvant_de_ghicit)):
                    if(cuvant_de_ghicit[i] == litera):
                        cuvant_de_ghicit[i] = " "
                        progres[i] = litera
                for i in progres:
                    print(i, end="")
                print("")
        else:
            incercari_ramase -= 1
            print("Litera ", litera, " nu se regaseste in cuvant.")
            print(f"Mai ai {incercari_ramase} incercari!")

    if incercari_ramase > 0:
        print("Bravo! Ai ghicit cuvantul!")
    else:
        print(f"Ai pierdut! HaHaHa! Cuvantul era {cuvant2}")
