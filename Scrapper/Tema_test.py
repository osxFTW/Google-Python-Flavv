import requests
from bs4 import BeautifulSoup
import pandas as pd


# Function to scrape data for a given date and create a DataFrame
def scrape_data(date):
    url = f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{date}-decembrie-ora-13-00-2/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')

        data = {'NR. CRT': [], 'Judet': [], f'Ziua_{date}': []}

        for index, row in enumerate(table.find_all('tr')[1:], start=1):
            columns = row.find_all('td')
            data['NR. CRT'].append(str(index))  # Use a consistent NR. CRT across all dates
            data['Judet'].append(columns[1].text.strip())
            data[f'Ziua_{date}'].append(columns[2].text.strip())

        df = pd.DataFrame(data)
        return df
    else:
        print(f"Failed to fetch data for {date}")
        return None


# List of dates to scrape
dates = ['10', '11', '12', '13', '14']

# Create an empty DataFrame with the desired columns
final_table = pd.DataFrame()

# Loop through dates, scrape data, and append to the final table
for date in dates:
    df = scrape_data(date)
    if df is not None:
        # Update 'NR. CRT' and 'Judet' columns in the final table
        final_table = pd.concat([final_table, df.set_index(['NR. CRT', 'Judet'])], axis=1, sort=False)

# Reset the index to include 'NR. CRT' and 'Judet' as regular columns
final_table = final_table.reset_index()

# Reorder the columns to have 'NR. CRT' as the first column
final_table = final_table[
    ['NR. CRT', 'Judet'] + [col for col in final_table.columns if col not in ['NR. CRT', 'Judet']]]

# Drop duplicate columns manually
final_table = final_table.loc[:, ~final_table.columns.duplicated()]

# Add the "Total" row from the last row of the main data table
total_row = final_table.iloc[-1].tolist()
final_table.loc[len(final_table)] = total_row

# Export the final table to Excel
final_table.to_excel("covid_data_table_modified_single_nr_crt.xlsx", index=False)