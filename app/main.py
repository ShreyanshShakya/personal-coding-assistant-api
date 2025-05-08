from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.features.suggest_code import suggest_code
from app.features.explain_code import explain_code
from app.features.detect_errors import detect_errors_from_code
from app.features.refactor_code import suggest_refactoring
from app.features.learning_mode import provide_tips
from fastapi.openapi.models import APIKey
from fastapi.openapi.utils import get_openapi

app = FastAPI()  # Define the app first

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Personal Coding Assistant API",
        version="1.0.0",
        description="An API for code suggestions, explanations, error detection, refactoring, and learning tips.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "APIKeyHeader": {
            "type": "apiKey",
            "name": "x-api-key",
            "in": "header",
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"APIKeyHeader": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi  # Assign the custom OpenAPI schema after defining the app

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