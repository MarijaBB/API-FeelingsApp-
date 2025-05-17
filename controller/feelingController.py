from flask import jsonify, request
from flask_apispec.views import MethodResource
from flask_apispec import use_kwargs, marshal_with
from flask.views import MethodView

from schema.schemas import *
from model.feelingsModel import *


class GetAllFeelings(MethodResource, MethodView):
    def get(self):
        feelings = get_feelings()
        return jsonify(feelings)

class GetFeelingById(MethodResource, MethodView):
    def get(self, id):
        feeling = get_feeling(id)
        return jsonify(feeling)

class CreateFeeling(MethodResource, MethodView):
    @use_kwargs(FeelingSchema, location="json")
    @marshal_with(ResponseSchema, code=201)
    def post(self, **kwargs):
        data = request.get_json()

        schema = FeelingSchema()
        errors = schema.validate(data)
        if errors:
            return jsonify(errors), 400

        feeling_name = kwargs.get("feeling_name")
        image_file = kwargs.get("image_file")
        color = kwargs.get("color")

        # Create feeling (your logic)
        feeling_id = new_feeling(feeling_name, image_file, color)
        print(feeling_id)
        return {"message": "Feeling created", "feelingid": feeling_id}, 201

class UpdateFeeling(MethodResource, MethodView):
    @use_kwargs(UpdateFeelingSchema, location="json")
    @marshal_with(OnlyMessageResponseSchema)
    def put(self, feeling_id, feeling_name, color, image_file):
        try:
            update_feeling(feeling_id, feeling_name, image_file, color)
            return {"message": f"Feeling {feeling_id} updated successfully"}
        except Exception:
            return {"message": "Feeling not found"}, 404

class UpdateFeelingName(MethodResource, MethodView):
    @use_kwargs(UpdateFeelingNameSchema, location="json")
    @marshal_with(OnlyMessageResponseSchema)
    def patch(self, feeling_id, feeling_name):
        try:
            change_feeling_name(feeling_id, feeling_name)
            return {"message": f"Feeling {feeling_id} updated successfully"}
        except Exception:
            return {"message": "Feeling not found"}, 404

class DeleteFeeling(MethodResource,MethodView):
    @marshal_with(ResponseSchema, code=200)
    def delete(self,feeling_id):
        try:
            delete_feeling_by_id(feeling_id)
            return {"message": f"Feeling with ID {feeling_id} deleted."}, 200
        except Exception:
            return {"message": "Feeling not found."}, 404