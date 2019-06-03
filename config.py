import os


class Config:
    """Main configurations class"""

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/blog'
    SECRET_KEY = 'SECRET_KEY'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/blog'


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
export SECRET_KEY='SECRET_KEY'

export EMAIL_USERNAME='alvinmichoma@gmail.com'
export EMAIL_PASSWORD='itisfinallyhere'
export FLASK_DEBUG=1
export FLASK_APP=app

python3.6 manage.py server