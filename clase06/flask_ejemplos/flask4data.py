from clase06.flask_ejemplos import Flask, request, jsonify
import json


app = Flask(__name__)
app.datos = {}

@app.route('/user/<username>/datos',  methods=['GET', 'PUT','POST'])
def data(username):
    if request.method in ['PUT', 'POST']:
        app.datos[username] = json.loads(request.data)
        return jsonify(request.data)

    elif request.method == 'GET':
        return jsonify(app.datos)



if __name__ == '__main__':
    app.run()

