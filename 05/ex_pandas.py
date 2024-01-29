import pandas as pd

# lista = [10, 20, 30, 40, 50]
# etichete = ['a', 'b', 'c', 'd', 'e']
# serie = pd.Series(lista, index=etichete)
# print(serie)
# print(serie[['a', 'c']])

data = {'Nume': ['Ana', 'Bogdan', 'Cristina'],
        'Varsta': [25, 30, 22],
        'Salariu': [50000, 60000, 45000]}

df = pd.DataFrame[data]

print(df)