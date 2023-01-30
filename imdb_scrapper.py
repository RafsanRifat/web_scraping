import requests
from bs4 import BeautifulSoup

""" 
Required data ------->>>
 
"""

url = "https://www.imdb.com/search/title/?release_date=2017&amp&sort=num_votes,desc&amp&page=1"
html_data = requests.get(url)

# html data into text
html_data_into_text_form = html_data.text

# parse text data using Beautifulsoup
soup = BeautifulSoup(html_data_into_text_form, 'html.parser')

# find movie div
movie_containers = soup.find_all('div', class_='lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))
