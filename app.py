from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/secure')
def secure_page():
    return "This is a secure page only in production!"

if __name__ == '__main__':
    app.run()
