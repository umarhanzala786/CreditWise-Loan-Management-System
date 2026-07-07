import streamlit as st
import pandas as pd
from datetime import datetime
from pdf_report import generate_pdf
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")



# Load Model

st.title("🏦 Loan Prediction")

st.write("Fill all applicant details below.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    applicant_income = st.number_input("Applicant Income", min_value=0)
    age = st.number_input("Age", min_value=18)
    existing_loans = st.number_input("Existing Loans", min_value=0)
    collateral = st.number_input("Collateral Value", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    education = st.selectbox(
        "Education",
        ["Graduate", "Post Graduate", "High School"]
    )

with col2:
    co_income = st.number_input("Coapplicant Income", min_value=0)
    dependents = st.number_input("Dependents", min_value=0)
    savings = st.number_input("Savings", min_value=0)
    loan_term = st.number_input("Loan Term (Months)", min_value=1)
    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=650
    )

    dti_ratio = st.number_input(
        "DTI Ratio",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.01
    )
    employment = st.selectbox(
        "Employment",
        ["Salaried", "Self-employed", "Unemployed"]
    )

    marital = st.selectbox(
        "Marital Status",
        ["Married", "Single"]
    )

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

purpose = st.selectbox(
    "Loan Purpose",
    ["Home", "Education", "Car", "Personal"]
)

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

employer = st.selectbox(
    "Employer Category",
    ["Government", "MNC", "Private", "Unemployed"]
)

# Feature Engineering


# Squared Features
credit_score_sq = credit_score ** 2
dti_ratio_sq = dti_ratio ** 2

# Employment
employment_salaried = 1 if employment == "Salaried" else 0
employment_self = 1 if employment == "Self-employed" else 0
employment_unemployed = 1 if employment == "Unemployed" else 0

# Marital
marital_single = 1 if marital == "Single" else 0

# Loan Purpose
purpose_car = 1 if purpose == "Car" else 0
purpose_education = 1 if purpose == "Education" else 0
purpose_home = 1 if purpose == "Home" else 0
purpose_personal = 1 if purpose == "Personal" else 0

# Property Area
property_semiurban = 1 if property_area == "Semiurban" else 0
property_urban = 1 if property_area == "Urban" else 0

# Gender
gender_male = 1 if gender == "Male" else 0

# Employer Category
employer_gov = 1 if employer == "Government" else 0
employer_mnc = 1 if employer == "MNC" else 0
employer_private = 1 if employer == "Private" else 0
employer_unemployed = 1 if employer == "Unemployed" else 0

# Education Mapping
education_level = {
    "High School": 0,
    "Graduate": 1,
    "Post Graduate": 2
}[education]

input_data = pd.DataFrame([{

    "Applicant_Income": applicant_income,
    "Coapplicant_Income": co_income,
    "Age": age,
    "Dependents": dependents,
    "Existing_Loans": existing_loans,
    "Savings": savings,
    "Collateral_Value": collateral,
    "Loan_Amount": loan_amount,
    "Loan_Term": loan_term,
    "Education_Level": education_level,

    "Employment_Status_Salaried": employment_salaried,
    "Employment_Status_Self-employed": employment_self,
    "Employment_Status_Unemployed": employment_unemployed,

    "Marital_Status_Single": marital_single,

    "Loan_Purpose_Car": purpose_car,
    "Loan_Purpose_Education": purpose_education,
    "Loan_Purpose_Home": purpose_home,
    "Loan_Purpose_Personal": purpose_personal,

    "Property_Area_Semiurban": property_semiurban,
    "Property_Area_Urban": property_urban,

    "Gender_Male": gender_male,

    "Employer_Category_Government": employer_gov,
    "Employer_Category_MNC": employer_mnc,
    "Employer_Category_Private": employer_private,
    "Employer_Category_Unemployed": employer_unemployed,

    "DTI_Ratio_sq": dti_ratio_sq,
    "Credit_Score_sq": credit_score_sq

}])
st.divider()

if st.button("🔍 Predict Loan"):

    # Scale Input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0][1] * 100

    st.subheader("🎯 Prediction Result")

    if prediction == 1:
        st.markdown("""
        <div style="
        background:#0f5132;
        padding:20px;
        border-radius:15px;
        text-align:center;
        color:white;
        font-size:28px;
        font-weight:bold;
        border:2px solid #00ff88;
        ">
        
        ✅ LOAN APPROVED
        
        </div>
        """, unsafe_allow_html=True)
        st.progress(min(int(probability), 100))
        st.metric(
            label="Approval Probability",
            value=f"{probability:.2f}%"
        )

    else:
        st.markdown("""
        <div style="
        background:#842029;
        padding:20px;
        border-radius:15px;
        text-align:center;
        color:white;
        font-size:28px;
        font-weight:bold;
        border:2px solid red;
        ">
        
        ❌ LOAN REJECTED
        
        </div>
        """, unsafe_allow_html=True)
        st.progress(min(int(100 - probability), 100))
        st.metric(
            label="Approval Probability",
            value=f"{probability:.2f}%"
        )
    # Risk Level
    # Risk Variable
    if probability >= 80:
        risk = "LOW"
        st.success("🟢 Risk Level : LOW")
    
    elif probability >= 50:
        risk = "MEDIUM"
        st.warning("🟡 Risk Level : MEDIUM")
    
    else:
        risk = "HIGH"
        st.error("🔴 Risk Level : HIGH")
        
    if prediction == 1:
        st.success("""
    Applicant satisfies most eligibility criteria.
    
    ✔ Recommended for Loan Approval
    """)
    else:
        st.error("""
    Applicant has higher loan risk.
    
    ✖ Loan Approval Not Recommended
    """)
    st.divider()

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Approval %", f"{probability:.2f}%")
    
    with col2:
        st.metric("Risk", risk)
    
    with col3:
        st.metric("Model", "Logistic Reg")

    # Show Input Data
    with st.expander("View Submitted Details"):
        st.dataframe(input_data)
    
    
    # Download Prediction Report
    
    
    report = pd.DataFrame({
    
        "Applicant Income":[applicant_income],
        "Coapplicant Income":[co_income],
        "Loan Amount":[loan_amount],
        "Credit Score":[credit_score],
        "Prediction":[
            "Approved" if prediction==1 else "Rejected"
        ],
        "Approval Probability":[round(probability,2)]
    
    })
    
    csv = report.to_csv(index=False).encode()
    
    st.download_button(
    
        "📥 Download Prediction Report",
    
        csv,
    
        file_name="Loan_Prediction_Report.csv",
    
        mime="text/csv"
    
    )
    generate_pdf(
        applicant_income,
        loan_amount,
        credit_score,
        prediction,
        probability
    )
    
    with open("Loan_Report.pdf", "rb") as pdf:
    
        st.download_button(
    
            "📄 Download PDF Report",
    
            pdf,
    
            file_name="Loan_Report.pdf",
    
            mime="application/pdf"
    
        )
    
    
    # Prediction History
    
    
    if "history" not in st.session_state:
        st.session_state.history = []
    
    st.session_state.history.append({
    
        "Time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    
        "Prediction":
        "Approved" if prediction==1 else "Rejected",
    
        "Probability":
        round(probability,2)
    
    })
    
    st.divider()
    
    st.subheader("🕒 Prediction History")
    
    history_df = pd.DataFrame(st.session_state.history)
    
    st.dataframe(
        history_df,
        use_container_width=True
    )


st.divider()

st.caption(
"© 2026 CreditWise Loan Management System | Prediction."
)