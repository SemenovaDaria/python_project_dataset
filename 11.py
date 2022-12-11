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

fig1 = plt.figure(figsize=(16,9))
import matplotlib.pyplot as plt
def hermes(name):
    return
def difference(firm):
    hermes(firm)
    close = a[(a.Symbol == firm)]
    l_h = list(close['Close'].values)
    h_first = l_h[0]
    h_last = l_h[-1]
    return (h_last/h_first)

difference('Christian Dior')
difs = [difference('Hermes'), difference('Christian Dior'), difference('Louis Vuitton'), difference('Kering')]
plt.bar(['Hermes', 'Christian Dior', 'Louis Vuitton', 'Kering'], difs, color="hotpink")
st.pyplot(fig1)