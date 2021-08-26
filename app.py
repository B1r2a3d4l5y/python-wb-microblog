import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://Bradley:0810200BradleyArnold@microblog-app.ucno1.mongodb.net/test",
                         ssl=True, ssl_cert_reqs='CERT_NONE')
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")

    entries_with_date = [
                (
                    entry["content"],
                    entry["date"],
                    datetime.datetime.strptime(
                        entry["date"], "%Y-%m-%d").strftime("%b %d")
                )
                for entry in app.db.entries.find({})
            ]

    return render_template("home.html", entries=entries_with_date)

    return app
                 



            
