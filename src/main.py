from src.flight import Flight

# Initialize flight parameters in dictionary form
# Keys would include drone hardware specs, mission type, environment data
flight_parameters = {}
# Configure the Flight object which delegates UAV's actions
flight = Flight(flight_parameters)
# Complete the tasks
flight.takeoff()
flight.fly()
flight.terminate()