"""Flask configuration."""

FLASK_ENV = 'development'
TESTING = True
SECRET_KEY = "*******"
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "********"
MYSQL_DB = "olympic_historical_data"
MYSQL_CURSORCLASS = "DictCursor"
