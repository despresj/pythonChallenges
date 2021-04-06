from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.imdb.com/chart/top'
page = requests.get(URL)
soup = BeautifulSoup(page.text)
movies = soup.select('.titleColumn a') 
movies

titles = [title.text for title in movies]

movies_links = ["http://imdb.com"+ title["href"] for title in movies]
movies_links

def movie_grabber(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.text)
    text = soup.find_all('script')
    return(text)

meta = movie_grabber(movies_links[0])

meta

movie_grabber(URL=movies_links[0])

first = meta.select('input')[0].get('value')
print(first)

for tag in soup.find_all("h4"):
    if tag.get("property", None) == "og:title":
        print(tag.get("content", None))
    elif tag.get("property", None) == "og:url":
        print(tag.get("content", None))

[a for a in soup.find_all('meta')]