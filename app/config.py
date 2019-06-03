import os

class Config:
    SECRET_KEY = '06b428d12ac878e0e11f4a432921c41a'  
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/pitch'

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alvin:alvin123@localhost/pitch'
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
