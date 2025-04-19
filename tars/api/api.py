
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tars.api.routers import projects

app = FastAPI()

# Need to connect to the DB and load the projects and available TARs images

# Add this before including any routers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
root_api_prefix = "/tars/api"
app.include_router(projects.router, prefix=f"{root_api_prefix}")

@app.get("/tars/api/")
def read_root():
    return {"Hello": "World"}