meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

lista_extra = []

while(studenti):
    lista_extra.append(studenti[0])
    lista_extra.append(comenzi[0])
    studenti.pop(0) # Eliminam studentul din coada
    tavi.pop(0) # Eliminam tava din stiva
    comenzi.pop(0)  # Eliminam comanda studentului din coada
    istoric_comenzi.append(lista_extra) # Adaugam elementele fiecarei comenzi la istoric ex.: "Liviu a comandat guias" --> ['Liviu', 'guias']
    lista_extra = [] # Golim lista ajutatoare

for i in istoric_comenzi:
    print(i[0], "a comandat", i[1])

numar_guias = 0
numar_papanasi = 0
numar_ceafa = 0
for comanda in istoric_comenzi:
    if(comanda[1] == "guias"):
        numar_guias += 1
    if(comanda[1] == "papanasi"):
        numar_papanasi += 1
    if(comanda[1] == "ceafa"):
        numar_ceafa += 1
print("")
print(istoric_comenzi)
print("")
print("S-au comandat", numar_ceafa, "ceafa,", numar_guias, "guias,", numar_papanasi, "papanasi.")
print("")
print("Mai sunt", len(tavi), "tavi.")

meniu = ['papanasi'] * (10 - numar_papanasi) + ['ceafa'] * (3 - numar_ceafa) + ["guias"] * (6 - numar_guias)
if(meniu.count("papanasi")):
    print("Mai sunt papanasi: True")
else:
    print("Mai sunt papanasi: False")
if(meniu.count("ceafa")):
    print("Mai este ceafa: True")
else:
    print("Mai este ceafa: False")
if(meniu.count("guias")):
    print("Mai este guias: True")
else:
    print("Mai este guias: False")

numar_comenzi = []
numar_comenzi.append(numar_papanasi)
numar_comenzi.append(numar_ceafa)
numar_comenzi.append(numar_guias)
n = 0
suma = 0
while(n < len(preturi)):
    suma = suma + (preturi[n][1] * numar_comenzi[n])
    n += 1
print("")
print("Cantina a incasat:",suma, "lei.")

lista_bonus = []
m=0
while(m < len(preturi)):
    if(preturi[m][1] <= 7):
        lista_bonus.append(preturi[m][0])
    m += 1

print("Produse care costa cel mult 7 lei sunt:", lista_bonus)