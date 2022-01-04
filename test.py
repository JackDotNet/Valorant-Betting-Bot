from bs4 import BeautifulSoup
import requests

html_doc = requests.get("https://esports.leetify.com/stats").content
soup = BeautifulSoup(html_doc, 'html_parser')
print(soup.prettify)