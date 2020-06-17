from flask_mongoengine import *
db=MongoEngine()

def initialize_db(app):
    db.init_app(app)