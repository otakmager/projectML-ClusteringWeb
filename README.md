# [Project Machine Learning : Clustering with Flask Website](https://github.com/otakmager/projectML-ClusteringWeb)
![Python](https://img.shields.io/badge/python->=3.11.0-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap->=5.2-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![Flask](https://img.shields.io/badge/flask->=2.2-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Introduction

This repo is the result of a project assignment for a machine learning course at my university which was assisted by other group members. This project is to create a website that can cluster from the models that have been made. This model was created using the KMeans algorithm with 3 clusters that were trained with the seed dataset.

## Reminder
This project mostly use Bahasa Indonesia in the documentation but if you read the code it will be easy without having to understand Bahasa Indonesia

## Link Dataset 
- [UCI](https://archive.ics.uci.edu/ml/datasets/seeds)
- [Kaggle](https://www.kaggle.com/datasets/rwzhang/seeds-dataset)

## Tech
This project uses a number of open source projects to work properly:

- HTML, CSS, and JS
- Python
- Flask
- VSCode
- Jupyter Notebook
- Google Colab

## Installation

Clone this repository
```
https://github.com/otakmager/projectML-ClusteringWeb.git
```
Open CMD and install flask
```
pip install Flask
```
Move to work directory (cloned repo)
```
cd projectML-ClusteringWeb
```
Make python environment
```
py -3 -m venv venv
```
Activate the environemnet
```
venv\Scripts\activate
```
Make sure you have installed numpy, pandas, and scikit learn, if not you must install with this prompt in CMD
```
pip install numpy
pip install pandas
pip install -U scikit-learn scipy matplotlib
```
Open VSCode
```
Change python interpreter to global version 
```
In active CMD or via terminal VSCode in working directory run flask
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
Open browser and paste the link from flask
```
ex: http://127.0.0.1:5000
```
Finish
