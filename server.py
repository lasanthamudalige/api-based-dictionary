from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TOKEN = "Token fc0d5b9f1129ef3cd87d2000bc5a2f54e9952d5d"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        word = request.form.get("word")
        data = look_up(word)

        found = None
        try:
            if data["word"]:
                found = True
        except TypeError:
            found = False

        return render_template("index.html", found=found, data=data)

    return render_template("index.html")


def look_up(word):
    url = f"https://owlbot.info/api/v4/dictionary/{word}"
    response = requests.get(url=url, headers={"Authorization": TOKEN})
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
