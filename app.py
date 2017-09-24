from flask import Flask
my_app = Flask(__name__)

@my_app.route('/')

def root():
    return '<h1><font color = "pink">Hi Everybody!</h1>'

@my_app.route('/welcome')

def foo():
    return '<h1><font color = "purple">Welcome to my site!</h1>'

@my_app.route('/bye')

def moo():
    return '<h1><font color = #3498DB>Have a nice day!</h1>'

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
