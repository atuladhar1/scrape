from cgitb import handler
from http.client import ResponseNotReady
from operator import truediv
from bs4 import BeautifulSoup
import requests

chapter = "964"
url = f"https://ww5.manganelo.tv/chapter/manga-jn986670/chapter-{chapter}"

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

request = requests.get(url, headers=headers)

soup = BeautifulSoup( request.content ,'html.parser')

# Dig down to div that holds all the images
body_site = soup.find("div", {"class" : "body-site"})
chapter_container = body_site.find("div", {"class": "container-chapter-reader"})

# find all images and and save them in imageHolder
imageHolder = chapter_container.find_all("img")

for num,i in enumerate(imageHolder):
    imgurl = i['data-src']
    # if imgurl exists make network call and retrieve it and save it in "{chaptername}_{imagenumber}.jpg"
    if imgurl is not None:
        response = requests.get(imgurl)
        if response.status_code == 200:
            with open(f"{chapter}_{num}.jpg",'wb') as handler:
                handler.write(response.content)