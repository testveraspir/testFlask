# переименовать во Flask на сервер
from flask import Flask
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return """<html>
    <head>
	    <title>Flask-page</title>
	    <meta charset="utf-8">
        </head>
    <body>
        <h2>Китайская стена</h2>
        <img src="static/wall1.jpg">
        <img src="static/wall2.jpg">
        <img src="static/wall3.jpg">
    </body>
    </html>
    """


if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
    #  app.run()

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 8000))
#     app.run(host='127.0.0.1', port=port)
