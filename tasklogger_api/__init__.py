from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('tasklogger_api.settings.DevelopmentConfig')
api = Api(app)

from tasklogger_api.resources.Task import TasksListApi

api.add_resource(TasksListApi, '/api/tasks', endpoint='taskslist')
