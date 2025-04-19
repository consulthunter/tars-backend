# schemas/project.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Project(BaseModel):
    id: int
    name: str
    url: str
    created_at: datetime
    modified_at: datetime
    docker: Optional[int]
    version: Optional[str]
    docker_volume: Optional[str]
