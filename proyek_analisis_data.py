import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Menonaktifkan tampilan peringatan terkait penggunaan st.pyplot() tanpa argumen di Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Membaca data
orders_payments_df = pd.read_csv("https://raw.githubusercontent.com/FrenciliaPA/ProjectDicoding/main/orders_payments2_df.csv")
customers_df = pd.read_csv("https://raw.githubusercontent.com/FrenciliaPA/ProjectDicoding/main/customers2_df.csv")
orders_items_df = pd.read_csv("https://raw.githubusercontent.com/FrenciliaPA/ProjectDicoding/main/orders_items2_df.csv")

# Membuat sidebar dan menambahkan foto 
with st.sidebar:
     st.sidebar.title('Dashboard E-Commerce')
     st.image("https://github.com/FrenciliaPA/ProjectDicoding/raw/871a4b3c528f9af3e9e5387731af782fdc1af76d/E-Commerce.jpg")
     st.sidebar.markdown('''
---
Created by [Frencilia Paulina Agustin](https://github.com/FrenciliaPA).
''')

# Fungsi untuk menghitung tipe pembayaran dan membuat visualisasi
def plot_payment_type(orders_payments_df):
    # Menghitung tipe pembayaran yang dilakukan oleh pelanggan dan mengurutkannya
    tipe_pembayaran = orders_payments_df['payment_type'].value_counts().sort_values(ascending=False)

    # Menemukan tipe pembayaran yang paling umum dilakukan oleh pelanggan
    tipe_pembayaran_umum = tipe_pembayaran.idxmax()

    # Mengatur gaya plot menggunakan Seaborn
    sns.set(style="ticks")

    # Membuat bar chart jumlah pelanggan untuk setiap tipe pembayaran
    plt.figure(figsize=(15, 5))
    sns.barplot(x=tipe_pembayaran.index, 
                y=tipe_pembayaran.values, 
                order=tipe_pembayaran.index,
                palette=["red" if tipe == tipe_pembayaran_umum else "brown" for tipe in tipe_pembayaran.index]
                )

    # Menambahkan judul dan keterangan label sumbu
    plt.title("Tipe Pembayaran Berdasarkan Jumlah Pelanggan ", fontsize=20)
    plt.xlabel("Tipe Pembayaran")
    plt.ylabel("Jumlah Pelanggan")
    plt.xticks(fontsize=13)
    st.pyplot()

    # Menambahkan keterangan
    st.markdown("""
        <p>Berdasarkan bar chart tipe pembayaran berdasarkan jumlah pelanggan di atas, dapat dilihat bahwa tipe pembayaran yang paling banyak digunakan oleh pelanggan adalah credit card dengan jumlah pelanggan pada rentang 70000 sampai 80000, dan tipe pembayaran yang paling sedikit digunakan oleh pelanggan adalah debit card dengan jumlah pelanggan kurang dari 10000.</p>
    """, unsafe_allow_html=True)


# Fungsi untuk menghitung jumlah pelanggan untuk setiap negara dan membuat visualisasi
def plot_top_countries(customers_df):
    # Menghitung jumlah pelanggan untuk setiap negara dan diurutkan
    negara_pelanggan = customers_df['customer_state'].value_counts().sort_values(ascending=False)

    # Mengambil top 5 negara 
    top_5_negara = negara_pelanggan.head(5)

    # Mengatur gaya plot menggunakan Seaborn
    sns.set(style="whitegrid")

    # Membuat bar chart jumlah pelanggan untuk top 5 negara
    plt.figure(figsize=(15, 5))
    sns.barplot(x=top_5_negara.values, 
                y=top_5_negara.index, 
                palette="YlOrBr"  
               )

    plt.title("Top 5 Negara dengan Jumlah Pelanggan Terbanyak", fontsize=20)
    plt.xlabel("Negara")
    plt.ylabel("Jumlah Pelanggan")
    plt.xticks(fontsize=13, rotation=45) 
    plt.yticks(fontsize=13)
    st.pyplot()

    # Menambahkan keterangan
    st.markdown("""
        <p>Berdasarkan bar chart top 5 (lima) negara dengan jumlah pelanggan terbanyak di atas, dapat dilihat bahwa 5 (lima) negara yang paling banyak memiliki jumlah pelanggan adalah SP dengan jumlah pelanggan lebih dari 40000, dilanjutkan RJ dan MG dengan jumlah pelanggan pada rentang 10000 sampai 15000, RS dan PR dengan jumlah pelanggan pada rentang 5000 sampai 10000.</p>
    """, unsafe_allow_html=True)


# Fungsi untuk menghitung harga setiap penjualan produk dan membuat visualisasi
def plot_product_prices(orders_items_df):
    # Menghitung harga setiap penjualan produk
    harga = orders_items_df['price'].value_counts()

    # Membuat histogram
    plt.figure(figsize=(15, 5))
    plt.hist(orders_items_df['price'], bins=range(0, 1000), color='brown', edgecolor='brown')
    plt.title('Harga Berdasarkan Produk yang Dijual', fontsize=20)
    plt.xlabel('Harga')
    plt.ylabel('Produk Penjualan')
    plt.grid(True)
    st.pyplot()

    # Menambahkan keterangan
    st.markdown("""
        <p>Berdasarkan histogram harga berdasarkan produk yang dijual di atas dapat dilihat bahwa rentang harga produk yang paling banyak dijual yaitu 0 sampai 200 dollar.</p>
    """, unsafe_allow_html=True)

# Menampilkan dashboard
st.title('Dashboard Analisis E-Commerce')

# Menambahkan kolom untuk menampilkan visualisasi
plot_payment_type(orders_payments_df)
plot_top_countries(customers_df)
plot_product_prices(orders_items_df)

# Menambah copyright
st.caption('Copyright (c) Frencilia Paulina Agustin')
