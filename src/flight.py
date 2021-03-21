from typing import Dict

from src.drone import Drone
from src.mission import Task, Route
from api import data_parser, get_location


class Flight:

    """
    Base to configure a 'mission' based on drone specs, goal, and relevant environmental data
    """

    def __init__(self, flight_parameters: Dict):
        """
        Initialize the drone's available sensor specs based on the model type.
        :param flight_parameters:
        """
        # Drone object which holds physical specs such as available sensors,
        self.drone = Drone.build(flight_parameters)
        # Based on the input paramters, what type of mission is this going to be?
        # Also will store important information like idle/monitoring/stall time (over wildfires, livestock)
        self.task = Task.build(flight_parameters)
        # Stores and processes necessary environment information for pre-flight optimization of route
        self.data = data_parser()
        # Store 'nodes' of discrete check-in points
        # As well as the physical requirements (wing rev/s, force, etc.) between each checkpoint
        self.path = Route(self.task, flight_parameters, self.data)

    def takeoff(self):
        """
        Activates engine and sensor calibration in accordance with configured Route
        :return:
        """

    def fly(self):
        # Some loop that checks for location
        while():
            # Get location data, see if endpoint has reached
            current_state = get_location()
            # The drone will update the command centre with any information it has collected based on the type mission,
            # as well as battery and other details
            Task.notify()
            # Will recalculate the route from the data parser 
            self.drone.parse_sensor_data()
            # Update previous environment data with continously collected information
            self.data.update(self.path.recalculate_motor_data())
            # Re-optimize motor control based on new thermal plume and air current information
            self.path.recalculate_motor_data(self.data)
        #
        self._terminate()


    def terminate(self):
        """
        Prepare for landing
        :return:
        """


