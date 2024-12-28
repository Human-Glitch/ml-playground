from flask import abort, Blueprint, request
from pydantic import ValidationError

from schemas.apartment import Apartment
from services import model_inference_service

bp = Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get('/')
def get_prediction() -> dict:

    try:  # get and check input parameters (feature values)
        apartment_features = Apartment(**request.args)
    except ValidationError:
        abort(code=400, description='Bad input error')

    # feed input parameters to the loaded ML model to get a prediction
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    # return a prediction value
    return {'prediction': prediction}


@bp.post('/')
def get_prediction_post() -> dict:
    try:  # get and check input parameters (feature values)
        apartment_features = Apartment(**request.json)
    except ValidationError:
        abort(code=400, description='Bad input error')

    # feed input parameters to the loaded ML model to get a prediction
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )

    # return a prediction value
    return {'prediction': prediction}
