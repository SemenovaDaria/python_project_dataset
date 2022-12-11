import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

a = pd.read_csv("fashion.csv")
st.title('Mid-term report')


fig = plt.figure(dpi=150, figsize=(16,9))
sns.pairplot(a[["Symbol", "Close", "Open"]],
             hue='Symbol',
             plot_kws=dict(marker="o", linewidth=1, alpha=0.5),
             height=5)
st.pyplot(fig)