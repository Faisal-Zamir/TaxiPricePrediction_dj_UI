from multiprocessing import context
from turtle import pd
from django.shortcuts import render
from predictor.ML_Files.taxi_price_Prediction import get_model_performance, predict_taxi_price
from predictor.forms import FarePredictionForm
from django.http import JsonResponse
import math
import pandas as pd
def homepage(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        form = FarePredictionForm(request.POST)
        
        if form.is_valid():
            # Get cleaned data
            data = form.cleaned_data
            
            # Prepare data dictionary (exactly as received from form)
            user_data = {
                "Passenger_Count": data['Passenger_Count'],
                "Base_Fare": data['Base_Fare'],
                "Per_Km_Rate": data['Per_Km_Rate'],
                "Per_Minute_Rate": data['Per_Minute_Rate'],
                "Trip_Duration_Minutes": data['Trip_Duration_Minutes'],
                "Trip_Distance_km": data['Trip_Distance_km'],
                "Time_Of_Day": data['Time_Of_Day'],  # Keep original value
                "Day_Type": data['Day_Type'],        # Keep original value
                "Traffic_Conditions": data['Traffic_Conditions'],  # Keep original value
                "Weather_Condition": data['Weather_Condition'],    # Keep original value
            }
            
            # Print the raw data received from user
            # print("Raw user data:", user_data)
            
            # Prepare ML-ready data
            # Prepare ML-ready data in DataFrame format (each value in list)
            ml_data = {
                "Passenger_Count": [int(data['Passenger_Count'])],
                "Base_Fare": [float(data['Base_Fare'])],
                "Per_Km_Rate": [float(data['Per_Km_Rate'])],
                "Per_Minute_Rate": [float(data['Per_Minute_Rate'])],
                "Trip_Duration_Minutes": [float(data['Trip_Duration_Minutes'])],
                "Trip_Distance_km_log": [math.log(data['Trip_Distance_km'])],
                
                # Time encoding - afternoon is base case (all zeros)
                "Time_Evening": [1 if data['Time_Of_Day'] == 'evening' else 0],
                "Time_Morning": [1 if data['Time_Of_Day'] == 'morning' else 0],
                "Time_Night": [1 if data['Time_Of_Day'] == 'night' else 0],
                
                # Day encoding
                "Day_Weekend": [1 if data['Day_Type'] == 'weekend' else 0],
                
                # Traffic mapping
                "Traffic_Conditions_mapped": [{
                    'low': 1,
                    'medium': 2, 
                    'high': 3
                }[data['Traffic_Conditions']]],
                
                # Weather encoding
                "Weather_Rain": [1 if data['Weather_Condition'] == 'rain' else 0],
                "Weather_Snow": [1 if data['Weather_Condition'] == 'snow' else 0],
            }
            # print("ML-ready data:", ml_data)
            # print(type(ml_data))
            # # print("user data:", user_data)
            new_data = pd.DataFrame(ml_data)
            # print(new_data)
            # print(type(new_data))
            linear_price, poly_price = predict_taxi_price(new_data)
            avg_price = (linear_price + poly_price) / 2
            avg_price = float(avg_price[0])  # if it's a 1-element array
            print("Average Predicted Price:", avg_price)
            linear_R2_accuracy = get_model_performance()[0]['R2'] * 100  # convert to percentage
            poly_R2_accuracy = get_model_performance()[1]['R2'] * 100  # convert to percentage
            return JsonResponse({
                "average_prediction": float(avg_price),
                "linear_prediction": float(linear_price),
                "poly_prediction": float(poly_price),
                "linear_R2_accuracy": float(linear_R2_accuracy),
                "poly_R2_accuracy": float(poly_R2_accuracy)
            })

    else:
        # GET request - show empty form
        form = FarePredictionForm()


    linear_metrics, poly_metrics = get_model_performance()

    # Convert to percentage + round
    formatted_linear_metrics = {
        key: f"{round(value, 2)}" for key, value in linear_metrics.items()
    }
    formatted_poly_metrics = {
        key: f"{round(value, 2)}" for key, value in poly_metrics.items()
    }

    context = {
        "linear_metrics": formatted_linear_metrics,
        "poly_metrics": formatted_poly_metrics,
        'form':form,
    }
    return render(request, 'predictor/homepage.html', context)
