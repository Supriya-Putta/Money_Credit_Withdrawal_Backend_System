from . import data_validation

class Registration:
    def __init__(self):
        pass
    
    def collecting_registration_inputs(self):
        first_name=input("Please enter your first name: ")
        data_validation.validate_name(first_name)
        last_name=input("Please enter your last name: ")
        data_validation.valid_name(last_name)
        
        
    
    