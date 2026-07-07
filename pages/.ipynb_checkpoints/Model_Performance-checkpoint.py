import streamlit as st

st.set_page_config(page_title="Model Performance", layout="wide")

st.title("📈 Model Performance")

st.markdown("### Logistic Regression Performance")


c1,c2,c3,c4 = st.columns(4)

c1.metric("Accuracy","88%")
c2.metric("Precision","78.46%")
c3.metric("Recall","83.60%")
c4.metric("F1 Score","80.95%")


import plotly.express as px
import pandas as pd

cm = pd.DataFrame(
    [[125,14],
     [10,51]],

    index=["Actual No","Actual Yes"],
    columns=["Pred No","Pred Yes"]
)

fig = px.imshow(
    cm,
    text_auto=True,
    color_continuous_scale="Blues",
    title="Confusion Matrix"
)

st.plotly_chart(fig,use_container_width=True)


report = pd.DataFrame({

    "Metric":[
        "Precision",
        "Recall",
        "F1 Score",
        "Accuracy"
    ],

    "Value":[
        0.7846,
        0.8360,
        0.8095,
        0.88
    ]

})

st.dataframe(report,use_container_width=True)


st.info("""
Model Used : Logistic Regression

Scaler : StandardScaler

Dataset : Loan Approval Dataset

Training Accuracy : 88%
""")


st.divider()

st.caption(
    "© 2026 CreditWise Loan Management System | Model Performance"
)