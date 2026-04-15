from flask import Flask, request, render_template

# Create the Flask application
app = Flask(__name__)

# Route 1: Show the input form
@app.route("/")
def show_form():
    return render_template("form.html")

# Route 2: Receive form data and display the profile
@app.route("/profile", methods=["POST"])
def show_profile():
    name  = request.form["name"]
    age   = request.form["age"]
    city  = request.form["city"]
    hobby = request.form["hobby"]
    return render_template("profile.html",
                           name=name,
                           age=age,
                           city=city,
                           hobby=hobby)

if __name__ == "__main__":
    app.run(debug=True)
