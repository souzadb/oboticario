from flask import Flask

app = Flask(__name__)

app.run(debug=True)

@app.route('/', methods=['GET', 'POST', 'PUT'])
def home():

    return 'Hello World'