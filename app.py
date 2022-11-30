from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

# Inisialisasi aplikasi and model prediction
app = Flask(__name__)
model = pickle.load(open("best_model.pkl", "rb"))

# Routing aplikasi awal -> menampilkan index page
@app.route("/")
def home():
    return render_template('index_2.html')

# Routing /prediksi -> prediksi class object
@app.route("/predict", methods=["POST"])
def predict():
    # Simpan data fitur object dalam array dan diubah ke float 
    float_features = np.array([float(x) for x in request.form.values()])
    # Buat dalam array 2D karena model hanya menerima 2D array
    features = np.array([float_features])
    # Prediksi class object dengan model yang telah dibuat
    prediction = model.predict(features)
    # Karena class prediksi berupa int, ubah ke bentuk 
    if(prediction==np.array([0])):
        res = "Rosa Wheat"
    elif(prediction==np.array([1])):
        res = "Canadian Wheat"
    elif(prediction==np.array([2])):
        res = "Kama Wheat"
    # Mengembalikan hasil prediksi ke index.html dalam variabel result
    return render_template("index_2.html", result = "{}".format(res))

# Menjalankan aplikasi dengan konfigurasi host dan debug mode
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
