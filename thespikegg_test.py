from bs4 import BeautifulSoup
import requests


html_doc = requests.get("https://www.thespike.gg/player/tenz/265").content
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find(class_="stat-bar-wrap").prettify)
