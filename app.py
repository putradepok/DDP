import streamlit as st

# Side bar directory
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
Nabung = st.Page("./fitur/nabung.py", title="nabung")
Penarikan = st.Page("./fitur/penarikan.py", title="penarikan")
pg = st.navigation (
    {
        "dashboard":[dashboard],
        "nabung":[Nabung,Penarikan]
    }
)

if  'Jumlah' not in st.session_state:
    st.session_state['Jumlah'] = []


#Menjalankan Navigasi
pg.run()


