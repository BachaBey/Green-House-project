import json
import plantyactu

#function to load and read the data to .json(java script object notation) file 
def load_data(filename):
    try:
        # Open the file in read mode with an optional 'x' mode to create if missing
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # If file not found, create it with an empty dictionary
        with open(filename, 'w') as file:
            json.dump({}, file)
        return {}
    
    
ref=load_data("C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/user_database_reference_file.json")

def control_light(plant_name,pin_actuator,sensor_value):
    ref_value=ref[plant_name]["illumination"]
    ref_value_max=ref_value+10
    ref_value_min=ref_value-10

    if sensor_value>ref_value_max:
        plantyactu.activate_led(pin_actuator,False)
        return False
    
    elif sensor_value<ref_value_min:
        plantyactu.activate_led(pin_actuator,True)
        return False
    
    else:
        plantyactu.activate_led(pin_actuator,False)
        return True
    

def control_moisture(plant_name,pin_actuator,sensor_value):
    ref_value=ref[plant_name]["moisture"]
    ref_value_max=ref_value+10
    ref_value_min=ref_value-10

    if sensor_value>ref_value_max:
        plantyactu.activate_irrigation(pin_actuator,False)
        return True
    
    elif sensor_value<ref_value_min:
        plantyactu.activate_irrigation(pin_actuator,True)
        return False
    
    else:
        plantyactu.activate_irrigation(pin_actuator,False)
        return True
    

def control_temperature(plant_name,pin_actuator_cooler,pin_actuator_heater,pin_actuator_ventilator,sensor_value):
    ref_value=ref[plant_name]["temperature"]
    ref_value_max=ref_value+10
    ref_value_min=ref_value-10

    if sensor_value>ref_value_max:
        plantyactu.activate_cooler(pin_actuator_cooler,True)
        plantyactu.activate_ventilator(pin_actuator_ventilator,True)
        plantyactu.activate_heater(pin_actuator_heater,False)
        return False
    
    elif sensor_value<ref_value_min:
        plantyactu.activate_heater(pin_actuator_heater,True)
        plantyactu.activate_ventilator(pin_actuator_ventilator,True)
        plantyactu.activate_cooler(pin_actuator_cooler,False)
        return False
    
    else:
        plantyactu.activate_heater(pin_actuator_heater,False)
        plantyactu.activate_cooler(pin_actuator_cooler,False)
        plantyactu.activate_ventilator(pin_actuator_ventilator,False)
        return True
    


def control_humidity(plant_name,pin_actuator_ventilator,pin_actuator_humidity_water,sensor_value):
    ref_value=ref[plant_name]["humidity"]
    ref_value_max=ref_value+10
    ref_value_min=ref_value-10

    if sensor_value>ref_value_max:
        plantyactu.activate_ventilator(pin_actuator_ventilator,False)
        plantyactu.activate_humidity_water(pin_actuator_humidity_water,True)
        return False
    
    elif sensor_value<ref_value_min:
        plantyactu.activate_ventilator(pin_actuator_ventilator,True)
        plantyactu.activate_humidity_water(pin_actuator_humidity_water,True)
        return False
    
    else:
        plantyactu.activate_ventilator(pin_actuator_ventilator,False)
        plantyactu.activate_humidity_water(pin_actuator_humidity_water,True)
        return True
    



