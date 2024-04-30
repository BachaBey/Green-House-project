from flask import Flask, render_template , request , session , redirect, url_for
import control
import planty


app = Flask(__name__)

app.secret_key="hello"
#files needed
file="C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/collected_data_file.json"
user_database_reference_filepath="C:/Users/PC-Victus/personal_growth/projet_iss_malek/flask_page/user_database_reference_file.json"


#functions needed

    #create graphs
def my_program_to_get_graphs(filename):
    data=control.load_data(filename)
    for plant_name in data:     
        for date in data[plant_name]:
            for variable in data[plant_name][date]:
                control.draw_graph(filename,plant_name,variable)

    #search for a plant
def search_plant_to_delete(ch):
    user_loaded_data_base = planty.load_data(user_database_reference_filepath)
    return ch in user_loaded_data_base
        


#sign page
@app.route("/")
def sign():
    return render_template("page_1.html")

#home page
@app.route("/page_2")
def home():
    my_program_to_get_graphs(file)
    return render_template("page_2.html")

#add plant page
@app.route("/page_3",methods=["GET", "POST"])
def add_plant_page():

    message=request.args.get("message", "")

    #if button "search" clicked
    if request.method == "POST":
        #get name and save it in a dict
        plant_name = request.form.get("plant name")
        session["plant_name"]=plant_name
        #for misclicked on "search" button while the input is clear
        if plant_name=='':
            return render_template("page_3.html", test_existance=False,message='',name='')
        #input contains a value
        else:
            #check the existance of the plant
            test_existance=planty.search_plant(plant_name)
                #case: plant exists; we show its data
            if test_existance==True :

                infos=planty.plant_info(plant_name)

                light_value=infos['illumination']
                moisture_value=infos['moisture']
                humidity_value=infos['humidity']
                temperature_value=infos['temperature']

                return render_template("page_3.html", test_existance=test_existance,light_value=light_value,moisture_value=moisture_value,humidity_value=humidity_value,temperature_value=temperature_value,name=plant_name,greenhouse='KM')
                
                #case: plant doesn't exists
            else :                
                return render_template("page_3.html", test_existance=test_existance,message="Plant doesn't exist in our DataBase. Add your own",name=plant_name)
    
    #case: button is not clicked
    else:       
        return render_template("page_3.html",message=message)


#when "use" button in the add plant page is clicked we use this function
@app.route("/save_data_page3", methods=["GET","POST"]) 
def activate_function():
    plant_name = session["plant_name"]
    #if button "use" is clicked
    if request.method == "POST":
        #case: misclicked (if button is clicked and we dont have data about the plant)
        if plant_name==None:
            return render_template("page_3.html",name='',message='',greenhouse="KM")
        #case: plant doesn't exist in our database
        elif planty.search_plant(plant_name)==False:
            return render_template("page_3.html",message="Can't use this plant because it doesn't exist in our database")
        #case: plant exist in our database
        else:
            plant_location=request.form.get("greenhouse_input","")

            print("5"+str(plant_location)+"5")
            if plant_location!="":
                infos=planty.plant_info(plant_name)

                light_value=infos['illumination']
                moisture_value=infos['moisture']
                humidity_value=infos['humidity']
                temperature_value=infos['temperature']
                plant_location=int(plant_location)

                planty.add_plant(plant_name,plant_location,temperature_value,light_value,moisture_value,humidity_value)

                session["plant_name"]=plant_name

                return render_template("page_3.html",name='',message=session["plant_name"].upper()+": Plant Added")
            else:
                return render_template("page_3.html",name=plant_name,greenhouse="give number")
    #button is not clicked
    else:
        return render_template("page_3.html",name=plant_name)



#add own data page 
@app.route('/save_data_page4',methods=["GET", "POST"])
def add_own_page():
    
    plant_name=session["plant_name"]
    #if button "use" is clicked
    if request.method == "POST":
        
        
        plant_illumination=request.form.get("light_input","")
        plant_moisture=request.form.get("moisture_input","")
        plant_humidity=request.form.get("humidity_input","")
        plant_temperature=request.form.get("temperature_input","")
        plant_location=request.form.get("greenhouse_input","")

        try:
            
            if plant_location!="":
                
                plant_illumination=float(plant_illumination)
                plant_moisture=float(plant_moisture)
                plant_humidity=float(plant_humidity)
                plant_temperature=float(plant_temperature)
                plant_location=int(plant_location)
                
                planty.add_plant(plant_name,plant_location,plant_temperature,plant_illumination,plant_moisture,plant_humidity)
                #go back to page_3
                return redirect(url_for("add_plant_page",message=plant_name.upper()+": Plant Added!"))
        #if entered data not valid
        except ValueError:
            return render_template("page_4.html",name=plant_name,greenhouse="KM")
    #button is not clicked    
    return render_template("page_4.html",name=plant_name,greenhouse="KM")




#delete plant page
@app.route("/delete",methods=["GET", "POST"])
def delete_plant_page():
    #if button "delete" is clicked
    if request.method == "POST":
        plant_name = request.form.get("plant name")
        #case: misclicked (if button is clicked and we dont have data about the plant)
        if plant_name=='':
            return render_template("page_5.html",message='')
        #plant entered
        else:
            #check existance of the plant
            test_existance=search_plant_to_delete(plant_name)
            #case: plant exists
            if test_existance==True :
    
                planty.remove_plant(plant_name)

                return render_template("page_5.html",message=plant_name+': Plant Deleted Succesfully',name=plant_name)
            #case: plant doesn't exist
            else :
                return render_template("page_5.html",message=plant_name+": Plant Doesn't Exist",name=plant_name)
    #button is not clicked 
    else:   
        return render_template("page_5.html")



    




if __name__ == "__main__":
    app.run(debug=True)

    

