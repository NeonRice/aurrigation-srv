import paho.mqtt.client as mqtt
from message_callbacks import on_data
import config

if __name__ == "__main__":
    client = mqtt.Client()

    client.connect(config.broker_ip)

    client.subscribe(config.data_topic)
    client.message_callback_add(config.data_topic, callback=on_data)

    client.loop_forever()
