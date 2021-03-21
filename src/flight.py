from typing import Dict

from src.drone import Drone
from src.mission import Task, Route
from api import data_parser
from api import signal_parser
from api import hazard_detection
from api import hazard_data
import time

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
        
        while (self.path == True):
            # The drone will update the command centre with any information it has collected based on the type mission, as well as battery and other details
            Task.task_update()
            # Should wait 5 seconds to recalibrate
            time.sleep(5)
            # Will recalculate the route from the data parser 
            self.path = Route.recalculate_motor_data(signal_parser)
            # If it detects any motion nearby or potential collision, the route will recalculate itself
            if motion_sensor_activation() == True:
                Route.recalculate_motor_data(hazard_data)
            # This allows the drone system itself to change the force/acceleration/power it is flying at to readjust for the route, and this uses neural calculations
            self.system = System(recalculate_system_data)


        


            



