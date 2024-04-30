Project Overview:
  -This peoject is an IoT project
  -This project is a web application designed to monitor and control greenhouse conditions for optimal plant growth. It utilizes sensors to gather environmental data and actuators to manage factors like    irrigation and lighting.

Features:

  -Plant Management: Add, delete, and view plant information within the web interface.
  -Data Visualization: Generate graphs depicting sensor data trends over time.
  -Real-Time Monitoring: Continuously monitor sensor readings for temperature, humidity, etc.
  -Automated Control: Set reference points for environmental variables and trigger actuators based on sensor readings.
  -Data Storage: Store sensor data and plant details in JSON files for future reference.

Project Structure:

  -flask_page: Contains Flask application files for handling web page interactions and back-end communication.
    *launch_web.py: Main Flask program connecting HTML pages with Python back-end logic.
    
  -plant_app_functions: Provides functionalities for managing plant information within the application.
    *planty.py: Library for plant-related actions like adding, deleting, and retrieving plant data from JSON files.
    
  -plant_actuators_functions: Controls actuator actions on the Raspberry Pi.
    *plantyactu.py: Library for sending commands to activate actuators connected to the Raspberry Pi.
    
  -plant_sensors_functions: Handles sensor interaction on the Raspberry Pi.
    *plantysens.py: Library for collecting data from sensors connected to the Raspberry Pi.
    
  -plant_control_functions: Processes sensor data using Pandas and Matplotlib.
    *control.py: Library for data manipulation, cleaning, organization, and visualization with Pandas. It utilizes Matplotlib to create graphs and save them. Saved graphs are stored in the static/images/graphs folder for web display.
    
  -raspberry_pi: Contains scripts for Raspberry Pi integration.
    *activate_rasberry.py: Reads sensor data, updates plant information in the JSON file, activates actuators based on user-defined reference values, and stores collected data in a separate JSON file.
    *linking.py: Links sensor functions with actuator control based on reference data.
