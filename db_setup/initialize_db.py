import sqlite3

def create_table():
    """
    Create the car_speeds table if it doesn't exist.
    """
    DB_FILE = 'traffic_data.db'

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS car_speeds (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            car_id TEXT NOT NULL,
                            speed INTEGER NOT NULL,
                            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                        )''')
        conn.commit()

if __name__ == "__main__":
    create_table()
    print("Database and table initialized successfully.")