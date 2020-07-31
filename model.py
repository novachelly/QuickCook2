import requests


# def getRecipeFromIngredients(ingredients, number, key):
#     search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
#     data = requests.get(search_url)
#     recipe_info = data.json()
#     recipe_id = []
#     # for recipe in recipe_info:
#     #     recipe_id.append(recipe['id'])
#     # missedIngredients = recipe_info[0]['missedIngredients']
#     # recipe = {'title': recipe_info[0]['title'],
#     #           'img': recipe_info[0]['image'],
#     #           'id_number': recipe_info[id]
#     #           'missedIngredients': missedIngredients}
#     # return recipe_ids
#     return recipe_info[0]['id']


# # def getRecipeFromIngredients1(ingredients, number, key):
# #     search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
# #     data = requests.get(search_url)
# #     recipe_info = data.json()
# #     missedIngredients1 = recipe_info[1]['missedIngredients']
# #     recipe1 = {'title': recipe_info[1]['title'],
# #                'img': recipe_info[1]['image'],
# #                'missedIngredients': missedIngredients1}
# #     return getRecipeFromIngredients1


# def getRecipeInfo(id_number, key):
#     search_url = "https://api.spoonacular.com/recipes/" + id_number + "/analyzedInstructions?apiKey=" + key
#     data = requests.get(search_url)
#     recipe_info = data.json()
#     return recipe_info


def getRecipeFromIngredients(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[0]["id"]


def getRecipeInfo(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients1(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[1]["id"]


def getRecipeInfo1(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients2(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[2]["id"]


def getRecipeInfo2(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients3(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[3]["id"]


def getRecipeInfo3(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients4(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[4]["id"]


def getRecipeInfo4(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients5(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[5]["id"]


def getRecipeInfo5(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients6(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[6]["id"]


def getRecipeInfo6(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients7(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[7]["id"]


def getRecipeInfo7(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients8(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[8]["id"]


def getRecipeInfo8(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients9(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[9]["id"]


def getRecipeInfo9(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info


def getRecipeFromIngredients10(ingredients, number, key):
    search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + ingredients + "&number=" + number
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info[10]["id"]


def getRecipeInfo10(id_number, key):
    search_url = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    # search_url = f'https://api.spoonacular.com/recipes/{id_number}/information?apiKey={key}'
    data = requests.get(search_url)
    recipe_info = data.json()
    return recipe_info
