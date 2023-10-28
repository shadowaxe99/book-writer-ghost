```python
from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='AI Interviewer API',
    description='A detailed API documentation for the AI Interviewer platform',
)

# Define namespaces
ns_interview = api.namespace('interview', description='Interview operations')
ns_narrative = api.namespace('narrative', description='Narrative operations')
ns_user = api.namespace('user', description='User operations')

# Define models
interview = api.model('Interview', {
    'id': fields.String(required=True, description='The interview identifier'),
    'content': fields.String(required=True, description='Interview content'),
})

narrative = api.model('Narrative', {
    'id': fields.String(required=True, description='The narrative identifier'),
    'content': fields.String(required=True, description='Narrative content'),
})

user = api.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'name': fields.String(required=True, description='User name'),
})

# Define routes
@ns_interview.route('/')
class InterviewList(Resource):
    @ns_interview.doc('list_interviews')
    def get(self):
        '''List all interviews'''
        pass

@ns_narrative.route('/')
class NarrativeList(Resource):
    @ns_narrative.doc('list_narratives')
    def get(self):
        '''List all narratives'''
        pass

@ns_user.route('/')
class UserList(Resource):
    @ns_user.doc('list_users')
    def get(self):
        '''List all users'''
        pass

if __name__ == '__main__':
    app.run(debug=True)
```