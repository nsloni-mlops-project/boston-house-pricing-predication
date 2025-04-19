import json
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# API Endpoint for testing with JSON (e.g., Postman)
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)
    return jsonify(output[0])

# Web form route - show prediction on res.html
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    output = regmodel.predict(final_input)[0]
    return render_template("res.html", prediction=round(output, 2))

if __name__ == "__main__":
    app.run(debug=True)
