
SQLITE = "sqlite:///contacts.db"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = SQLITE
