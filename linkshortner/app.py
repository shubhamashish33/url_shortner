from flask import Flask, jsonify, render_template, request
import pyperclip
import pyshorteners

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    shortenurl = ""
    if request.method == "POST":
        url = request.form.get("urlrequest")
        shortener = pyshorteners.Shortener()
        x = shortener.tinyurl.short(url)
        pyperclip.copy(x)
        shortenurl = x
    return render_template("index.html", shortenurl=shortenurl)


if __name__ == "__main__":
    app.run()
