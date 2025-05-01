import requests
import random
import time

# Endpoint URL
url = "http://localhost:5000/api/push-log"

# Example log messages
log_messages = [
    ("Service started successfully", "Startup Service"),
    ("High memory usage detected", "Monitoring Agent"),
    ("Disk space running low", "Storage Engine"),
    ("User login failure", "Authentication Service"),
    ("Database connection restored", "SQL Service")
]

message, service = random.choice(log_messages)
# Pick a random log type and message
log_entry = {
    "type": random.choice(["INFO", "WARN", "ERROR"]),
    "message": message,
    "service": service
}

# Send the POST request
response = requests.post(url, json=log_entry)

# Print server response
print(f"Sent log: {log_entry}")