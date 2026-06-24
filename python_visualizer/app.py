from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def hello():
    # On the web, the form replaces input("What's your name? ")
    name = request.form["name"]

    # Same idea as: print("Hello, " + name + "!")
    message = "Hello, " + name + "!"

    return render_template(
        "result.html",
        name=name,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True)
