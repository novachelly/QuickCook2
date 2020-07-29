import requests


def getImageUrlFrom(query, key):
    search_url = "https://api.edamam.com/search"
    data = requests.get("https://api.edamam.com/search")
    recipe_info = data.json()
    img_url = recipe_info['data'][0]['images']['original']['url']
    print (img_url)
    return img_url
