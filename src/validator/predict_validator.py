from donttrust import DontTrust, Schema

inputDataPredictValidation = DontTrust(
    tweet_id=Schema().string().required(),
    tweet_text=Schema().string().required(),
    user_id=Schema().string().required()
    )