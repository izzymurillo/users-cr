from flask import Flask, render_template, request, redirect

from user_model import User

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route("/")
def index():
    return render_template("create.html")

@app.route("/users/new")
def new_user_page():
    return render_template("create.html")


@app.route("/users/create", methods = ["POST"])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect("/users")

@app.route("/users")
def show_all():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)