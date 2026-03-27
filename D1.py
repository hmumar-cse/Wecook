from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

power_history = []
total_units = 0.0

TARIFF_PER_UNIT = 6      
BUDGET_LIMIT = 500        


def generate_power():
    global total_units

    power = random.randint(100, 1200)   
    timestamp = int(time.time())

    
    units = power / 1000 / 3600
    total_units += units

    power_history.append({
        "time": timestamp,
        "power": power
    })

   
    if len(power_history) > 50:
        power_history.pop(0)

    return power
