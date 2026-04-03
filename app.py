import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

st.title("Anomaly Detection App")

# 1. Load Dataset
data = pd.read_csv("dataset.csv")

# 2. Select Only Numeric Columns
numeric_data = data.select_dtypes(include=['int64', 'float64'])

# 3. Train Isolation Forest Model
model = IsolationForest(contamination=0.1, random_state=42)
data['Anomaly'] = model.fit_predict(numeric_data)

# 4. Convert Model Output
data['Anomaly'] = data['Anomaly'].map({1: 0, -1: 1})

# 5. Display Anomalies
st.write("Detected Anomalies:")
anomalies = data[data['Anomaly'] == 1]
st.dataframe(anomalies)

# 6. Plotting
fig, ax = plt.subplots()
ax.scatter(range(len(data)), numeric_data.iloc[:, 0], c=data['Anomaly'])
ax.set_title("Anomaly Detection")
ax.set_xlabel("Index")
ax.set_ylabel("Value")
st.pyplot(fig)