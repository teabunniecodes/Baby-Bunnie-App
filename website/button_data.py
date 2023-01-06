from typing import Literal
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
import SQL_db

buttons = Blueprint("buttons", __name__)

# @buttons.route("/")
# @login_required
# def home():
#     return render_template("home.html")

@buttons.route("/tummy_time", methods=["GET", "POST"])
@login_required
def tummy_time():
    db = SQL_db.Tummy_Time()
    db.connect_db()
    # db.create_table()
    # user = current_user.get_id()
    # GET method
    # if request.method == "GET":
    #     pass

    # POST method
    if request.method == "POST":
        button = request.get_data(as_text=Literal[True])
        return jsonify(button)