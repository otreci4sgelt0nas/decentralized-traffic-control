import json
from datetime import datetime

# File to store logged data
LOG_FILE = 'traffic_data_log.json'

def log_car_data(car_id, speed):
    """
    Log the car ID and speed in a JSON file.

    Parameters:
    - car_id (str): The unique ID of the car
    - speed (int): The current speed of the car
    """
    log_entry = {
        'car_id': car_id,
        'speed': speed,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Open the log file and append data
    try:
        with open(LOG_FILE, 'a') as log_file:
            json.dump(log_entry, log_file)
            log_file.write('\n')  # Newline for each log entry
    except Exception as e:
        print(f"Error logging car data: {e}")

def get_traffic_log():
    """
    Retrieve the logged traffic data.

    Returns:
    - data (list): List of logged car speed data
    """
    try:
        with open(LOG_FILE, 'r') as log_file:
            data = [json.loads(line) for line in log_file]
        return data
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error reading log file: {e}")
        return []