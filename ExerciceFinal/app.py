from flask import Flask, render_template, request
from matplotlib.pyplot import text

app = Flask(__name__)

# functions : 
# Create a note
def write_note(text):
    file = open("noteapp.txt", "a")
    file.write("----\n")
    file.write(text + "\n")
    file.close()

# Search through notes 
def search(text):
    file = open("noteapp.txt", "a")
    content = file.read()
    file.close()
    result = ""
    notes = content.split("----")

    for note in notes:
        if note.find(text) != -1:
            result += "\n----" + note

    if result == "":
        print("Nothing found!")
    else:
        print(result)

#read all notes
def get_notes():
    notes= open("noteapp.txt", "a")
    content= notes.read()
    all_notes = content.split("\n")
    all_notes.pop(len(all_notes)-1)
    notes.close()
    return all_notes

# search notes
def search_notes():
  notes = get_notes()
  result = ""
  for note in notes:
    if note.lower().find(search_value.lower()) != -1: 
      #je sais que search_value n'est pas defined je ne sais pas encore ce que je veux en faire 
      result += "<p>" + note + "<p>"
    if result == "":
            result = "<p> no matching note </p>"





@app.route("/")
def home():
  return render_template("index.html", SearchNotes = search())

@app.route("/add", methods = ["GET"])
def add_notes():
  return render_template("add.html", Addnotes = write_note())
  # TypeError: write_note() missing 1 required positional argument: 'text'

@app.route("/notes")
def view_all_notes():
  return render_template("notes.html", ViewNotes = get_notes())

@app.route("/search-results")
def search():
  return render_template("search-results.html")

@app.route("/save-note")
def save_note():
    return render_template("index.html")