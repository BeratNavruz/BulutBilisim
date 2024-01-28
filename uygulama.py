from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Merhaba, Docker ve Python!'

if __name__ == 'main':
    app.run(debug=True,host='0.0.0.0')