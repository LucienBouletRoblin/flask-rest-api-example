from flask import Flask
from flask_restful import Api
from user.user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
