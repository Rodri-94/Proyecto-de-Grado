from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    #return "hola mundo"
    return ('index.html')

app.run(debug=True, port=5000)
