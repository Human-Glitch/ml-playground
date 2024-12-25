from model_service import ModelService
from config import logger

@logger.catch
def main():
    logger.info("Running the application.")
    
    model_service = ModelService()
    model_service.load_model()
    predictions = model_service.predict([85, 2015, 2, 20, 1, 1, 0, 0, 1])
    
    logger.info(f"Prediction: {predictions}")
    print(f"Prediction: {predictions}")

if __name__ == '__main__':
    main()