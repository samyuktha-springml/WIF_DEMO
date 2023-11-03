import os
import json
from google.cloud import pubsub_v1

# Set the environment variable to point to the service account key file
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# Replace these with your Google Cloud Project and Pub/Sub topic details
project_id = os.getenv("PROJECT_ID")
topic_id = os.getenv("TOPIC_ID")

# Read the JSON message data from a file
with open("data/message.json", "r") as file:
    message_data = json.load(file)

# Create a Pub/Sub client
publisher = pubsub_v1.PublisherClient()

# Create the topic path
topic_path = publisher.topic_path(project_id, topic_id)

# Convert the message data to a JSON string
message_str = json.dumps(message_data)
message_bytes = message_str.encode("utf-8")

# Publish the message to the topic
future = publisher.publish(topic_path, data=message_bytes)
print(f"Published message {future.result()}")
