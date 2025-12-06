# home-assistant-mqtt-assignment
# Home Assistant + MQTT Assignment — Nakshatra Automation

**Name:** Mohamed Yaseen  
**Register Number:** 42611081  

---

## 📌 Project Overview

This project demonstrates real-time communication using:

- A Python script that publishes MQTT messages  
- Mosquitto MQTT broker  
- Home Assistant MQTT sensor to read the message  

The objective is to show live sensor updates inside Home Assistant when data is published.

---

## 🧩 MQTT Details

| Item | Value |
|------|-------|
| Broker | Mosquitto |
| Host | `<192.168.1.3>` |
| Port | `1883` |
| Topic Used | `<home/mohamedyaseen-2025/sensor>` |

---

## ▶️ Python Publisher Script

To run the script:

```sh
pip install paho-mqtt
python mqtt_publisher.py
