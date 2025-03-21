import paho.mqtt.client as mqtt
import json

# AWS IoT Core setup
AWS_IOT_ENDPOINT = "your-iot-endpoint.iot.region.amazonaws.com"
CERT_PATH = "path/to/your-certificate.pem.crt"
KEY_PATH = "path/to/your-private.pem.key"
CA_PATH = "path/to/AmazonRootCA1.pem"
TOPIC_SUB = "iot/threat/alerts"
TOPIC_PUB = "iot/threat/commands"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe(TOPIC_SUB)

def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode())
    if payload.get('status') == 'Threat':
        print(f"Threat detected: {payload['message']}")
        # Respond: e.g., pause device
        client.publish(TOPIC_PUB, json.dumps({"command": "PAUSE"}))
        print("Sent PAUSE command")

# Initialize MQTT client
client = mqtt.Client(client_id="ThreatResponder")
client.tls_set(CA_PATH, CERT_PATH, KEY_PATH)
client.on_connect = on_connect
client.on_message = on_message
client.connect(AWS_IOT_ENDPOINT, 8883, 60)

client.loop_forever()
