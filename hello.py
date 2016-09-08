from flask import Flask, render_template

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return " This is my home page "

@app.route("/profile/<name>")
def profile(name):
	return render_template("profile.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
