"""
This module contains the ModelService class which is
responsible for loading the model and making predictions.
"""

import pickle as pk
from pathlib import Path

from config.config import settings, logger
from models.pipeline.model import build_model


class ModelService:

    def __init__(self) -> None:
        self.model = None

    def load_model(self) -> None:
        model_path = Path(f'{settings.model_path}/{settings.model_name}')
        logger.info(f'Loading model from {model_path}')

        if not model_path.exists():
            logger.warning(
                f'Model not found in {model_path}. Building a new model.'
            )

            build_model()

        logger.info(f'Model {settings.model_name} exists. Loading model.')

        with open(model_path, 'rb') as file:
            self.model = pk.load(file)

    def predict(self, input_parameters: list) -> list:
        logger.info(
            f'Making prediction with input parameters: {input_parameters}'
        )
        return self.model.predict([input_parameters])
