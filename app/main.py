from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.features.suggest_code import suggest_code
from app.features.explain_code import explain_code
from app.features.detect_errors import detect_errors_from_code
from app.features.refactor_code import suggest_refactoring
from app.features.learning_mode import provide_tips

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal Coding Assistant API!"}

@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon available"}

class CodeRequest(BaseModel):
    code: str

@app.post("/suggest")
def suggest(request: CodeRequest):
    try:
        result = suggest_code(request.code)
        return {"suggestion": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/explain")
def explain(request: CodeRequest):
    try:
        result = explain_code(request.code)
        return {"explanation": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/detect")
def detect(request: CodeRequest):
    try:
        result = detect_errors_from_code(request.code)
        return {"errors": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/refactor")
def refactor(request: CodeRequest):
    try:
        result = suggest_refactoring(request.code)
        return {"refactored_code": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/learn")
def learn(request: CodeRequest):
    try:
        result = provide_tips(request.code)
        return {"tips": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
