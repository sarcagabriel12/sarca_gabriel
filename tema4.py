# 1. Lista de cuvinte și alegerea cuvântului la întâmplare
import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2. Inițializarea numărului de încercări
incercari_ramase = 6
litere_incercate = []

print("\n***************************************************\n")
print("Bine ai venit la jocul 'Spanzuratoarea'!")

while incercari_ramase > 0 and "_" in progres:
    print("Ghiceste cuvantul: " + " ".join(progres))
    guess = input("Alege o litera: ")
    if guess in litere_incercate:
        print("Ai mai introdus aceasta litera, incearca din nou!")
        continue
    else:
        if guess in cuvant_de_ghicit:
            for index, litera in enumerate(cuvant_de_ghicit):
                if guess == litera:
                    progres[index] = guess
                    litere_incercate.append(guess)
        elif guess.isdigit():
            print("Te rog sa introduci o litera, nu un numar!")
        elif len(guess) > 1:
            print("Te rog sa introduci o singura litera!")
        elif guess not in cuvant_de_ghicit:
            incercari_ramase -= 1
            litere_incercate.append(guess)
            print(f"Litera nu este in cuvant! Mai ai {incercari_ramase} incercari!")

if incercari_ramase > 0 and "_" not in progres:
    print(f"Felicitari!!! Ai ghicit cuvantul care era {cuvant_de_ghicit}!")
else:
    print(f"Ai pierdut!!! Incearca din nou, cuvantul era {cuvant_de_ghicit}!")




