from flask import Blueprint, request

from schemas.apartment import Apartment
from services.model_inference_service import ModelInferenceService

bp = Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get('/')
def get_prediction() -> dict:
    # get and check input parameters (feature values)
    apartment_features = Apartment(**request.args)

    # load an existing ML model
    model_inference_service = ModelInferenceService()
    model_inference_service.load_model()

    # feed input parameters to the loaded ML model to get a prediction
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    # return a prediction value
    return {'prediction': prediction}
