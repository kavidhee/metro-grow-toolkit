#!/usr/bin/env python3
"""
Data logging script for Metro-Grow vertical farming toolkit.
Reads simulated sensor data (pH, humidity, temperature, light) and logs to CSV.
"""

import csv
import time
import random
from datetime import datetime

# Configuration
LOG_INTERVAL = 60  # seconds between readings
CSV_FILE = "sensor_data.csv"
SENSOR_NAMES = ["pH", "humidity", "temperature", "light"]

def read_sensor(sensor_type):
    """
    Simulate reading a sensor. In a real setup, this would interface with hardware.
    Returns a float value.
    """
    # Simulate realistic ranges
    if sensor_type == "pH":
        return round(random.uniform(5.5, 7.5), 2)
    elif sensor_type == "humidity":
        return round(random.uniform(40.0, 85.0), 2)
    elif sensor_type == "temperature":
        return round(random.uniform(18.0, 28.0), 2)
    elif sensor_type == "light":
        return round(random.uniform(0, 1000), 2)
    else:
        return 0.0

def log_data():
    """
    Read all sensors and write a row to the CSV file.
    """
    timestamp = datetime.now().isoformat()
    row = [timestamp]
    for sensor in SENSOR_NAMES:
        value = read_sensor(sensor)
        row.append(value)
    
    # Write to CSV
    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        # Write header if file is empty
        if f.tell() == 0:
            writer.writerow(["timestamp"] + SENSOR_NAMES)
        writer.writerow(row)
    
    print(f"Logged: {timestamp} - {dict(zip(SENSOR_NAMES, row[1:]))}")
    return row

def main():
    print("Metro-Grow Data Logger starting...")
    print(f"Logging interval: {LOG_INTERVAL} seconds")
    print(f"Data will be saved to: {CSV_FILE}")
    
    try:
        while True:
            log_data()
            time.sleep(LOG_INTERVAL)
    except KeyboardInterrupt:
        print("\nData logger stopped by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()