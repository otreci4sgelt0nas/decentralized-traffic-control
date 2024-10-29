import sqlite3

DB_FILE = 'data/traffic_data.db'

def get_average_speed():
    """Calculate and return the average speed of all recorded vehicles."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(speed) FROM cars")
        result = cursor.fetchone()
        average_speed = result[0] if result[0] is not None else 0
        return average_speed

def update_weekly_speed_limit(new_limit):
    """Update and log the new weekly speed limit."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        
        # Ensure table for storing weekly speed limits exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS weekly_limits (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            speed_limit REAL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                          )''')
        
        # Insert new weekly speed limit
        cursor.execute("INSERT INTO weekly_limits (speed_limit) VALUES (?)", (new_limit,))
        conn.commit()