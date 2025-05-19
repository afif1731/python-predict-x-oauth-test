import src.service.predict_service as PredictService

from quart import Blueprint, request, jsonify
from src.validator.predict_validator import inputDataPredictValidation
from src.middleware.custom_error import CustomError
from src.middleware.custom_response import CustomResponse
from src.middleware.validator import do_validate

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('', methods=['POST'])
async def RegisterController():
    try:
        req = await request.get_json()

        if not req['tweet_data']:
            raise CustomError(403, 'tweet_data tidak boleh kosong')
        elif type(req['tweet_data']) is not list:
            raise CustomError(403, 'tweet_data harus berupa array')

        data = []
        for tweetData in req['tweet_data']:
            dataValidated = do_validate(inputDataPredictValidation, tweetData)
            data.append(dataValidated)

        result = await PredictService.batch_predict_service(data)

        response = CustomResponse(201, 'sukses melakukan prediksi', {
            'result': result
        })
        return jsonify(response.JSON()), response.code
    except CustomError as err:
        return jsonify(err.JSON()),err.code