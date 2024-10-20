import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or\
                              'postgresql+pg8000://postgres:demopassword@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
