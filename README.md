# IoT Threat Monitoring Dashboard

A system to monitor IoT threats using an Arduino simulator, AWS Lambda for detection, Grafana for visualization, and Python for response, integrated with AWS IoT Core.

## Prerequisites
- Arduino (e.g., Uno)
- AWS IoT Core (certs, endpoint), Lambda, CloudWatch
- Grafana (local or cloud)
- Python 3, `paho-mqtt`, `boto3`
- Arduino IDE

## Setup
1. **Arduino**: Flash `arduino_code/threat_simulator.ino`.
2. **AWS IoT**: Set up a thing, certs, and rule to trigger Lambda on `iot/threat/data`.
3. **Lambda**: Deploy `lambda_function.py` (update region).
4. **Grafana**: Install locally (`sudo apt install grafana`), connect to CloudWatch (LOG_GROUP: IoTThreatMonitor).
5. **Response**: Run `response_script.py` with AWS certs.
6. **Test**: Simulate a flood, check Grafana alerts, and verify PAUSE command.

## Demo
- Detects rapid message floods and visualizes in Grafana.
- [Demo Screenshot](demo.png) <!-- Add after testing -->
