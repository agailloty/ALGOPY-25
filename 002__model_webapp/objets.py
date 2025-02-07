from dataclasses import dataclass

@dataclass
class MLInput:
    age : int
    gender_male : bool
    annual_revenue : float
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

    def convert_to_mlinput(self):
        mlinput = MLInput(
            age = self.age,
            annual_revenue = self.annual_revenue,
            gender_male = self.gender == "Homme",
            marital_status_divorced = self.marital_status == "Divorcé",
            marital_status_single = self.marital_status == "Célibataire",
            number_dependents= self.number_dependants,
            education_level_high_school= self.education_level == "Lycée",
            education_level_masters= self.education_level == "Master",
            education_level_phd= self.education_level == "Doctorat",
            occupation_employed= self.occupation == "Employé",
            occupation_unemployed= self.occupation == "Sans emploi",
            health_score= self.health_score,
            location_rural= self.location == "Rural",
            location_suburban= self.location == "Semi-urbain",
            policy_type_basic= self.policy_type == "Basic",
            policy_type_comprehensive= self.policy_type == "Complet",
            previous_claims= self.previous_claims,
            vehicle_age= self.vehicle_age,
            insurance_duration= self.insurance_duration,
            smoking_status_yes= self.smoking_status == "Oui",
            exercise_frequency_daily= self.exercise_frequency == "Quotidien",
            exercise_frequency_monthly= self.exercise_frequency == "Mensuel",
            exercise_frequency_rarely= self.exercise_frequency == "Rarement",
            property_type_condo= self.property_type == "Copropriété",
            property_type_apartment= self.property_type == "Appartement"
        )
        return mlinput