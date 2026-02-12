from fastapi import FastAPI
from routes import route
app = FastAPI()

app.include_router(route)
@app.get("/")
def root():
    return {"message":"healthy"}




