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

while(incercari_ramase > 0 and progres.count("_") > 1):
    litera = input()
    while(len(litera) > 1):
        print("Introduce-ti o SINGURA litera")
        litera = input()
    while(litere_incercate.count(litera) != 0):
        print("Introduce-ti o litera NOUA >:(")
        litera = input()
    while(litera.isalpha() != 1):
        print("Introduce-ti o LITERA! o_o")
        litera = input()
    list(cuvant_de_ghicit)
    while(litera in cuvant_de_ghicit):
