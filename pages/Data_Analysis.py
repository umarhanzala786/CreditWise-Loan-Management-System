import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Analysis", layout="wide")


# Load Dataset


df = pd.read_csv("loan_approval_data.csv")

st.title("📈 Data Analysis Dashboard")
st.markdown("### Explore the Loan Dataset")
st.divider()


# Dataset Overview

rows = df.shape[0]
cols = df.shape[1]
missing = df.isnull().sum().sum()
duplicates = df.duplicated().sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", rows)
c2.metric("Columns", cols)
c3.metric("Missing Values", missing)
c4.metric("Duplicates", duplicates)

st.divider()


# Statistical Summary


st.subheader("📊 Statistical Summary")
st.dataframe(df.describe(), use_container_width=True)

st.divider()

# Charts Row 1


col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        df,
        x="Applicant_Income",
        nbins=30,
        title="Applicant Income Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.histogram(
        df,
        x="Credit_Score",
        nbins=30,
        title="Credit Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


# Charts Row 2


col3, col4 = st.columns(2)

with col3:

    fig = px.box(
        df,
        y="Savings",
        title="Savings Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    fig = px.histogram(
        df,
        x="Loan_Amount",
        nbins=30,
        title="Loan Amount Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()


# Categorical Analysis

left, right = st.columns(2)

with left:

    fig = px.bar(
        df["Property_Area"].value_counts().reset_index(),
        x="Property_Area",
        y="count",
        title="Property Area Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.bar(
        df["Education_Level"].value_counts().reset_index(),
        x="Education_Level",
        y="count",
        title="Education Level Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Loan Status


fig = px.pie(
    df,
    names="Loan_Approved",
    hole=0.5,
    title="Loan Approval Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()


# Dataset Preview

st.subheader("📋 Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)

st.divider()

st.caption(
"© 2026 CreditWise Loan Management System | Data Analysis."
)