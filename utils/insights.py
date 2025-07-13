def generate_advice(row):
    if row["anomaly"] == "Anomaly":
        if row["heart_rate"] > 110:
            return "High heart rate detected. Consider resting and hydrating."
        elif row["spo2"] < 92:
            return "Low SpO₂ detected. Ensure proper ventilation or consult a doctor."
    return "Vitals appear normal. Keep up the good work!"
