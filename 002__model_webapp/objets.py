from dataclasses import dataclass

@dataclass
class MLInput:
    age : int
    gender_male : bool
    annual_income : float
    marital_status_divorced : bool
    marital_status_single : bool
    number_dependents : float
    education_level_high_school : bool
    education_level_masters : bool
    education_level_phd : bool
    occupation_employed : bool
    occupation_unemployed : bool
    health_score : bool
    location_rural : bool
    location_suburban : bool
    policy_type_basic : bool
    policy_type_comprehensive : bool
    previous_claims : bool
    vehicle_age : bool
    insurance_duration : bool
    smoking_status_yes : bool
    exercise_frequency_daily : bool
    exercise_frequency_monthly : bool
    exercise_frequency_rarely : bool
    property_type_apartment : bool
    property_type_condo : bool

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