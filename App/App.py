from pyexpat import model
from flask import Flask, jsonify , request, render_template
#import numpy as np
#import flask
import pickle

#################################################
# Flask Setup
#################################################
app = flask.Flask(__name__, template_folder='templates')


# Load the pickle model

model = pickle.load(open("finalized_model.pkl", "rb"))


# #################################################
# # Flask Routes
# #################################################

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

    elif flask.request.method == 'POST':
        Nitrogen = flask.request.form["Nutrient - Nitrogen (kg/ha)"]
        Phosphate = flask.request.form["Nutrient - Phosphate (kg/ha)"]
        Potash = flask.request.form["Nutrient - Potash (kg/ha)"]
        Rainfall = flask.request.form["Annual Mean Rainfall (mm)"]

        input_variables = [[Nitrogen, Phosphate, Potash,Rainfall]]

        prediction = model.predict(input_variables)[0]

        return flask.render_template('index.html',
                                     original_input={"Nutrient - Nitrogen (kg/ha)": Nitrogen,
                                                     "Nutrient - Phosphate (kg/ha)": Phosphate,
                                                     "Nutrient - Potash (kg/ha)": Potash,
                                                     "Annual Mean Rainfall (mm)": Rainfall},
                                    result = prediction)

if __name__ == "__main__":
    app.run(debug=True)








