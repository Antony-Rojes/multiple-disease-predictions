import streamlit as st

# ✅ Completely remove Deploy button and its dialog
hide_deploy_style = """
    <style>
    [data-testid="stDeploymentButton"] {
        display: none !important;
    }
    [data-testid="stHeaderActionMenuDeployItem"] {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_deploy_style, unsafe_allow_html=True)



import pickle
from streamlit_option_menu import option_menu

# loading saved models
diabetes_model = pickle.load(open('C:/Users/M.ANTONY ROJES/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/M.ANTONY ROJES/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/M.ANTONY ROJES/OneDrive/Desktop/Multiple Disease Prediction System/Saved Models/parkinsons_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart-pulse', 'person-standing'],
        default_index=0
    )

# ---------------- Diabetes Prediction ----------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    if st.button('Diabetes Test Result'):
        try:
            user_input = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]
            if not (0 <= user_input[7] <= 120):
                st.error("⚠️ Age must be 0–120")
            else:
                prediction = diabetes_model.predict([user_input])
                if prediction[0] == 1:
                    st.error("The Person is Diabetic")
                else:
                    st.success("The Person is Not Diabetic")
        except ValueError:
            st.error("⚠️ Enter numeric values only!")

# ---------------- Heart Disease Prediction ----------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, _, col2, _, col3 = st.columns([1,0.2,1,0.2,1])
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (0=Female,1=Male)')
    with col3:
        cp = st.text_input('Chest Pain Type (0–3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar >120 (1=True,0=False)')

    with col1:
        restecg = st.text_input('Resting ECG (0–2)')
    with col2:
        thalach = st.text_input('Max Heart Rate')
    with col3:
        exang = st.text_input('Exercise Angina (1=Yes,0=No)')

    with col1:
        oldpeak = st.text_input('ST Depression')
    with col2:
        slope = st.text_input('Slope (0–2)')
    with col3:
        ca = st.text_input('Major Vessels (0–3)')

    col1, _, col2, _, col3 = st.columns([1,0.2,1,0.2,1])
    with col2:
        thal = st.text_input('Thalassemia (1=Normal,2=Fixed,3=Reversible)')

    if st.button('Heart Disease Test Result'):
        try:
            user_input = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]
            if not (0 <= user_input[0] <= 120):
                st.error("⚠️ Age must be 0–120")
            else:
                prediction = heart_disease_model.predict([user_input])
                if prediction[0] == 1:
                    st.error("The Person has Heart Disease")
                else:
                    st.success("The Person does NOT have Heart Disease")
        except ValueError:
            st.error("⚠️ Enter numeric values only!")

# ---------------- Parkinsons Prediction ----------------
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction using ML')

    col1, _, col2, _, col3, _, col4, _, col5 = st.columns([1,0.2,1,0.2,1,0.2,1,0.2,1])
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        jitter_abs = st.text_input('MDVP:Jitter(Abs)')

    col1, _, col2, _, col3, _, col4, _, col5 = st.columns([1,0.2,1,0.2,1,0.2,1,0.2,1])
    with col1:
        rap = st.text_input('MDVP:RAP')
    with col2:
        ppq = st.text_input('MDVP:PPQ')
    with col3:
        ddp = st.text_input('Jitter:DDP')
    with col4:
        shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        shimmer_db = st.text_input('MDVP:Shimmer(dB)')

    col1, _, col2, _, col3, _, col4, _, col5 = st.columns([1,0.2,1,0.2,1,0.2,1,0.2,1])
    with col1:
        apq3 = st.text_input('Shimmer:APQ3')
    with col2:
        apq5 = st.text_input('Shimmer:APQ5')
    with col3:
        apq = st.text_input('MDVP:APQ')
    with col4:
        dda = st.text_input('Shimmer:DDA')
    with col5:
        nhr = st.text_input('NHR')

    col1, _, col2, _, col3, _, col4, _, col5 = st.columns([1,0.2,1,0.2,1,0.2,1,0.2,1])
    with col1:
        hnr = st.text_input('HNR')
    with col2:
        rpde = st.text_input('RPDE')
    with col3:
        dfa = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('Spread1')
    with col5:
        spread2 = st.text_input('Spread2')

    col1, _, col2, _, col3, _, col4, _, col5 = st.columns([1,0.2,1,0.2,1,0.2,1,0.2,1])
    with col2:
        d2 = st.text_input('D2')
    with col4:
        ppe = st.text_input('PPE')

    if st.button('Parkinsons Test Result'):
        try:
            user_input = [
                float(fo), float(fhi), float(flo), float(jitter_percent), float(jitter_abs),
                float(rap), float(ppq), float(ddp), float(shimmer), float(shimmer_db),
                float(apq3), float(apq5), float(apq), float(dda), float(nhr),
                float(hnr), float(rpde), float(dfa), float(spread1), float(spread2),
                float(d2), float(ppe)
            ]
            prediction = parkinsons_model.predict([user_input])
            if prediction[0] == 1:
                st.error("The Person has Parkinson’s Disease")
            else:
                st.success("The Person does NOT have Parkinson’s Disease")
        except ValueError:
            st.error("⚠️ Enter numeric values only!")
