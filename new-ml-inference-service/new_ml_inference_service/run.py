from flask import Flask

from api.prediction import bp as prediction_bp

app = Flask(__name__)
app.register_blueprint(prediction_bp)


if __name__ == '__main__':
    app.run(debug=True)
