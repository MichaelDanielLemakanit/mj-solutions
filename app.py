from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for the App page
@app.route("/app")
def app_page():
    return render_template("app.html")

# Route for the Beauty page
@app.route("/beauty")
def beauty():
    return render_template("beauty.html")

# Route for the Printing page
@app.route("/printing")
def printing():
    return render_template("printing.html")

# Route for the Sofware page
@app.route("/software")
def software():
    return render_template("software.html")

# cleaning route
@app.route("/cleaning")
def cleaning():
    return render_template("cleaning.html")

# Dynamic Route Example (e.g., user profiles)
@app.route("/user/<username>")
def user_profile(username):
    return f"<h1>Welcome to {username}'s profile!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
app = app