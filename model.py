import requests
import app
from flask import request
# # from app import recipes_results

if request.method == 'POST':
    number = request.form['number']
if app.recipes_results.number >= 0:
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
        if app.recipes_results.number >= 1:
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
                if app.recipes_results.number >= 2:
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
                        if app.recipes_results.number >= 3:
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
                                if app.recipes_results.number >= 4:
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
                                        if recipes_results.number >= 5:
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
                                                if recipes_results.number >= 6:
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
                                                        if recipes_results.number >= 7:
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
                                                                if recipes_results.number >= 8:
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
                                                                        if recipes_results.number >= 9:
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
                                                                                if recipes_results.number >= 10:
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
                                                                                else:
                                                                                    print("Hope you found what you needed! :)")
                                                                        else:
                                                                            print("Hope you found what you needed! :)")
                                                                else:
                                                                    print("Hope you found what you needed! :)")
                                                        else:
                                                            print("Hope you found what you needed! :)")
                                                else:
                                                    print("Hope you found what you needed! :)")
                                        else:
                                            print("Hope you found what you needed! :)")
                                else:
                                    print("Hope you found what you needed! :)")
                        else:
                            print("Hope you found what you needed! :)")
                else:
                    print("Hope you found what you needed! :)")
        else:
            print("Hope you found what you needed! :)")
else:
    print("Hope you found what you needed! :)")
