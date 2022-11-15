from flask import Flask
from flask import jsonify
import serial

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)