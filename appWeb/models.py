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

