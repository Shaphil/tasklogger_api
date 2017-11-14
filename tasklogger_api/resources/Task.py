from flask_restful import abort, Resource, fields, marshal_with, reqparse

from tasklogger_api import db
from tasklogger_api.models.task import Task


task_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'date': fields.DateTime,
    'uri': fields.Url(endpoint='task', absolute=True)
}


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('date')


class TaskApi(Resource):
    """ Deal with single task """
    @marshal_with(task_fields)
    def get(self, id):
        task = Task.query.filter_by(id=id).first()
        return task


class TasksListApi(Resource):
    """ Deal with a list of tasks """
    @marshal_with(task_fields)
    def get(self):
        tasks = Task.query.all()
        return tasks

    @marshal_with(task_fields)
    def post(self):
        args = parser.parse_args()
        task_name = args['name']
        if task_name:
            task = Task(name=task_name)
            db.session.add(task)
            db.session.commit()
            return task, 201

        return abort(400)
