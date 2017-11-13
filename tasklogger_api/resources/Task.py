from flask_restful import Resource, fields, marshal_with

from tasklogger_api.models.task import Task


task_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'date': fields.DateTime()
}


class TasksListApi(Resource):
    @marshal_with(task_fields)
    def get(self):
        tasks = Task.query.all()
        return tasks
