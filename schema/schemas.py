from marshmallow import Schema, fields

class FeelingSchema(Schema):
    feeling_name = fields.String()
    image_file = fields.String()
    color = fields.String()

class UpdateFeelingSchema(Schema):
    feeling_name = fields.String(required=True)
    color = fields.String(required=True)
    image_file = fields.String(required=True)
    
class UpdateFeelingNameSchema(Schema):
    feeling_name = fields.String(required=True) 
    
class ResponseSchema(Schema):
    message = fields.String()
    feelingid = fields.Integer()
    
class OnlyMessageResponseSchema(Schema):
    message = fields.String()
