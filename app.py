from bs4 import BeautifulSoup
import requests
import re

def isFloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

query = raw_input("Textbook: ").replace(" ", "-")
location = raw_input("Location (mississauga/waterloo): ")

BASE_URL = "http://www.kijiji.ca/b-books/"
LOCATION = ""
ENDING = ""

if (location == "mississauga"):
    LOCATION = "mississauga-peel-region/"
    ENDING = "/k0c109l1700276?sort=priceAsc"
else:
    LOCATION = "kitchener-waterloo/"
    ENDING = "/k0c109l1700212?sort=priceAsc"

GREEN = '\033[92m'
RED = '\033[91m'
WHITE = '\033[0m'

response = requests.get(BASE_URL + LOCATION + query + ENDING)
print(BASE_URL + LOCATION + query + ENDING)
soup = BeautifulSoup(response.content, "html.parser")

results = soup.find('div', attrs={"class":"container-results"})

for searchItem in results.findAll('div', attrs={"class": "search-item regular-ad"}):
    title = searchItem.find('div', attrs={"class": "title"})
    desc = title.get_text().strip()
    price = searchItem.find('div', attrs={"class": "price"}).get_text().strip()
    if (isFloat(price[1:])):
        link = "www.kijiji.ca" + title.find('a').get('href')
        print(desc + "\t" +
            GREEN+price+WHITE + "\t" +
            RED+link+WHITE )
