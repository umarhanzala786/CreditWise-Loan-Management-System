import streamlit as st
import pandas as pd
import math

# ----------------------------------------
# Page Config
# ----------------------------------------

st.set_page_config(
    page_title="Loan Tools",
    page_icon="🛠",
    layout="wide"
)

st.title("🛠 Loan Tools")
st.write("Search Applicant Details and Calculate Loan EMI")
st.divider()

# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv("loan_approval_data.csv")

# ========================================
# SECTION 1 : SEARCH APPLICANT
# ========================================

st.subheader("🔍 Search Applicant")

search_id = st.number_input(
    "Enter Applicant ID",
    min_value=1,
    step=1
)

if st.button("🔎 Search Applicant"):

    result = df[df["Applicant_ID"] == search_id]

    if not result.empty:

        row = result.iloc[0]

        st.success("✅ Applicant Found")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Income",
                f"₹ {row['Applicant_Income']:,}"
            )

        with col2:
            st.metric(
                "Credit Score",
                row["Credit_Score"]
            )

        with col3:
            st.metric(
                "Loan Amount",
                f"₹ {row['Loan_Amount']:,}"
            )

        with col4:
            st.metric(
                "Status",
                row["Loan_Approved"]
            )

        with st.expander("📄 View Complete Applicant Details"):

            st.dataframe(
                result,
                use_container_width=True
            )

        csv = result.to_csv(index=False).encode()

        st.download_button(
            "⬇ Download Applicant Details",
            csv,
            file_name=f"Applicant_{search_id}.csv",
            mime="text/csv"
        )

    else:

        st.error("❌ Applicant Not Found")

st.divider()

# ========================================
# SECTION 2 : EMI CALCULATOR
# ========================================

st.subheader("💰 EMI Calculator")

left, right = st.columns(2)

with left:

    loan_amount = st.number_input(
        "Loan Amount (₹)",
        min_value=1000,
        value=500000,
        step=1000
    )

    interest = st.number_input(
        "Interest Rate (%)",
        min_value=1.0,
        value=8.5,
        step=0.1
    )

with right:

    years = st.number_input(
        "Loan Tenure (Years)",
        min_value=1,
        value=20
    )

if st.button("💳 Calculate EMI"):

    monthly_rate = interest / (12 * 100)

    months = years * 12

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
    ) / (
        (1 + monthly_rate) ** months - 1
    )

    total_payment = emi * months

    total_interest = total_payment - loan_amount

    st.success("✅ EMI Calculated Successfully")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Monthly EMI",
            f"₹ {emi:,.2f}"
        )

    with c2:

        st.metric(
            "Total Interest",
            f"₹ {total_interest:,.2f}"
        )

    with c3:

        st.metric(
            "Total Payment",
            f"₹ {total_payment:,.2f}"
        )

    st.progress(100)

st.divider()

# ========================================
# LOAN TIPS
# ========================================

st.subheader("💡 Loan Tips")

col1, col2 = st.columns(2)

with col1:

    st.success(
        "✔ Maintain a good Credit Score."
    )

    st.success(
        "✔ Keep Existing Loans Low."
    )

    st.success(
        "✔ Increase Savings before applying."
    )

with col2:

    st.info(
        "✔ Stable Income improves approval."
    )

    st.info(
        "✔ Lower DTI Ratio increases eligibility."
    )

    st.info(
        "✔ Choose a suitable Loan Tenure."
    )

st.divider()

st.caption(
    "© 2026 CreditWise Loan Management System | Loan Tools"
)