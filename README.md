# aurrigation-srv
Simple MQTT client "backend" for Aurrigation (Irrigation automation)

## Prerequisites

- Python 3.x

## Setup

1. Clone the repository:
git clone <repository_url>

2. Navigate to the project directory:
cd aurrigation-srv

3. Create a virtual environment:
python3 -m venv .venv

4. Activate the virtual environment:
On macOS/Linux:
source .venv/bin/activate

On Windows:
.venv\Scripts\activate

5. Install the project dependencies:
pip install -r requirements.txt

6. Start the server
python3 main.py

## Configuration
Configure the following environment variables:
- MQTT_BROKER_IP (default - localhost)
- MQTT_DATA_TOPIC (default - data)
- DATA_FILE (default ./data/data.csv)
