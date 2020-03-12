from app import mqtt
from flask import Blueprint

communications = Blueprint('communications', __name__)


@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('test')


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic = message.topic,
        payload = message.payload.decode()
    )
    print(f"Topic: {data['topic']}\nMessage: {data['payload']}")
