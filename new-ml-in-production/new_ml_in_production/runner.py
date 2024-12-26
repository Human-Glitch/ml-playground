"""
This module is the entry point of the application.
It loads the model and makes a prediction.
"""

from models.model_service import ModelService
from config.config import logger


@logger.catch
def main():
    logger.info("Running the application.")

    feature_values = {
        'area': 85,
        'constraction_year': 2015,
        'bedrooms': 2,
        'garden_area': 20,
        'balcony_present': 1,
        'parking_present': 1,
        'furnished': 0,
        'garage_present': 0,
        'storage_present': 1
    }

    model_service = ModelService()
    model_service.load_model()
    predictions = model_service.predict(list(feature_values.values()))

    logger.info(f"Prediction: {predictions}")
    print(f"Prediction: {predictions}")


if __name__ == '__main__':
    main()
