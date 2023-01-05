import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Y7a2fnZByUl"
html_page = requests.get(url)

soup = BeautifulSoup(html_page.content, 'html.parser')

seven_day = soup.find(id='seven-day-forecast')

tombstone_container = seven_day.find_all(class_="tombstone-container")
tonight = tombstone_container[0]

# getting data from tonight
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
img = tonight.find('img', class_="forecast-icon")
image = img['title']

# print(period, short_desc, image)

period_tags = seven_day.select(".tombstone-container .period-name")
period = [pt.get_text() for pt in period_tags]
# print(period)

period = [pt.get_text() for pt in seven_day.select(".tombstone-container .period-name")]
short_desc = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
image = [img['title'] for img in seven_day.select(".tombstone-container .forecast-icon")]

# print(period)
# print(short_desc)
# print(image)

import pandas as pd

weather = pd.DataFrame({
    "period": period,
    "short_desc": short_desc,
    "image": image
})

weather.to_csv('weather.csv')
print(weather)
