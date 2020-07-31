import requests


# def getImageUrlFrom(query, key):
#     search_url = "https://api.edamam.com/search"
#     data = requests.get("https://api.edamam.com/search")
#     recipe_info = data.json()
#     img_url = recipe_info['data'][0]['images']['original']['url']
#     print (img_url)
#     return img_url

def getRecipeFromIngredients(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    # recipe_name = recipe_info['data'][0]['name']['original']['url']
    # recipe_img =
    # recipe_link =
    # cuisine = cuisine
    # diet = diet
    # excludeIngredients = excludeIngredients
    # intolerances = intolerances
    # instructionsRequired = instructionsRequired
    # recipe_name =
    missedIngredients = recipe_info[0]['missedIngredients']
    recipe = {'title': recipe_info[0]['title'],
              'img': recipe_info[0]['image'],
              'missedIngredients': missedIngredients}
    return recipe


def getRecipeFromIngredients1(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    missedIngredients1 = recipe_info[1]['missedIngredients']
    recipe1 = {'title': recipe_info[1]['title'],
               'img': recipe_info[1]['image'],
               'missedIngredients': missedIngredients1}
    return recipe1
