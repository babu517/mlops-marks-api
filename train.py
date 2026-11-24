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

def get_result(marks: int):
    result = model.predict([[marks]])
    return {"marks": marks, "pass": int(result[0])}

@app.post("/predict")
def predict(data: Input):
    return get_result(data.marks)

@app.get("/predict")
def predict_get(marks: int):
    return get_result(marks)