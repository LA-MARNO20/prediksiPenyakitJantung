import pickle
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Penyakit Jantung",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load model
penyakit_jantung = pickle.load(open('penyakitjantung.sav', 'rb'))

# Styling halaman
st.markdown(
    """
    <style>
        .title {
            font-size: 24px;
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }
        .footer {
            font-size: 12px;
            text-align: center;
            color: gray;
            margin-top: 20px;
        }
        .container {
            background: linear-gradient(to bottom, #ffffff, #e0f7fa);
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            margin-top: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 5px;
            height: 40px;
            margin-top: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Footer dengan nama
st.markdown(
    """
    <div class="footer">
        Dibuat oleh <b>La Marno</b>
    </div>
    """,
    unsafe_allow_html=True
)

# Judul web
st.markdown('<div class="title">Data Mining Prediksi Penyakit Jantung</div>', unsafe_allow_html=True)

st.markdown('<div class="container">', unsafe_allow_html=True)

# Input nilai
col1, col2 = st.columns(2)

with col1:
    age = st.text_input('Input nilai age', '0')
    sex = st.text_input('Input nilai sex', '0')
    cp = st.text_input('Input nilai cp', '0')
    trestbps = st.text_input('Input nilai trestbps', '0')
    chol = st.text_input('Input nilai chol', '0')
    fbs = st.text_input('Input nilai fbs', '0')

with col2:
    restecg = st.text_input('Input nilai restecg', '0')
    thalach = st.text_input('Input nilai thalach', '0')
    exang = st.text_input('Input nilai exang', '0')
    oldpeak = st.text_input('Input nilai oldpeak', '0')
    slope = st.text_input('Input nilai slope', '0')
    ca = st.text_input('Input nilai ca', '0')
    thal = st.text_input('Input nilai thal', '0')

# Prediksi
diab_diagnosis = ''

if st.button('Test Prediksi Penyakit Jantung'):
    try:
        diab_prediction = penyakit_jantung.predict([[int(age), int(sex), int(cp), float(trestbps), float(chol),
                                                     int(fbs), int(restecg), float(thalach), int(exang),
                                                     float(oldpeak), int(slope), int(ca), int(thal)]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'Pasien Terkena Penyakit Jantung'
        else:
            diab_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
        st.success(diab_diagnosis)
    except ValueError:
        st.error("Masukkan angka yang valid!")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)

