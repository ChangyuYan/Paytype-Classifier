from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np
import pickle

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer

# Loading our ML Model
rf_use_hours = pickle.load(open("models/RandomForest_use_hours.pkl", "rb"))
rf_use_salaries = pickle.load(open("models/RandomForest_use_salaries.pkl", "rb"))
rf_is_productive = pickle.load(open("models/RandomForest_is_productive.pkl", "rb"))

# Loading the String Classifier
string_classifier = pickle.load(open("models/string_classifier.pkl", "rb"))


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Read from user input
    input_features = [x for x in request.form.values()]
    payment_type_string = str.upper(str(input_features[0]))
    float_features = input_features[1:]
    float_features = np.array([float(x) for x in float_features])
    float_features = float_features.reshape((1, -1))

    # Prediction
    if payment_type_string in string_classifier:
        pred_use_hours = string_classifier[payment_type_string]['use_hours']
        pred_use_salaries = string_classifier[payment_type_string]['use_salaries']
        pred_is_productive = string_classifier[payment_type_string]['is_productive']

    else:
        pred_use_hours = rf_use_hours.predict(float_features)[0]
        pred_use_salaries = rf_use_salaries.predict(float_features)[0]
        pred_is_productive = rf_is_productive.predict(float_features)[0]


    return render_template('results.html', pred_use_hours = pred_use_hours, pred_use_salaries = pred_use_salaries, pred_is_productive = pred_is_productive,
    total_dollars = float_features[0][0], total_hours = float_features[0][1], hourly_rate = float_features[0][2])



if __name__ == '__main__':
	app.run(debug=True)