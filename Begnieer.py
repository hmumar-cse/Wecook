import time
import random
import requests

API_URL = "http://127.0.0.1:5000/data"

appliances = {
    "light": 20,
    "fan": 75,
    "tv": 120,
    "ac": 1500
}

while True:
    total_power = 0
    running = []

    for app, power in appliances.items():
        if random.choice([0, 1]):
            total_power += power
            running.append(app)

    data = {
        "power": total_power,
        "appliances": running
    }

    requests.post(API_URL, json=data)
    print("Sent:", data)

    time.sleep(5)
