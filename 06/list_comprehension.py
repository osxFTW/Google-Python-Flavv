var = 'comprehension'

# list_for_loop = []
# for i in var:
#     list_for_loop.append(i)
# print(list_for_loop)

# ECHIVALENT CU

# list_for_loop = [i for i in var]  #primul i reprezinta ce vrem sa adaugam la lista
# print(list_for_loop)


# list_for_loop = []
# for x in range(30):
#     if x % 2 == 0:
#         list_for_loop.append(x)

#ECHIVALENT CU

# list_for_loop = [x for x in range(30) if x % 2 == 0]   # x reprezinta ce vrem sa adaugam la lista
#
# print(list_for_loop)

list_for_loop = [x if x % 2 == 0 else 0 for x in range(30)]  # primul x reprez ce se adauga la lista, if ul se scrie primul primul daca exista else si else dupa if
print(list_for_loop)
