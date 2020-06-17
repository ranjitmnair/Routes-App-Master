from .resources import *

def initialize_routes(api):
    api.add_resource(ResourcesApi, '/api/resources')
    api.add_resource(ResourcesApi2, '/api/resources/<domain>')
    api.add_resource(ResourceApi, '/api/resources/<id>')

from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')