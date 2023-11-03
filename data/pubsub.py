import os
from google.cloud import pubsub_v1

# Set the environment variable to point to the service account key file
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# Replace these with your Google Cloud Project and Pub/Sub topic details
# project_id = "arched-campus-400411"
# topic_id = "topic1"
project_id = os.getenv("PROJECT_ID")
topic_id=os.getenv("TOPIC_ID")
# Create a Pub/Sub client
publisher = pubsub_v1.PublisherClient()

# Create the topic path
topic_path = publisher.topic_path(project_id, topic_id)

# Define the message to publish
message_data = "Hello, Pub/Sub!"
message_bytes = message_data.encode("utf-8")

# Publish the message to the topic
future = publisher.publish(topic_path, data=message_bytes)
print(f"Published message {future.result()}")

# # Clean up the client
# publisher.close()
