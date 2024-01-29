# def filtare(x):
#     lista_forloop = []
#     for i in x:
#         if i % 2 == 0:
#             lista_forloop.append(i)
#     return lista_forloop

list1 = [1, 5, 4, 6, 8, 11, 3]

filtrare = filter(lambda x: x % 2 == 0, list1)

print(list(filtrare))