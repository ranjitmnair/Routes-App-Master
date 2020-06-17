from flask import Flask, request, Response
from database.db import initialize_db
from flask_bcrypt import Bcrypt 
from flask_restful import Api
from resource.routes import initialize_routes
from database.models import *
from flask_jwt_extended import jwt_required, JWTManager

app=Flask(__name__)
api=Api(app)
app.config['MONGODB_SETTINGS']={
    'host':'mongodb+srv://stcapp:stcappbackend@cluster0-0k4za.mongodb.net/masterdb?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)











if __name__ == "__main__":
    app.run()