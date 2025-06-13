from flask import Flask, render_template
from flask_socketio import SocketIO, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    message = f'{username} has joined {room}'
    print(message)
    socketio.emit('notify', {'msg': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5006)
