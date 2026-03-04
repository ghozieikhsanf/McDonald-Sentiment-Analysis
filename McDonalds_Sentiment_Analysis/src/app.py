import streamlit as st
import eda
import predict

navigation = st.sidebar.selectbox('Pilih Halaman:',('EDA','Review'))

if navigation == 'EDA':
    eda.run()
elif navigation == 'Review':
    predict.run()