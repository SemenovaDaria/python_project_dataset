import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

a = pd.read_csv("fashion.csv")
st.title('Mid-term report')

a['Symbol'] = a['Symbol'].apply(lambda name: name.replace("CDI.PA", "Christian Dior"))
a.head(6)
a['Symbol'] = a['Symbol'].apply(lambda name: name.replace("RMS.PA", "Hermes"))
a.head(6)
a['Symbol'] = a['Symbol'].apply(lambda name: name.replace("MC.PA", "Louis Vuitton"))
a.head(6)
a['Symbol'] = a['Symbol'].apply(lambda name: name.replace("KER.PA", "Kering"))
a.head(6)
a["purchase price"] = (a["High"] - a["Open"])
a["sale price"] = (a["Close"] - a["Low"])
a["estimated income"] = (a["Close"] - a["Open"])
a["profit"] = a["estimated income"].apply(lambda x: True if x > 0 else False)
del a["sale price"]
del a["purchase price"]

fig = plt.figure(dpi=150, figsize=(16,9))
sns.pairplot(a[["Symbol", "Close", "Open"]],
             hue='Symbol',
             plot_kws=dict(marker="o", linewidth=1, alpha=0.5),
             height=5)
st.pyplot(fig)


fig2 = plt.figure(figsize=(16,9))

ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)

ax_1.hist(a[a["Symbol"] == "Louis Vuitton"]["Volume"], color="maroon", label="Louis Vuitton")
ax_2.hist(a[a["Symbol"] == "Kering"]["Volume"], color="crimson", label="Kering")
ax_3.hist(a[a["Symbol"] == "Hermes"]["Volume"], color="pink", label="Hermes")
ax_4.hist(a[a["Symbol"] == "Christian Dior"]["Volume"], color="salmon", label="Christian Dior")

ax_1.set_ylabel("Price", fontsize=12)
ax_2.set_ylabel("Price", fontsize=12)
ax_3.set_ylabel("Price", fontsize=12)
ax_4.set_ylabel("Price", fontsize=12)

ax_1.set_xlabel("items sold")
ax_2.set_xlabel("items sold")
ax_3.set_xlabel("items sold")
ax_4.set_xlabel("items sold")

ax_1.set_title("Volume of trade of Louis Vuitton")
ax_2.set_title("Volume of trade of Kering")
ax_3.set_title("Volume of trade of Hermes")
ax_4.set_title("Volume of trade of Christian Dior")

ax_1.grid()
ax_2.grid()
ax_3.grid()
ax_4.grid()

st.pyplot(fig2)

