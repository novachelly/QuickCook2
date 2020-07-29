import requests


# def getImageUrlFrom(query, key):
#     search_url = "https://api.edamam.com/search"
#     data = requests.get("https://api.edamam.com/search")
#     recipe_info = data.json()
#     img_url = recipe_info['data'][0]['images']['original']['url']
#     print (img_url)
#     return img_url

def getRecipeFromIngredients(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey="+key+"&ingredients="+ ingredients + "&number="+ number
    data = requests.get(search_url)
    recipe_info = data.json()
    # recipe_name =
    # recipe_img =
    # recipe_link =
    print (recipe_info)

getRecipeFromIngredients("tomato, cheese", "25")