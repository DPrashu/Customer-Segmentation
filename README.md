# 🧠 Customer Segmentation using RFM Analysis

**Live App 🔗**: [Streamlit Deployment](https://customer-segmentation-dkyu4q3gfuys72ns5dw6wu.streamlit.app/)

---

## 📝 Problem Statement

In modern retail and e-commerce platforms, **understanding customer behavior** is crucial for driving sales, designing marketing strategies, and building long-term customer relationships. However, raw transactional data is often vast and unstructured, making it difficult to segment customers meaningfully.

To tackle this, we implement **RFM Analysis (Recency, Frequency, Monetary)** — a tried-and-tested customer segmentation model that uses customer purchasing behavior to categorize them into valuable segments like:

- 🟢 Loyal & High-Value Customers
- 🟡 Regular but Moderate Spenders
- 🔴 At-Risk or Inactive Customers

---

## 🎯 Objectives

- Segment customers using RFM values.
- Identify key customer clusters using ML clustering techniques.
- Provide actionable insights for targeting specific customer groups.
- Build an interactive web app using **Streamlit** to test and explore these segments.

---

## 📊 Dataset

The dataset used contains anonymized customer transactions with fields like:

- **Customer ID**
- **Date of Purchase**
- **Total Number of Visits**
- **Amount Spent**

RFM values are computed from these fields and stored in a processed DataFrame (`my_df.pkl`).

---

## 📌 Features of the Web App

### 🔍 1. **RFM Values Page**
- Explains what **Recency**, **Frequency**, and **Monetary** mean.
- Helps users understand how these metrics are calculated from raw data.

### 🧬 2. **Identifiable Clusters Page**
- Visual breakdown of clusters using pie charts and bar plots.
- Shows how customers are grouped and what characteristics each group has.

### 🧠 3. **Find the Cluster Page**
- Takes user input:
  - Customer ID
  - Last Visit Date
  - Total Visits
  - Total Amount Spent
- Calculates RFM values automatically.
- Uses pre-trained clustering model (`model.pkl`) and standard scaler (`Scaler.pkl`) to predict the customer segment.

### 🔎 4. **Filter the Customers Page**
- Lets you filter customers based on a selected metric:
  - Recency
  - Frequency
  - Monetary
- User inputs range values (lower and upper limits).
- Displays all customers that fall within the selected range.

---

## 🛠️ Tech Stack

- **Language**: Python 🐍
- **Libraries**: `pandas`, `numpy`, `scikit-learn`,`pickle`
- **Frontend & Web App**: Streamlit
- **Deployment**: Streamlit Cloud

---
### 🧪 Local Setup (Optional)

```bash
git clone https://github.com/DPrashu/Customer-Segmentation.git
cd Customer-Segmentation
pip install -r requirements.txt
streamlit run streamlit_app.py

