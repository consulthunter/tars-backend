from typing import List
from psycopg2.extras import RealDictCursor
from tars.core.db.database import get_connection
from tars.core.models.project import Project

def fetch_all_projects() -> List[Project]:
    with get_connection().cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("SELECT * FROM projects;")
        rows = cur.fetchall()
        return [Project(**row) for row in rows]
