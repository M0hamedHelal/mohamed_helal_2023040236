from flask import Flask

# Constants
PORT = 8080
HOST = '0.0.0.0'

# App
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World from Python Flask!"

if __name__ == '__main__':
    print(f"Application started successfully on http://{HOST}:{PORT}")
    app.run(host=HOST, port=PORT)
