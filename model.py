import requests


def getImageUrlFrom(query, key):
    search_url = "https://spoonacular.com/recipeImages/" + ID + "-" + SIZE + "." + TYPE
    # 90x90
    # 240x150
    # 312x150
    # 312x231
    # 480x360
    # 556x370
    # 636x393
    data = requests.get("https://api.spoonacular.com/recipes/complexSearch")
    recipe_info = data.json()
    img_url = recipe_info['data'][0]['images']['original']['url']
    print (img_url)
    return img_url
