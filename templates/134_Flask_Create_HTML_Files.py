from flask import Flask, render_template

app_try = Flask(__name__)

@app_try.route("/")
def skills_app():
    name = "Seraj"
    return render_template("try_homepage.html", name=name)

@app_try.route("/but/<message>")
def but(message):
    return message

if __name__ == "__main__":
    app_try.run(debug=True, port=5000)