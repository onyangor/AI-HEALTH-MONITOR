# 💓 AI-Powered Health Monitoring System

An intelligent, real-time health monitoring web application that analyzes wearable data to detect anomalies and generate personalized advice using Machine Learning.

## 📦 Features

- 📂 Upload biometric data (heart rate, SpO2, steps)
- 🔍 Run anomaly detection using Isolation Forest
- 🩺 Get personalized advice for each entry
- 📈 View interactive trend charts and comparisons
- 📥 Download analyzed results as CSV
- 🔁 Compare multiple uploads during session
- 📱 Mobile responsive with UI enhancements

---

## 🧠 Tech Stack

- Python 3
- Streamlit
- Pandas
- Scikit-learn (Isolation Forest)
- Altair (charts)
- Joblib

---

## 📊 Sample Data Format

```csv
timestamp,heart_rate,spo2,steps
2025-07-13 08:00:00,75,98,100

▶️ How to Run Locally
bash
Copy
Edit
git clone https://github.com/your-username/ai-health-monitor.git
cd ai-health-monitor
pip install -r requirements.txt
streamlit run app.py
☁️ How to Deploy to Streamlit Cloud
Push your code to GitHub

Visit https://streamlit.io/cloud

Click “New app”

Connect your GitHub repo

Set app.py as the main file

Deploy 🚀

 You can now share your app URL with others.

🧩 Future Work / IoT Integration
For deploying with IoT Wearables, follow this direction:

## Edge Deployment Plan
Use a wearable device (e.g., Raspberry Pi + Heart Rate/SpO₂ Sensor)

Send data via MQTT or REST API to a cloud server

Append streamed data to a CSV log or database

Periodically re-run analysis with the AI model

Visualize live data with Streamlit or Plotly Dash

 Tools you could integrate later:

MQTT (Mosquitto)

Node-RED or Flask API server

Firebase or Supabase backend

Raspberry Pi + MAX30102 sensor

## Author
Ray Otieno
PLP Academy Final AI Project – July 2025