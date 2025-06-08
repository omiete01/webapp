from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello there, DevOps!!!\n"

if __name__ in "__main__":
    app.run(host='0.0.0.0', port=5000)