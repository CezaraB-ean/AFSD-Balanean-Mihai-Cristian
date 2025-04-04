import random
import hashlib

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

cod = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

baza = ["a","a","a","A","0","!"]
l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
S = ['!', '@', '#', '$']
sir = ''
def generator():
    sir = ''
    numere = [1,2,3,4,5,6]
    for i in range(6):
        numar = str(random.choice(numere))
        sir = sir + numar
        numere.remove(int(numar))
    return sir

def generator_aranjamente():
    lista = []
    for i in range(720):
        sir = generator()
        while lista.count(sir) != 0:
            sir = generator()
        lista.append(sir)
    return lista

def generator_permutari():
    contor = 0
    for a in range(26):
        baza[0] = l1[a]
        for b in range(26):
            baza[1] = l2[b]
            for c in range(26):
                baza[2] = l3[c]
                for d in range(26):
                    baza[3] = L[d]
                    for e in range(10):
                        baza[4] = C[e]
                        for f in range(4):
                            baza[5] = S[f]
                            for j in range(720):
                                p = 100000
                                parola = ''
                                copie = int(lista[j])
                                for i in range(6):
                                    parola = parola + baza[copie // p - 1]
                                    copie = copie % p
                                    p = p // 10
                                contor = contor + 1
                                if str(get_hash(parola)) == cod:
                                    print(f"Parola gasita: {parola}")
                                    print(f"Numar apeluri: {contor}")
                                    return 0



lista = generator_aranjamente()
generator_permutari()
#print(cod)
#print(get_hash("Uare#1"))