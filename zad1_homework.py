# zadaca 1
# Da se napise funkcija koja za vnesena lista i vnesen broj ke gi ispecati
# indeksite na dva broevi taka sto nivniot zbir ke bide ednakov na vneseniot broj.

"""
funkcija koja za vnesena lista i vnesen broj ke gi ispecati
indeksite na dva broevi taka sto nivniot zbir ke bide ednakov na vneseniot broj

param: broj: vneseniot broj od tastatura
param: lista: vnesenata lista od tastatura

return return broevi_indeksi[razlika] + 1, indeks + 1: gi vrakja
vrednostite na indeksite na broevite

return None: ne e najdeno
"""
def najdi_indeks(broj, lista):
    broevi_indeksi = {}

    for indeks, vrednost in enumerate(lista):
        razlika = broj - vrednost

        if razlika in broevi_indeksi:
            return broevi_indeksi[razlika] + 1, indeks + 1
        else:
            broevi_indeksi[vrednost] = indeks

    return None

vnesen_broj = int(input("Vnesete broj: "))
vnesena_lista = [int(x) for x in input(
    "Vnesete lista od broevi (odvoeni so prazno mesto): ").split()]

rezultat = najdi_indeks(vnesen_broj, vnesena_lista)

if rezultat:
    print(f"Indeksite na dva broevi koi davaat zbir {vnesen_broj} se: {rezultat[0]} i {rezultat[1]}")
else:
    print("Ne se najdeni dva broevi so takov zbir.")
    
# zadaca 2
# Da se napise funkcija koja za vnesena lista so elementi ke ispecati dali e toa lista so palindromi.
"""
PRVA VERZIJA:
funkcija_palindrom(lista): funkcija koja za vnesena lista so elementi ke ispecati 
dali e toa lista so palindromi

PRIMER: hi nice to meet you you meet to nice hi

:param lista: lista od zborovi

return True: Ciklusot ke se izvrsi se dodeka ne
se najde zbor sto ne e palindrom
return False: najden e zbor sto ne e palindrom
"""


def funkcija_palindrom(lista):
    dolzina = len(lista)

    for i in range(dolzina // 2):
        if lista[i] != lista[dolzina - 1 - i]:
            return False
    return True

vnesena_lista = input(
    "Vnesete lista od elementi odvoeni so prazno mesto: ").split()
rezultat = funkcija_palindrom(vnesena_lista)

if rezultat:
    print("Ova lista e palindrom.")
else:
    print("Ova lista ne e palindrom.")

"""
vtora VERZIJA:
funkcija_palindrom2(lista): funkcija koja za vnesena lista so elementi ke ispecati 
dali e toa lista so palindromi

#PRIMER: civic radar level kayak madam refer

:param lista: lista od zborovi

return True: Ciklusot ke se izvrsi se dodeka ne
se najde zbor sto ne e palindrom
return False: najden e zbor sto ne e palindrom
"""
def funkcija_palindrom2(lista):
    for zbor in lista:
        if zbor != zbor[::-1]:
            return False
    return True


vnesena_lista = input(
    "Vnesete lista od elementi odvoeni so prazno mesto: ").split()
rezultat = funkcija_palindrom2(vnesena_lista)

if rezultat:
    print("Ova lista od zborovi e palindrom.")
else:
    print("Ova lista od zborovi ne e palindrom.")

# zadaca 3
# Da se napise funkcija koja za vnesena recenica ke ja isprinta dolzinata na posledniot zbor.
"""
funkcija_za_dolzina(recenica): funkcija koja za vnesena recenica ke ja isprinta dolzinata na posledniot zbor.
param: recenica: vnesenata recenica od tastatura
"""


def funkcija_za_dolzina(recenica):
    zborovi = recenica.split()
    posleden_zbor = zborovi[-1]
    dolzina = len(posleden_zbor)
    print(f"Dolzinata na posledniot zbor e: {dolzina}")


element = input("Vnesete recenica: ")
funkcija_za_dolzina(element)

# zadaca 4
# Da se napise funkcija koja za vnesen broj N1 i broj N2 ke pecati dali e N1 ednakov na N2 na nekoj stepen.

"""
funkcija_stepen(N1, N2): funkcija koja za vnesen broj N1 i broj N2 ke pecati dali e N1 ednakov na N2 na nekoj stepen.

param: N1: prviot broj vnesen od tastatura
param: N2: vtoriot broj vnesen od tastatura

return False, None:

return True, stepen: AKO e najdeno vrednost na stepen za koja shto N1 == N2 ** stepen togas,
treba da ja vratime toj stepen (so cel da se isprinta)

return False, None: AKO ne e najdeno vrednost
"""
def funkcija_stepen(N1, N2):
    stepen = 1

    while stepen <= N2:
        if N1 == N2 ** stepen:
            return True, stepen
        stepen += 1

    return False, None


broj1 = int(input("Vnesete go prviot broj: "))
broj2 = int(input("Vnesete vtoriot broj: "))

rezultat, stepen = funkcija_stepen(broj2, broj1)

if rezultat:
    print(f"{broj2} e ednakov na {broj1} na stepen {stepen}.")
else:
    print(f"{broj2} ne e ednakov na {broj1} na nekoi stepen.")

# zadaca 5
# Imame zadadeno mnozestvo so zborovi so ednakva dolzina, i imame zadadeno poceten (start) i kraen zbor (kraj).
# Da se najde najkratkiot pat (N) pomegju pocetniot i krajniot zbor, dokolku takov pat postoi,
# taka sto sosednite zborovi vo mnozestvoto se razlikuvaat megju sebe za 1 bukva.
# Da se ispecatat ovie zborovi na sledniot nacin
# start--->zbor1_1--->zbor2_2--->...--->zborN_N--->kraj .
