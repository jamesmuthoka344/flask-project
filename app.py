from flask import Flask,render_template,request,flash

app = Flask(__name__)
app.secret_key = "jamie"

@app.route("/")
def index():
    flash("whats your name")
    return render_template("index.html")

@app.route("/greet", methods = ["POST","GET"])
def greet():
    flash("hi " + str(request.form["nm"])+ ",welcome here")
    return render_template("login.html")


if __name__== "__main__":
    app.run(debug = True)
