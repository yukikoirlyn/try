import imp
import streamlit as st
import lorem
from numerize import numerize
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout="wide")

st.write("Hello World!")

"Ini hello world, tapi pake magic"

st.markdown("Nama saya **Yukiko**")
st.markdown("---")

st.title("Ini Judul")
st.subheader("Ini subheader")
st.write(lorem.paragraph())

st.code("import stramlit as st")


# deklarasi dataset
df = pd.read_csv("store.csv")

# data prep
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# end of data prep

st.dataframe(df)

# metrics
st.metric("Total Saless", 1000, 10)

st.metric("Total Profit", "$ 10M", "-2.3%")

st.title("Charting")

# sidebar
with st.sidebar:
    st.title("Dashboard Store")

# line chart (sales)
sales = df[['Order Date', 'Sales']].set_index('Order Date').resample('W').sum()

cap1, cht1 = st.columns([1, 4])
with cap1:
    st.write(lorem.paragraph())
with cht1:
    st.line_chart(sales)
#st.line_chart(
#    sales
#)

# metrics
met1, met2, met3 = st.columns(3)
with met1:
    st.metric("Total Sales", "$ "+ numerize.numerize(df['Sales'].sum()))
with met2:
    st.metric("Total Order", df['Order ID'].nunique())
with met3:
    st.metric("Number of Customers", df['Customer ID'].nunique())

# line chart (sales)
freq = st.selectbox("Masukkan frekuensi", ('D', 'W', 'M', 'Q', 'Y'))
sales = df[['Order Date', 'Sales']].set_index('Order Date').resample(freq).sum()

cap1, cht1 = st.columns([1, 4])
with cap1:
    st.dataframe(sales)
with cht1:
    st.line_chart(sales)

fig1, ax1 = plt.subplots(figsize=(10,10))
sns.scatterplot(
    data = df,
    x='Sales',
    y='Profit',
    ax=ax1
)
st.pyplot(fig1)

# input
st.title("Input")
tombol1 = st.button("Tekan tombol yuk")
st.write(tombol1)

jurusan = st.selectbox(
    "Pilih jurusan kamu",
    ('Matematika', 'Fisika', 'Kimia')
)
st.write("Kamu memilih jurusan", jurusan)

setuju = st.checkbox("Centang untuk setuju")
if setuju:
    st.write("Anda sudah setuju")
else:
    st.write("Anda belum setuju")

nama = st.text_input("Masukan nama kamu")
st.write("Hello", nama)

# Image
image = Image.open('quiz_2.png')
st.image(image, caption = "Ini gambar")

# penggunaan kolom
st.title("kolom")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(lorem.paragraph())

with col2:
    st.write(lorem.paragraph())

with col3:
    st.write(lorem.paragraph())
