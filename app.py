import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

# =================================================
# Page Configuration (FIRST Streamlit command)
# =================================================
st.set_page_config(
    page_title="Pharmacy Drug Safety Alert",
    page_icon="💊",
    layout="centered"
)

# =================================================
# Global Styling (SAFE & WORKING)
# =================================================
st.markdown("""
<style>

/* Full app background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e8f1fd, #ffffff);
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
}

/* Text colors */
h1, h2, h3, h4, h5 {
    color: #0f3c63 !important;
}
p, span, label {
    color: #1f2937 !important;
}

/* Button styling */
.stButton > button {
    background-color: #1976d2 !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 0.6em 1.6em !important;
    font-size: 16px !important;
}
.stButton > button:hover {
    background-color: #0d47a1 !important;
}

/* Input fields */
input, textarea {
    border-radius: 8px !important;
}

</style>
""", unsafe_allow_html=True)

# =================================================
# Load Dataset
# =================================================
df = pd.read_csv("drug_data.dataset.csv")



X = df.drop("safety_label", axis=1)
y = df["safety_label"]

model = LogisticRegression()
model.fit(X, y)

# =================================================
# Title Section (Card Style)
# =================================================
# =================================================
# Title Section (Pink Gradient Text Style)
# =================================================
# =================================================
# Header Section (Exact Pink Gradient Text Style)
# =================================================
st.markdown("""
<div style="
text-align:center;
margin-top:20px;
margin-bottom:30px;
">

<h1 style="
font-size:48px;
font-weight:900;
background: linear-gradient(90deg, #f97316, #ec4899);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
margin-bottom:10px;
">
💊 Pharmacy Drug Safety Alert<br>System
</h1>

</div>
""", unsafe_allow_html=True)


st.divider()

# =================================================
# Input Form Section
# =================================================
st.markdown("""
<div style="
background-color:white;
padding:20px;
border-radius:12px;
box-shadow:0 2px 8px rgba(0,0,0,0.08);
">
<h3>📝 Enter Patient & Drug Details</h3>
</div>
""", unsafe_allow_html=True)

with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        dosage = st.number_input("💉 Drug Dosage (mg)", 50, 500, 100, 10)
        age = st.number_input("👤 Patient Age", 18, 80, 30)

    with col2:
        severity = st.selectbox("⚠️ Reaction Severity", [1, 2, 3, 4, 5])
        interactions = st.number_input("🔗 Drug Interactions", 0, 5, 1)

    previous = st.radio(
        "📋 Previous Safety Alert",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    submit = st.form_submit_button("🔍 Predict Drug Safety")

# =================================================
# Prediction Output
# =================================================
if severity >= 3 or interactions >= 2 or previous == 1:
    st.markdown("""
    <div style="
    background-color:#fdecea;
    padding:20px;
    border-left:6px solid #e53935;
    border-radius:10px;
    ">
    <h4>⚠️ HIGH RISK ALERT</h4>
    <p>This drug may cause safety issues. Review carefully.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="
    background-color:#e8f5e9;
    padding:20px;
    border-left:6px solid #43a047;
    border-radius:10px;
    ">
    <h4>✅ SAFE DRUG</h4>
    <p>No safety alert detected for this prescription.</p>
    </div>
    """, unsafe_allow_html=True)


# =================================================
# Dataset Preview
# =================================================
st.divider()
st.subheader("📂 Dataset Preview")

if st.checkbox("Show sample data"):
    st.dataframe(df.head())

# =================================================
# Footer
# =================================================
st.markdown("""
<hr>
<center>
<small>Pharmacy Drug Safety Alert System | Mini Project</small>
</center>
""", unsafe_allow_html=True)
