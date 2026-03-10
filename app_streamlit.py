import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
	page_title = "Klasifikasi data Maskapai",
	page_icon = ":rocket:",
	layout = "wide"
)

model = joblib.load("maskapai.joblib")

st.title(":rocket: Klasifikasi Maskapai Penerbangan")
st.markdown("aplikasi untuk memprediksi ketepatan waktu pesawat")

maskapai = st.selectbox("Maskapai", ["Garuda","Lion Air","AirAsia","Citilink","Batik Air","Qatar Airways","Emirates","Scoot","Singapore Airlines","Japan Airlines","Turkish Airlines"]) 	
asal = st.selectbox("Asal", ["Jakarta","Surabaya","Denpasar","Medan","Makasar"])
tujuan = st.selectbox("Tujuan", ["Jakarta","Kuala Lumpur","Tokyo","Singapore","Sydney","Singapura","Denpasar","Bali","Doha","Dubai","Makassar","Bangkok","Seoul","Surabaya","Hong Kong","London","Batam","Perth","Yogyakarta","Jeddah","Taipei","Balikpapan","Melbourne","Padang","Manila","Ho Chi Minh","Palembang","Solo","Amsterdam","Paris","Semarang","Istanbul","Lombok","Pontianak","Medan","Johor Bahru","Milan","Osaka","Antalya"])	
durasi = st.slider("Durasi", 0.0, 15.0, 8.0)	
kapasitas_kursi	= st.slider("Kapasitas Kursi", 180, 350, 200)
pax = st.slider("Pax", 0, 348, 100)

if st.button("prediksi", type="primary"):
	data_baru = pd.DataFrame([[maskapai, asal,tujuan,durasi,kapasitas_kursi,pax]], columns=["Maskapai", "Asal","Tujuan","Durasi","Kapasitas_Kursi","Pax"])
	prediksi = model.predict(data_baru)[0]
	presentase = max(model.predict_proba(data_baru)[0])
	st.success(f"model memprediksi **{prediksi}** dengan tingkat keyakinan {presentase*100:.2f}%")
	st.balloons()

st.divider()

st.caption("dibuat oleh **AVIATION**")
