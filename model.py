"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from sqlalchemy import distinct

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM


class Brand(db.Model):

    __tablename__ = "brands"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.Integer)
    discontinued = db.Column(db.Integer)

    def __repr__(self):
        """Show brand's info"""

        return "<brand's id=%s name=%s founded=%s headquarters=%s discontinued=%s>" % (
                                                                  self.id,
                                                                  self.name,
                                                                  self.founded,
                                                                  self.headquarters,
                                                                  self.discontinued,
                                                                  )

class Model(db.Model):

    __tablename__ = "models"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50), db.ForeignKey('brands.name'))
    name = db.Column(db.String(50), nullable=False)


    brand = db.relationship('Brand', backref=db.backref("brands", order_by=id))


    def __repr__(self):
        """Show model's info"""

        return "<model's id=%s year=%s brand name=%s name=%s>" % (self.id,
                                                                  self.year,
                                                                  self.brand_name,
                                                                  self.name,
                                                                  )


# End Part 1
##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
