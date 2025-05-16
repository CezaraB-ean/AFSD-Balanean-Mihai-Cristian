bancnote = [[10,20], [5,40], [2,50], [1,100]] # [valoare, cantitate]
produse = [["lapte",7], ["paine",3], ["ciocolata",5], ["apa",2], ["cafea",9]] # [nume, pret]

lista_resturi = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

def min_coins(coins,total):
    dp = [float('inf')] * (total+1)
    dp[0] = 0

    for j in range(1,total + 1):
        for coin in coins:
            if coin <= j:
                dp[j] = min(dp[j],dp[j-coin]+1)

    return dp[total] if dp[total] != float('inf') else -1

def gasire_combinatie(rest):
    rest_platit = 0
    lista = []
    for i in range(len(bancnote)):
        while bancnote[i][1] and rest_platit + bancnote[i][0] <= rest:
            rest_platit = rest_platit + bancnote[i][0]
            bancnote[i][1] -= 1
            lista.append(bancnote[i][0])
            print(lista)
        if rest_platit == rest:
            lista_resturi[rest] = lista


def calculare_rest(suma_platita,produs):
    pret_produs = 0
    for i in range(len(produse)):
        if produse[i][0] == produs:
            pret_produs = produse[i][1]
            continue
    if suma_platita - pret_produs >= 0:
        rest = suma_platita - pret_produs
    else:
        print("Fonduri insuficiente, săracule.")
        return 0
    if lista_resturi[rest]:
        print(f"Clientul a cumparat: {produs} in valoarea de {pret_produs} lei.\nAcesta a platit {suma_platita} lei.\n"
              f"Restul oferit este {rest} lei care a fost platit cu urmatoarele bancnote {lista_resturi[rest]}.")
    else:
        gasire_combinatie(rest)
        print(f"Clientul a cumparat: {produs} in valoarea de {pret_produs} lei.\nAcesta a platit {suma_platita} lei.\n"
              f"Restul oferit este {rest} lei care a fost platit cu urmatoarele bancnote {lista_resturi[rest]}.")

calculare_rest(3,"paine")