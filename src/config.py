class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^' 

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'UNcampus'
config={
    'development':DevelopmentConfig,
}