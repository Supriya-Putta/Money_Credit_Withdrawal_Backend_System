import re

def validation_name(name):
    #print(f"Inside validation name function{name}")
    pattern = r'^[a-zA-Z]+$'
    if len(name) > 3 and len(name) < 30 and re.match(pattern, name):
        print(f"{name} is valid ")
        
    else:
        print(f"{name} is invalid, please enter only charactors")
        

def validate_first_name(first_name):
    validation_name(first_name)

def validate_last_name(last_name):
    validation_name(last_name)
