import os

# Config file, put all your keys and passwords and whatnot in here
DB_URI = os.environ.get("DATABASE_URL", "sqlite:///supplycache.db")
SECRET_KEY = "booyakasha"

DEBUG=True