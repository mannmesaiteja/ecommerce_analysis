import os
from dotenv import load_dotenv


load_dotenv(os.getenv("dotenv_file")) # LOAD DOTENV_FILE

db_name = os.getenv("EC_DBNAME")
db_host = os.getenv("DB_HOST")
db_password = os.getenv("DB_PASSWORD")
db_user = os.getenv("DB_USER")