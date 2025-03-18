import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

# Load the Excel file
file_path = '241202 - Greenerway Alnabru battericase+eng.xlsx'
monthly_cash_flow_sheet = pd.read_excel(file_path, sheet_name='Månedlig kontantstrøm', header=1)  # Adjust if needed

# Extract relevant columns
months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des']

# Ensure correct indexing for values and convert to float
income = pd.Series(monthly_cash_flow_sheet.iloc[7, 1:13].values).apply(pd.to_numeric, errors='coerce').fillna(0).astype(float)
savings = pd.Series(monthly_cash_flow_sheet.iloc[2, 1:13].values).apply(pd.to_numeric, errors='coerce').fillna(0).astype(float)

# Create a polar plot
theta = np.linspace(0, 2 * np.pi, 12, endpoint=False)  # 12 evenly spaced points

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, income, label='Income', marker='o')
ax.plot(theta, savings, label='Savings', marker='s')

# Fixing label positions
ax.set_xticks(theta)
ax.set_xticklabels(months, fontsize=10, rotation=15)  # Rotate labels slightly

ax.legend()
st.pyplot(fig)

st.title('Market Compatibility')

# Example of market compatibility matrix
markets = ['Peak Shaving', 'Price Arbitrage', 'FFR', 'FCR-D up', 'FCR-N', 'mFRR', 'aFRR', 'Euroflex']
compatibility_matrix = [
    [1, 1, 0, 0, 0, 0, 0, 0],  # Peak Shaving
    [1, 1, 0, 0, 0, 0, 0, 0],  # Price Arbitrage
    [0, 0, 1, 0, 0, 0, 0, 0],  # FFR
    [0, 0, 0, 1, 0, 0, 0, 0],  # FCR-D up
    [0, 0, 0, 0, 1, 0, 0, 0],  # FCR-N
    [0, 0, 0, 0, 0, 1, 0, 0],  # mFRR
    [0, 0, 0, 0, 0, 0, 1, 0],  # aFRR
    [0, 0, 0, 0, 0, 0, 0, 1]   # Euroflex
]

st.write(pd.DataFrame(compatibility_matrix, index=markets, columns=markets))
