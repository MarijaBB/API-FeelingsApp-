from flask import Flask
from flask_apispec import FlaskApiSpec
from controller.feelingController import *

app = Flask(__name__)

# Basic config
app.config.update({
    'APISPEC_TITLE': 'API feeldb',
    'APISPEC_VERSION': '1.0.0',
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui',
    'APISPEC_SWAGGER_URL': '/swagger.json',
})


docs = FlaskApiSpec(app)

#routes
app.add_url_rule('/feelings', view_func=GetAllFeelings.as_view('get_all_feelings'))
app.add_url_rule('/feeling/<int:id>', view_func=GetFeelingById.as_view('get_feeling_by_id'))
app.add_url_rule('/feeling', view_func=CreateFeeling.as_view('create_feeling'))
app.add_url_rule('/feeling/<int:feeling_id>', view_func=UpdateFeeling.as_view('update_feeling'), methods=['PUT'])
app.add_url_rule('/feeling/<int:feeling_id>', view_func=UpdateFeelingName.as_view('update_feelingName'), methods=['PATCH'])
app.add_url_rule('/feeling/<int:feeling_id>', view_func=DeleteFeeling.as_view('delete_feeling'), methods=['DELETE'])


docs.register(GetAllFeelings, endpoint='get_all_feelings')
docs.register(GetFeelingById, endpoint='get_feeling_by_id')
docs.register(CreateFeeling, endpoint='create_feeling')
docs.register(UpdateFeeling, endpoint='update_feeling')
docs.register(UpdateFeelingName, endpoint='update_feelingName')
docs.register(DeleteFeeling, endpoint='delete_feeling')

if __name__ == '__main__':
    app.run(debug=True)