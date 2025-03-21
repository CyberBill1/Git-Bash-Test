import json
import boto3
from datetime import datetime

cloudwatch = boto3.client('logs')
LOG_GROUP = 'IoTThreatMonitor'
LOG_STREAM = 'ThreatLogs'

# Threshold for detecting a flood (e.g., 10 messages in 5 seconds)
MESSAGE_THRESHOLD = 10
TIME_WINDOW = 5  # seconds
message_count = 0
last_time = None

def log_to_cloudwatch(message):
    cloudwatch.put_log_events(
        logGroupName=LOG_GROUP,
        logStreamName=LOG_STREAM,
        logEvents=[{
            'timestamp': int(datetime.now().timestamp() * 1000),
            'message': message
        }]
    )

def lambda_handler(event, context):
    global message_count, last_time
    
    # Parse MQTT message
    payload = json.loads(event['payload'])
    current_time = datetime.now().timestamp()
    
    # Initialize timing
    if last_time is None:
        last_time = current_time
        message_count = 1
        return {'status': 'Normal'}
    
    # Check for flood
    time_diff = current_time - last_time
    message_count += 1
    
    if time_diff <= TIME_WINDOW:
        if message_count >= MESSAGE_THRESHOLD:
            alert = f"Threat detected: {message_count} messages in {time_diff}s"
            log_to_cloudwatch(alert)
            return {'status': 'Threat', 'message': alert}
    else:
        # Reset if window expires
        last_time = current_time
        message_count = 1
    
    return {'status': 'Normal'}
