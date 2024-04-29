"""
Module for managing anomalies.
"""

import logging
from app.anomalies.random_anomaly import RandomAnomalyGenerator

logger = logging.getLogger(__name__)

class AnomalyManager:
    """
    Class for managing anomalies.
    """

    def __init__(self):
        """
        Initializes the AnomalyManager.
        """
        self.anomaly_classes = {
            'random': RandomAnomalyGenerator,
        }

    def apply_anomaly(self, anomaly_type: str, **kwargs):
        """
        Applies the specified anomaly type with the given parameters.

        Args:
            anomaly_type (str): The type of anomaly to apply.
            **kwargs: Additional keyword arguments for the anomaly generator.

        Returns:
            function: A function for generating anomaly data.
        """
        logger.info("Applying anomaly: %s with parameters: %s", anomaly_type, kwargs)
        try:
            anomaly_class = self.anomaly_classes[anomaly_type]
            generator_instance = anomaly_class(**kwargs)
            return generator_instance.generate_data
        except KeyError:
            logger.error("Anomaly type %s not found.", anomaly_type)
            raise
        except Exception as error:
            logger.exception("An unexpected error occurred while applying anomaly: %s", error)
            raise
