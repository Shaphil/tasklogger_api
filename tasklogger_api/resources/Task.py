from flask_restful import Resource


class TasksListApi(Resource):
    def get(self):
        return {'message': '.:: Welcome to TaskLogger Api ::.'}
