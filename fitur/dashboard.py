import streamlit as st

st.title ("Halaman dashboard")

#Fungsi untuk Menghitung dan menyimpang total nabung 
def total():
    total_nabung = sum (t['Jumlah'] for t in st.session_state ['Jumlah'] if t ['Tipe'] == 'Menabung')

    return f"Total Nabung Anda {total_nabung}"

st.write(total())