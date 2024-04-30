# %%
#libraries needed
import json
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import os

# %%
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

# %% [markdown]
# Function for automated data collection for a choosed frequency 
filepath="C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/collected_data_file.json"
# Convert the dictionnaries in the json file to a DataFrame using pandas


def organize_data_to_create_dataframe(filepath,plant_name):

    #get data from the file 
    data_to_convert=load_data(filepath)
    data_to_convert=data_to_convert[plant_name]

    #convert data to a datframe and treat it
    data_to_draw_graph=pd.DataFrame(data_to_convert)
    data_to_draw_graph=data_to_draw_graph.transpose()
    data_to_draw_graph=data_to_draw_graph.reset_index(names='date')
    
    return data_to_draw_graph

# %% [markdown]
# Create graphs

# %% [markdown]
# Delete data according to a time period

# %%
def get_first_date_for_period(filepath,plant_name,period):

    #load data
    data=load_data(filepath)

    #get all dates
    all_dates_collected=list(data[plant_name].keys())

    #get last date collected
    last_date_collected=all_dates_collected.pop()

    #convert it to this format ("%Y-%m-%d %H:%M:%S")
    last_date_collected=datetime.datetime.strptime(last_date_collected,"%Y-%m-%d %H:%M:%S")

    #get the first date depending on the period
    first_date_collected=last_date_collected-datetime.timedelta(seconds=period)

    return str(first_date_collected)

# %% [markdown]
# ### !!!For real usage we use this function because the period will be on days!!!

'''def get_first_date_for_period(filepath,plant_name,period):
    data=load_data(filepath)
    all_dates_collected=list(data[plant_name].keys())
    last_date_collected=all_dates_collected.pop()
    last_date_collected=datetime.datetime.strptime(last_date_collected,"%Y-%m-%d %H:%M:%S")
    first_date_collected=last_date_collected-datetime.timedelta(days=period)
    print(first_date_collected)'''

def remove_file(filepath):
    if os.path.exists(filepath):
         os.remove(filepath)


def draw_graph(filepath,plant_name,variable):
    name='C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/static/images/graphs/'+plant_name+'_'+variable+"_graph.png"
    filename = name
    remove_file(filename)


    #define th type of the graph
    fig , ax = plt.subplots()

    #get the dataframe to draw the graph
    df=organize_data_to_create_dataframe(filepath,plant_name)

    #filter data frame depending on the period
    filtered_df = df[df['date'] > get_first_date_for_period(filepath,plant_name,60)]

    #choose the axis and the type of the graph 
    ax.plot(filtered_df['date'], filtered_df[variable.lower()], marker='o')
    
    #add graph's legend
    ax.set_title(plant_name+": "+variable+' Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel(variable)

    plt.savefig(filename, format='png')




