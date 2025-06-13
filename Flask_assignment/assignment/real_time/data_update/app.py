from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

counter = 0  # Shared global counter

@app.route('/')
def index():
    return render_template('index.html', count=counter)

@socketio.on('increment')
def handle_increment():
    global counter
    counter += 1
    emit('update_count', counter, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5005)
