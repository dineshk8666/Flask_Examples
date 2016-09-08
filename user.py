from flask import Flask, render_template

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return " This is my home page "

@app.route("/profile/")
@app.route("/profile/<user>")
def profile(user=None):
    return render_template("user.html", user=user)

@app.route("/shopping")
def shoping():
    grocerry_items=["Book", "Pencil", "Pen", "Notebook", "Ink"]
    return render_template("shopping.html", items=grocerry_items)
    

if __name__ == "__main__":
    app.run(debug=True)
