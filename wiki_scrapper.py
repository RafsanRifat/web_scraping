import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')

table = soup.find('table', class_='wikitable')

state_names = []
all_th = table.find_all('th')
for th in all_th:
    all_a = th.find_all('a')
    for a in all_a:
        state_names.append(a.string)

final_list1 = state_names[9: ]

final_list = []

for name in final_list1:
    if len(name) > 3:
        final_list.append(name)

# print(final_list)

df = pd.DataFrame()
df['state'] = final_list
df.to_csv('us_info.csv')
print(df)
