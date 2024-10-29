from speed_check import check_for_fine
from traffic_data import collect_traffic_data

def process_traffic_data():
    # Get the collected traffic data
    traffic_data = collect_traffic_data()
    
    for data in traffic_data:
        vehicle_speed = data["vehicle_speed"]
        posted_speed_limit = data["posted_speed_limit"]
        
        # Check if the vehicle should be fined
        violation = check_for_fine(vehicle_speed, posted_speed_limit)
        if violation:
            print("Violation processed.")
        else:
            print("No violation for this vehicle.")

if __name__ == "__main__":
    process_traffic_data()