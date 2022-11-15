from flask import Flask
from flask import jsonify
import serial

app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()

@app.route('/led/encender',methods=['POST'])
def save_encenderLed():
    data = "encendido"
    message = data.encode('latin-1')
    ser.write(message)
    response = {'estadoLed': 'encendido'}
    return jsonify(response)
@app.route('/led/apagar',methods=['GET'])
def get_apagarLed():
    data="apagado"
    message=data.encode('latin-1')
    ser.write(message)
    response = {'estadoLed': 'apagado'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)