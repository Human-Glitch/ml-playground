from pathlib import Path
from model import build_model
import pickle as pk
from config import settings, logger

class ModelService:
    def __init__(self) -> None:
        self.model = None

    def load_model(self):
        model_path =  Path(f'{settings.model_path}/{settings.model_name}')
        logger.info(f"Loading model from {model_path}")

        if not model_path.exists():
            logger.warning(f"Model not found in {model_path}. Building a new model.")
            build_model()

        logger.info(f"Model {settings.model_name} exists. Loading model.")
        self.model = pk.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        logger.info(f"Making prediction with input parameters: {input_parameters}")
        return self.model.predict([input_parameters])