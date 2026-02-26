from fastapi import FastAPI
import numpy as np
import joblib as jb
import pydantic as pc


app = FastAPI()

kmeans = jb.load("/model/kmeans.pkl") #jayanth
scaler = jb.load("/modle/scaler.pkl") #prasad

cluster_map = {
    0: "defender",
    1: "midfielder",
    2: "striker",
    3: "winger",
    4: "goalkeeper"
}

@app.post('/cluster')
def predict(data: dict):
    features = np.array([[
        data['pace'],
        data['shooting'],
        data['passing'],
        data['dribbling'],
        data['defending'],
        data['physical']
    ]])

    scaled_data = scaler.transform(features)
    cluster = int(kmeans.predict(scaled_data)[0])

    return {
        "player_img" : "imageURL",
        "cluster_id": cluster,
        "role":cluster_map[cluster]
    }