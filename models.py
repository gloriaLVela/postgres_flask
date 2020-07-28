from flask_sqlalchemy import SQLAlchemy
import datetime

#Initialize a database object from Flask-Alchemy

db = SQLAlchemy()


#Define the class models below

"""Base data model for all object"""

class BaseModel(db.model):
    # Base data for all objects
    __abstract__ = True
    # define here __repr__ and json methods for any common method
    # that you will need for all the models

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__clas__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        """ Define a base way to jsonify models, dealing """
        return {
            column: value if not ininstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class Station(BaseModel, db.Model):
    #model for the stations table
    __tablename__ = 'stations'
    
    id = db.Column(db.integer, primary_key = True)
    lat = db,Column(db.Float)
    lng = db.Column(db.Float)
