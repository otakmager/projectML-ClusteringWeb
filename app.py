from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open("best_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    int_feature = [int(x) for x in request.form.values()]
    feature = [np.array[int_feature]]
    prediction = model.predict(feature)
    return render_template("index.html", prediction = "{}".format(prediction))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
