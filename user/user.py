from flask_restful import Resource, reqparse

users = [
    {
        "name": "Vlad",
        "hobby": "Sporting",
        "customer": False
    },
    {
        "name": "Vloud",
        "hobby": "Theater",
        "customer": True
    },
    {
        "name": "Vlid",
        "hobby": "Fishing",
        "customer": False
    }
]


class User(Resource):
    def get(self, name):
        for user in users:
            if name == user["name"]:
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("hobby")
        parser.add_argument("customer")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                return "{} is already used".format(name), 400

        user = {
            "name": name,
            "hobby": args["hobby"],
            "customer": args["customer"]
        }

        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("hobby")
        parser.add_argument("customer")
        args = parser.parse_args()

        for user in users:
            if name == user["name"]:
                user["hobby"] = args["hobby"]
                user["customer"] = args["customer"]
                return user, 200

        user = {
            "name": name,
            "hobby": args["hobby"],
            "customer": args["customer"]
        }

        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted".format(name), 200
