from dotenv import load_dotenv
from pymongo import MongoClient
from flask import Flask, render_template, request
import datetime

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient("mongodb+srv://Bradley:0810200BradleyArnold@microblog-app.ucno1.mongodb.net/test",ssl=True, ssl_cert_reqs='CERT_NONE')
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert({"content": entry_content,"date": formatted_date})
        
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date","%Y-%m_%d"]).strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries = entries_with_date)

    return app
