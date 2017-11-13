from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('tasklogger_api.settings.DevelopmentConfig')
api = Api(app)
db = SQLAlchemy(app)

from tasklogger_api.resources.task import TaskApi, TasksListApi

api.add_resource(TasksListApi, '/api/tasks', endpoint='taskslist')
api.add_resource(TaskApi, '/api/tasks/<id>', endpoint='task')
