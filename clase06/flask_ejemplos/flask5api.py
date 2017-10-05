#pip install Flask-API
from flask_api import FlaskAPI
from flask import request
import json

app = FlaskAPI(__name__)
app.datos = {}


@app.route('/')
def hello_world():
    return {'hello': 'world'}


@app.route('/user/<username>/datos',  methods=['GET', 'PUT','POST'])
def data(username):
    if request.method in ['PUT', 'POST']:
        app.datos[username] = request.data
        return request.data

    elif request.method == 'GET':
        return app.datos


if __name__ == '__main__':
    app.run()
