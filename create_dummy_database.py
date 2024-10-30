import sqlite3

# Define the path for the database
db_path = 'traffic_data.db'

# Data to be inserted
data = [
    (1, "XIZ-556", 32.85, "2024-10-30"),
    (2, "OCE-033", 86.58, "2024-10-28"),
    (3, "LQN-844", 62.27, "2024-10-25"),
    (4, "KEK-678", 72.77, "2024-10-30"),
    (5, "TYZ-390", 71.35, "2024-10-29"),
    (6, "GEJ-037", 65.78, "2024-10-28"),
    (7, "OPL-113", 55.22, "2024-10-27"),
    (8, "IXW-716", 38.55, "2024-10-26"),
    (9, "UPT-108", 45.87, "2024-10-27"),
    (10, "VMD-070", 75.14, "2024-10-26"),
    (11, "CHB-002", 82.94, "2024-10-30"),
    (12, "YSA-372", 46.66, "2024-10-26"),
    (13, "BNQ-246", 73.19, "2024-10-24"),
    (14, "PHW-458", 71.19, "2024-10-30"),
    (15, "LOU-249", 53.84, "2024-10-27"),
    (16, "HSI-576", 72.48, "2024-10-29"),
    (17, "UUH-728", 59.52, "2024-10-30"),
    (18, "AMS-039", 86.38, "2024-10-29"),
    (19, "EYN-812", 54.97, "2024-10-24"),
    (20, "VTC-572", 51.35, "2024-10-28")
]

# Connect to the database and create the table
with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            license_plate TEXT NOT NULL,
            speed REAL NOT NULL,
            recorded_date DATE NOT NULL
        )
    ''')

    # Clear any existing data and insert new data
    cursor.execute("DELETE FROM cars")
    cursor.executemany("INSERT INTO cars (id, license_plate, speed, recorded_date) VALUES (?, ?, ?, ?)", data)
    conn.commit()

print(f"Database '{db_path}' created successfully.")