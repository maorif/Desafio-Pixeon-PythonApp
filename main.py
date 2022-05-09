from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from routes import LoginRoute, PatientRoute

app = FastAPI()

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     raise HTTPException(status_code=400, detail=str(exc))
    

@app.get("/")
def root():
    return {"message": "Welcome to the API :)"}

# Endpoint that checks server status (needs work)
@app.get("/health", status_code=200)
async def health():
    raise HTTPException(status_code=200, detail="Healthy :)")

# Including routes
app.include_router(LoginRoute.router)
app.include_router(PatientRoute.router)