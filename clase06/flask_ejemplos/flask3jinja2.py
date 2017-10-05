from clase06.flask_ejemplos import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    random.seed()
    rango = range(10)
    nums = [n * random.randint(1, 9) for n in rango]
    return render_template('template1.html', name=username, nums=nums)


@app.route('/user/<username>/datos')
def datos(username):
    random.seed()
    rango = range(10)
    nums = [n * random.randint(1, 9) for n in rango]
    return jsonify({"nombre": username, "nums": nums})


if __name__ == '__main__':
    app.run()

