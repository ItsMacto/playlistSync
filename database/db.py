import sqlite3
from config import DATABASE_PATH, PRAGMA_SETTINGS

class DatabaseManager:
    def __init__(self, db_path=DATABASE_PATH):
        self.db_path = db_path
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self._apply_pragmas()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            if exc_type is None:
                self.connection.commit()
            else:
                self.connection.rollback()
            self.connection.close()

    def _apply_pragmas(self):
        for pragma, value in PRAGMA_SETTINGS:
            self.cursor.execute(f"PRAGMA {pragma} = {value}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or [])
        except sqlite3.Error as e:
            print(f"SQLite Error: {e}")
            raise

    def fetchall(self, query, params=None):
        self.execute_query(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):
        self.execute_query(query, params)
        return self.cursor.fetchone()

    def execute_script(self, script):
        try:
            self.cursor.executescript(script)
        except sqlite3.Error as e:
            print(f"SQLite Script Error: {e}")
            raise

    def create_tables(self, schema_path='database/schema.sql'):
        with open(schema_path, 'r') as schema_file:
            schema_script = schema_file.read()
        self.execute_script(schema_script)