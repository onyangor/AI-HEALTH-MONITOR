# app.py
import streamlit as st
import pandas as pd
from utils.preprocessing import preprocess_data, load_model
from utils.insights import generate_advice
import altair as alt
from io import BytesIO

st.set_page_config(page_title="AI Health Monitor", layout="wide")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("💓 AI-Powered Health Monitoring System")
st.caption("Empowering users with real-time, personalized health insights using AI")

uploaded_file = st.file_uploader("📂 Upload your wearable data (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    st.success(f"✅ File uploaded: `{uploaded_file.name}`")
    st.dataframe(df.head(), use_container_width=True)

    if st.button("🔍 Run Health Analysis"):
        model = load_model(df)
        df = preprocess_data(df, model)
        df["advice"] = df.apply(generate_advice, axis=1)

        st.session_state["latest_result"] = df
        st.session_state.history.append((uploaded_file.name, df.copy()))

        st.subheader("📉 Health Metrics Summary")
        col1, col2 = st.columns([3, 1])

        with col1:
            chart = alt.Chart(df).mark_line().encode(
                x='timestamp:T',
                y=alt.Y('heart_rate:Q', title="Heart Rate"),
                color=alt.value('crimson')
            ).properties(title="Heart Rate Trend")
            st.altair_chart(chart, use_container_width=True)

        with col2:
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download CSV Report",
                data=csv,
                file_name=f"{uploaded_file.name.split('.')[0]}_analyzed.csv",
                mime='text/csv'
            )
            st.info("📝 PDF Export Coming Soon (or use browser print > save as PDF)")

        st.subheader("🩺 Personalized Advice Table")
        st.dataframe(df, use_container_width=True)

# Historical Comparison
if len(st.session_state.history) > 1:
    st.subheader("📊 Historical Comparison Across Files")
    all_data = []
    for fname, d in st.session_state.history:
        d["source_file"] = fname
        all_data.append(d)
    combined = pd.concat(all_data)
    chart = alt.Chart(combined).mark_line().encode(
        x="timestamp:T",
        y="heart_rate:Q",
        color="source_file:N"
    ).properties(title="Heart Rate Trend Comparison")
    st.altair_chart(chart, use_container_width=True)

    st.subheader("📂 Upload History Summary")
    for fname, d in st.session_state.history:
        anomaly_counts = d['anomaly'].value_counts().to_dict()
        st.markdown(f"**{fname}** — {len(d)} records | Anomalies: {anomaly_counts.get('Anomaly', 0)}, Normal: {anomaly_counts.get('Normal', 0)}")

# Optional responsive tweaks
st.markdown("""
    <style>
        .block-container { padding: 1rem 2rem; }
        @media only screen and (max-width: 600px) {
            .block-container { padding: 0.5rem 1rem; }
            h1 { font-size: 1.5rem; }
            .css-1aumxhk { font-size: 0.85rem; }
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("🧠 Developed by **Ray Otieno** | PLP Academy | July 2025")