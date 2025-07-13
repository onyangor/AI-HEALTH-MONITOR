import pandas as pd
from sklearn.ensemble import IsolationForest

def preprocess_data(df, model):
    df["anomaly"] = model.predict(df[["heart_rate", "spo2", "steps"]])
    df["anomaly"] = df["anomaly"].map({1: "Normal", -1: "Anomaly"})
    return df

def load_model(df):
    model = IsolationForest(n_estimators=100, contamination=0.15, random_state=42)
    model.fit(df[["heart_rate", "spo2", "steps"]])
    return model
