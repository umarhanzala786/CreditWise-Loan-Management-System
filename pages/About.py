import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")

st.title("ℹ️ About CreditWise")

st.markdown("""
### 🏦 CreditWise Loan Management System

CreditWise is an AI-powered Loan Approval System developed using Machine Learning.
It predicts whether a loan application should be approved or rejected based on applicant information.
""")

st.divider()

col1 = st.columns(1)


with col1:

    st.subheader("🤖 Machine Learning Model")

    st.success("""
Model : Logistic Regression

Accuracy : 88%

Precision : 78%

Recall : 83%

F1 Score : 80%
""")

st.divider()

st.subheader("🛠 Technology Stack")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
🐍 Python

📊 Pandas

🔢 NumPy
""")

with c2:
    st.success("""
🤖 Scikit-learn

📈 Plotly

💾 Joblib
""")

with c3:
    st.success("""
🌐 Streamlit

📄 ReportLab

📁 CSV
""")

st.divider()

st.subheader("⚙️ Project Workflow")

st.markdown("""
1️⃣ Load Dataset

⬇️

2️⃣ Data Preprocessing

⬇️

3️⃣ Feature Engineering

⬇️

4️⃣ Logistic Regression Model

⬇️

5️⃣ Loan Prediction

⬇️

6️⃣ Risk Analysis

⬇️

7️⃣ CSV / PDF Report Generation
""")

st.divider()

st.subheader("✨ Features")

st.success("✔ Loan Prediction")

st.success("✔ Interactive Dashboard")

st.success("✔ Data Analysis")

st.success("✔ Risk Level Detection")

st.success("✔ Recommendation System")

st.success("✔ CSV Report Download")

st.success("✔ PDF Report Download")

st.success("✔ Prediction History")

st.divider()

st.caption(
    "© 2026 CreditWise Loan Management System."
)
