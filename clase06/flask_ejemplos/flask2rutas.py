from clase06.flask_ejemplos import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hola')
def hello():
    return 'hola mundo!'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'Hola %s!' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Mini Facebook Post: %d' % post_id


if __name__ == '__main__':
    app.run()

