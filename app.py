from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
app = Flask(__name__)
CORS(app)   
district_summary = pd.read_csv("district_summary.csv")
daily_cases = pd.read_csv("daily_cases.csv")
X = daily_cases[["Day_Number"]]
y = daily_cases["Hospitalized"]
model = LinearRegression()
model.fit(X, y)
@app.route("/")
def home():
    return "COVID API Running"
@app.route("/districts")
def districts():
    return jsonify(district_summary.to_dict(orient="records"))
@app.route("/predict")
def predict():
    last_day = daily_cases["Day_Number"].max()

    future_days = np.array(range(last_day+1, last_day+31)).reshape(-1,1)
    predictions = model.predict(future_days)

    result = []
    for i, val in enumerate(predictions):
        result.append({
            "Day": int(last_day + i + 1),
            "Predicted_Hospitalized": int(val)
        })

    return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)
