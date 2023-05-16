import json
import csv
import os
import datetime
from schemas.schema import validate, get_properties
from config import data_file

data_schema = "schemas/data_schema.json"


# Callback for data topic, expects JSON encoded data of greenhouse state
def on_data(client, userdata, message):
    # Capturing time is done server-side, so small inaccuracies expected
    time = datetime.datetime.now().isoformat()
    print(message.payload.decode('utf-8'))
    try:
        data = json.loads(message.payload.decode('utf-8'))
        # Process the data here
        print(data)
    except json.decoder.JSONDecodeError:
        print("Error: Bad JSON format")
        return

    # Add timestamp
    data["timestamp"] = time

    if not validate(data, data_schema):
        print("Data entry not saved, bad format of sent data")
        return

    data_dir_path = os.path.dirname(data_file)

    # Create the directory structure if it does not exist
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)

    # Open the CSV file in append mode
    with open(data_file, mode="a", newline="") as file:
        fieldnames = get_properties(data_schema)
        # Create a CSV writer object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if os.stat(data_file).st_size == 0:
            writer.writeheader()

        writer.writerow(data)
