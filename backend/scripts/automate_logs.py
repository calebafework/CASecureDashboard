import requests
import random
import time

# Endpoint URL
url = "http://localhost:5000/api/push-log"

# Example log messages
log_messages = [
    "Service started successfully",
    "High memory usage detected",
    "Disk space running low",
    "User login failure detected",
    "Database connection restored"
]

# Pick a random log type and message
log_entry = {
    "type": random.choice(["INFO", "WARN", "ERROR"]),
    "message": random.choice(log_messages)
}

# Send the POST request
response = requests.post(url, json=log_entry)

# Print server response
print(f"Sent log: {log_entry}")
print(f"Server response: {response.status_code} {response.text}") 