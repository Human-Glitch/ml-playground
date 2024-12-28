"""
This module contains the ModelInferenceService class which is
responsible for loading the model and making predictions.
"""

import pickle as pk
from pathlib import Path

from config.config import settings, logger


class ModelInferenceService:

    def __init__(self) -> None:
        self.model_path = settings.model_path
        self.model_name = settings.model_name

    def load_model(self) -> None:
        model_path = Path(f'{self.model_path}/{self.model_name}')
        logger.info(f'Loading model from {model_path}')

        if not model_path.exists():
            raise FileNotFoundError(
                f'Model not found in {model_path}. Please build the model.'
            )

        logger.info(f'Model {self.model_name} exists. Loading model.')

        with open(model_path, 'rb') as file:
            self.model = pk.load(file)

    def predict(self, input_parameters: list) -> list:
        logger.info(
            f'Making prediction with input parameters: {input_parameters}'
        )
        return self.model.predict([input_parameters]).tolist()
