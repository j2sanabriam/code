from flask import Flask, render_template, request, send_from_directory
from models import prediction
import pandas as pd

app = Flask(__name__, static_url_path='/static')
userid = ""

@app.route("/" , methods=['GET'])
def login():
    global userid
    userid = ""
    return render_template("login.html")

@app.route("/register" , methods=['GET'])
def register():
    return render_template("register.html")

@app.route("/index" , methods=['GET'])
def index():
    global userid
    if userid == "":
        userid = request.args.get('loginUser')
    if userid == "Juan":
        imagen = 'src=./static/img/undraw_profile_m.svg'
    else:
        imagen = 'src=./static/img/undraw_profile_f.svg'
    return render_template("index.html", usuario=userid, imagen=imagen)



if __name__ == "__main__":
    app.run()

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))