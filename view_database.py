import sqlite3

DB_FILE = 'data/traffic_data.db'

def view_database():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        
        # Check and display data from 'cars' table
        print("Contents of the 'cars' table:")
        cursor.execute("SELECT * FROM cars")
        cars_data = cursor.fetchall()
        if cars_data:
            for row in cars_data:
                print(row)
        else:
            print("No data found in the 'cars' table.")

        print("\n" + "-" * 40 + "\n")
        
        # Check and display data from 'weekly_limits' table
        print("Contents of the 'weekly_limits' table:")
        cursor.execute("SELECT * FROM weekly_limits")
        weekly_limits_data = cursor.fetchall()
        if weekly_limits_data:
            for row in weekly_limits_data:
                print(row)
        else:
            print("No data found in the 'weekly_limits' table.")
    
if __name__ == "__main__":
    view_database()