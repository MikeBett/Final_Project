#from pyexpat import model
from flask import Flask, jsonify , request, render_template
#import numpy as np
#import flask
import pickle

#################################################
# Flask Setup
#################################################
app =Flask(__name__, template_folder='templates')


# Load the pickle model

model = pickle.load(open("finalized_model.pkl", "rb"))


# #################################################
# # Flask Routes
# #################################################

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return(render_template('index.html'))

    elif request.method == 'POST':
        Nitrogen = request.form["Nutrient - Nitrogen (kg/ha)"]
        Phosphate = request.form["Nutrient - Phosphate (kg/ha)"]
        Potash = request.form["Nutrient - Potash (kg/ha)"]
        Rainfall = request.form["Annual Mean Rainfall (mm)"]

        input_variables = [[Nitrogen, Phosphate, Potash,Rainfall]]

        prediction = model.predict(input_variables)[0]

        return render_template('index.html',
                                     original_input={"Nutrient - Nitrogen (kg/ha)": Nitrogen,
                                                     "Nutrient - Phosphate (kg/ha)": Phosphate,
                                                     "Nutrient - Potash (kg/ha)": Potash,
                                                     "Annual Mean Rainfall (mm)": Rainfall},
                                    result = prediction)

if __name__ == "__main__":
    app.run(debug=True)








