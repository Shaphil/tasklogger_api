from flask_restful import Resource, fields, marshal_with

from tasklogger_api.models.task import Task


task_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'date': fields.DateTime,
    'uri': fields.Url(endpoint='task', absolute=True)
}


class TaskApi(Resource):
    @marshal_with(task_fields)
    def get(self, id):
        task = Task.query.filter_by(id=id).first()
        return task


class TasksListApi(Resource):
    @marshal_with(task_fields)
    def get(self):
        tasks = Task.query.all()
        return tasks
