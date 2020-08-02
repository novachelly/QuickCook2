from flask import Flask, render_template
from flask import request
from datetime import datetime
import os
import requests


app = Flask(__name__)
app.config['SPOON_KEY'] = os.getenv('SPOON_KEY')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())


if __name__ == "__main__":
    app.run('0.0.0.0', 8080)


@app.route('/recipes')
def recipes():
    return render_template('recipes.html', time=datetime.now())


@app.route('/recipes_results', methods=['GET', 'POST'])
def recipes_results():
    if request.method == 'POST':
        number = request.form['number']
        # number_ask = 10
        query = request.form['ingredients']
        key = app.config['SPOON_KEY']
        search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + key + "&ingredients=" + query + "&number=10" # + number

        def getRecipeFromIngredients(query, number, key):
            data = requests.get(search_url)
            recipe_info = data.json()
            return recipe_info[0]["id"]

        def getRecipeInfo(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info = data.json()
            return recipe_info

        def getRecipeFromIngredients1(query, number, key):
            data = requests.get(search_url)
            recipe_info1 = data.json()
            return recipe_info1[1]["id"]

        def getRecipeInfo1(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info1 = data.json()
            return recipe_info1

        def getRecipeFromIngredients2(query, number, key):
            data = requests.get(search_url)
            recipe_info2 = data.json()
            return recipe_info2[2]["id"]

        def getRecipeInfo2(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info2 = data.json()
            return recipe_info2

        def getRecipeFromIngredients3(query, number, key):
            data = requests.get(search_url)
            recipe_info3 = data.json()
            return recipe_info3[3]["id"]

        def getRecipeInfo3(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info3 = data.json()
            return recipe_info3

        def getRecipeFromIngredients4(query, number, key):
            data = requests.get(search_url)
            recipe_info4 = data.json()
            return recipe_info4[4]["id"]

        def getRecipeInfo4(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info4 = data.json()
            return recipe_info4

        def getRecipeFromIngredients5(query, number, key):
            data = requests.get(search_url)
            recipe_info5 = data.json()
            return recipe_info5[5]["id"]

        def getRecipeInfo5(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info5 = data.json()
            return recipe_info5

        def getRecipeFromIngredients6(query, number, key):
            data = requests.get(search_url)
            recipe_info6 = data.json()
            return recipe_info6[6]["id"]

        def getRecipeInfo6(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info6 = data.json()
            return recipe_info6

        def getRecipeFromIngredients7(query, number, key):
            data = requests.get(search_url)
            recipe_info7 = data.json()
            return recipe_info7[7]["id"]

        def getRecipeInfo7(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info7 = data.json()
            return recipe_info7

        def getRecipeFromIngredients8(query, number, key):
            data = requests.get(search_url)
            recipe_info8 = data.json()
            return recipe_info8[8]["id"]

        def getRecipeInfo8(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info8 = data.json()
            return recipe_info8

        def getRecipeFromIngredients9(query, number, key):
            data = requests.get(search_url)
            recipe_info9 = data.json()
            return recipe_info9[9]["id"]

        def getRecipeInfo9(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info9 = data.json()
            return recipe_info9

        def getRecipeFromIngredients10(query, number, key):
            data = requests.get(search_url)
            recipe_info10 = data.json()
            return recipe_info[10]["id"]

        def getRecipeInfo10(id_number, key):
            search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
            data = requests.get(search_url_recipe)
            recipe_info10 = data.json()
            return recipe_info10
        # def getMissedIngredients(query, number, key):
        #     data = requests.get(search_url)
        #     recipe_info = data.json()
        #     missedIngredients = [recipe_info[0]["missedIngredients"]]  # [5]["name"],
        #                         # recipe_info[0]["missedIngredients"][1]["amount"],
        #                         # recipe_info[0]["missedIngredients"][9]["unitLong"]]
            # return missedIngredients
        recipe_id = getRecipeFromIngredients(query, number, key)
        recipe_info = getRecipeInfo(recipe_id, key)
        recipe_id1 = getRecipeFromIngredients1(query, number, key)
        recipe_info1 = getRecipeInfo1(recipe_id1, key)
        recipe_id2 = getRecipeFromIngredients2(query, number, key)
        recipe_info2 = getRecipeInfo2(recipe_id2, key)
        recipe_id3 = getRecipeFromIngredients3(query, number, key)
        recipe_info3 = getRecipeInfo3(recipe_id3, key)
        recipe_id4 = getRecipeFromIngredients4(query, number, key)
        recipe_info4 = getRecipeInfo4(recipe_id4, key)
        recipe_id5 = getRecipeFromIngredients5(query, number, key)
        recipe_info5 = getRecipeInfo5(recipe_id5, key)
        recipe_id6 = getRecipeFromIngredients6(query, number, key)
        recipe_info6 = getRecipeInfo6(recipe_id6, key)
        recipe_id7 = getRecipeFromIngredients7(query, number, key)
        recipe_info7 = getRecipeInfo7(recipe_id7, key)
        recipe_id8 = getRecipeFromIngredients8(query, number, key)
        recipe_info8 = getRecipeInfo8(recipe_id8, key)
        recipe_id9 = getRecipeFromIngredients9(query, number, key)
        recipe_info9 = getRecipeInfo9(recipe_id9, key)
        recipe_id10 = getRecipeFromIngredients10(query, number, key)
        recipe_info10 = getRecipeInfo10(recipe_id10, key)
        return render_template('recipes_results.html', query=query, recipe_info=recipe_info, recipe_info1=recipe_info1, recipe_info2=recipe_info2, recipe_info3=recipe_info3, recipe_info4=recipe_info4, recipe_info5=recipe_info5, recipe_info6=recipe_info6, recipe_info7=recipe_info7, recipe_info8=recipe_info8, recipe_info9=recipe_info9, recipe_info10=recipe_info10, time=datetime.now())
    else:
        return "no"
        # missedIngredients = getMissedIngredients(query, number, key)
        #For if the consumer wants to decide how many recipes they want
        # if int(number) == 1:
    #         return render_template('recipes_results.html', query=query, number, recipe_info=recipe_info, time=datetime.now())
    #     else:
    #         def getRecipeFromIngredients1(ingredients, number, key):
    #             data = requests.get(search_url)
    #             recipe_info = data.json()
    #             return recipe_info[1]["id"]

    #         def getRecipeInfo1(id_number, key):
    #             search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    #             data = requests.get(search_url_recipe)
    #             recipe_info1 = data.json()
    #             return recipe_info1
    #    id_number1 = getRecipeFromIngredients1(query, number, number, key)
    #         recipe_info1 = getRecipeInfo1(id_number1, key)
    #         if int(number) == 2:
    #             return render_template('recipes_results.html', query=query, number, recipe_info=recipe_info, recipe_info1=recipe_info1, time=datetime.now())
    #         else:
    #             def getRecipeFromIngredients2(ingredients, number, key):
    #                 data = requests.get(search_url)
    #                 recipe_info = data.json()
    #                 return recipe_info[2]["id"]

    #             def getRecipeInfo2(id_number, key):
    #                 search_url_recipe = "https://api.spoonacular.com/recipes/" + str(id_number) + "/information?apiKey=" + key
    #                 data = requests.get(search_url_recipe)
    #                 recipe_info2 = data.json()
    #                 return recipe_info2
    #        id_number2 = getRecipeFromIngredients2(query, number, number, key)
    #             recipe_info2 = getRecipeInfo2(id_number2, key)
    #             if int(number) == 3:
    #                 return render_template('recipes_results.html', query=query, number, recipe_info=recipe_info, recipe_info1=recipe_info1, recipe_info2=recipe_info2, time=datetime.now())
    #             else:
    #                 print ("no no")
    # else:
    #     return "no"


# @app.route('/print_recipes', methods=['GET', 'POST'])
# def print_recipes():
#     number = request.form['number']
#     recipe_dict = [("recipe": )]


@app.route('/contactus')
def contactus():
    return render_template('contactus.html', time=datetime.now())


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', time=datetime.now())


@app.route('/downloadQuickCook')
def download():
    return "Download"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', time=datetime.now())
    else:
        print("eek")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('/signin.html')
    else:
        print("no")


@app.route('/forgot_password')
def forgot_password():
    return render_template('/forgot_password.html')


@app.route('/forgot_username')
def forgot_username():
    return render_template('/forgot_username.html')


@app.route('/donate')
def donate():
    return render_template('/donate.html')
