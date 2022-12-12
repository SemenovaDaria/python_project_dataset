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

sns.boxplot(x="Symbol", y="High", data=a)

months = ['06', '12']
df_hermes = a[a["Symbol"] == "Hermes"][['Date', 'Open']]
df_lv = a[a["Symbol"] == "Louis Vuitton"][['Date', 'Open']]
df_cd = a[a["Symbol"] == "Christian Dior"][['Date', 'Open']]
df_kering = a[a["Symbol"] == "Kering"][['Date', 'Open']]
df_hermes["Date"] = df_hermes.Date.apply(lambda x: x if ((x[-5: -3] in months) and x[-2:] == '01') else np.NaN)
df_hermes.dropna(inplace=True)
df_hermes.rename(columns={'Open': 'Cost'}, inplace=True)
df_hermes.index = np.arange(df_hermes.shape[0])
df_lv["Date"] = df_lv.Date.apply(lambda x: x if ((x[-5: -3] in months) and x[-2:] == '01') else np.NaN)
df_lv.dropna(inplace=True)
df_lv.rename(columns={'Open': 'Cost'}, inplace=True)
df_lv.index = np.arange(df_lv.shape[0])
df_hermes["Date"] = df_hermes.Date.apply(lambda x: x if ((x[-5: -3] in months) and x[-2:] == '01') else np.NaN)
df_hermes.dropna(inplace=True)
df_hermes.rename(columns={'Open': 'Cost'}, inplace=True)
df_hermes.index = np.arange(df_hermes.shape[0])
df_lv["Date"] = df_lv.Date.apply(lambda x: x if ((x[-5: -3] in months) and x[-2:] == '01') else np.NaN)
df_lv.dropna(inplace=True)
df_lv.rename(columns={'Open': 'Cost'}, inplace=True)
df_lv.index = np.arange(df_lv.shape[0])
df_cd["Date"] = df_cd.Date.apply(lambda x: x if ((x[-5: -3] in months) and x[-2:] == '01') else np.NaN)
df_cd.dropna(inplace=True)
df_cd.rename(columns={'Open': 'Cost'}, inplace=True)
df_cd.index = np.arange(df_cd.shape[0])
df_kering["Date"] = df_kering.Date.apply(lambda x: x if ((x[-5: -3] in months) and x[-2:] == '01') else np.NaN)
df_kering.dropna(inplace=True)
df_kering.rename(columns={'Open': 'Cost'}, inplace=True)
df_kering.index = np.arange(df_kering.shape[0])
DF = pd.DataFrame()
DF['Date'] = df_hermes["Date"]
DF['Cost_hermes'] = df_hermes["Cost"]
DF['Cost_lv'] = df_lv["Cost"]
DF['Cost_cd'] = df_cd["Cost"]
DF['Cost_kering'] = df_kering["Cost"]
DF = pd.DataFrame()
DF['Date'] = df_hermes["Date"]
DF['Cost_hermes'] = df_hermes["Cost"]
DF['Cost_lv'] = df_lv["Cost"]
DF['Cost_cd'] = df_cd["Cost"]
DF['Cost_kering'] = df_kering["Cost"]
DF.dropna(inplace=True)
DF
import plotly.express as px
fig5 = plt.figure(figsize=(16,9))
fig = px.line(DF, x='Date', y=DF.columns)
fig.update_xaxes(
    dtick="M6",
    tickformat="%b  %Y",
    ticklabelmode="period")
st.pyplot(fig5)




