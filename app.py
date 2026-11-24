from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    marks: int

@app.get("/")
def home():
    return {"message": "Model API is running"}

def get_result(marks: int):
    # Real college rule: 40+ = Pass
    return {"marks": marks, "pass": 1 if marks >= 40 else 0}

@app.post("/predict")
def predict(data: Input):
    return get_result(data.marks)

@app.get("/predict")
def predict_get(marks: int):
    return get_result(marks)