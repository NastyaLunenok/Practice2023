import requests
from loguru import logger
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def checkURL(link):
    result=urlparse(link)
    
    if result.scheme!="https":
        return False
    
    if result.netloc!='music.yandex.ru':
        return False
    
    path=result.path.split("/")
    if len(path)!=3:
        return False
    
    if path[1]!="artist":
        return False
    
    if not(path[2].isdigit()):
        return False
    
    return True


def getTopTracks(link):
    if not(checkURL(link)):
        logger.error("Некорректная ссылка (пример: https://music.yandex.ru/artist/xxxxxx)")
        return
    try:
        response = requests.get(link)
            
    except requests.exceptions.RequestException as e:
        logger.error(e)
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    if soup.find('div', class_='page-404')!=None or soup.find('div', class_='page-500')!=None:
        logger.error("Страница не найдена")
        return

    artist = soup.find('h1', class_='page-artist__title').text
    print(f"Топ 10 песен {artist} на сервисе Yandex Music: ")
    print("-"*50)
    number_tracks = 10
    tracks = soup.find_all('div', class_='d-track')[:number_tracks]
    if len(tracks)==0:
        print("У данного исполнителя нет песен")
        
    k=1
    for track in tracks:
        title = track.find('a', class_='d-track__title').text.strip()
        print(f"{k:2}. {title}")
        k+=1


linkOnTracks = input("Вставьте ссылку на исполнителя в сервисе Yandex Music: ")
getTopTracks(linkOnTracks)
