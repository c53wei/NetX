from typing import Dict
from abc import ABC, abstractmethod

class Drone(ABC):
    """
    Holds drone object, containing physical specs of the used model
    """

    @abstractmethod
    def __int__(self):
        """

        :return:
        """

    @staticmethod
    @abstractmethod
    def build(drone_parameters: Dict)\:
        """

        :param drone_parameters:
        :return:
        """

        drone = Drone()
        for name, value in drone_parameters.items():
            setattr(drone, name, value)

        return drone
