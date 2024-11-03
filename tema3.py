meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

cata_ceafa_era_la_inceput = meniu.count("ceafa")
cata_ceafa_a_comandat = comenzi.count("ceafa")
pret_ceafa = preturi[1][1]
print(cata_ceafa_era_la_inceput)

papanasi_la_inceput = meniu.count("papanasi")
papanasi_comandati = comenzi.count("papanasi")
pret_papanasi = preturi[0][1]
print(papanasi_la_inceput)

guias_la_inceput = meniu.count("guias")
guias_comandati = comenzi.count("guias")
pret_guias = preturi[2][1]
print(guias_la_inceput)

while studenti:
    print(f"{studenti[0]} a comandat {comenzi[0]}.")
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tavi.pop(0)
    istoric_comenzi.append(comanda)
    meniu.remove(comanda)

papanasi_ramas = papanasi_la_inceput - papanasi_comandati
ceafa_ramas = cata_ceafa_era_la_inceput - cata_ceafa_a_comandat
guias_ramas = guias_la_inceput - guias_comandati

print(f"S-au comandat {papanasi_comandati} papanasi, {cata_ceafa_a_comandat} ceafa, {guias_comandati} guias.")
tavi_ramase = tavi.count("tava")
print(f"Mai sunt {tavi_ramase} tavi.")

meniu_simplu = ["papanasi", "ceafa", "guias"]

for mancare in meniu_simplu:
    if mancare in meniu:
        print(f"Mai este {mancare}:True.")
    else:
        print(f"Mai este {mancare}:False.")

print(istoric_comenzi)

pret_meniuri = [pret_ceafa, pret_papanasi, pret_guias]


pret_comanda_ceafa_total = 3 * pret_ceafa
pret_comanda_papanasi_total = pret_papanasi
pret_comanda_guias_total = pret_guias

pret_total = pret_comanda_ceafa_total + pret_comanda_papanasi_total + pret_comanda_guias_total
print(f"Cantina a incasat: {pret_total} lei.")




produse_7_lei = []

doar_preturi = [preturi[0][1], preturi[1][1], preturi[2][1]]

print(doar_preturi)

for pret in doar_preturi:
    if pret <= 7:
        produse_7_lei.append(pret)
        stergere_pret = doar_preturi.pop(0)
    elif:
        continue

print(produse_7_lei)

