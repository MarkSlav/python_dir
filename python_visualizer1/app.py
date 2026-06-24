from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hello_name", methods=["POST"])
def hello():
    # On the web, the form replaces input("What's your name? ")
    name = request.form["name"]
    age = request.form["age"]
    city = request.form["city"]
    # Same idea as: print("Hello, " + name + "!")
    message = "Hello, " + name + "!"
    message1 = " You are " + age + " years old."
    message2 = " You live in " + city + "."
    return render_template(
        "result.html",
        name=name,
        age=age,
        city=city,
        message=message,
        message1=message1,
        message2=message2,
    )

if __name__ == "__main__":
    app.run(debug=True)