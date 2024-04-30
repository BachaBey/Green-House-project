#save the data in lists
import json

#function to save the data to .json(java script object notation) file 
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

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

app_database_reference_filepath="C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/database_reference_file.json"
user_database_reference_filepath="C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/user_database_reference_file.json"


#search if a plant is in our data base or not
def search_plant(ch):
    user_loaded_data_base = load_data(user_database_reference_filepath)
    app_loaded_data_base = load_data(app_database_reference_filepath)
    if ch in user_loaded_data_base or ch in app_loaded_data_base :
        return True
    else:
        return False

#plant search function that returns list of plant's information 
def plant_info(ch):
    user_loaded_data_base=load_data(user_database_reference_filepath)
    app_loaded_data_base=load_data(app_database_reference_filepath)
    if ch in user_loaded_data_base:
        return user_loaded_data_base[ch]
    else:
        return app_loaded_data_base[ch]


#add plant and its data to the lists
def add_plant(plant_name,plant_location,plant_temperature,plant_illumination,plant_moisture,plant_humidity):
    user_loaded_data_base=load_data(user_database_reference_filepath)
    user_loaded_data_base.update({plant_name:{"greenhouse":plant_location,"temperature":plant_temperature,"illumination":plant_illumination,"moisture":plant_moisture,"humidity":plant_humidity}})  
    save_data(user_loaded_data_base,user_database_reference_filepath)

#remove plant and its data to the lists
def remove_plant(ch):
    user_loaded_data=load_data(user_database_reference_filepath)
    user_loaded_data.pop(ch)
    save_data(user_loaded_data,user_database_reference_filepath)

#to delete all the data of the app run this cell
def delete_all():
        global list_plant_name,list_plant_temperature,list_plant_illumination,list_plant_moisture,list_plant_wind,list_plant_humidity
        ch=input("are you sure you want to delete if yes press'y'")
        if ch.upper()=='Yes':
            save_data({},user_database_reference_filepath)

            
