from fastapi import FastAPI
import pickle
import pandas as pd
from src.data_model import Water


app = FastAPI(
    title= "Water Potability Prediction",
    description= "Prediction Water Potability"
)

with open("model.pkl","rb") as f:
    model = pickle.load(f)


@app.get("/")
def index():
    return "Welcome to Water Potability Prediction FastAPI"


@app.post("/predict")
def model_predict(water: Water):
    sample = pd.DataFrame({
        'ph' : [water.ph],
        'Hardness' : [water.Hardness],
        'Solids' : [water.Solids],
        'Chloramines' : [water.Chloramines],
        'Sulfate' : [water.Sulfate],
        'Conductivity' : [water.Conductivity],
        'Organic_carbon' : [water.Organic_carbon],
        'Trihalomethanes' : [water.Trihalomethanes],
        'Turbidity' : [water.Turbidity]
    })

    predicted_value = model.predict(sample)[0]

    if predicted_value == 1:
        return {"message": "Water is Consumable"}
    else:
        return {"message": "Water is not Consumable"}



