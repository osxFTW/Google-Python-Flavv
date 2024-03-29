import requests
from bs4 import BeautifulSoup
import pandas as pd


r = requests.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-10-decembrie-ora-13-00-2/")
link = BeautifulSoup(r.text, 'html.parser')

table = link.find('table')
data = {'NR. CRT': [], 'Judet': []}

for index, row in enumerate(table.find_all('tr')[1:], start=1):  # Ignoră prima linie dacă conține antete
    columns = row.find_all('td')
    data['NR. CRT'].append(str(index))
    data['Judet'].append(columns[1].text.strip())

df_final = pd.DataFrame(data)

df_zile = {}

df_total = {}

total_values = []

for zile in range(10,15):
    r = requests.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{zile}-decembrie-ora-13-00-2/")
    link = BeautifulSoup(r.text, 'html.parser')

    table = link.find('table')
    data_zile = {f'Ziua_{zile}': []}
    ziua_data = []

    for index, row in enumerate(table.find_all('tr')[1:-1]):  # Ignoră prima linie dacă conține antete
        columns = row.find_all('td')
        data_zile[f'Ziua_{zile}'].append(columns[2].text.strip())

    data_total = {'NR. CRT': [], 'Judet': [], f'Ziua_{zile}': []}

    for index, row in enumerate(table.find_all('tr')[45:], start=45):
        columns = row.find_all('td')
        if len(columns) > 1:
            df_final.at[index, f'{zile}_12'] = columns[1].text.strip()
        else:
            df_final.at[index, f'{zile}_12'] = None

    df_total = pd.DataFrame(data_total)

    df_zi = pd.DataFrame(data_zile)
    df_zi.columns = [f'{zile}_12']

    df_zile[zile] = df_zi


#Lipeste primele 2 coloane facute in primul for cu coloanele pt fiecare luna
df_final = pd.concat([df_final] + list(df_zile.values()), axis=1)
#df_final = pd.merge(df_final, data_total, on=['NR. CRT', 'Judet'], how='left')

print(df_final.to_string(index=False))
