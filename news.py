from bs4 import BeautifulSoup
import requests
import json

link = 'https://gorod214.by/news'
response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')
block_img = soup.find_all('div', class_='img-new-two')
block_title = soup.find_all('div', class_='l-new')[0]

print(block_title)
