from dataclasses import dataclass

@dataclass
class UserInput:
    age : int
    gender : str
    annual_revenue : float
    marital_status : str
    number_dependants : int
    education_level : str
    occupation : str
    health_score : float
    location : str
    policy_type : str
    previous_claims : int
    vehicle_age: int
    insurance_duration : int
    smoking_status : str
    exercise_frequency : str
    property_type : str