from datetime import datetime
from traffic_system.traffic_data import get_average_speed, update_weekly_speed_limit

def main():
    # Get the current week number
    current_week = datetime.now().isocalendar()[1]  # ISO week number of the year

    # Calculate the average speed for the data recorded
    average_speed = get_average_speed()
    print(f"Week {current_week}: The average speed is {average_speed:.2f} km/h")

    # Update and log the new weekly speed limit based on average speed
    update_weekly_speed_limit(average_speed)
    print(f"New weekly speed limit set to: {average_speed:.2f} km/h")

if __name__ == "__main__":
    main()