import pandas as pd
from prediction_model import PredictionModel
from joblib import load


def toJson(dataframe):
    result = dataframe.to_dict()
    return result


def prediction(df):
    predicion_model = PredictionModel()
    results = predicion_model.make_predictions(df)
    return results.tolist()

def getUsers():
    url = "./static/data/userid-profile.tsv"
    users_db = pd.read_csv(url, sep="\t")
    return users_db

def getItems():
    url2 = "./static/data/userid-timestamp-artid-artname-traid-traname.tsv"
    items_db = pd.read_csv(url2, sep="\t")
    return items_db

def getProfileImg(gender):
    profile_img = 'src=./static/img/undraw_profile_m.svg'
    if gender == "f":
        profile_img = 'src=./static/img/undraw_profile_f.svg'
    return profile_img

def getGenderText(gender):
    genero_text = ""
    if gender == "f":
        genero_text = "Femenino"
    elif gender == "m":
        genero_text = "Masculino"
    return genero_text

def getTopTen():
    top_ten = []
    top_ten.append(["Id Artista 1", "Nombre Artista 1", "Id Canción 1", "Nombre Canción 1"])
    top_ten.append(["Id Artista 2", "Nombre Artista 2", "Id Canción 2", "Nombre Canción 2"])
    top_ten.append(["Id Artista 3", "Nombre Artista 3", "Id Canción 3", "Nombre Canción 3"])
    top_ten.append(["Id Artista 4", "Nombre Artista 4", "Id Canción 4", "Nombre Canción 4"])
    top_ten.append(["Id Artista 5", "Nombre Artista 5", "Id Canción 5", "Nombre Canción 5"])
    top_ten.append(["Id Artista 6", "Nombre Artista 6", "Id Canción 6", "Nombre Canción 6"])
    top_ten.append(["Id Artista 7", "Nombre Artista 7", "Id Canción 7", "Nombre Canción 7"])
    top_ten.append(["Id Artista 8", "Nombre Artista 8", "Id Canción 8", "Nombre Canción 8"])
    top_ten.append(["Id Artista 9", "Nombre Artista 9", "Id Canción 9", "Nombre Canción 9"])
    top_ten.append(["Id Artista 10", "Nombre Artista 10", "Id Canción 10", "Nombre Canción 10"])
    return top_ten

def getFavoriteArts():
    fav_arts = []
    fav_arts.append(["Id Artista 1", "Nombre Artista 1", "Conteo 1"])
    fav_arts.append(["Id Artista 2", "Nombre Artista 2", "Conteo 2"])
    fav_arts.append(["Id Artista 3", "Nombre Artista 3", "Conteo 3"])
    fav_arts.append(["Id Artista 4", "Nombre Artista 4", "Conteo 4"])
    fav_arts.append(["Id Artista 5", "Nombre Artista 5", "Conteo 5"])
    fav_arts.append(["Id Artista 6", "Nombre Artista 6", "Conteo 6"])
    fav_arts.append(["Id Artista 7", "Nombre Artista 7", "Conteo 7"])
    fav_arts.append(["Id Artista 8", "Nombre Artista 8", "Conteo 8"])
    fav_arts.append(["Id Artista 9", "Nombre Artista 9", "Conteo 9"])
    fav_arts.append(["Id Artista 10", "Nombre Artista 10", "Conteo 10"])
    return fav_arts

def getRecomendations():
    recommd = []
    recommd.append(["Id Artista 1", "Nombre Artista 1", "Rating 1"])
    recommd.append(["Id Artista 2", "Nombre Artista 2", "Rating 2"])
    recommd.append(["Id Artista 3", "Nombre Artista 3", "Rating 3"])
    recommd.append(["Id Artista 4", "Nombre Artista 4", "Rating 4"])
    recommd.append(["Id Artista 5", "Nombre Artista 5", "Rating 5"])
    recommd.append(["Id Artista 6", "Nombre Artista 6", "Rating 6"])
    recommd.append(["Id Artista 7", "Nombre Artista 7", "Rating 7"])
    recommd.append(["Id Artista 8", "Nombre Artista 8", "Rating 8"])
    recommd.append(["Id Artista 9", "Nombre Artista 9", "Rating 9"])
    recommd.append(["Id Artista 10", "Nombre Artista 10", "Rating 10"])
    return recommd

def getSimilarUsers():
    similar = []
    similar.append(["Usuario 1"])
    similar.append(["Usuario 2"])
    similar.append(["Usuario 3"])
    similar.append(["Usuario 4"])
    similar.append(["Usuario 5"])
    similar.append(["Usuario 6"])
    similar.append(["Usuario 7"])
    similar.append(["Usuario 8"])
    similar.append(["Usuario 9"])
    similar.append(["Usuario 10"])
    return similar