import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pickle

# Set config
st.set_page_config(page_title="Customer Segmentation", layout="centered")

# Light green and white theme
st.markdown("""
<style>
html, body, .stApp {
    background-color: #fdfefc;
    font-family: 'Segoe UI', sans-serif;
    color: #2e7d32;
}
h1, h2, h3, h4 {
    color: #1b5e20;
}

/* ✅ Input fields */
.stTextInput input,
.stNumberInput input,
.stDateInput input {
    background-color: #ffffff;
    border: 2px solid #a5d6a7;
    border-radius: 8px;
    padding: 10px;
    color: #1b5e20;
    font-weight: 500;
}

/* ✅ Fix for label text color */
label, .stTextInput label, .stNumberInput label, .stDateInput label {
    color: #2e7d32 !important;
    font-weight: 600;
}

/* ✅ Buttons */
.stButton>button {
    background-color: #81c784;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s ease;
}
.stButton>button:hover {
    background-color: #66bb6a;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)


# Load model and scaler
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('Scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Simulate page using session state
if 'prediction_done' not in st.session_state:
    st.session_state.prediction_done = False

# Input Page
if not st.session_state.prediction_done:
    st.title("🌿 Customer Segmentation App")
    st.subheader("Predict customer cluster using RFM analysis")

    customer_id = st.text_input("Customer ID")
    total_visits = st.number_input("Total Visits", min_value=0, step=1)
    total_spent = st.number_input("Total Money Spent (₹)", min_value=0.0, step=10.0)
    last_visit_date = st.date_input("Last Visit Date")

    if st.button("Predict Cluster"):
        if last_visit_date:
            today = datetime.today().date()
            recency = (today - last_visit_date).days
            user_data = pd.DataFrame([[recency, total_visits, total_spent]],
                                     columns=["Recency", "Frequency", "Monetary"])
            user_scaled = scaler.transform(user_data)
            cluster = model.predict(user_scaled)[0]

            st.session_state.customer_id = customer_id
            st.session_state.cluster = cluster
            st.session_state.prediction_done = True
            st.rerun()

# Result Page
else:
    st.title("📊 Prediction Result")

    cluster = st.session_state.cluster
    customer_id = st.session_state.customer_id

    cluster_desc = {
        0: "🟢 **Loyal Customers** – They shop frequently and spend well. Nurture them with rewards!",
        1: "🟡 **Potential Loyalists** – Good spending, but infrequent visits. Send engagement offers!",
        2: "🔴 **At-Risk Customers** – Haven't visited in a while. Try win-back strategies!",
        3: "⚪ **New Customers** – Recently acquired. Guide them with welcome deals."
    }

    st.markdown(f"### Customer ID: `{customer_id}`")
    st.markdown(f"### 🔍 Predicted Cluster: **Cluster {cluster}**")
    st.markdown(cluster_desc.get(cluster, "No description available for this cluster."))

    if st.button("🔙 Back to Input"):
        st.session_state.prediction_done = False
        st.rerun()
