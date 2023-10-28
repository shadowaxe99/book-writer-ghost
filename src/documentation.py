```python
from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='AI Interviewer API',
    description='A detailed API documentation for the AI Interviewer application',
)

ns = api.namespace('AI_Interviewer', description='Operations related to AI Interviewer')

user = api.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'username': fields.String(required=True, description='The user username'),
})

interview = api.model('Interview', {
    'id': fields.String(required=True, description='The interview identifier'),
    'questions': fields.List(fields.String, description='The interview questions'),
})

narrative = api.model('Narrative', {
    'id': fields.String(required=True, description='The narrative identifier'),
    'content': fields.String(required=True, description='The narrative content'),
})

@ns.route('/users/<string:id>')
@api.doc(responses={404: 'User not found'}, params={'id': 'The User ID'})
class UserResource(Resource):
    @api.doc(description='Get a specific user')
    @api.marshal_with(user)
    def get(self, id):
        return {}

@ns.route('/interviews/<string:id>')
@api.doc(responses={404: 'Interview not found'}, params={'id': 'The Interview ID'})
class InterviewResource(Resource):
    @api.doc(description='Get a specific interview')
    @api.marshal_with(interview)
    def get(self, id):
        return {}

@ns.route('/narratives/<string:id>')
@api.doc(responses={404: 'Narrative not found'}, params={'id': 'The Narrative ID'})
class NarrativeResource(Resource):
    @api.doc(description='Get a specific narrative')
    @api.marshal_with(narrative)
    def get(self, id):
        return {}

if __name__ == '__main__':
    app.run(debug=True)
```
This Python code uses Flask and Flask-RESTPlus to create a web API with Swagger documentation. The API has three endpoints: one for users, one for interviews, and one for narratives. Each endpoint supports a GET operation to retrieve a specific resource by its ID. The API documentation includes detailed descriptions of the API, its operations, and its data models.