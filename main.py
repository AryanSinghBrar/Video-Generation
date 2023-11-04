import requests
from bs4 import BeautifulSoup

url = "https://time.com/6315607/bryan-johnsons-quest-for-immortality/" # url of target website
html = requests.get(url) # This gets the html code of the TB (target website = TB)

s = BeautifulSoup(html.content, 'html.parser')
