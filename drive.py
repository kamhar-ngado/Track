import socketio
import eventlet
from flask import Flask

sio = socketio.Server()

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=3000)
    app = socketio.Midleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
