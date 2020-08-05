from flask import Flask, render_template
from flask import request
from datetime import datetime
import os
import requests
from model import getRecipeFromIngredients
from model import getRecipeInfo
# from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['SPOON_KEY'] = os.getenv('SPOON_KEY')
# app.config['MONGO_DBNAME'] = 'QuickCook'
# app.cofig['MONGO_URI'] = ''

# mongo = PyMongo(app)


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
        recipes = []
        for x in range(0, int(number)):
            recipe_id = getRecipeFromIngredients(query, number, key, search_url, x)
            recipe_info = getRecipeInfo(recipe_id, key)
            recipes.append(recipe_info)
        return render_template('recipes_results.html', query=query, recipes=recipes, time=datetime.now())
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
        return render_template('/signin.html', time=datetime.now())
    else:
        print("no")


@app.route('/forgot_password')
def forgot_password():
    return render_template('/forgot_password.html', time=datetime.now())


@app.route('/forgot_username')
def forgot_username():
    return render_template('/forgot_username.html', time=datetime.now())


@app.route('/donate')
def donate():
    return render_template('/donate.html', time=datetime.now())


@app.route('/signin_results')
def signin_results():
    return render_template('/signin_results.html', time=datetime.now())


@app.route('/register_results')
def register_results():
    return render_template('register_results.html', time=datetime.now())


@app.route('/donate_results')
def donate_results():
    return render_template('donate_results.html', time=datetime.now())


@app.route('/submit_recipes', methods=['GET', 'POST'])
def submit_recipes():
    return render_template('submit_recipes.html', time=datetime.now())


@app.route('/submit_recipes_results', methods=['GET', 'POST'])
def submit_recipes_results():
    return render_template('submit_recipes_results.html', time=datetime.now())
