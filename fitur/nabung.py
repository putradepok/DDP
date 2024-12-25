import streamlit as st

st.title ("Halaman Menabung")

#Halaman menabung
with st.form ("menabung"):
    nama = st.text_input ("Nama",)
    jumlah = st.number_input ("Jumlah (Rp.)",min_value=0 ) 
    submit_button = st.form_submit_button (label="Simpan")

    if submit_button:
        st.session_state ['Jumlah'].append({
            "Tipe" : "Menabung",
            "Nama" : nama,
            "Jumlah" : jumlah
        })
        st.success ("Anda Berhasil Menabung")
    else:
        st.error ("Anda Belum Menabung")
