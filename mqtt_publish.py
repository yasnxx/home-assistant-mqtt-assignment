import time
import json
import paho.mqtt.client as mqtt

student_name = "MOHAMED YASEEN"
unique_id = "42611081"
topic = "home/mohamedyaseen-2025/sensor"

client = mqtt.Client()
client.username_pw_set("mqtt", "1234")
client.connect("192.168.1.3", 1883, 60)  

while True:
    payload = {
        "temperature": 25,
        "humidity": 60,
        "sound": 75
    }

    client.publish(topic, json.dumps(payload), qos=1, retain=True)
    print("Published:", payload)
    time.sleep(5)
