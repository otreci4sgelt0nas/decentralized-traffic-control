import sqlite3
from datetime import date

DB_FILE = 'data/traffic_data.db'

def initialize_database():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            license_plate TEXT,
                            speed REAL,
                            recorded_date DATE
                          )''')
        conn.commit()

def log_car_speed(license_plate, speed):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cars (license_plate, speed, recorded_date) VALUES (?, ?, ?)", 
                       (license_plate, speed, date.today()))
        conn.commit()

def get_daily_average_speed():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(speed) FROM cars WHERE recorded_date = ?", (date.today(),))
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0

def get_cars_exceeding_threshold():
    avg_speed = get_daily_average_speed()
    threshold = avg_speed + 5
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, license_plate, speed FROM cars WHERE recorded_date = ? AND speed > ?", 
                       (date.today(), threshold))
        return cursor.fetchall()

def get_all_car_speeds():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, license_plate, speed, recorded_date FROM cars")
        return cursor.fetchall()