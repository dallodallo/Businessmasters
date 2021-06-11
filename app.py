from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import joblib

#load our model
model = joblib.load("modell")

#make our Flask api...
app = Flask(__name__, template_folder = "template" )

#form urls/...
@app.route("/")
def home():
    return render_template("type.html")
    

@app.route("/prediction", methods = ["POST"])
def prediction():
    q = request.form["Gender"] #Accepting form data
    w = request.form["Nationality"]
    e = request.form["Age"]
    r = request.form["Juice"]
    t = request.form["Dessert"]
    damp = {"Gender":q, "Nationality":w, "Age":e, "Juice":r,"Dessert":t} #creating an out of sample data/question using dictonary
    test = pd.DataFrame(damp, index = [289]) # converting the dictonary into Pandas dataframe
    result = model.predict(test) #parsing it to our model for predicting
    results = result
    for result in results: # comparing predicted value to the value of the tranformed labels
        if result>=4 and result<=4.9:
            result = "Traditional Food"
        elif result>=5 and result<=5.9:
            result = "Western Food"
        elif result<=0 and result<=0.9:
            result = "African Food"
        elif result>=3 and result<=3.9:
            result = "Asian Food"
        elif result>=2 and result<=2.9:
            result = "European Food"
        else:
            print("Sea Food")
    return render_template("type.html", pred = "They will most likely order : {}".format(result)) #return prediction, which is the result result.
    

if __name__ == "__main__": # Run this file as the main file...
    app.run(debug = True)
   

            
