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


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Read from user input
    float_features = np.array([float(x) for x in request.form.values()])
    float_features = float_features.reshape((1, -1))

    # Prediction
    pred_use_hours = rf_use_hours.predict(float_features)[0]
    pred_use_salaries = rf_use_salaries.predict(float_features)[0]
    pred_is_productive = rf_is_productive.predict(float_features)[0]


    return render_template('results.html', pred_use_hours = pred_use_hours, pred_use_salaries = pred_use_salaries, pred_is_productive = pred_is_productive,
    total_dollars = float_features[0][0], total_hours = float_features[0][1], hourly_rate = float_features[0][2])



if __name__ == '__main__':
	app.run(debug=True)