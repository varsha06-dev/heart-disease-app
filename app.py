import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CardioSense · Heart Disease Risk Predictor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* Base */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Background */
.stApp {
    background-color: #F7F5F2;
    color: #1A1A2E;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1A1A2E;
    border-right: none;
}
section[data-testid="stSidebar"] * {
    color: #E8E4DC !important;
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stSlider label,
section[data-testid="stSidebar"] .stNumberInput label {
    color: #A8A4B0 !important;
    font-size: 0.78rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #E8E4DC !important;
}

/* Main header */
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 3.2rem;
    font-weight: 400;
    color: #1A1A2E;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 0.2rem;
}
.hero-title em {
    color: #C0392B;
    font-style: italic;
}
.hero-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 1rem;
    color: #6B6B7B;
    font-weight: 400;
    letter-spacing: 0.01em;
    margin-bottom: 2rem;
}

/* Divider */
.rule {
    border: none;
    border-top: 1.5px solid #D9D5CE;
    margin: 1.5rem 0;
}

/* Result cards */
.result-card {
    border-radius: 12px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.2rem;
}
.result-low {
    background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
    border-left: 5px solid #27AE60;
}
.result-high {
    background: linear-gradient(135deg, #FDECEA 0%, #FFF3E0 100%);
    border-left: 5px solid #C0392B;
}
.result-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.4rem;
    color: #6B6B7B;
}
.result-verdict {
    font-family: 'DM Serif Display', serif;
    font-size: 2.4rem;
    line-height: 1.1;
    margin-bottom: 0.5rem;
}
.result-verdict-low { color: #1B5E20; }
.result-verdict-high { color: #7B1010; }
.result-desc {
    font-size: 0.92rem;
    color: #4A4A5A;
    line-height: 1.6;
}

/* Probability bar */
.prob-track {
    background: #E0DDD8;
    border-radius: 999px;
    height: 10px;
    width: 100%;
    margin: 1rem 0 0.4rem 0;
    overflow: hidden;
}
.prob-fill-low {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #27AE60, #52C986);
}
.prob-fill-high {
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #E67E22, #C0392B);
}
.prob-labels {
    display: flex;
    justify-content: space-between;
    font-size: 0.72rem;
    color: #9A9AA8;
    font-family: 'JetBrains Mono', monospace;
}

/* Key factors */
.factor-row {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.55rem 0;
    border-bottom: 1px solid #E8E4DC;
    font-size: 0.88rem;
}
.factor-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}
.factor-name { color: #4A4A5A; flex: 1; }
.factor-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    color: #1A1A2E;
    font-weight: 500;
}
.factor-flag {
    font-size: 0.72rem;
    padding: 2px 8px;
    border-radius: 999px;
    font-weight: 500;
}
.flag-concern { background: #FDECEA; color: #C0392B; }
.flag-ok { background: #E8F5E9; color: #27AE60; }
.flag-note { background: #FFF8E1; color: #B7770D; }

/* Info box */
.info-box {
    background: #EEF0F8;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    font-size: 0.84rem;
    color: #4A4A5A;
    line-height: 1.6;
    border-left: 3px solid #3D52A0;
}

/* Section label */
.section-eyebrow {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #C0392B;
    margin-bottom: 0.3rem;
}
.section-heading {
    font-family: 'DM Serif Display', serif;
    font-size: 1.5rem;
    color: #1A1A2E;
    margin-bottom: 1rem;
}

/* Sidebar nav label */
.nav-label {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #A8A4B0 !important;
    margin-top: 1.5rem;
    margin-bottom: 0.5rem;
    display: block;
}

/* Metric chip */
.metric-chip {
    display: inline-block;
    background: #1A1A2E;
    color: #E8E4DC;
    border-radius: 6px;
    padding: 0.3rem 0.75rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
}
.metric-chip span {
    color: #C0392B;
    font-weight: 600;
}

/* Disclaimer */
.disclaimer {
    font-size: 0.75rem;
    color: #9A9AA8;
    line-height: 1.5;
    margin-top: 1.5rem;
    padding-top: 1rem;
    border-top: 1px solid #D9D5CE;
}

/* Model comparison table */
.model-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
}
.model-table th {
    text-align: left;
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #9A9AA8;
    padding: 0.5rem 0.8rem;
    border-bottom: 2px solid #D9D5CE;
}
.model-table td {
    padding: 0.7rem 0.8rem;
    border-bottom: 1px solid #E8E4DC;
    color: #4A4A5A;
}
.model-table tr.best td { color: #1A1A2E; font-weight: 600; }
.model-table tr.best td:first-child::before {
    content: '★ ';
    color: #C0392B;
}
</style>
""", unsafe_allow_html=True)


# ─── Preprocessing helper ──────────────────────────────────────────────────────
def preprocess_input(raw: dict) -> pd.DataFrame:
    """Apply the same pipeline as the notebook: cap outliers, log chol,
    clip oldpeak, scale numerics, one-hot encode categoricals."""

    # IQR bounds derived from the training data (heart.csv, 1025 rows)
    IQR_BOUNDS = {
        "trestbps": (94.0, 172.0),
        "thalach":  (103.5, 187.5),
    }
    SCALER_PARAMS = {
        # (mean, std) fitted on training data after transformations
        "age":      (54.37, 9.08),
        "trestbps": (132.18, 17.56),
        "chol":     (5.543, 0.198),   # post log1p
        "thalach":  (149.65, 22.49),
        "oldpeak":  (1.055, 1.166),
    }

    d = raw.copy()

    # Sex encoding
    d["sex"] = 1 if d["sex"] == "Male" else 0

    # Outlier capping
    for col, (lo, hi) in IQR_BOUNDS.items():
        d[col] = float(np.clip(d[col], lo, hi))

    # Log transform cholesterol
    d["chol"] = float(np.log1p(d["chol"]))

    # Clip oldpeak
    d["oldpeak"] = float(np.clip(d["oldpeak"], 0, 4.5))

    # Standard scaling
    for col, (mean, std) in SCALER_PARAMS.items():
        d[col] = (d[col] - mean) / std

    # One-hot encode restecg (0 baseline → restecg_1, restecg_2)
    rg = int(d.pop("restecg"))
    d["restecg_1"] = 1 if rg == 1 else 0
    d["restecg_2"] = 1 if rg == 2 else 0

    # One-hot encode cp (0 baseline → cp_1, cp_2, cp_3)
    cp = int(d.pop("cp"))
    d["cp_1"] = 1 if cp == 1 else 0
    d["cp_2"] = 1 if cp == 2 else 0
    d["cp_3"] = 1 if cp == 3 else 0

    # One-hot encode thal (0 baseline → thal_1, thal_2, thal_3)
    th = int(d.pop("thal"))
    d["thal_1"] = 1 if th == 1 else 0
    d["thal_2"] = 1 if th == 2 else 0
    d["thal_3"] = 1 if th == 3 else 0

    FEATURE_ORDER = [
        "age", "sex", "trestbps", "chol", "fbs",
        "thalach", "exang", "oldpeak", "slope", "ca",
        "restecg_1", "restecg_2",
        "cp_1", "cp_2", "cp_3",
        "thal_1", "thal_2", "thal_3",
    ]
    return pd.DataFrame([[d[f] for f in FEATURE_ORDER]], columns=FEATURE_ORDER)


def get_factor_flags(raw: dict) -> list:
    """Return list of (label, value_str, flag) tuples for key features."""
    factors = []

    # Age
    age_flag = "flag-concern" if raw["age"] > 60 else ("flag-note" if raw["age"] > 50 else "flag-ok")
    age_tag  = "Elevated risk" if raw["age"] > 60 else ("Moderate risk" if raw["age"] > 50 else "Normal range")
    factors.append(("Age", f"{raw['age']} yrs", age_flag, age_tag))

    # Resting BP
    bp_flag = "flag-concern" if raw["trestbps"] > 140 else ("flag-note" if raw["trestbps"] > 120 else "flag-ok")
    bp_tag  = "Hypertensive" if raw["trestbps"] > 140 else ("Pre-hypertensive" if raw["trestbps"] > 120 else "Normal")
    factors.append(("Resting BP", f"{raw['trestbps']} mmHg", bp_flag, bp_tag))

    # Cholesterol
    chol_flag = "flag-concern" if raw["chol"] > 240 else ("flag-note" if raw["chol"] > 200 else "flag-ok")
    chol_tag  = "High" if raw["chol"] > 240 else ("Borderline" if raw["chol"] > 200 else "Desirable")
    factors.append(("Cholesterol", f"{raw['chol']} mg/dL", chol_flag, chol_tag))

    # Max heart rate
    thalach_flag = "flag-concern" if raw["thalach"] < 120 else ("flag-ok" if raw["thalach"] > 150 else "flag-note")
    thalach_tag  = "Low — possible issue" if raw["thalach"] < 120 else ("Good capacity" if raw["thalach"] > 150 else "Moderate")
    factors.append(("Max Heart Rate", f"{raw['thalach']} bpm", thalach_flag, thalach_tag))

    # ST Depression
    op_flag = "flag-concern" if raw["oldpeak"] > 2.0 else ("flag-note" if raw["oldpeak"] > 1.0 else "flag-ok")
    op_tag  = "Significant" if raw["oldpeak"] > 2.0 else ("Mild" if raw["oldpeak"] > 1.0 else "Minimal")
    factors.append(("ST Depression", f"{raw['oldpeak']}", op_flag, op_tag))

    # Chest pain type
    cp_labels = {0: "Typical Angina", 1: "Atypical Angina", 2: "Non-anginal", 3: "Asymptomatic"}
    cp_flag = "flag-concern" if raw["cp"] in [0, 3] else "flag-ok"
    cp_tag  = "Higher risk type" if raw["cp"] in [0, 3] else "Lower risk type"
    factors.append(("Chest Pain Type", cp_labels[raw["cp"]], cp_flag, cp_tag))

    # Major vessels
    ca_flag = "flag-concern" if raw["ca"] >= 2 else ("flag-note" if raw["ca"] == 1 else "flag-ok")
    ca_tag  = "Significant narrowing" if raw["ca"] >= 2 else ("Mild narrowing" if raw["ca"] == 1 else "Clear vessels")
    factors.append(("Major Vessels (CA)", str(raw["ca"]), ca_flag, ca_tag))

    return factors


# ─── Model loading ─────────────────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "final_heart_model.pkl")
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None


model = load_model()


# ─── Sidebar — Patient Inputs ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🫀 CardioSense")
    st.markdown("<span class='nav-label'>Patient Profile</span>", unsafe_allow_html=True)

    age = st.slider("Age", min_value=20, max_value=90, value=52, step=1)
    sex = st.selectbox("Sex", ["Male", "Female"])

    st.markdown("<span class='nav-label'>Cardiac Symptoms</span>", unsafe_allow_html=True)

    cp_options = {
        "Typical Angina (0)": 0,
        "Atypical Angina (1)": 1,
        "Non-anginal Pain (2)": 2,
        "Asymptomatic (3)": 3,
    }
    cp = st.selectbox("Chest Pain Type", list(cp_options.keys()))
    exang = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])
    thalach = st.slider("Max Heart Rate Achieved", 60, 210, 150, step=1)
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.2, 1.0, step=0.1)
    slope_opts = {"Upsloping (0)": 0, "Flat (1)": 1, "Downsloping (2)": 2}
    slope = st.selectbox("Slope of Peak ST Segment", list(slope_opts.keys()))

    st.markdown("<span class='nav-label'>Lab Results</span>", unsafe_allow_html=True)

    trestbps = st.slider("Resting Blood Pressure (mmHg)", 80, 200, 130, step=1)
    chol = st.slider("Serum Cholesterol (mg/dL)", 100, 600, 240, step=1)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["No (0)", "Yes (1)"])

    st.markdown("<span class='nav-label'>Diagnostic Tests</span>", unsafe_allow_html=True)

    restecg_opts = {
        "Normal (0)": 0,
        "ST-T Abnormality (1)": 1,
        "Left Ventricular Hypertrophy (2)": 2,
    }
    restecg = st.selectbox("Resting ECG Results", list(restecg_opts.keys()))
    ca = st.slider("Major Vessels Colored by Fluoroscopy (CA)", 0, 4, 0)
    thal_opts = {
        "Normal (0)": 0,
        "Fixed Defect (1)": 1,
        "Reversable Defect (2)": 2,
        "Unknown (3)": 3,
    }
    thal = st.selectbox("Thalassemia", list(thal_opts.keys()))

    st.markdown("---")
    predict_btn = st.button("Run Assessment →", use_container_width=True, type="primary")


# ─── Collect raw inputs ────────────────────────────────────────────────────────
raw_inputs = {
    "age": age,
    "sex": sex,
    "cp": cp_options[cp],
    "trestbps": trestbps,
    "chol": chol,
    "fbs": 1 if "Yes" in fbs else 0,
    "restecg": restecg_opts[restecg],
    "thalach": thalach,
    "exang": 1 if exang == "Yes" else 0,
    "oldpeak": oldpeak,
    "slope": slope_opts[slope],
    "ca": ca,
    "thal": thal_opts[thal],
}


# ─── Main Layout ───────────────────────────────────────────────────────────────
col_main, col_info = st.columns([3, 2], gap="large")

with col_main:
    st.markdown("<div class='hero-title'>Heart Disease<br><em>Risk Assessment</em></div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-subtitle'>Clinical decision support · XGBoost model · Trained on 1,025 patient records</div>", unsafe_allow_html=True)
    st.markdown("<hr class='rule'>", unsafe_allow_html=True)

    # ── Result Panel ──
    if predict_btn or True:  # always show a panel; update on button press
        input_df = preprocess_input(raw_inputs)

        if model is not None:
            pred = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0][1]
        else:
            # Demo mode — simulate a plausible result from the raw values
            risk_score = 0.0
            if raw_inputs["cp"] in [0, 3]: risk_score += 0.25
            if raw_inputs["ca"] >= 2: risk_score += 0.25
            if raw_inputs["thalach"] < 130: risk_score += 0.15
            if raw_inputs["oldpeak"] > 2.0: risk_score += 0.15
            if raw_inputs["trestbps"] > 140: risk_score += 0.10
            if raw_inputs["chol"] > 240: risk_score += 0.05
            if raw_inputs["age"] > 60: risk_score += 0.05
            prob = min(risk_score, 0.99)
            pred = 1 if prob >= 0.5 else 0

        is_high = pred == 1

        if is_high:
            st.markdown(f"""
            <div class='result-card result-high'>
                <div class='result-label'>Assessment Result</div>
                <div class='result-verdict result-verdict-high'>Elevated Risk<br>Detected</div>
                <div class='result-desc'>
                    The model indicates a <strong>high probability of heart disease</strong>
                    ({prob*100:.1f}%). This result should be reviewed by a qualified cardiologist
                    before any clinical decisions are made.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='result-card result-low'>
                <div class='result-label'>Assessment Result</div>
                <div class='result-verdict result-verdict-low'>Lower Risk<br>Profile</div>
                <div class='result-desc'>
                    The model indicates a <strong>lower probability of heart disease</strong>
                    ({prob*100:.1f}%). Regular monitoring and a healthy lifestyle remain important.
                    Consult your physician for a full evaluation.
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Probability bar
        fill_class = "prob-fill-high" if is_high else "prob-fill-low"
        st.markdown(f"""
        <div class='prob-track'><div class='{fill_class}' style='width:{prob*100:.1f}%'></div></div>
        <div class='prob-labels'><span>0% risk</span><span style="font-weight:600;color:{'#C0392B' if is_high else '#27AE60'}">{prob*100:.1f}%</span><span>100% risk</span></div>
        """, unsafe_allow_html=True)

        st.markdown("<hr class='rule'>", unsafe_allow_html=True)

        # Key factors
        st.markdown("<div class='section-eyebrow'>Clinical Indicators</div>", unsafe_allow_html=True)
        st.markdown("<div class='section-heading'>Key Factors in This Assessment</div>", unsafe_allow_html=True)

        factors = get_factor_flags(raw_inputs)
        factor_html = ""
        for name, val, flag_cls, tag in factors:
            dot_color = "#C0392B" if "concern" in flag_cls else ("#27AE60" if "ok" in flag_cls else "#E67E22")
            factor_html += f"""
            <div class='factor-row'>
                <div class='factor-dot' style='background:{dot_color}'></div>
                <span class='factor-name'>{name}</span>
                <span class='factor-val'>{val}</span>
                <span class='factor-flag {flag_cls}'>{tag}</span>
            </div>"""
        st.markdown(factor_html, unsafe_allow_html=True)

        if model is None:
            st.markdown("""
            <div style='margin-top:1rem;padding:0.7rem 1rem;background:#FFF8E1;border-radius:8px;
                        font-size:0.8rem;color:#7B5E00;border-left:3px solid #F0B429;'>
            ⚠️ <strong>Demo mode:</strong> No trained model file found. Place
            <code>final_heart_model.pkl</code> in the same folder as <code>app.py</code>
            to enable live XGBoost predictions.
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <p class='disclaimer'>
        ⚕️ <strong>Medical disclaimer:</strong> CardioSense is a research tool and
        <em>not</em> a substitute for professional medical advice, diagnosis, or treatment.
        All predictions must be reviewed by a qualified clinician. This model was trained
        on the UCI Heart Disease dataset (1,025 records) and may not generalize to all
        patient populations.
        </p>
        """, unsafe_allow_html=True)

with col_info:
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Model performance summary
    st.markdown("<div class='section-eyebrow'>Model Performance</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>Why XGBoost?</div>", unsafe_allow_html=True)

    st.markdown("""
    <table class='model-table'>
      <thead>
        <tr>
          <th>Model</th><th>Accuracy</th><th>Recall</th><th>ROC-AUC</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Logistic Regression</td><td>84.9%</td><td>91.4%</td><td>~0.93</td></tr>
        <tr><td>Random Forest</td><td>99.0%</td><td>98.1%</td><td>~0.99</td></tr>
        <tr class='best'><td>XGBoost</td><td>100%</td><td>100%</td><td>1.00</td></tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style='font-size:0.82rem;color:#6B6B7B;margin-top:0.8rem;line-height:1.6;'>
    In medical diagnosis, <strong>recall is the critical metric</strong> — a missed
    heart disease case (false negative) is far more dangerous than a false alarm.
    XGBoost achieved zero false negatives on the held-out test set.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)

    # Feature guide
    st.markdown("<div class='section-eyebrow'>Input Guide</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>What Each Field Means</div>", unsafe_allow_html=True)

    with st.expander("Chest Pain Type"):
        st.markdown("""
- **Typical Angina (0):** Classic chest pain triggered by exertion
- **Atypical Angina (1):** Chest pain not fully matching typical pattern
- **Non-anginal Pain (2):** Chest discomfort unrelated to heart
- **Asymptomatic (3):** No chest pain symptoms — often highest risk
        """)
    with st.expander("ST Depression (Oldpeak)"):
        st.markdown("""
ST depression is measured in mm on an ECG during exercise testing.
Values above 2.0 mm are considered clinically significant and associated
with higher risk of coronary artery disease.
        """)
    with st.expander("Thalassemia"):
        st.markdown("""
- **Normal (0):** Normal blood flow
- **Fixed Defect (1):** Permanent reduced blood flow area
- **Reversable Defect (2):** Reduced flow during stress, recovers at rest
        """)
    with st.expander("Major Vessels (CA)"):
        st.markdown("""
Number of major coronary vessels (0–4) showing significant narrowing
(≥50% stenosis) on fluoroscopy imaging. Higher numbers indicate more
extensive coronary artery disease.
        """)

    st.markdown("<hr class='rule'>", unsafe_allow_html=True)

    st.markdown("<div class='section-eyebrow'>About This Project</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
    Built as a capstone ML project using the
    <a href='https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset'
       style='color:#3D52A0;'>UCI Heart Disease dataset</a>.
    The pipeline covers EDA, outlier handling, feature engineering, model selection
    across three classifiers, cross-validation, and a simulated deployment plan
    with HIPAA compliance and ethical considerations.
    </div>
    """, unsafe_allow_html=True)
