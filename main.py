from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    
teas : List[Tea] = []

@app.get("/")
def read_root():
    return {"message" : "welcome..."}

@app.get("/teas")
def read_teas():
    return {"teas": ["green tea", "black tea", "oolong tea"]}


@app.post("/teas")  
def create_tea(tea: Tea):
    teas.append(tea)
    return {"message": "Tea added successfully", "tea": tea}

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, tea: Tea):
    for i, t in enumerate(teas):
        if t.id == tea_id:
            teas[i] = tea
            return {"message": "Tea updated successfully", "tea": tea}
    return {"error": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for i, t in enumerate(teas):
        if t.id == tea_id:
            del teas[i]
            return {"message": "Tea deleted successfully"}
    return {"error": "Tea not found"}