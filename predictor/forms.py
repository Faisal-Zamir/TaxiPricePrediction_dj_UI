from django import forms

class FarePredictionForm(forms.Form):
    # Passenger Count - Integer
    Passenger_Count = forms.IntegerField(
        min_value=1,
        max_value=10,
        label="Number of Passengers",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter number of passengers'
        })
    )
    
    # Base Fare - Float
    Base_Fare = forms.FloatField(
        min_value=0.1,
        initial=3.56,
        label="Base Fare ($)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01'
        })
    )
    
    # Per Km Rate - Float
    Per_Km_Rate = forms.FloatField(
        min_value=0.1,
        initial=0.8,
        label="Rate per Kilometer ($)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01'
        })
    )
    
    # Per Minute Rate - Float
    Per_Minute_Rate = forms.FloatField(
        min_value=0.1,
        initial=0.32,
        label="Rate per Minute ($)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.01'
        })
    )
    
    # Trip Duration - Float
    Trip_Duration_Minutes = forms.FloatField(
        min_value=1,
        label="Trip Duration (minutes)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter trip duration in minutes',
            'step': '0.1'
        })
    )
    
    # Trip Distance (will be converted to log in backend)
    Trip_Distance_km = forms.FloatField(
        min_value=0.1,
        label="Trip Distance (km)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter trip distance in km',
            'step': '0.1'
        })
    )
    
    # Time of Day - Single Selection (One Hot Encoding)
    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'), 
        ('evening', 'Evening'),
        ('night', 'Night'),
    ]
    
    Time_Of_Day = forms.ChoiceField(
        choices=TIME_CHOICES,
        label="Time of Day",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Day Type - Single Selection (Weekday/Weekend)
    DAY_CHOICES = [
        ('weekday', 'Weekday (Monday-Friday)'),
        ('weekend', 'Weekend (Saturday-Sunday)'),
    ]
    
    Day_Type = forms.ChoiceField(
        choices=DAY_CHOICES,
        label="Day Type",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Traffic Conditions - Mapped to numerical values
    TRAFFIC_CHOICES = [
        ('low', 'Low Traffic (1)'),
        ('medium', 'Medium Traffic (2)'),
        ('high', 'High Traffic (3)'),
    ]
    
    Traffic_Conditions = forms.ChoiceField(
        choices=TRAFFIC_CHOICES,
        label="Traffic Conditions",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Weather Conditions - Single Selection
    WEATHER_CHOICES = [
        ('none', 'Clear/None'),
        ('rain', 'Rainy'),
        ('snow', 'Snowy'),
    ]
    
    Weather_Condition = forms.ChoiceField(
        choices=WEATHER_CHOICES,
        label="Weather Condition",
        widget=forms.Select(attrs={'class': 'form-control'})
    )