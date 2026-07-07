import joblib
import pandas as pd


# Load Model (Only Once)


model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")


def predict_loan(input_data: pd.DataFrame):
    """
    Predict Loan Approval

    Parameters
    ----------
    input_data : DataFrame

    Returns
    -------
    prediction
    probability
    """

    scaled = scaler.transform(input_data)

    prediction = model.predict(scaled)[0]

    probability = model.predict_proba(scaled)[0][1] * 100

    return prediction, probability