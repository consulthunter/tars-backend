# routes/projects.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/projects")
def list_projects():
    return [{"id": 1, "name": "Project Alpha"}, {"id": 2, "name": "Project Beta"}]