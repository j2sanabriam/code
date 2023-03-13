import pandas as pd
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

def getFavoriteArts(user):
    url = './static/data/df_ratings.csv'
    favorites = pd.read_csv(url, sep=",")
    user_favorite = favorites[favorites['user_id'] == user][['artist_id', 'artist_name', 'rating']]
    user_favorite = user_favorite.sort_values(by='rating', ascending=False).head(10)
    user_favorite_list = user_favorite.values.tolist()

    if len(user_favorite_list) < 10:
        user_favorite_list = completeList(user_favorite_list, 10)

    return user_favorite_list


def getRecomendationsUser(user):
    url = './static/data/Dataset_pearson_user.csv'
    users_recom = pd.read_csv(url, sep=",")
    user_x = users_recom[users_recom['user_id'] == user][['artist_id', 'artist_name', 'estimation_rounded']]
    user_x = user_x.sort_values(by='estimation_rounded', ascending=False).head(10)
    recommd_user = user_x.values.tolist()

    if len(recommd_user) < 10:
        recommd_user = completeList(recommd_user, 10)

    return recommd_user


def getNeighborsUser(user):
    neighbors_user = []
    url = './static/data/UsuariosCercanos_Usuarios_Pearson.csv'
    neighbors = pd.read_csv(url, sep=",")
    user_x = neighbors[neighbors['user_id'] == user][['neighbors']]
    if len(user_x) > 0:
        user_x_text = user_x["neighbors"].values[0]
        user_x_text = user_x_text.replace("['", "").replace("']", "")
        neighbors_user = user_x_text.split("', '")
    else:
        neighbors_user = ["", "", "", "", ""]

    return neighbors_user


def getRecomendationsItem(user):
    url = './static/data/Dataset_coseno_item.csv'
    users_recom_item = pd.read_csv(url, sep=",")
    user_x = users_recom_item[users_recom_item['user_id'] == user][['artist_id', 'artist_name', 'estimation_rounded']]
    user_x = user_x.sort_values(by='estimation_rounded', ascending=False).head(10)
    recommd_item = user_x.values.tolist()

    if len(recommd_item) < 10:
        recommd_item = completeList(recommd_item, 10)

    return recommd_item


def getNeighborsItem(fav_list):
    url = './static/data/ItemsCercanos_Items_Coseno_nombres.csv'
    neighbors_item = pd.read_csv(url, sep=",")

    arts_ids = []
    arts_name = []
    neighbors_artist = []

    for fav in fav_list:
        if fav[0] != "":
            arts_ids.append(fav[0])
        if fav[1] != "":
            arts_name.append(fav[1])

    if len(arts_ids) > 0:
        neighbors_artist = []
        for artist in arts_ids:
            favorite_row = neighbors_item[neighbors_item['artist_id'] == artist][
                ['neighbor_1', 'neighbor_2', 'neighbor_3', 'neighbor_4', 'neighbor_5']]
            if favorite_row["neighbor_1"].values[0] not in neighbors_artist and favorite_row["neighbor_1"].values[
                0] not in arts_name:
                neighbors_artist.append(favorite_row["neighbor_1"].values[0])
            if favorite_row["neighbor_2"].values[0] not in neighbors_artist and favorite_row["neighbor_2"].values[
                0] not in arts_name:
                neighbors_artist.append(favorite_row["neighbor_2"].values[0])
            if favorite_row["neighbor_3"].values[0] not in neighbors_artist and favorite_row["neighbor_3"].values[
                0] not in arts_name:
                neighbors_artist.append(favorite_row["neighbor_3"].values[0])
            if favorite_row["neighbor_4"].values[0] not in neighbors_artist and favorite_row["neighbor_4"].values[
                0] not in arts_name:
                neighbors_artist.append(favorite_row["neighbor_4"].values[0])
            if favorite_row["neighbor_5"].values[0] not in neighbors_artist and favorite_row["neighbor_5"].values[
                0] not in arts_name:
                neighbors_artist.append(favorite_row["neighbor_5"].values[0])
        neighbors_artist = neighbors_artist[:10]
    else:
        neighbors_artist = ["", "", "", "", "", "", "", "", "", ""]

    return neighbors_artist

def completeList(lista, num):
    while len(lista) <= num:
        lista.append(["", "", ""])
    return lista


def insertFavorite(user, artis_id, artis_name):
    url = './static/data/df_ratings.csv'
    ratings = pd.read_csv(url, sep=",")

    new_row = {'user_id': user, 'artist_id': artis_id, 'rating': 1, 'scaled_rating': 1, 'rounded_scaled_rating': 1,
               'artist_name': artis_name}
    ratings = ratings.append(new_row, ignore_index=True)
    # Guarda dataframe a archivo plano
    ratings.to_csv(url, sep=",", index=False)