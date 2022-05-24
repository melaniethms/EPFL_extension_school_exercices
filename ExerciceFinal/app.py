from flask import Flask, render_template

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
    file = open("noteapp.txt")
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



@app.route("/")
def home():
  write_note()
  return render_template("index.html")

@app.route("/add")
def add_notes():
  return render_template("add.html")

@app.route("/notes")
def view_all_notes():
  return render_template("notes.html")

@app.route("/search-results")
def search():
  return render_template("search-results.html")

@app.route("/save-note")
