import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Customer Segmentation App", layout="wide")

# ✅ Custom Light Theme with Green Accents
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

/* ✅ Sidebar text color */
[data-testid="stSidebar"] {
    background-color: #e8f5e9;
}
[data-testid="stSidebar"] * {
    color: #1b5e20 !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# ✅ Sidebar Navigation
st.sidebar.title("Navigation")
nav = st.sidebar.radio("Go to", ["Landing Page", "What is RFM Analysis ?","Our Identifiable Clusters", "Find the Cluster", "Filter the Customers"])

# Placeholder routing (no content yet)
if nav == "Landing Page":
    st.title("Customer Segmentation using RFM Analysis")
    st.markdown("---")

    st.header("🔍 Problem Statement")
    st.markdown("""
    Modern businesses accumulate vast amounts of customer purchase data, but struggle to derive actionable insights. 
    Without knowing which customers are the most valuable, most loyal, or at risk of churning, it becomes difficult 
    to personalize marketing strategies or improve retention.

    This project aims to solve that problem by applying RFM (Recency, Frequency, Monetary) Analysis to segment customers 
    based on their purchasing behavior.

    By doing so, businesses can:

    - 🔍 Identify high-value loyal customers  
    - ⚠️ Detect inactive or at-risk customers  
    - 📈 Target specific groups with tailored marketing campaigns  
    - 💡 Maximize ROI by focusing on the right customer segments  
    """)

    st.markdown("---")
    st.header("📘 About the Project")
    st.markdown("""
    This project utilizes historical customer transaction data to perform segmentation using RFM analysis. 
    RFM stands for:
    
    - **Recency**: How recently a customer made a purchase  
    - **Frequency**: How often they purchase  
    - **Monetary**: How much money they spend  

    In this project:
    
    - We have calculated **three features**: Recency, Frequency, and Monetary.
    - Instead of calculating an RFM score, we directly applied **clustering algorithms** on these features.
    - The goal was to group customers into meaningful clusters that reflect their purchasing behavior.
    """)



elif nav == "What is RFM Analysis ?":
    st.title("📊 What is RFM Analysis?")

    st.markdown("""
    RFM Analysis is a powerful customer segmentation technique used in marketing and customer relationship management. It helps businesses identify and group customers based on their purchasing behavior using three key metrics:

    ### 🧩 Components of RFM:

    - **Recency (R):**  
    How recently a customer made a purchase.  
    ➤ Customers who purchased recently are more likely to respond to promotions.

    - **Frequency (F):**  
    How often a customer makes a purchase.  
    ➤ Frequent buyers are usually more loyal and engaged.

    - **Monetary (M):**  
    How much money a customer has spent.  
    ➤ High-spending customers are often your most valuable ones.

    ---

    ### 🧠 Why is RFM Analysis Important?

    - 🎯 **Customer Segmentation:**  
    Group customers into meaningful segments like loyal, new, or at-risk customers.

    - 📢 **Personalized Marketing:**  
    Tailor campaigns to specific customer groups, improving engagement and conversion rates.

    - 💰 **Maximize ROI:**  
    Focus resources on high-value segments to get the best return on investment.

    - 🔄 **Retention Strategies:**  
    Identify and re-engage customers who haven’t purchased in a while.

    ---

    ### 💼 Real-World Applications:

    - **E-commerce:**  
    Target top-spending customers with exclusive deals.

    - **Retail:**  
    Send reminders or discounts to customers who haven’t visited in a while.

    - **Subscription Services:**  
    Identify users at risk of canceling their plans.

    """)
elif nav == 'Our Identifiable Clusters':
    st.title("🧩 Our Identifiable Clusters")
    st.markdown("""
    ### 🟢 Cluster 1 – Loyal & High-Value Customers
    - **Recency:** 3.69 (very recent)
    - **Frequency:** 1623.69 (extremely frequent)
    - **Monetary:** ₹79,646.54 (very high spenders)

    **📌 Description:**  
    These are your **most valuable and loyal customers**. They shop frequently, spend heavily, and have purchased very recently. Perfect for VIP treatment, loyalty programs, and exclusive offers.

    ---

    ### 🟡 Cluster 0 – Regular but Moderate Spenders
    - **Recency:** 38.77 (recent)
    - **Frequency:** 65.96 (moderate)
    - **Monetary:** ₹1,430.23 (moderate)

    **📌 Description:**  
    This group includes **engaged and moderately valuable customers**. They buy occasionally and spend a fair amount. With some nurturing, they could become loyal top-tier customers.

    ---

    ### 🔴 Cluster 2 – At-Risk or Inactive Customers
    - **Recency:** 244.70 (very old)
    - **Frequency:** 17.99 (low)
    - **Monetary:** ₹342.94 (low)

    **📌 Description:**  
    These customers are **inactive or at risk of churning**. They rarely buy, haven’t purchased in a long time, and spend little. Re-engagement through personalized offers or surveys might revive them.
    """, unsafe_allow_html=True)
elif nav == "Find the Cluster":
    st.title("🔍 Find the Customer's Cluster")

    # Load Scaler and Model
    with open('Scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)

    st.markdown("Enter customer details below to predict which RFM cluster they belong to:")

    # Input Fields
    customer_id = st.text_input("Customer ID")
    last_visit = st.date_input("Last Visit Date")
    total_visits = st.number_input("Total Number of Visits", min_value=1, step=1)
    total_spent = st.number_input("Total Amount Spent (₹)", min_value=0.0, step=10.0)

    # Calculate Recency
    today = datetime.today().date()
    if last_visit:
        recency = (today - last_visit).days
    else:
        recency = None

    # On Predict Button Click
    if st.button("Predict Cluster"):
        if not customer_id or recency is None:
            st.warning("⚠️ Please fill all the fields.")
        else:
            # Create dataframe
            input_df = pd.DataFrame({
                'Recency': [recency],
                'Frequency': [total_visits],
                'Monetary': [total_spent]
            })

            # Standardize the data
            scaled_input = scaler.transform(input_df)

            # Predict the cluster
            cluster = model.predict(scaled_input)[0]

            # Display the result with interpretation
            if cluster == 1:
                st.markdown(
                    f"<div style='background-color:#d4edda;padding:15px;border-radius:10px;'>"
                    f"<strong style='color:#155724;'>🟢 Customer '{customer_id}' belongs to Cluster 1 - Loyal & High-Value Customers.</strong>"
                    f"</div>",
                    unsafe_allow_html=True
                )
            elif cluster == 0:
                st.markdown(
                    f"<div style='background-color:#fff3cd;padding:15px;border-radius:10px;'>"
                    f"<strong style='color:#856404;'>🟡 Customer '{customer_id}' belongs to Cluster 0 - Regular but Moderate Spenders.</strong>"
                    f"</div>",
                    unsafe_allow_html=True
                )
            elif cluster == 2:
                st.markdown(
                    f"<div style='background-color:#f8d7da;padding:15px;border-radius:10px;'>"
                    f"<strong style='color:#721c24;'>🔴 Customer '{customer_id}' belongs to Cluster 2 - At-Risk or Inactive Customers.</strong>"
                    f"</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"<div style='background-color:#f5c6cb;padding:15px;border-radius:10px;'>"
                    f"<strong style='color:#721c24;'>⚠️ Unknown cluster detected.</strong>"
                    f"</div>",
                    unsafe_allow_html=True
                )
elif nav == "Filter the Customers":
    st.title("🔍 Filter the Customers")
    st.markdown("Use this tool to extract customers based on **Recency**, **Frequency**, or **Monetary** values.")
    with open('my_df.pkl', 'rb') as f:
        df = pickle.load(f)

    # Dropdown for filter basis
    st.markdown("""
        <style>
        /* Force light theme on selectbox */
        div[data-baseweb="select"] > div {
            background-color: white !important;
            color: black !important;
        }

        div[data-baseweb="select"] span {
            color: black !important;
        }

        div[data-baseweb="select"] svg {
            color: black !important;
        }

        /* Dropdown menu options */
        div[data-baseweb="popover"] {
            background-color: white !important;
            color: black !important;
        }

        div[data-baseweb="popover"] div[role="option"] {
            background-color: white !important;
            color: black !important;
        }

        div[data-baseweb="popover"] div[role="option"]:hover {
            background-color: #e6f7ff !important;
            color: black !important;
        }
        </style>
    """, unsafe_allow_html=True)


    filter_basis = st.selectbox("On what basis do you want to filter customers?", ["Recency", "Frequency", "Monetary"])

    # Input for range
    col1, col2 = st.columns(2)
    with col1:
        lower_limit = st.number_input(f"Enter Lower Limit for {filter_basis}", min_value=0.0, value=0.0)
    with col2:
        upper_limit = st.number_input(f"Enter Upper Limit for {filter_basis}", min_value=0.0, value=1000.0)

    # Filter and show results
    if st.button("🔍 Show Customers"):
        filtered_df = df[(df[filter_basis] >= lower_limit) & (df[filter_basis] <= upper_limit)]

        st.markdown("""
            <style>
            /* Fix st.success background and text */
            .stAlert-success {
                background-color: #e6f4ea !important;
                color: black !important;
            }

            /* Fix st.warning background and text */
            .stAlert-warning {
                background-color: #fff4e5 !important;
                color: black !important;
            }

            /* Fix st.info background and text */
            .stAlert-info {
                background-color: #e8f0fe !important;
                color: black !important;
            }

            /* Fix st.error if used anywhere */
            .stAlert-error {
                background-color: #fdecea !important;
                color: black !important;
            }

            /* Optional: Make all alerts light themed with borders */
            .stAlert {
                border: 1px solid #ccc !important;
                border-radius: 6px !important;
            }
            </style>
        """, unsafe_allow_html=True)

        if not filtered_df.empty:
            st.markdown(f"""
                <div style="background-color: #e6f4ea; padding: 10px; border-radius: 5px; border: 1px solid #b6e2c6;">
                    <p style="color: black; font-weight: 500;">
                        ✅ Found {len(filtered_df)} customers between {lower_limit} and {upper_limit} based on {filter_basis}.
                    </p>
                </div>
            """, unsafe_allow_html=True)

            st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)
        else:
            st.markdown("""
                <div style="background-color: #fff4e5; padding: 10px; border-radius: 5px; border: 1px solid #ffd58a;">
                    <p style="color: black; font-weight: 500;">
                        ⚠️ No customers found in the given range.
                    </p>
                </div>
            """, unsafe_allow_html=True)
