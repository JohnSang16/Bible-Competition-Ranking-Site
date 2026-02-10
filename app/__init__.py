from flask import Flask

app = Flask(__name__)


from app import routes


















# from flask_mysqldb import MySQL
# from dotenv import load_dotenv
# import os

# This loads the variables from .env into your system environment
# load_dotenv() 

# app = Flask(__name__)

# # Use os.getenv to pull the values securely
# app.secret_key = os.getenv('SECRET_KEY')

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
# app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
# app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

# mysql = MySQL(app)