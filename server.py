# from flask import Flask, send_from_directory
# from flask_socketio import SocketIO, emit

# app = Flask(__name__, static_folder='.')
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Serve static files (like HTML, CSS, JS)
# @app.route('/')
# def index():
#     return send_from_directory('.', 'index.html')

# # Socket.IO events
# @socketio.on('chat message')
# def handle_message(msg):
#     print(f"Message received")
#     emit('chat message', msg, broadcast=True)

# @socketio.on('connect')
# def handle_connect():
#     print("A user connected")

# @socketio.on('disconnect')
# def handle_disconnect():
#     print("A user disconnected")

# if __name__ == '__main__':
#     socketio.run(app, host='0.0.0.0', port=3001, debug=True)


from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='.')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@socketio.on('chat message')
def handle_message(msg):
    msg['sender'] = request.sid  # Attach sender ID
    # Broadcast to all clients except the sender
    emit('chat message', msg, broadcast=True, include_self=False)

@socketio.on('connect')
def handle_connect():
    print("A user connected:", request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    print("A user disconnected:", request.sid)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3001, debug=True)
