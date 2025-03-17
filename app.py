from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hi Everyone .! Welcome to Demo Project. Which is deployed on baremetal kubernetes cluster "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
