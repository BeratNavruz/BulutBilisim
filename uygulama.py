from flask import Flask

app = Flask(name)

@app.route('/')
def hello():
    return 'Merhaba, Docker ve Python!'

if name == 'main':
    app.run(debug=True,host='0.0.0.0')