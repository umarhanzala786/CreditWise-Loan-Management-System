import streamlit as st
def load_css():

    with open("styles.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


st.set_page_config(
    page_title="CreditWise Loan Management System",
    page_icon="🏦",
    layout="wide"
)
#  Sidebar 
with st.sidebar:

    st.markdown("""
    # 🏦 CreditWise

    ### AI Loan Management

    ---
    """)

    st.success("✔ AI Powered")

    st.info("Version 1.0")

st.markdown("""
<style>

.main-title{
    font-size:50px;
    font-weight:bold;
    color:#4CAF50;
    text-align:center;
}

.sub-title{
    font-size:22px;
    text-align:center;
    color:gray;
}

.card{
    background:#262730;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 10px rgba(255,255,255,.15);
    text-align:center;
}

.metric{
    font-size:35px;
    color:#00E676;
    font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🏦 CreditWise Loan Management System</h1>",unsafe_allow_html=True)

st.markdown("<p class='sub-title'>AI Powered Credit Based Loan Approval System</p>",unsafe_allow_html=True)

st.write("")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.markdown("""
    <div class='card'>
    <div class='metric'>614</div>
    Total Applications
    </div>
    """,unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <div class='metric'>422</div>
    Approved Loans
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <div class='metric'>192</div>
    Rejected Loans
    </div>
    """,unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='card'>
    <div class='metric'>88%</div>
    Accuracy
    </div>
    """,unsafe_allow_html=True)

st.divider()

st.header(" Features")

c1,c2=st.columns(2)

with c1:
    st.success("✔ Loan Prediction")
    st.success("✔ Dashboard")
    st.success("✔ Data Analysis")

with c2:
    st.success("✔ Machine Learning Model")
    st.success("✔ Beautiful UI")
    st.success("✔ Real-Time Prediction")

st.divider()

st.header(" Quick Navigation")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
### 📊 Dashboard

• Analytics

• Charts

• Insights
""")

with c2:
    st.success("""
### 🤖 Prediction

• Loan Prediction

• PDF Report

• History
""")

with c3:
    st.warning("""
### 🛠 Loan Tools

• Search Applicant

• EMI Calculator
""")

c4, c5 = st.columns(2)

with c4:
    st.info("""
### 📈 Data Analysis

• Dataset

• Statistics

• Correlation
""")

with c5:
    st.success("""
### 📉 Model Performance

• Accuracy

• Confusion Matrix

• Metrics
""")

st.divider()

st.header("👨‍💻 Project Information")

left, right = st.columns(2)

with left:

    st.markdown("""
### 📌 Project

CreditWise Loan Management System

Artificial Intelligence based Loan Approval System.
""")

with right:

    st.markdown("""
### ⚙ Technologies

• Python

• Streamlit

• Scikit-Learn

• Pandas

• Plotly

• Joblib
""")

st.info("👈 Select a page from the sidebar.")

st.divider()

st.caption(
"""
© 2026 CreditWise Loan Management System

Developed using ❤️ Python & Streamlit
"""
)
