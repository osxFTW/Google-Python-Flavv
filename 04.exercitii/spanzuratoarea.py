cuvant = 'onomatopee'.lower() # o _ o _ _ _ o _ e e
cuvant_de_ghicit = list(cuvant)
prima_litera = cuvant[0]
ultima_litera = cuvant[-1]

for index, value in enumerate(cuvant):
    if value != prima_litera and value != ultima_litera:
        cuvant_de_ghicit[index] = '_'

cuvant_de_ghicit = ''.join(cuvant_de_ghicit)

print(cuvant_de_ghicit)
litere_incercate = set()
vieti = 7
while vieti != 0:
    litera = input("Alege o litera: ")
    litere_incercate.add(litera)
    cuvant_de_ghicit = list(cuvant_de_ghicit)
    if litera in cuvant:
        for index, value in enumerate(cuvant):
            if litera == value:
                cuvant_de_ghicit[index] = litera
        if '_' not in cuvant_de_ghicit:
            print(f"Ai castigat! Cuvantul era {cuvant}")
            break
    else:
        if litera in litere_incercate:
            vieti -= 1
            if vieti == 0:
                print(f"Ai pierdut! Cuvantul era {cuvant}")
                break
            print(f"Mai ai {vieti} vieti!")

    cuvant_de_ghicit = ''.join(cuvant_de_ghicit)
    print(cuvant_de_ghicit)
