import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Risk Predictor · CardioSense", page_icon="🔬", layout="wide")

# ── Shared styles ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif;}
.stApp{background-color:#F7F5F2;color:#1A1A2E;}
section[data-testid="stSidebar"]{background-color:#1A1A2E;}
section[data-testid="stSidebar"] *{color:#E8E4DC !important;}
section[data-testid="stSidebar"] label{color:#A8A4B0 !important;font-size:0.75rem;font-weight:600;letter-spacing:0.09em;text-transform:uppercase;}
.hero-title{font-family:'DM Serif Display',serif;font-size:2.4rem;color:#1A1A2E;line-height:1.1;letter-spacing:-0.02em;margin-bottom:0.2rem;}
.hero-title em{color:#C0392B;font-style:italic;}
.hero-subtitle{font-size:0.95rem;color:#6B6B7B;margin-bottom:1.5rem;}
.rule{border:none;border-top:1.5px solid #D9D5CE;margin:1.5rem 0;}
.section-eyebrow{font-size:0.7rem;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#C0392B;margin-bottom:0.3rem;}
.section-heading{font-family:'DM Serif Display',serif;font-size:1.5rem;color:#1A1A2E;margin-bottom:1rem;}
.result-card{border-radius:12px;padding:2rem 2.2rem;margin-bottom:1.2rem;}
.result-low{background:linear-gradient(135deg,#E8F5E9,#F1F8E9);border-left:5px solid #27AE60;}
.result-high{background:linear-gradient(135deg,#FDECEA,#FFF3E0);border-left:5px solid #C0392B;}
.result-label{font-size:0.72rem;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#6B6B7B;margin-bottom:0.4rem;}
.result-verdict{font-family:'DM Serif Display',serif;font-size:2.4rem;line-height:1.1;margin-bottom:0.5rem;}
.result-verdict-low{color:#1B5E20;}
.result-verdict-high{color:#7B1010;}
.result-desc{font-size:0.92rem;color:#4A4A5A;line-height:1.6;}
.prob-track{background:#E0DDD8;border-radius:999px;height:10px;width:100%;margin:1rem 0 0.4rem;overflow:hidden;}
.prob-fill-low{height:100%;border-radius:999px;background:linear-gradient(90deg,#27AE60,#52C986);}
.prob-fill-high{height:100%;border-radius:999px;background:linear-gradient(90deg,#E67E22,#C0392B);}
.prob-labels{display:flex;justify-content:space-between;font-size:0.72rem;color:#9A9AA8;font-family:'JetBrains Mono',monospace;}
.factor-row{display:flex;align-items:center;gap:0.8rem;padding:0.55rem 0;border-bottom:1px solid #E8E4DC;font-size:0.88rem;}
.factor-dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.factor-name{color:#4A4A5A;flex:1;}
.factor-val{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#1A1A2E;font-weight:500;}
.factor-flag{font-size:0.72rem;padding:2px 8px;border-radius:999px;font-weight:500;}
.flag-concern{background:#FDECEA;color:#C0392B;}
.flag-ok{background:#E8F5E9;color:#27AE60;}
.flag-note{background:#FFF8E1;color:#B7770D;}
.disclaimer{font-size:0.75rem;color:#9A9AA8;line-height:1.5;margin-top:1.5rem;padding-top:1rem;border-top:1px solid #D9D5CE;}
.info-box{background:#EEF0F8;border-radius:8px;padding:1rem 1.2rem;font-size:0.84rem;color:#4A4A5A;line-height:1.6;border-left:3px solid #3D52A0;}
.model-table{width:100%;border-collapse:collapse;font-size:0.88rem;}
.model-table th{text-align:left;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:#9A9AA8;padding:0.5rem 0.8rem;border-bottom:2px solid #D9D5CE;}
.model-table td{padding:0.7rem 0.8rem;border-bottom:1px solid #E8E4DC;color:#4A4A5A;}
.model-table tr.best td{color:#1A1A2E;font-weight:600;background:#FEF9F9;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🫀 CardioSense")
    st.markdown("---")
    st.page_link("app.py",                    label="🏠  Home")
    st.page_link("pages/1_predictor.py",       label="🔬  Risk Predictor")
    st.page_link("pages/2_model_analysis.py",  label="📊  Model Analysis")
    st.page_link("pages/3_deployment.py",      label="🚀  Deployment Plan")
    st.page_link("pages/4_ethics.py",          label="⚖️  Ethics & Fairness")
    st.markdown("---")
    st.markdown("<span style='font-size:0.72rem;color:#A8A4B0;'>Patient Inputs</span>", unsafe_allow_html=True)
    age      = st.slider("Age", 20, 90, 52)
    sex      = st.selectbox("Sex", ["Male", "Female"])
    cp       = st.selectbox("Chest Pain Type", ["Typical Angina (0)","Atypical Angina (1)","Non-anginal Pain (2)","Asymptomatic (3)"])
    exang    = st.selectbox("Exercise-Induced Angina", ["No","Yes"])
    thalach  = st.slider("Max Heart Rate (bpm)", 60, 210, 150)
    oldpeak  = st.slider("ST Depression (Oldpeak)", 0.0, 6.2, 1.0, 0.1)
    slope    = st.selectbox("ST Slope", ["Upsloping (0)","Flat (1)","Downsloping (2)"])
    st.markdown("---")
    trestbps = st.slider("Resting Blood Pressure (mmHg)", 80, 200, 130)
    chol     = st.slider("Serum Cholesterol (mg/dL)", 100, 600, 240)
    fbs      = st.selectbox("Fasting Blood Sugar >120", ["No (0)","Yes (1)"])
    restecg  = st.selectbox("Resting ECG", ["Normal (0)","ST-T Abnormality (1)","LV Hypertrophy (2)"])
    ca       = st.slider("Major Vessels (CA)", 0, 4, 0)
    thal     = st.selectbox("Thalassemia", ["Normal (0)","Fixed Defect (1)","Reversable Defect (2)","Unknown (3)"])
    st.markdown("---")
    predict_btn = st.button("Run Assessment →", use_container_width=True, type="primary")

# ── Helpers ────────────────────────────────────────────────────────────────────
CP_MAP    = {"Typical Angina (0)":0,"Atypical Angina (1)":1,"Non-anginal Pain (2)":2,"Asymptomatic (3)":3}
SLOPE_MAP = {"Upsloping (0)":0,"Flat (1)":1,"Downsloping (2)":2}
RECG_MAP  = {"Normal (0)":0,"ST-T Abnormality (1)":1,"LV Hypertrophy (2)":2}
THAL_MAP  = {"Normal (0)":0,"Fixed Defect (1)":1,"Reversable Defect (2)":2,"Unknown (3)":3}

raw = {
    "age": age, "sex": sex,
    "cp": CP_MAP[cp], "trestbps": trestbps, "chol": chol,
    "fbs": 1 if "Yes" in fbs else 0,
    "restecg": RECG_MAP[restecg], "thalach": thalach,
    "exang": 1 if exang=="Yes" else 0,
    "oldpeak": oldpeak, "slope": SLOPE_MAP[slope], "ca": ca, "thal": THAL_MAP[thal],
}

IQR_BOUNDS   = {"trestbps":(94.0,172.0),"thalach":(103.5,187.5)}
SCALER_PARAMS= {"age":(54.37,9.08),"trestbps":(132.18,17.56),"chol":(5.543,0.198),"thalach":(149.65,22.49),"oldpeak":(1.055,1.166)}

def preprocess(r):
    d = r.copy()
    d["sex"] = 1 if d["sex"]=="Male" else 0
    for col,(lo,hi) in IQR_BOUNDS.items(): d[col]=float(np.clip(d[col],lo,hi))
    d["chol"]    = float(np.log1p(d["chol"]))
    d["oldpeak"] = float(np.clip(d["oldpeak"],0,4.5))
    for col,(mean,std) in SCALER_PARAMS.items(): d[col]=(d[col]-mean)/std
    rg=int(d.pop("restecg")); d["restecg_1"]=1 if rg==1 else 0; d["restecg_2"]=1 if rg==2 else 0
    cp=int(d.pop("cp")); d["cp_1"]=1 if cp==1 else 0; d["cp_2"]=1 if cp==2 else 0; d["cp_3"]=1 if cp==3 else 0
    th=int(d.pop("thal")); d["thal_1"]=1 if th==1 else 0; d["thal_2"]=1 if th==2 else 0; d["thal_3"]=1 if th==3 else 0
    ORDER=["age","sex","trestbps","chol","fbs","thalach","exang","oldpeak","slope","ca","restecg_1","restecg_2","cp_1","cp_2","cp_3","thal_1","thal_2","thal_3"]
    return pd.DataFrame([[d[f] for f in ORDER]],columns=ORDER)

def get_flags(r):
    facts=[]
    a=r["age"]; facts.append(("Age",f"{a} yrs","flag-concern" if a>60 else "flag-note" if a>50 else "flag-ok","Elevated risk" if a>60 else "Moderate risk" if a>50 else "Normal range"))
    b=r["trestbps"]; facts.append(("Resting BP",f"{b} mmHg","flag-concern" if b>140 else "flag-note" if b>120 else "flag-ok","Hypertensive" if b>140 else "Pre-hypertensive" if b>120 else "Normal"))
    c=r["chol"]; facts.append(("Cholesterol",f"{c} mg/dL","flag-concern" if c>240 else "flag-note" if c>200 else "flag-ok","High" if c>240 else "Borderline" if c>200 else "Desirable"))
    t=r["thalach"]; facts.append(("Max Heart Rate",f"{t} bpm","flag-concern" if t<120 else "flag-ok" if t>150 else "flag-note","Low — possible issue" if t<120 else "Good capacity" if t>150 else "Moderate"))
    o=r["oldpeak"]; facts.append(("ST Depression",f"{o}","flag-concern" if o>2 else "flag-note" if o>1 else "flag-ok","Significant" if o>2 else "Mild" if o>1 else "Minimal"))
    cp_l={0:"Typical Angina",1:"Atypical Angina",2:"Non-anginal",3:"Asymptomatic"}; cp=r["cp"]; facts.append(("Chest Pain Type",cp_l[cp],"flag-concern" if cp in [0,3] else "flag-ok","Higher risk type" if cp in [0,3] else "Lower risk type"))
    ca=r["ca"]; facts.append(("Major Vessels",str(ca),"flag-concern" if ca>=2 else "flag-note" if ca==1 else "flag-ok","Significant narrowing" if ca>=2 else "Mild narrowing" if ca==1 else "Clear vessels"))
    return facts

@st.cache_resource
def load_model():
    p = os.path.join(os.path.dirname(os.path.dirname(__file__)), "final_heart_model.pkl")
    return joblib.load(p) if os.path.exists(p) else None

model = load_model()

# ── Layout ─────────────────────────────────────────────────────────────────────
st.markdown("<div class='hero-title'>Patient<br><em>Risk Assessment</em></div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>Adjust the patient profile in the sidebar, then click Run Assessment</div>", unsafe_allow_html=True)
st.markdown("<hr class='rule'>", unsafe_allow_html=True)

col_main, col_info = st.columns([3,2], gap="large")

with col_main:
    df_in = preprocess(raw)

    if model is not None:
        pred = model.predict(df_in)[0]
        prob = model.predict_proba(df_in)[0][1]
    else:
        score=0.0
        if raw["cp"] in [0,3]: score+=0.25
        if raw["ca"]>=2: score+=0.25
        if raw["thalach"]<130: score+=0.15
        if raw["oldpeak"]>2: score+=0.15
        if raw["trestbps"]>140: score+=0.10
        if raw["chol"]>240: score+=0.05
        if raw["age"]>60: score+=0.05
        prob=min(score,0.99); pred=1 if prob>=0.5 else 0

    is_high = pred==1

    if is_high:
        st.markdown(f"""<div class='result-card result-high'>
            <div class='result-label'>Assessment Result</div>
            <div class='result-verdict result-verdict-high'>Elevated Risk<br>Detected</div>
            <div class='result-desc'>The model indicates a <strong>high probability of heart disease</strong>
            ({prob*100:.1f}%). This result should be reviewed by a qualified cardiologist before any clinical decisions are made.</div>
        </div>""", unsafe_allow_html=True)
    else:
        st.markdown(f"""<div class='result-card result-low'>
            <div class='result-label'>Assessment Result</div>
            <div class='result-verdict result-verdict-low'>Lower Risk<br>Profile</div>
            <div class='result-desc'>The model indicates a <strong>lower probability of heart disease</strong>
            ({prob*100:.1f}%). Regular monitoring and a healthy lifestyle remain important.</div>
        </div>""", unsafe_allow_html=True)

    fill = "prob-fill-high" if is_high else "prob-fill-low"
    color = "#C0392B" if is_high else "#27AE60"
    st.markdown(f"""
    <div class='prob-track'><div class='{fill}' style='width:{prob*100:.1f}%'></div></div>
    <div class='prob-labels'><span>0%</span><span style='font-weight:600;color:{color}'>{prob*100:.1f}% disease probability</span><span>100%</span></div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    st.markdown("<div class='section-eyebrow'>Clinical Indicators</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>Key Factors in This Assessment</div>", unsafe_allow_html=True)

    html=""
    for name,val,fc,tag in get_flags(raw):
        dot="#C0392B" if "concern" in fc else ("#27AE60" if "ok" in fc else "#E67E22")
        html+=f"<div class='factor-row'><div class='factor-dot' style='background:{dot}'></div><span class='factor-name'>{name}</span><span class='factor-val'>{val}</span><span class='factor-flag {fc}'>{tag}</span></div>"
    st.markdown(html, unsafe_allow_html=True)

    if model is None:
        st.markdown("""<div style='margin-top:1rem;padding:0.7rem 1rem;background:#FFF8E1;border-radius:8px;font-size:0.8rem;color:#7B5E00;border-left:3px solid #F0B429;'>
        ⚠️ <strong>Demo mode:</strong> Place <code>final_heart_model.pkl</code> in the app root folder to enable live XGBoost predictions.</div>""", unsafe_allow_html=True)

    st.markdown("<p class='disclaimer'>⚕️ <strong>Medical disclaimer:</strong> CardioSense is a research tool and not a substitute for professional medical advice. All predictions must be reviewed by a qualified clinician.</p>", unsafe_allow_html=True)

with col_info:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div class='section-eyebrow'>Model</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>XGBoost Performance</div>", unsafe_allow_html=True)
    st.markdown("""<table class='model-table'><thead><tr><th>Model</th><th>Accuracy</th><th>Recall</th><th>AUC</th></tr></thead><tbody>
    <tr><td>Logistic Regression</td><td>84.9%</td><td>91.4%</td><td>0.93</td></tr>
    <tr><td>Random Forest</td><td>99.0%</td><td>98.1%</td><td>0.99</td></tr>
    <tr class='best'><td>★ XGBoost</td><td>100%</td><td>100%</td><td>1.00</td></tr>
    </tbody></table>""", unsafe_allow_html=True)
    st.markdown("<hr class='rule'>", unsafe_allow_html=True)
    st.markdown("<div class='section-eyebrow'>Input Guide</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>What Each Field Means</div>", unsafe_allow_html=True)
    with st.expander("Chest Pain Type"):
        st.markdown("- **Typical Angina (0):** Classic exertion-triggered chest pain\n- **Atypical Angina (1):** Chest pain not fully matching typical pattern\n- **Non-anginal Pain (2):** Chest discomfort unrelated to heart\n- **Asymptomatic (3):** No symptoms — often highest risk in this dataset")
    with st.expander("ST Depression (Oldpeak)"):
        st.markdown("Measured in mm on an ECG during exercise. Values above 2.0 mm are clinically significant and associated with higher risk of coronary artery disease.")
    with st.expander("Thalassemia"):
        st.markdown("- **Normal (0):** Normal blood flow\n- **Fixed Defect (1):** Permanent reduced flow area\n- **Reversable Defect (2):** Reduced flow during stress, recovers at rest")
    with st.expander("Major Vessels (CA)"):
        st.markdown("Number of major coronary vessels (0–4) showing ≥50% stenosis on fluoroscopy. Higher numbers = more extensive coronary artery disease.")
    with st.expander("Max Heart Rate (Thalach)"):
        st.markdown("Maximum heart rate achieved during exercise stress test. A lower-than-expected maximum heart rate can indicate reduced cardiac function.")
