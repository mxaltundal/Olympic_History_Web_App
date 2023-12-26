"""Flask configuration."""

FLASK_ENV = 'development'
TESTING = True
SECRET_KEY = "KPC4LKd7KvF0nRPGpvmv3Q"
STATIC_FOLDER = 'static'
TEMPLATES_FOLDER = 'templates'
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"
MYSQL_DB = "pytest"
MYSQL_CURSORCLASS = "DictCursor"