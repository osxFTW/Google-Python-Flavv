# def suma(x, y):
#     return x + y

# suma = lambda x,y: x+y

# print(suma(1, 2))

jucatori = [
    {
        "first_name": "Ion",
        "last_name": "Vasile",
        "age": 20
    },
    {
        "first_name": "Ionut",
        "last_name": "Barbu",
        "age": 23
    },
    {
        "first_name": "Elena",
        "last_name": "Tudora",
        "age": 12
    }
]

sorted_players = sorted(jucatori, key=lambda jucator: jucator['last_name'])
print(sorted_players)