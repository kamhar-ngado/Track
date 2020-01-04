import socketio
import eventlet
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image


sio = socketio.Server()

app = Flask(__name__)

@sio.on('telemetry')
def telemetry(sid, data):
    image = Image.open(bytesIO(base64.b64decode(data['image'])))
    image = np.asarray(image)
    

@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0, 0)
    
def send_control(steering_angle, throttle):
    sio.emit('steer', data = {
        'steering_angle': steering_angle.__str__(),
        'throttle': throttle.__str__()
    })

if __name__ == '__main__':
    model = load_model('model.h5')
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
