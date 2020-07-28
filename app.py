from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)

# Configure Flask by providing the PostgreSQL URI so the app is able to connect to the database

POSTGRES = {
    'user': 'root',
    'pw': 'password',
    'db': 'test_db',
    'host': 'localhost',
    'port': '5432'

}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

print ("app.config['SQLALCHEMY_DATABASE_URI'] : ", app.config['SQLALCHEMY_DATABASE_URI'])

print ("app.config : ", app.config)

# Connect the SQLAlchemy object to the app

db.init_app(app)

@app.route("/")
def main():
    return 'Hello World !'

if __name__ == '__main__':
    # Set the application in debug mode so that the server is reloaded on any code change
    app.config['DEBUG'] = True
    app.run()