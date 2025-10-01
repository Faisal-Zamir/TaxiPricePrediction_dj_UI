import pandas as pd
import joblib
import os
import json
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and scaler
model = joblib.load(os.path.join(BASE_DIR, "linear_model.pkl"))
poly_model = joblib.load(os.path.join(BASE_DIR, "poly_model.pkl"))
poly = joblib.load(os.path.join(BASE_DIR, "poly_transformer.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "taxi_scaler.pkl"))

# New taxi ride data (same features as X_train)
new_data = pd.DataFrame({
    "Passenger_Count": [3],           # number of passengers
    "Base_Fare": [3.56],              # fixed base fare
    "Per_Km_Rate": [0.8],             # rate per km
    "Per_Minute_Rate": [0.32],        # rate per minute
    "Trip_Duration_Minutes": [53.82], # duration of trip
    "Trip_Distance_km_log": [2.996],  # log of trip distance in km
    "Time_Evening": [0],              # binary time features
    "Time_Morning": [1],
    "Time_Night": [0],
    "Day_Weekend": [0],               # 0=weekday, 1=weekend
    "Traffic_Conditions_mapped": [0], # mapped traffic condition
    "Weather_Rain": [0],              # binary weather features
    "Weather_Snow": [0]
})

def predict_taxi_price(new_data):

    # Predict (this will give you log-price if your target was Trip_Price_log)

    # Suppose these are the features to scale (same as training)
    cols_to_scale = ['Trip_Duration_Minutes', 'Base_Fare', 'Per_Km_Rate']

    #  Fit the scaler on training data
    new_data[cols_to_scale] = scaler.transform(new_data[cols_to_scale])


    new_data_poly = poly.transform(new_data) # Polynomial
    y_pred_new = poly_model.predict(new_data_poly)

    y_pred = model.predict(new_data)   # Linear
    real_price_linear = np.expm1(y_pred)

    # print("Predicted log-price:", y_pred_new)

    # Convert log-price back to real price
    real_price_poly = np.expm1(y_pred_new)   # inverse of log1p
    # print("Predicted real price (Polynomial):", real_price_poly)
    # print("Predicted real price (Linear):", real_price_linear)
    return real_price_linear, real_price_poly


def get_model_performance():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(BASE_DIR, "taxi_linear_metrics.json"), "r") as f:
        linear_metrics = json.load(f)   # loads into a Python dict

    with open(os.path.join(BASE_DIR, "taxi_poly_metrics.json"), "r") as f:
        poly_metrics = json.load(f)   # loads into a Python dict

    return linear_metrics, poly_metrics

# Example usage
# print("Model Performance Metrics:")
# linear_MSE = get_model_performance()[0]['MSE']
# linear_MAE = get_model_performance()[0]['MAE']


# linear_RMSE = get_model_performance()[0]['RMSE']


# This block will only run when executing this file directly (e.g. python titanic_predict.py)
if __name__ == "__main__":
    # test code (won’t run in Django)
    predict_taxi_price(new_data)
    get_model_performance()