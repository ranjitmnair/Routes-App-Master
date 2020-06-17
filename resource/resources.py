from flask import Response, request
from database.models import resources
from flask_restful import Resource

class ResourcesApi2(Resource):
    def get(self,domain):
        obj=resources.objects(domain=domain).to_json()
        return Response(obj, mimetype="application/json", status=200)

class ResourcesApi(Resource):
    def post(self):
        body = request.get_json()
        obj = resources(**body).save()
        id = obj.id
        return {'id': str(id)}, 200

class ResourceApi(Resource):
    def put(self, id):
        body = request.get_json()
        resources.objects.get(id=id).update(**body)
        return '', 200
    def delete(self, id):
        obj = resources.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        obj = resources.objects.get(id=id).to_json()
        return Response(obj, mimetype="application/json", status=200)

