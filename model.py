import requests


# # from app import recipes_results


def getRecipeFromIngredients(query, number, key, search_url, recipe_number):
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[recipe_number]["id"]


def getRecipeInfo(id_number, key):
    search_url_recipe = "https://api.spoonacular.com/recipes/" + \
        str(id_number) + "/information?apiKey=" + key
    data = requests.get(search_url_recipe)
    recipe_info = data.json()
    return recipe_info





