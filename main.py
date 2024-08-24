from flask import Flask

app = Flask(__name__)

@app.route('/')
def not_hello_world():
    return 'Not an Happy Hello, World!'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3300)
