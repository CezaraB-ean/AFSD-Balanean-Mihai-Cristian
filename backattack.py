import hashlib
import random
import math
import sys


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
contor = 0
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

def switch(n):
    if n == 0 or n == 1 or n == 2:
        return l1
    elif n == 3:
        return L
    elif n == 4:
        return C
    elif n == 5:
        return S

def incercare_aranjamente(string):
    global contor
    baza = list(string)
    for j in range(720):
        p = 100000
        parola = ''
        copie = int(lista[j])
        for i in range(6):
            parola = parola + baza[copie // p - 1]
            copie = copie % p
            p = p // 10
        contor = contor + 1
        print(f"Parola {contor} este: {parola}")
        if str(get_hash(parola)) == cod:
            print(f"Parola gasita: {parola}")
            print(f"Numar apeluri: {contor}")
            sys.exit()
def test(string,kontor,n,deplasare):
    global i
    if kontor == len(switch(n)) and n:
        copie_deplasare = deplasare
        while copie_deplasare>-1:
            baza[n+copie_deplasare] = switch(n+copie_deplasare)[0]
            baza[n+copie_deplasare-1] = switch(n+copie_deplasare-1)[1]
            copie_deplasare = copie_deplasare - 1
        string = baza
        return test(string,0,n-1,deplasare+1)
    else:
        baza[n] = switch(n)[kontor]
        string = baza
        #incercare_aranjamente(string)
        print(string)
        return test(string,kontor+1,n,deplasare)
n = 6

def backtrack(string):
    if len(string) == n:
        incercare_aranjamente(string)
        return
    if len(string) <3:
        for caracter in l1:
            backtrack(string + caracter)
    elif len(string) == 3:
        for caracter in L:
            backtrack(string + caracter)
    elif len(string) == 4:
        for caracter in C:
            backtrack(string + caracter)
    else:
        for caracter in S:
            backtrack(string + caracter)
lista = generator_aranjamente()
backtrack('')