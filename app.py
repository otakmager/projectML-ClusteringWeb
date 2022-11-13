from flask import Flask, request, jsonify, render_template
from pyexpat import features
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open("best_model.pkl", "rb"))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template("index.html", prediction_text = "{}".format(prediction))

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)