from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    title = "Daniel Portifólio"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    names = ["John", "Mary"]
    return render_template("about.html")

@app.route('/subscribe')
def subscribe():
    title = "Subscribe"
    return render_template("subscribe.html", title=title)


@app.route('/form', methods=["POST"])
def form():
    email = request.form.get("email")
    senha = request.form.get("senha")
    title = "Thank you"
    return render_template("form.html", title=title, email=email, senha=senha)