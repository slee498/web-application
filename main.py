from crypt import methods
import imghdr
from flask import Flask,render_template, g,request,redirect
from flask import g
import sqlite3 
connect = sqlite3.connect("product.db")
 
app = Flask(__name__)

# retrieving database
DATABASE = "product.db"
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# directs to a specific part of the application that is running rather than the whole app
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route("/")
# renders the home page. aka the first page the web browser opens up to
def home():
    return render_template("home.html")

@app.route("/product")
# this page displays contents from 'product' database
def product():
    # retrieves data from database
    cursor = get_db().cursor()
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("product.html", results=results)

@app.route("/product/<int:product_id>")
# extends from product.html, <int:product_id refers to id in database
def showpost(product_id):
    cursor = get_db().cursor()
    sql = "SELECT * FROM product WHERE id=?"
    cursor.execute(sql, (product_id,))
    variable = cursor.fetchone()
    # print(variable)
    return render_template("var.html", variable=variable)

@app.route("/learn")
# this route will direct to the learn page
def learn():
    return render_template("learn.html")

# source file
if __name__ == "__main__":
    app.run(debug=True)
