import json
import time
import datetime
import plantysens
import linking


#function to save the data to .json(java script object notation) file 
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

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


filepath="C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/collected_data_file.json"
user_database_reference_filepath="C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/user_database_reference_file.json"
plant_configuration_database_filepath="C:/Users/PC-Victus/personal_growth/projet_iss_malek/rasberry_pi/plant_configuration_database.json"



def activate_the_program(filepath):
    while True:    
        #load data from file
        collected_data=load_data(filepath)
        user_database_reference=load_data(user_database_reference_filepath)
        
        for plant_name in user_database_reference:
            
            #check the existance of a plant in the file and add it if not
            if plant_name not in collected_data:
                collected_data.update({plant_name:{}})
                save_data(collected_data,filepath)
                
        collected_data=load_data(filepath)
        for plant_name in user_database_reference:

            plant_config=load_data(plant_configuration_database_filepath)

            #get the current time
            current_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            #get pins for sensors
            moisture_pin_number=plant_config[plant_name]['sensor']['moisture']
            temperature_pin_number=plant_config[plant_name]['sensor']['temperature']
            light_pin_number=plant_config[plant_name]['sensor']['light']
            humidity_pin_number=plant_config[plant_name]['sensor']['humidity']
            
            #get data from sensors
            moisture_sensor_data=plantysens.read_moisture(moisture_pin_number)
            temperature_sensor_data=plantysens.read_temperature(temperature_pin_number)
            illumination_sensor_data=plantysens.read_light(light_pin_number)
            humidity_sensor_data=plantysens.read_humidity(humidity_pin_number)
           
            #add the collected data from sensors to the file
            infos={"temperature":temperature_sensor_data,"illumination":illumination_sensor_data,"moisture":moisture_sensor_data,"humidity":humidity_sensor_data}
            collected_data[plant_name].update({current_time:infos})
            
            #save data in the file
            save_data(collected_data,filepath)

            #get greenhouse number
            greenhouse_number="greenhouse"+str(user_database_reference[plant_name]['greenhouse'])
            
            #get pins for sensors
            led_pin_number=plant_config[greenhouse_number]['actuator']['led']
            irrigation_pin_number=plant_config[greenhouse_number]['actuator']['irrigation']
            ventilator_pin_number=plant_config[greenhouse_number]['actuator']['ventilator']
            cooler_pin_number=plant_config[greenhouse_number]['actuator']['cooler']
            heater_pin_number=plant_config[greenhouse_number]['actuator']['heater']
            humidity_water_pin_number=plant_config[greenhouse_number]['actuator']['humidity_water']

            #control the greenhouse
            while not( linking.control_light(plant_name,led_pin_number,illumination_sensor_data) and linking.control_moisture(plant_name,irrigation_pin_number,moisture_sensor_data) and linking.control_temperature(plant_name,cooler_pin_number,heater_pin_number,ventilator_pin_number,temperature_sensor_data) and linking.control_humidity(plant_name,ventilator_pin_number,humidity_water_pin_number,humidity_sensor_data)):
                time.sleep(5)
                moisture_sensor_data=plantysens.read_moisture(moisture_pin_number)
                temperature_sensor_data=plantysens.read_temperature(temperature_pin_number)
                illumination_sensor_data=plantysens.read_light(light_pin_number)
                humidity_sensor_data=plantysens.read_humidity(humidity_pin_number)


            
        #choose the period for taking data
        time.sleep(10) #in second so for example for example for 6 hours we can put 6*3600 (3600 is the number of seconds in an hour)

activate_the_program(filepath)