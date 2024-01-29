#daca folosim primul parametru ca default trb sa avem toti parametrii as default
# def suma(a=2, b=2):
#     return a + b, a - b
#
# suma = suma(3)
# print(suma)

def suma(a=1, b=2, *args, **kwargs):
    total = a + b
    for i in args:
        total += i
    for j in kwargs:
        total += j
    return total


suma_1 = suma(1, 7, 3, 5, 6, 6, d=7, e=8)

print(suma_1)