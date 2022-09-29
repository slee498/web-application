from crypt import methods
import imghdr
from flask import Flask,render_template, g,request,redirect
from flask import g
import sqlite3 
connect = sqlite3.connect("product.db")

# retrieving database
DATABASE = "product.db"
 
app = Flask(__name__)

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

# routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/product")
def product():
    cursor = get_db().cursor()
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("product.html", results=results)

@app.route("/product/<int:product_id>")
def showpost(product_id):
    cursor = get_db().cursor()
    sql = "SELECT * FROM product WHERE id=?"
    cursor.execute(sql, (product_id,))
    variable = cursor.fetchone()
    print(variable)
    return render_template("var.html", variable=variable)

@app.route("/learn")
def learn():
    return render_template("learn.html")


if __name__ == "__main__":
    app.run(debug=True)
