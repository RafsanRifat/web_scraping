import requests
from bs4 import BeautifulSoup

source = "https://boomdevs.com/product-category/html-templates/"
html_data = requests.get(source).text

soup = BeautifulSoup(html_data, "html.parser")

main_div = soup.find(id='main')

all_li = main_div.find_all('li', class_='sales-flash-overlay')
for title in all_li:
    print(title.a.h2.text)

templates = main_div.find_all(text='Restaurant')
print(templates)
