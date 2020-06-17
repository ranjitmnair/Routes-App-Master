from .db import db
from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash

class resources(db.Document):
    domain=db.StringField(required=True)
    title=db.StringField(required=True)
    link1=db.StringField(required=True)
    link2=db.StringField()
    link3=db.StringField()
    
class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password) 

User.register_delete_rule(Movie, 'added_by', db.CASCADE)  #this rule means if the user is deleted, then movies created by him are also deleted
