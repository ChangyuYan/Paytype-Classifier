from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd
import numpy as np
import pickle

# ML Packages
from sklearn.feature_extraction.text import CountVectorizer


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Loading our ML Model
    rf = pickle.load(open("models/RandomForest.pkl", "rb"))
    int_features = np.array([float(x) for x in request.form.values()])
    int_features = int_features.reshape((1, -1))
    pred = rf.predict(int_features)[0]

    return render_template('index.html',prediction = pred)



if __name__ == '__main__':
	app.run(debug=True)