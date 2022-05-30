from crypt import methods
from flask import Flask,render_template, g,request,redirect
from flask import g
import sqlite3 
connect = sqlite3.connect("product.db")

DATABASE = "product.db"
 
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

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

@app.route("/product")
def product():
    cursor = get_db().cursor()
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("product.html", results=results)

@app.route("/add", methods=("GET","POST"))
def add():
    if request.method == "POST":
        cursor = get_db().cursor()
        new_product = request.form["product_name"]
        new_price = request.form["product_price"]
        sql = "INSERT INTO product(name, price) VALUES (?,?)"
        cursor.execute(sql,(new_product,new_price))
        get_db().commit()
    return redirect("/product")

@app.route("/delete", methods=("GET","POST"))
def delete():
    if request.method == "POST":
        cursor = get_db().cursor()
        id = int(request.form["product_name"])
        sql = "DELETE FROM product WHERE id=?"
        cursor.execute(sql,(id,))
        get_db().commit()
    return redirect("/product")

@app.route("/news")
def news():
    return render_template("news.html")

if __name__ == "__main__":
    app.run(debug=True)
