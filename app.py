from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/feature')
def new_feature():
    return "This is a new feature in dev!"

if __name__ == '__main__':
    app.run()
