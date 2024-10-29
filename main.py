from traffic_system.traffic_data import log_car_speed, get_daily_average_speed, get_cars_exceeding_threshold, get_all_car_speeds

def main():
    # initialize_database()

    
    # Calculate the daily average speed
    average_speed = get_daily_average_speed()
    print(f"Today's average speed: {average_speed} km/h")
    
    # Find cars exceeding the threshold
    violators = get_cars_exceeding_threshold()
    if violators:
        print("Cars exceeding speed limit and subject to fines:")
        for car_id, speed in violators:
            print(f"Car ID: {car_id}, Speed: {speed} km/h")
    else:
        print("No violations today.")
    
    # Retrieve and display all data in the cars table
    print("\nAll recorded car speeds:")
    all_data = get_all_car_speeds()
    for record in all_data:
        car_id, speed, recorded_date = record
        print(f"Car ID: {car_id}, Speed: {speed} km/h, Date: {recorded_date}")

if __name__ == "__main__":
    main()