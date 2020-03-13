from app import mqtt, socketio
from flask import Blueprint
import json

communications = Blueprint('communications', __name__)


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('test')


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('new_data', json.dumps({"message": data['payload']}))


# @socketio.on('test_socket')
# # def handle_socketio_test(message):
# #     socketio.emit('new_data', json.dumps({"test": message}))