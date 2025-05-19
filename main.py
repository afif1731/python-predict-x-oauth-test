from quart import Quart, jsonify
from quart_cors import cors
from src.controller.predict.routes import predict_bp
from src.middleware.custom_error import CustomError
from dotenv import load_dotenv

import os

load_dotenv()

PORT = os.getenv('PORT')

app = Quart(__name__)
app = cors(app, allow_origin="*")

app.register_blueprint(predict_bp, url_prefix='/predict')

@app.errorhandler(CustomError)
async def handle_custom_error(error):
    response = jsonify(error.JSON())
    response.status_code = error.code
    return response

@app.route('/')
def home():
    return 'Runnin Wild💫...'

if __name__ == '__main__':
    app.run(port=PORT)