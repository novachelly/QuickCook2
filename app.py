from flask import Flask, render_template
from flask import request
from datetime import datetime
import os
import requests
from model import getRecipeFromIngredients
from model import getRecipeInfo

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
        search_url = "https://api.spoonacular.com/recipes/findByIngredients?apiKey=" + \
            key + "&ingredients=" + query + "&number=" + number

        recipe_id = getRecipeFromIngredients(query, number, key, search_url, 0)
        recipe_info = getRecipeInfo(recipe_id, key)
        recipe_id1 = getRecipeFromIngredients(query, number, key, search_url, 1)
        recipe_info1 = getRecipeInfo(recipe_id1, key)
        recipe_id2 = getRecipeFromIngredients(query, number, key, search_url, 2)
        recipe_info2 = getRecipeInfo(recipe_id2, key)
        recipe_id3 = getRecipeFromIngredients(query, number, key, search_url, 3)
        recipe_info3 = getRecipeInfo(recipe_id3, key)
        recipe_id4 = getRecipeFromIngredients(query, number, key, search_url, 4)
        recipe_info4 = getRecipeInfo(recipe_id4, key)
        recipe_id5 = getRecipeFromIngredients(query, number, key, search_url, 5)
        recipe_info5 = getRecipeInfo(recipe_id5, key)
        recipe_id6 = getRecipeFromIngredients(query, number, key, search_url, 6)
        recipe_info6 = getRecipeInfo(recipe_id6, key)
        recipe_id7 = getRecipeFromIngredients(query, number, key, search_url, 7)
        recipe_info7 = getRecipeInfo(recipe_id7, key)
        recipe_id8 = getRecipeFromIngredients(query, number, key, search_url, 8)
        recipe_info8 = getRecipeInfo(recipe_id8, key)
        recipe_id9 = getRecipeFromIngredients(query, number, key, search_url, 9)
        recipe_info9 = getRecipeInfo(recipe_id9, key)
        return render_template('recipes_results.html', query=query, recipe_info=recipe_info, recipe_info1=recipe_info1, recipe_info2=recipe_info2, recipe_info3=recipe_info3, recipe_info4=recipe_info4, recipe_info5=recipe_info5, recipe_info6=recipe_info6, recipe_info7=recipe_info7, recipe_info8=recipe_info8, recipe_info9=recipe_info9, time=datetime.now())
    else:
        return "no"


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
