"""
This module is the entry point of the application.
It trains the model.
"""
from models.model_builder_service import ModelBuilderService
from config.config import logger


@logger.catch
def main():
    logger.info("Starting the application to build model.")

    model_builder_service = ModelBuilderService()
    model_builder_service.train_model()


if __name__ == '__main__':
    main()
