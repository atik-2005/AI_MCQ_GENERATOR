import os
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(BASE_DIR, "excel", "Book1.xlsx")

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    userid = request.form["userid"]
    password = request.form["password"]
    role = request.form["role"]

    print(EXCEL_FILE)

    if not os.path.exists(EXCEL_FILE):
        return f"<h2>Excel file not found!</h2><p>{EXCEL_FILE}</p>"

    df = pd.read_excel(EXCEL_FILE)

    user = df[
        (df["User ID"].astype(str) == userid) &
        (df["User Name"] == username) &
        (df["Password"].astype(str) == password) &
        (df["Role"] == role)
    ]

    if not user.empty:

        if role == "Student":
            return render_template("student.html")

        elif role == "Teacher":
            return render_template("teacher.html")

        elif role == "Principal":
            return render_template("principal.html")

    return "<h2>Invalid User ID or Password</h2>"


if __name__ == "__main__":
    app.run(debug=True)
