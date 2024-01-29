"""
r -> citire, nu adaugam, este valoare default cu care vine functia open
w -> scriem, daca fisierul nu exista, il adauga, daca exista informatie deja scrisa o rescrie
a -> scriem, daca exista informatie deja scrisa in fisier, adauga si NU rescrie
r+ -> scriere, citire, daca fisierul nu exista, apare eroare, informatia este rescrisa
"""
import csv

# file = open('data.txt', 'r+')
# file.write("Hello\n")
# file.close()
#
# file = open('data.txt', 'a')
# file.write("Hello1\n")
# file.close()

# with open('data.txt', 'w') as file:
#     file.write('hello')


# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(f"line {line}")

# ECHIVALENT CU

# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(f"line {line}")

# ECHIVALENT CU

# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(f"line {line}")
#

new_cars = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault', 'Clio', 2005, 75]
]
# with open('data.csv', 'w', newline='') as csv_file:
#     csv_write = csv.writer(csv_file, delimiter=',')
#     for new_car in new_cars:
#         csv_write.writerow(new_car)

with open('data.csv', 'r+') as file:
    lista_elemente = []
    categorie = csv.reader(file)
    for item in categorie:
        lista_elemente.append(item)

print(lista_elemente)