import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Trader Behaviour vs Market Sentiment Dashboard")

df = pd.read_csv("final_dataset.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Average PnL by Sentiment")
st.write(df.groupby("classification")["Closed PnL"].mean())

st.subheader("PnL Distribution")

fig, ax = plt.subplots()
sns.boxplot(x="classification", y="Closed PnL", data=df, ax=ax)
st.pyplot(fig)

st.subheader("Trading Frequency")

fig2, ax2 = plt.subplots()
sns.barplot(x="classification", y="num_trades", data=df, ax=ax2)
st.pyplot(fig2)

st.subheader("Key Insights")

st.write("""
- Profitability improves during Greed sentiment
- Traders increase trading activity in bullish regimes
- Overtrading risk observed among high-frequency traders
""")