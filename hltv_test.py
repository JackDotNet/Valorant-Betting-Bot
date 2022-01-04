from bs4 import BeautifulSoup
import requests

c = requests.get("https://www.hltv.org/stats/players?startDate=2020-06-27&endDate=2021-06-27").content
soup = BeautifulSoup(c, 'html.parser')
print(soup.prettify())
