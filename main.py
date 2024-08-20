from flask import Flask
from flask import *

app = Flask(__name__)

@app.route('/')
def render():
    return render_template('main.html')

@app.route("/get", methods= ["POST"])
def receive() :
    if request.method == "POST" :
        f = request.files['file']
        return "p"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)