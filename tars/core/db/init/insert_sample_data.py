from datetime import date
from tars.core.db.database import get_connection, release_connection

sample_data = {
    "available_docker_images": [
        (1, "python", "3.11")
    ],
    "projects": [
        (1, "SampleProject", "https://github.com/example/sample", date(2024, 4, 1), date(2024, 4, 2), 1, "v1.0.0", "sample_volume")
    ],
    "files": [
        (1, 1, "main", "main.py", "Python", "/app/main.py")
    ],
    "location": [
        (1, 1, 0, 10, 25),
        (2, 12, 0, 15, 20)
    ],
    "package_coverage": [
        (1, "main", 0.85, 0.75, 10, "main")
    ],
    "classes": [
        (1, 1, "MyClass", "public", "[]", "[]", "class MyClass:", "MyClass", "A test class", 0, "pytest", 1)
    ],
    "class_coverage": [
        (1, 1, 0.90, 0.80, 5, "MyClass")
    ],
    "methods": [
        (1, 1, "do_work", "public", ["static"], ["@staticmethod"], "def do_work():", "do_work", "Performs work", "Some docs", True, "pytest", "unit", 2)
    ],
    "imports": [
        (1, 1, "os", "os", "import os", False)
    ],
    "method_coverage": [
        (1, 1, 0.95, 0.85, 3, "do_work")
    ],
    "functions": [
        (1, 1, "helper_func", ["public"], ["@utility"], "def helper_func():", "helper_func", "Helps things", "Docstring here", False, None, None, 1)
    ],
    "test_cases": [
        (1, 1, None, True, date(2024, 4, 2), date(2024, 4, 1))
    ],
    "function_coverage": [
        (1, 1, 0.88, 0.77, 4, "helper_func")
    ],
    "invocations": [
        (1, 1, None, None, 1, False, "do_work()"),
        (2, None, 1, 1, None, False, "helper_func()")
    ],
    "properties": [
        (1, 1, "value", "private", ["final"], ["@property"], "private final int value;")
    ],
    "statements": [
        (1, 1, "print('Hello World')")
    ]
}

def insert_sample_data():
    with get_connection() as connection:
        cur = connection.cursor()
        cur.execute("SET session_replication_role = 'replica';")
        # Insert everything in dependency-safe order
        for table in [
            "available_docker_images", "projects", "files", "location",
            "package_coverage", "classes", "class_coverage", "methods",
            "imports", "method_coverage", "functions", "test_cases",
            "function_coverage", "invocations", "properties", "statements"
        ]:
            insert(cur, table, sample_data[table])
        connection.commit()
        connection.cursor().close()
        connection.close()
        release_connection(connection)

def insert(cur, table, values):
    placeholders = ", ".join(["%s"] * len(values[0]))
    query = f'INSERT INTO {table} VALUES ({placeholders})'
    cur.executemany(query, values)
