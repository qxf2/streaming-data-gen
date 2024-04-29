"""
Module for defining the AnomalyGenerator abstract base class.
"""

from abc import ABC, abstractmethod

class AnomalyGenerator(ABC):
    """
    Abstract base class for anomaly generators.
    """

    @abstractmethod
    def generate_data(self):
        """
        Abstract method to generate anomaly data.
        """
        pass
