
from fastapi import FastAPI

app = FastAPI()

# Need to connect to the DB and load the projects and available TARs images

@app.get("/tars/api/")
def read_root():
    return {"Hello": "World"}