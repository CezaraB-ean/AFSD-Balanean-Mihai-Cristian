propozitie = "Un tânăr s-a jucat cu nervii vatmanilor din Iaşi, după ce şi-a parcat maşina pe linia de tramvai. Găsit după o oră de poliţişti, a venit amuzat şi în pijamale"

print(propozitie)
print("")
lungime = len(propozitie)
mijloc = lungime//2

# 1. Impartim sirul in 2 parti:

jumatate1 = propozitie[:mijloc:]
jumatate2 = propozitie[mijloc+1::]

print("1" + ")" )
print(jumatate1)
print(jumatate2)

# 2. Transformam literele din prima jumatate in majuscule

jumatate1 = jumatate1.upper()
print("")
print("2" + ")" + " " + jumatate1)

# 3. Inversam a doua jumatate a sirului, transformam prima litera in majuscula si eliminam caracterele de punctuatie

jumatate2 = propozitie[:mijloc:-1]
jumatate2 = jumatate2.capitalize().replace(",","").replace(".","").replace("!","").replace("?","")
print("")
print("3" + ")" + " " + jumatate2)

# 4. Concatenam cele doua jumatati prelucrate si formam noua propozitie

propozitie_noua = jumatate1 + " " + jumatate2
print("")
print("4" + ")" + " " + propozitie_noua)