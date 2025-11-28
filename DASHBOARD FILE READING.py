import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# App title
st.title("VGU Streamlit Dashboard")
st.text("Welcome to our interactive dashboard!")
st.header("This is a header")
st.write("Example calculation: 10 + 5 =", 10 + 5)

# ----------------- User Inputs -----------------
st.subheader("User Information")

# Naam input
name = st.text_input("Apna naam likho:")
# Age input
age = st.number_input("Apni age likho:", min_value=0, max_value=120, step=1)
# Course selection
course = st.selectbox("Apna course select karo:", ["BCA", "BTECH", "MCA"])

st.write("Aapka naam:", name)
st.write("Aapki age:", age)
st.write("Aapka course:", course)

# Button
if st.button("Click Me"):
    st.success("Button clicked successfully!")

# ----------------- File Upload -----------------
st.subheader("CSV File Upload")
file = st.file_uploader("Apni CSV file upload karo", type=["csv"])
if file is not None:
    df_uploaded = pd.read_csv(file)
    st.success("File uploaded successfully!")
    st.dataframe(df_uploaded)

# ----------------- Sample DataFrame -----------------
st.subheader("Sample DataFrame Example")
data = {"Name": ["Tom", "Jack", "Ravi"], "Marks": [10, 20, 10]}
df = pd.DataFrame(data)
st.dataframe(df)

# ----------------- Charts -----------------
st.subheader("Charts Example")

chart_data = pd.DataFrame({"Marks": [10, 20, 10]}, index=["Tom", "Jack", "Ravi"])
st.line_chart(chart_data)
st.bar_chart(chart_data)

# ----------------- Pie Chart -----------------
st.subheader("Pie Chart Example")
subjects = ["Python", "C++", "Java"]
marks = [10, 20, 10]

fig, ax = plt.subplots()
ax.pie(marks, labels=subjects, autopct="%1.1f%%")
st.pyplot(fig)

# ----------------- Extra Section -----------------
st.subheader("Statistics of Sample Data")
st.write("Mean marks:", np.mean(df["Marks"]))
st.write("Total marks:", np.sum(df["Marks"]))
st.write("Max marks:", np.max(df["Marks"]))
