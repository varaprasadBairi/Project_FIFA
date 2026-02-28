from fastapi import FastAPI
import numpy as np
import joblib as jb
import uvicorn
from pydantic import BaseModel


app = FastAPI()

kmeans = jb.load("/model/kmeans.pkl") #jayanth
scaler = jb.load("/model/scaler.pkl") #prasad

cluster_map = {
    0: "striker",
    1: "midfielder",
    2: "defender",
}

class Features(BaseModel):
    name : str
    nationality : str
    age : int
    pace : int
    shooting : int
    passing : int
    dribbling : int
    defending : int
    physical : int

@app.post('/cluster')
def predict(data: Features):
    # Convert Features object to numpy array
    features = np.array([[
        data.age,
        data.pace,
        data.shooting,
        data.passing,
        data.dribbling,
        data.defending,
        data.physical
    ]])

    scaled_data = scaler.transform(features)
    cluster = int(kmeans.predict(scaled_data)[0])

    return {
        "player_img" : "imageURL",
        "cluster_id": cluster,
        "role":cluster_map[cluster]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)