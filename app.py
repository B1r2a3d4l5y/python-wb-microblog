from dotenv import load_dotenv
from pymongo import MongoClient
from flask import Flask, render_template, request
import datetime

load_dotenv()


def create_app():
    app = Flask(__name__)
    client = MongoClient("mongogodb+srv://Bradleymongodb+srv://Bradley:Bradley08102000Arnold@microblog-app.ucno1.mongodb.net/Microblog-app retryWrites=true&w=majority:@microblog-app.ucno1.mongodb.net/python-web-app retryWrites=true&w=majority")

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert(
                {"content": entry_content, "date": formatted_date})

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
