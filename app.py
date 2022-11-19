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
    return render_template('index.html')

# Routing /prediksi -> prediksi class object
@app.route("/predict", methods=["POST"])
def predict():
    # Simpan data fitur object dalam array dan diubah ke integer 
    int_features = np.array([int(x) for x in request.form.values()])
    # Buat dalam array 2D karena model hanya menerima 2D array
    features = np.array([int_features])
    # Prediksi class object dengan model yang telah dibuat
    prediction = model.predict(features)
    # Karena class prediksi berupa int, ubah ke bentuk tulisan
    if(prediction==[1]):
        res = "Normal Find"
    elif(prediction==[2]):
        res = "Metastases"
    elif(prediction==[3]):
        res = "Malign lymph"
    elif(prediction==[4]):
        res = "Fibrosis"
    # Mengembalikan hasil prediksi ke index.html dalam variabel result
    return render_template("index.html", result = "{}".format(res))

# Menjalankan aplikasi dengan konfigurasi host dan debug mode
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
