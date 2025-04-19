import os
from tars.core.db.database import get_connection, release_connection


def create_tables():

    # Read schema SQL from a file or paste directly as a string
    with open(os.path.join("migrations", "tars.sql"), "r") as file:
        schema_sql = file.read()
        with get_connection() as connection:
            connection.cursor().execute(schema_sql)
            connection.commit()
            connection.cursor().close()
            connection.close()
            release_connection(connection)
