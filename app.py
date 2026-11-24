import joblib
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load("model.pkl")

app = FastAPI()

class Input(BaseModel):
    marks: int

@app.get("/")
def home():
    return {"message": "Model API is running"}

@app.post("/predict")
def predict(data: Input):
    result = model.predict([[data.marks]])
    return {"marks": data.marks, "pass": int(result[0])}