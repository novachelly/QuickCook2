
from flask import Flask, render_template
from flask import request
from datetime import datetime
from model import getRecipeFromIngredients
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



@app.route('/recipes_results', methods=['GET', 'POST'])
def recipes_results():
    if request.method == 'POST':
        query = request.form['recipes']
        key = app.config['SPOON_KEY']
        img_link = getImageUrlFrom(query, key)
        return render_template('recipes_results.html', time=datetime.now())


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
