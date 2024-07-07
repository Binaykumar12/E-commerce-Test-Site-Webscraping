import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r= requests.get(url)


soup= BeautifulSoup(r.text,"lxml")

names = soup.find_all("a",class_ ="title")
for i in names:
  print(i.text)

prices = soup.find_all("h4",class_ ="price")
for i in prices:
   print(i.text)