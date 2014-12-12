''' -- Flask Hello World -- '''

# import the Flask class from the flask module
from flask import Flask

# Create the application object
app = Flask(__name__)

app.config['DEBUG'] = True
# Use decorators to link the function to a url
# Static route
@app.route('/')
@app.route('/hello')
# define the view using a function
def hello_world():
    return 'Hello, World!?!?!'


# Dynamic route
@app.route('/test/<search_query>')
def search(search_query):
    return search_query


@app.route('/integer/<int:value>')
def int_type(value):
    print(value + 1)
    return 'correct'


@app.route('/float/<float:value>')
def float_type(value):
    print(value + 1)
    return 'correct'


# Dynamic value that accecpts slashes
@app.route('/path/<path:value>')
def path_type(value):
    print(value)
    return 'correct'

@app.route('/name/<name>')
def index(name):
    if name.lower() == 'michael':
        return 'Hello {}'.format(name), 200
    else:
        return 'Not Found', 404


# start the development server by using the run() method
if __name__ == '__main__':
    app.run()
