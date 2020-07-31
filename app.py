
from flask import Flask, render_template
from flask import request
from datetime import datetime
from model import getRecipeFromIngredients, getRecipeInfo, getRecipeFromIngredients1, getRecipeInfo1, getRecipeFromIngredients2, getRecipeInfo2, getRecipeFromIngredients3, getRecipeInfo3, getRecipeFromIngredients4, getRecipeInfo4, getRecipeFromIngredients5, getRecipeInfo5, getRecipeFromIngredients6, getRecipeInfo6, getRecipeFromIngredients7, getRecipeInfo7, getRecipeFromIngredients8, getRecipeInfo8, getRecipeFromIngredients9, getRecipeInfo9, getRecipeFromIngredients10, getRecipeInfo10
import os


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


# @app.route('/recipes_results', methods=['GET', 'POST'])
# def recipes_results():
#     if request.method == 'POST':
#         query = request.form['ingredients']
#         key = app.config['SPOON_KEY']
#         number = request.form['number']
#         # recipe_ids = getRecipeFromIngredients(query, number, key)
#         recipe_id = getRecipeFromIngredients(query, number, key)
#         recipe_info = getRecipeInfo(recipe_id, key)
#         # recipes = getRecipeFromIngredients(query, number, key)
#         # for
#         # recipes1 = getRecipeFromIngredients1(query, number, key)
#         return render_template('recipes_results.html', query=query, number=number, recipe_id=recipe_id, recipe_info=recipe_info)
@app.route('/recipes_results', methods=['GET', 'POST'])
def recipes_results():
    if request.method == 'POST':
        query = request.form['ingredients']
        key = app.config['SPOON_KEY']
        number = request.form['number']
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
        print(recipe_info)
        return render_template('recipes_results.html', query=query, recipe_info=recipe_info, recipe_info1=recipe_info1, recipe_info2=recipe_info2, recipe_info3=recipe_info3, recipe_info4=recipe_info4, recipe_info5=recipe_info5, recipe_info6=recipe_info6, recipe_info7=recipe_info7, recipe_info8=recipe_info8, recipe_info9=recipe_info9, recipe_info10=recipe_info10)


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
# <!-- <h4>You need these ingredients: </h4>
#         {%for ingredient in recipes.missedIngredients:%}
#         {%endfor%}
#          -->
