from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/add_notes")
def add_notes():
  return render_template("add_notes.html")

@app.route("/view_all_notes")
def view_all_notes():
  return render_template("view_all_notes.html")

@app.route("/search")
def search():
  return render_template("search.html")