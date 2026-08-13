import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


st.set_page_config(page_title="Dashboard", layout="wide")


# Load Data


df = pd.read_csv("loan_approval_data.csv")

# Remove rows where target is missing
df = df.dropna(subset=["Loan_Approved"])


# Title


st.title("🏦 CreditWise Analytics Dashboard")
st.markdown("### Real-Time Loan Analytics & Insights")
st.divider()


# Sidebar


st.sidebar.header(" Dashboard Filters")

property_filter = st.sidebar.multiselect(
    "Property Area",
    options=sorted(df["Property_Area"].dropna().unique()),
    default=sorted(df["Property_Area"].dropna().unique())
)

education_filter = st.sidebar.multiselect(
    "Education",
    options=sorted(df["Education_Level"].dropna().unique()),
    default=sorted(df["Education_Level"].dropna().unique())
)

filtered_df = df[
    (df["Property_Area"].isin(property_filter)) &
    (df["Education_Level"].isin(education_filter))
]


# KPI Cards


approved = (filtered_df["Loan_Approved"] == "Yes").sum()
rejected = (filtered_df["Loan_Approved"] == "No").sum()

total = len(filtered_df)

approval_rate = (approved / total) * 100 if total > 0 else 0

avg_income = filtered_df["Applicant_Income"].mean()
avg_loan = filtered_df["Loan_Amount"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("📄 Applications", total)
c2.metric("✅ Approved", approved)
c3.metric("❌ Rejected", rejected)
c4.metric("📈 Approval Rate", f"{approval_rate:.1f}%")

c5, c6 = st.columns(2)

c5.metric("💰 Avg Income", f"₹ {avg_income:,.0f}")
c6.metric("🏦 Avg Loan", f"₹ {avg_loan:,.0f}")

st.divider()


# Charts


left, right = st.columns(2)

with left:

    pie = px.pie(
        filtered_df,
        names="Loan_Approved",
        hole=0.55,
        title="Loan Approval Status"
    )

    st.plotly_chart(pie, use_container_width=True)

with right:

    hist = px.histogram(
        filtered_df,
        x="Applicant_Income",
        nbins=30,
        title="Applicant Income Distribution"
    )

    st.plotly_chart(hist, use_container_width=True)

left2, right2 = st.columns(2)

with left2:

    box = px.box(
        filtered_df,
        y="Loan_Amount",
        color="Loan_Approved",
        title="Loan Amount Distribution"
    )

    st.plotly_chart(box, use_container_width=True)

with right2:

    scatter = px.scatter(
        filtered_df,
        x="Applicant_Income",
        y="Loan_Amount",
        color="Loan_Approved",
        hover_data=[
            "Age",
            "Savings",
            "Credit_Score"
        ],
        title="Income vs Loan Amount"
    )

    st.plotly_chart(scatter, use_container_width=True)

st.divider()


# Recent Applications


st.subheader("📋 Recent Loan Applications")

show_cols = [
    "Applicant_ID",
    "Applicant_Income",
    "Loan_Amount",
    "Credit_Score",
    "Property_Area",
    "Loan_Approved"
]

st.dataframe(
    filtered_df[show_cols].tail(10),
    use_container_width=True
)
st.subheader("Loan Approval by Education")

education_map = {
    0: "High School",
    1: "Graduate",
    2: "Post Graduate"
}

edu_df = df.copy()
edu_df["Education"] = edu_df["Education_Level"].map(education_map)

fig = px.histogram(
    filtered_df,
    x="Education_Level",
    color="Loan_Approved",
    barmode="group",
    title="Loan Approval by Education"
)

st.plotly_chart(fig, use_container_width=True)
fig.update_layout(
    xaxis_title="Education",
    yaxis_title="Number of Applicants"
)
chart_df = filtered_df.copy()

chart_df["Loan_Approved"] = chart_df["Loan_Approved"].map({
    0: "Rejected",
    1: "Approved"
})



st.subheader("Loan Approval by Employment")

emp_df = filtered_df.copy()

fig = px.histogram(
    emp_df,
    x="Employment_Status",
    color="Loan_Approved",
    barmode="group",
    title="Loan Approval by Employment",
    color_discrete_map={
        "Yes": "#22c55e",
        "No": "#ef4444"
    }
)

fig.update_layout(
    xaxis_title="Employment Status",
    yaxis_title="Applicants",
    legend_title="Loan Status",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)


st.subheader("Loan Approval by Property Area")

property_df = filtered_df.copy()

fig = px.histogram(
    property_df,
    x="Property_Area",
    color="Loan_Approved",
    barmode="group",
    title="Loan Approval by Property Area",
    color_discrete_map={
        "Yes": "#22c55e",
        "No": "#ef4444"
    }
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Property Area",
    yaxis_title="Applicants",
    legend_title="Loan Status"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Savings Distribution")

fig = px.histogram(
    filtered_df,
    x="Savings",
    nbins=30,
    title="Savings Distribution"
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Savings",
    yaxis_title="Applicants"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Correlation Heatmap")



numeric_df = filtered_df.select_dtypes(include="number")

corr = numeric_df.corr().round(2)

fig = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.index),
    colorscale="Viridis",
    showscale=True
)

fig.update_layout(
    template="plotly_dark",
    title="Correlation Heatmap",
    height=700,
    margin=dict(l=120, r=80, t=80, b=120),

    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

st.plotly_chart(fig, use_container_width=True)
fig.update_xaxes(
    tickangle=-35,
    tickfont=dict(size=10)
)

fig.update_yaxes(
    tickfont=dict(size=10)
)

st.divider()

st.subheader("Dashboard Insights")

approval_rate = (
    (filtered_df["Loan_Approved"] == "Yes").mean() * 100
)

avg_credit = filtered_df["Credit_Score"].mean()

avg_income = filtered_df["Applicant_Income"].mean()

avg_loan = filtered_df["Loan_Amount"].mean()

col1, col2 = st.columns(2)

with col1:

    if approval_rate >= 70:
        st.success(f"✅ High approval rate ({approval_rate:.1f}%).")
    elif approval_rate >= 50:
        st.warning(f"⚠ Moderate approval rate ({approval_rate:.1f}%).")
    else:
        st.error(f"❌ Low approval rate ({approval_rate:.1f}%).")

    st.info(f"💳 Average Credit Score : {avg_credit:.0f}")

with col2:

    st.info(f"Average Applicant Income : ₹ {avg_income:,.0f}")

    st.info(f"Average Loan Amount : ₹ {avg_loan:,.0f}")

st.subheader("Key Observations")

st.success(
    "✔ Applicants with higher Credit Score have better approval chances."
)

st.success(
    "✔ Salaried applicants dominate the loan applications."
)

st.success(
    "✔ Graduate applicants apply more frequently than non-graduates."
)

st.success(
    "✔ Semiurban and Urban areas contribute most loan applications."
)

st.divider()

st.caption(
"© 2026 CreditWise Loan Management System | Dashboard."
)
