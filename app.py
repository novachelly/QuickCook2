
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


app.run('0.0.0.0',8080)


@app.route('/recipes', methods=['GET','POST'])
def recipes():
  if request.method == "GET":
    return render_template('recipes.html')

@app.route('/aboutus')
def aboutus():
  return "Whatever we say"

@app.route('/shoppingcart')
def shoppingcart():
  return "Shopping Cart"

@app.route('/downloadQuickCook')
def download():
  return "Download"

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('register.html')
  else:
    print"eek"
@app.route('/signin')