from fastapi import FastAPI, UploadFile, File, HTTPException, Body
from pydantic import BaseModel
import utils

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/api/")
async def solve_question(query: Query = Body(...), file: UploadFile = None):
    try:
        answer = utils.process_question(query.question, file)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def home():
    return {"message": "TDS Solver API is running!"}



    
