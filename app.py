from flask import Flask, request
from flask_restful import Resource, Api
from models import Task
import config

app = config.app
mysql = config.mysql
api = Api(app)


class TaskAPI(Resource):
    def get(self, id=None):
        if id:
            task = Task(id)
            data = task.get()
        else:
            task = Task()
            data = task.get_all()

        return {
            'status': 'success',
            'data': data
        }

    def post(self):
        name = request.json['name']
        task = Task(name=name)
        task.save()
        return {'status': 'success'}

    def put(self, id):
        name = request.json['name']
        task = Task(id, name)
        task.update()
        return {'status': 'success'}

    def delete(self, id):
        task = Task(id)
        task.delete()
        return {'status': 'success'}


api.add_resource(TaskAPI, '/', '/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
