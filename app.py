import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl

file_path = '241202 - Greenerway Alnabru battericase+eng.xlsx'
monthly_cash_flow_sheet = pd.read_excel(file_path, sheet_name='Månedlig kontantstrøm', header=1)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Des']

income = pd.Series(monthly_cash_flow_sheet.iloc[7, 1:13].values).apply(pd.to_numeric, errors='coerce').fillna(0).astype(float)
savings = pd.Series(monthly_cash_flow_sheet.iloc[2, 1:13].values).apply(pd.to_numeric, errors='coerce').fillna(0).astype(float)

theta = np.linspace(0, 2 * np.pi, 12, endpoint=False)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, income, label='Monthly Income', marker='o')
ax.plot(theta, savings, label='Monthly Savings', marker='s')

ax.set_xticks(theta)
ax.set_xticklabels(months, fontsize=10, rotation=15)

ax.set_title('Annual Income and Savings Overview', va='bottom')
ax.legend()
ax.legend()
st.pyplot(fig)

st.title('Market Compatibility Analysis')

markets = ['Peak Shaving', 'Price Arbitrage', 'Fast Frequencies (FFR)', 'FCR-D Up', 'FCR-N', 'mFRR', 'aFRR', 'Euroflex']
compatibility_matrix = [
    [1, 1, 0, 0, 0, 0, 0, 0],  # Peak Shaving
    [1, 1, 0, 0, 0, 0, 0, 0],  # Price Arbitrage
    [0, 0, 1, 0, 0, 0, 0, 0],  # FFR
    [0, 0, 0, 1, 0, 0, 0, 0],  # FCR-D Up
    [0, 0, 0, 0, 1, 0, 0, 0],  # FCR-N
    [0, 0, 0, 0, 0, 1, 0, 0],  # mFRR
    [0, 0, 0, 0, 0, 0, 1, 0],  # aFRR
    [0, 0, 0, 0, 0, 0, 0, 1]   # Euroflex
]
st.write("The following matrix shows the compatibility of different markets. A value of '1' indicates that the markets can operate simultaneously, while '0' indicates that they must be isolated.")
st.write(pd.DataFrame(compatibility_matrix, index=markets, columns=markets))