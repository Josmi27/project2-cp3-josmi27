import chatchat
import os
import flask
import flask_socketio
from chatchat import ChatBot
from rfc3987 import parse


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)



@app.route('/')
def hello():
    return flask.render_template('index.html')


# Server emits an event to client
@socketio.on('connect')
def on_connect():
    # all_messages = []
    
    # socketio.emit('list of messages',{
    #  'allMessages': list
    # }, broadcast=True)
    print('Someone connected!')

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')


@socketio.on('Entered data')
def on_submitted_data(data):
    a_user = data['username']
    a_message = data['message']
    
# scans client's data for chatbot commands    
    if a_message[:2] == "!!":
        a_message = ChatBot(a_user, a_message)[1]
        a_user = "I-Phi-Bot"

    socketio.emit('Info is now sending from server', {
        'name': a_user,
        'post': a_message
    });
        
    
    


socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
