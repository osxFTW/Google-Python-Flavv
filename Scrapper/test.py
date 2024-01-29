import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-10-decembrie-ora-13-00-2/")
link = BeautifulSoup(r.text, 'html.parser')

table = link.find('table')
data = {'NR. CRT': [], 'Judet': []}

for index, row in enumerate(table.find_all('tr')[1:], start=1):
    columns = row.find_all('td')
    data['NR. CRT'].append(str(index))
    data['Judet'].append(columns[1].text.strip())

df_final = pd.DataFrame(data)

df_zile = {}

for zile in range(10, 15):
    r = requests.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{zile}-decembrie-ora-13-00-2/")
    link = BeautifulSoup(r.text, 'html.parser')

    table = link.find('table')
    data_zile = {f'Ziua_{zile}': []}

    for index, row in enumerate(table.find_all('tr')[1:], start=1):
        columns = row.find_all('td')
        judet = columns[1].text.strip()
        cazuri_noi = columns[2].text.strip()

        # Tratează cazul special "Cazuri noi nealocate pe județe"
        if judet == "Cazuri noi nealocate pe județe":
            total_value = table.find_all('tr')[-1].find_all('td')[1].text.strip()
            cazuri_noi = total_value  # Folosește valoarea totală

        # Verifică dacă cazurile noi pot fi convertite în număr
        try:
            cazuri_noi = int(cazuri_noi.replace('*', '').replace('.', ''))  # Elimină "*" și "."
        except ValueError:
            cazuri_noi = 0  # Setează la 0 în cazul în care conversia eșuează

        data_zile[f'Ziua_{zile}'].append(cazuri_noi)

    df_zi = pd.DataFrame(data_zile)
    df_zi.columns = [f'{zile}_12_{i}' for i in range(len(data_zile[f"Ziua_{zile}"]))]

    df_zile[zile] = df_zi

# Lipește primele 2 coloane făcute în primul for cu coloanele pentru fiecare lună
df_final = pd.concat([df_final] + list(df_zile.values()), axis=44)

# Calculăm totalurile pentru fiecare zi
for zile in range(10, 15):
    total_value = df_final[f'{zile}_12'].astype(float).sum()
    df_final[f'TOTAL_{zile}'] = [total_value] * len(df_final)

# Afișează dataframe-ul final
print(df_final.to_string(index=False))
