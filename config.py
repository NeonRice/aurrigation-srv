import os

# General
broker_ip = os.getenv("MQTT_BROKER_IP", "127.0.0.1")

# Topics
data_topic = os.getenv("MQTT_DATA_TOPIC", "data")

# Data files
data_file = os.getenv("DATA_FILE", os.path.join(
    os.path.dirname(__file__), 'data', 'data.csv'))
