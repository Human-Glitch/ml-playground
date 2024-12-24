from pathlib import Path
from model import build_model
import pickle as pk

class ModelService:
    def __init__(self) -> None:
        self.model = None

    def load_model(self, model_name = 'rf_v1'):
        model_path =  Path(f'models/{model_name}')

        if not model_path.exists():
            build_model()

        self.model = pk.load(open(f'models/{model_name}', 'rb'))

    def predict(self, input_parameters):
        return self.model.predict([input_parameters])