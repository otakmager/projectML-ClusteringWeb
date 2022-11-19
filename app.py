from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import pickle
from pyexpat import features
from flask_cors import CORS, cross_origin

app = Flask(__name__)
model = pickle.load(open("best_model.pkl", "rb"))
CORS(app, support_credentials=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        int_features = np.array([int(x) for x in request.form.values()])
        features = np.array([int_features])
        prediction = model.predict(features)
        return f'{prediction}'
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
@cross_origin(supports_credentials=True)
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def predict():
    if request.method == 'POST':
        return render_template('index.html', request.form.get("lymphatic"))
    
    # # int_features = [int(x) for x in request.form.values()]
    # int_features = request.form.values()
    # features = [np.array[int_features]]
    # prediction = model.predict(features)
    # return render_template("index.html", prediction_text = "OK")
    # # return render_template("index.html", prediction_text = "{}".format(prediction))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
