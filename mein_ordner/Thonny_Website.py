from flask import Flask, request
from Thonny import Kunden
#import autos

app = Flask(__name__)

"""@app.route("/") #oder dein dein eigener Pfad
def hello_world():  # beliebiger Funktionsname
    return "Autohandel Fritz" # Der Text der unter der Route angezeigt wird."""

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return '''
                  <h1>Autohandel Fritz</h1>
                  <h2>Benutzer Hinzufügen</h2>
                  <form method="POST">
                      <div><label>Username: <input type="text" name="username"></label></div>
                      <div><label>Firstname: <input type="text" name="first_name"></label></div>
                      <div><label>Lastname: <input type="text" name="last_name"></label></div>
                      <input type="submit" value="Submit">
                  </form>'''
    else:
        username = request.form.get("username")
        firstname = request.form.get("first_name")
        lastname = request.form.get("last_name")
        kunde = Kunden(username, firstname, lastname)
        kunde.to_db()
        return f"Benutzer {username} wurde hinzugefügt"        
