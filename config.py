import os

# Constants
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'db\app.db')

# Database setup constants
PRAGMA_SETTINGS = [
    ("foreign_keys", 1),
    ("journal_mode", "WAL"),
    ("synchronous", "NORMAL")
]