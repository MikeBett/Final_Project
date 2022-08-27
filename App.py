#from pyexpat import model
from flask import Flask, jsonify , request, render_template
import numpy as np
import pickle

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# Load the pickle model

model = pickle.load(open("finalized_model.pkl", "rb"))


#################################################
# Flask Routes
#################################################

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    prediction = model.predict

    output = prediction

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))


# @app.route("/")
# def welcome():
#     return (
#         f"Welcome to the Justice League API!<br/>"
#         f"Available Routes:<br/>"
#         f"/api/v1.0/justice-league<br/>"
#         f"/api/v1.0/justice-league/superhero/batman<br/>"
#         f"/api/v1.0/justice-league/real_name/bruce%20wayne"



# @app.route("/api/v1.0/justice-league/real_name/<real_name>")
# def justice_league_by_real_name(real_name):
#     """Fetch the Justice League character whose real_name matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = real_name.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["real_name"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": f"Character with real_name {real_name} not found."}), 404


# @app.route("/api/v1.0/justice-league/superhero/<superhero>")
# def justice_league_by_superhero__name(superhero):
#     """Fetch the Justice League character whose superhero matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = superhero.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["superhero"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": "Character not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
