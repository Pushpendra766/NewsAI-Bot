import requests
import urllib.request
from create_video import create_video

if __name__ == "__main__":
    url = "https://newsx.p.rapidapi.com/search"

    querystring = {"limit": "10", "skip": "0"}

    headers = {
        "X-RapidAPI-Key": "API_KEY",
        "X-RapidAPI-Host": "newsx.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())
    for i in range(5):
        image_url = response.json()[i]['image']  # the image on the web
        save_name = f'files/news_img{i}.jpg'  # local name to be saved
        urllib.request.urlretrieve(image_url, save_name)
        create_video(news_title = response.json()[i]['title'], news_summary=response.json()[i]['summary'], i=i)

