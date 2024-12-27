"""
This module is responsible for building the model.
"""

from config.config import logger
from models.pipeline.model import build_model


class ModelBuilderService:

    def __init__(self) -> None:
        self.model = None

    def train_model(self) -> None:  
        logger.info('Building the model')
        build_model()
