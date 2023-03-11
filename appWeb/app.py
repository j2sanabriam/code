from flask import Flask, render_template, request, send_from_directory
import models as mdl
from datetime import date
import pandas as pd

app = Flask(__name__, static_url_path='/static')

user_id = ""
user_gender = ""
user_age = 0
user_country = ""
user_date = ""

users_db = mdl.getUsers()
# items_db = mdl.getItems()


@app.route("/", methods=['GET'])
def login():
    global users_db, user_id, user_gender, user_age, user_country, user_date
    user_id = ""
    user_gender = ""
    user_age = 0
    user_country = ""
    user_date = ""

    print(type(request))
    print(request)
    print(request.args)

    print("Ingresa Get")
    return render_template("login.html")

@app.route("/create", methods=['GET'])
def create():
    global users_db, user_id, user_gender, user_age, user_country, user_date, url
    # limpiar variables para login con usuario nuevo
    user_id = ""
    user_gender = ""
    user_age = 0
    user_country = ""
    user_date = ""

    # Leer valores desde los campos del formulario de creación
    crea_user_id = request.args.get('createUserId')
    crea_gender = request.args.get('createGender')
    crea_age = request.args.get('createAge')
    crea_country = request.args.get('createCountry')

    # Si algún valor está vacío, genera mensaje de error y no crea usuario
    if not crea_user_id or not crea_gender or not crea_age or not crea_country:
        return render_template("404.html", mensaje="Datos Incompletos")
    else:
        # Valida si el usuario a crear ya existe
        user_row = users_db[users_db['#id'] == crea_user_id].reset_index()
        if len(user_row) > 0:
            return render_template("404.html", mensaje="Usuario Ya Existe")
        else:
            # Fecha de creación en string
            today = date.today()
            crea_date = today.strftime('%b') + " " + str(today.strftime('%d')) + ", " + str(today.strftime('%Y'))

            # Inserta registro nuevo usuario a dataframe
            new_row = {'#id': crea_user_id, 'gender': crea_gender, 'age': float(crea_age), 'country': crea_country,
                       'registered': crea_date}
            users_db = users_db.append(new_row, ignore_index=True)

            # Guarda dataframe a archivo plano
            users_db.to_csv(url, sep="\t", index=False)
            return render_template("login.html")


@app.route("/register", methods=['GET'])
def register():
    top_ten = mdl.getTopTen()
    return render_template("register.html", top10=top_ten)


@app.route("/index", methods=['GET'])
def index():
    global users_db, user_id, user_age, user_gender, user_country, user_date

    print(type(request))
    print(request)
    print(request.args)

    if user_id == "":
        user_id = request.args.get('loginUser')

    user_row = users_db[users_db['#id'] == user_id].reset_index()
    if len(user_row) > 0:
        user_gender = user_row["gender"].values[0]
        user_age = user_row["age"].values[0]
        user_country = user_row["country"].values[0]
        user_date = user_row["registered"].values[0]

        profile_img = mdl.getProfileImg(user_gender)

        fav = mdl.getFavoriteArts()
        rec = mdl.getRecomendations()
        sim_users = mdl.getSimilarUsers()

        return render_template("index.html", usuario=user_id, imagen=profile_img, favorites=fav, recommd=rec,
                           similarUsers=sim_users)
    else:
        return render_template("404.html", mensaje="Usuario No Existe")


@app.route("/profile", methods=['GET'])
def profile():
    global user_id, user_gender, user_age, user_country, user_date

    profile_img = mdl.getProfileImg(user_gender)
    genero_text = mdl.getGenderText(user_gender)

    return render_template("profile.html", usuario=user_id, imagen=profile_img, genero=genero_text, edad=user_age,
                           pais=user_country, fecha=user_date)


@app.route("/error", methods=['GET'])
def error():
    return render_template("404.html", mensaje="404")


if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))