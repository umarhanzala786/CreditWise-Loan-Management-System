import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(
    page_title="Feature Importance",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Feature Importance")
st.write("Understand which features influence loan approval the most.")
st.divider()

# Load Model


model = joblib.load("model.pkl")


# Feature Names

feature_names = [
    'Applicant_Income',
    'Coapplicant_Income',
    'Age',
    'Dependents',
    'Existing_Loans',
    'Savings',
    'Collateral_Value',
    'Loan_Amount',
    'Loan_Term',
    'Education_Level',
    'Employment_Status_Salaried',
    'Employment_Status_Self-employed',
    'Employment_Status_Unemployed',
    'Marital_Status_Single',
    'Loan_Purpose_Car',
    'Loan_Purpose_Education',
    'Loan_Purpose_Home',
    'Loan_Purpose_Personal',
    'Property_Area_Semiurban',
    'Property_Area_Urban',
    'Gender_Male',
    'Employer_Category_Government',
    'Employer_Category_MNC',
    'Employer_Category_Private',
    'Employer_Category_Unemployed',
    'DTI_Ratio_sq',
    'Credit_Score_sq'
]

# Feature Importance

importance = abs(model.coef_[0])

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)


# Top Metrics

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Features",
    len(feature_names)
)

c2.metric(
    "Most Important",
    importance_df.iloc[0]["Feature"]
)

c3.metric(
    "Importance Score",
    round(
        importance_df.iloc[0]["Importance"],
        3
    )
)

st.divider()

# Bar Chart

fig = px.bar(
    importance_df.head(10),
    x="Importance",
    y="Feature",
    orientation="h",
    color="Importance",
    color_continuous_scale="Viridis",
    title="Top 10 Important Features"
)

fig.update_layout(
    template="plotly_dark",
    yaxis=dict(categoryorder="total ascending"),
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# Complete Table


st.subheader("📋 All Feature Importance Scores")

st.dataframe(
    importance_df,
    use_container_width=True
)

st.divider()


# Insights


st.subheader("🧠 Model Insights")

top5 = importance_df.head(5)

for feature in top5["Feature"]:
    st.success(f"✔ {feature} has a strong influence on loan approval.")

st.info("""
Higher importance means the model relies more on that feature while making predictions.
""")