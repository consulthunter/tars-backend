# routes/projects.py
from typing import List
from fastapi import APIRouter
from tars.core.models.project import Project
from tars.core.db.queries.project_queries import fetch_all_projects

router = APIRouter()

@router.get("/projects", response_model=List[Project])
def list_projects():
    return fetch_all_projects()