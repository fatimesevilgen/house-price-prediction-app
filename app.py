import streamlit as st
from predict import predict

st.title("🏠 Ev Fiyat Tahmini")

st.markdown("""Aşağıya evinizin özelliklerini girin, ardından “Tahmin Et” butonuna basın.""")

CRIM    = st.number_input("CRIM (Suç oranı)", min_value=0.0, format="%.5f")
ZN      = st.number_input("ZN (İmar arsası yüzdesi)", min_value=0.0, format="%.2f")
INDUS   = st.number_input("INDUS (Sanayi oranı)", min_value=0.0, format="%.2f")
CHAS    = st.selectbox("CHAS (Charles Nehri kenarı mı?)", [0, 1])
NOX     = st.number_input("NOX (Hava kirliliği düzeyi)", min_value=0.0, format="%.3f")
RM      = st.number_input("RM (Oda sayısı ortalaması)", min_value=0.0, format="%.3f")
AGE     = st.number_input("AGE (Eski konut oranı)", min_value=0.0, format="%.3f")
DIS     = st.number_input("DIS (İş merkezlerine uzaklık)", min_value=0.0, format="%.3f")
RAD     = st.number_input("RAD (Karayoluna erişim indeksi)", min_value=0, step=1)
TAX     = st.number_input("TAX (Vergi oranı)", min_value=0, step=1)
PTRATIO = st.number_input("PTRATIO (Öğrenci-öğretmen oranı)", min_value=0.0, format="%.2f")
B       = st.number_input("B (Nüfus (%1000-x²) ağırlığı)", min_value=0.0, format="%.2f")
LSTAT   = st.number_input("LSTAT (Düşük gelirli %)", min_value=0.0, format="%.2f")

if st.button("🔮 Tahmin Et"):
    price = predict(**{
        "CRIM": CRIM, "ZN": ZN, "INDUS": INDUS, "CHAS": CHAS,
        "NOX": NOX, "RM": RM, "AGE": AGE, "DIS": DIS,
        "RAD": RAD, "TAX": TAX, "PTRATIO": PTRATIO,
        "B": B, "LSTAT": LSTAT
    })
    st.success(f"🏷️ Öngörülen Ev Fiyatı: {price:.5f} $")  # veya ₺ cinsine uyarlayın
