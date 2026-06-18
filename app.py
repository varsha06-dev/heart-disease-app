import streamlit as st

st.set_page_config(
    page_title="CardioSense · Heart Disease Risk Predictor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Shared CSS injected on every page ────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background-color: #F7F5F2; color: #1A1A2E; }

section[data-testid="stSidebar"] { background-color: #1A1A2E; }
section[data-testid="stSidebar"] * { color: #E8E4DC !important; }
section[data-testid="stSidebar"] label {
    color: #A8A4B0 !important; font-size: 0.75rem;
    font-weight: 600; letter-spacing: 0.09em; text-transform: uppercase;
}

.hero-title {
    font-family: 'DM Serif Display', serif; font-size: 3rem;
    color: #1A1A2E; line-height: 1.1; letter-spacing: -0.02em; margin-bottom: 0.2rem;
}
.hero-title em { color: #C0392B; font-style: italic; }
.hero-subtitle { font-size: 1rem; color: #6B6B7B; margin-bottom: 1.5rem; }
.rule { border: none; border-top: 1.5px solid #D9D5CE; margin: 1.5rem 0; }
.section-eyebrow {
    font-size: 0.7rem; font-weight: 600; letter-spacing: 0.14em;
    text-transform: uppercase; color: #C0392B; margin-bottom: 0.3rem;
}
.section-heading {
    font-family: 'DM Serif Display', serif; font-size: 1.6rem;
    color: #1A1A2E; margin-bottom: 1rem; line-height: 1.2;
}
.card {
    background: white; border-radius: 12px; padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem; border: 1px solid #E8E4DC;
}
.card-red { border-left: 4px solid #C0392B; }
.card-green { border-left: 4px solid #27AE60; }
.card-blue { border-left: 4px solid #2980B9; }
.card-amber { border-left: 4px solid #E67E22; }
.card-purple { border-left: 4px solid #8E44AD; }

.result-card { border-radius: 12px; padding: 2rem 2.2rem; margin-bottom: 1.2rem; }
.result-low { background: linear-gradient(135deg,#E8F5E9,#F1F8E9); border-left: 5px solid #27AE60; }
.result-high { background: linear-gradient(135deg,#FDECEA,#FFF3E0); border-left: 5px solid #C0392B; }
.result-label { font-size:0.72rem; font-weight:600; letter-spacing:0.14em; text-transform:uppercase; color:#6B6B7B; margin-bottom:0.4rem; }
.result-verdict { font-family:'DM Serif Display',serif; font-size:2.4rem; line-height:1.1; margin-bottom:0.5rem; }
.result-verdict-low { color:#1B5E20; }
.result-verdict-high { color:#7B1010; }
.result-desc { font-size:0.92rem; color:#4A4A5A; line-height:1.6; }

.prob-track { background:#E0DDD8; border-radius:999px; height:10px; width:100%; margin:1rem 0 0.4rem; overflow:hidden; }
.prob-fill-low { height:100%; border-radius:999px; background:linear-gradient(90deg,#27AE60,#52C986); }
.prob-fill-high { height:100%; border-radius:999px; background:linear-gradient(90deg,#E67E22,#C0392B); }
.prob-labels { display:flex; justify-content:space-between; font-size:0.72rem; color:#9A9AA8; font-family:'JetBrains Mono',monospace; }

.factor-row { display:flex; align-items:center; gap:0.8rem; padding:0.55rem 0; border-bottom:1px solid #E8E4DC; font-size:0.88rem; }
.factor-dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }
.factor-name { color:#4A4A5A; flex:1; }
.factor-val { font-family:'JetBrains Mono',monospace; font-size:0.82rem; color:#1A1A2E; font-weight:500; }
.factor-flag { font-size:0.72rem; padding:2px 8px; border-radius:999px; font-weight:500; }
.flag-concern { background:#FDECEA; color:#C0392B; }
.flag-ok { background:#E8F5E9; color:#27AE60; }
.flag-note { background:#FFF8E1; color:#B7770D; }

.model-table { width:100%; border-collapse:collapse; font-size:0.88rem; }
.model-table th { text-align:left; font-size:0.7rem; letter-spacing:0.1em; text-transform:uppercase; color:#9A9AA8; padding:0.5rem 0.8rem; border-bottom:2px solid #D9D5CE; }
.model-table td { padding:0.7rem 0.8rem; border-bottom:1px solid #E8E4DC; color:#4A4A5A; }
.model-table tr.best td { color:#1A1A2E; font-weight:600; background:#FEF9F9; }

.badge { display:inline-block; border-radius:6px; padding:0.25rem 0.7rem; font-size:0.75rem; font-weight:600; margin-right:0.4rem; }
.badge-red { background:#FDECEA; color:#C0392B; }
.badge-green { background:#E8F5E9; color:#1B5E20; }
.badge-blue { background:#EBF5FB; color:#1A5276; }
.badge-amber { background:#FFF3E0; color:#784212; }
.badge-purple { background:#F5EEF8; color:#6C3483; }
.badge-gray { background:#F2F3F4; color:#4A4A5A; }

.info-box { background:#EEF0F8; border-radius:8px; padding:1rem 1.2rem; font-size:0.84rem; color:#4A4A5A; line-height:1.6; border-left:3px solid #3D52A0; }
.warn-box { background:#FFF8E1; border-radius:8px; padding:1rem 1.2rem; font-size:0.84rem; color:#7B5E00; line-height:1.6; border-left:3px solid #F0B429; }
.disclaimer { font-size:0.75rem; color:#9A9AA8; line-height:1.5; margin-top:1.5rem; padding-top:1rem; border-top:1px solid #D9D5CE; }

.nav-pill {
    display:inline-block; background:#2C2C4A; color:#E8E4DC !important;
    border-radius:8px; padding:0.5rem 1rem; font-size:0.82rem;
    font-weight:500; margin-bottom:0.4rem; width:100%; text-align:left;
    cursor:pointer;
}
.home-feature { text-align:center; padding:1.5rem 1rem; }
.home-feature .icon { font-size:2.2rem; margin-bottom:0.6rem; }
.home-feature h3 { font-family:'DM Serif Display',serif; font-size:1.2rem; color:#1A1A2E; margin-bottom:0.4rem; }
.home-feature p { font-size:0.84rem; color:#6B6B7B; line-height:1.5; }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🫀 CardioSense")
    st.markdown("---")
    st.markdown("**Navigation**")
    st.page_link("app.py",                        label="🏠  Home",                  )
    st.page_link("pages/1_predictor.py",           label="🔬  Risk Predictor",        )
    st.page_link("pages/2_model_analysis.py",      label="📊  Model Analysis",        )
    st.page_link("pages/3_deployment.py",          label="🚀  Deployment Plan",       )
    st.page_link("pages/4_ethics.py",              label="⚖️  Ethics & Fairness",     )
    st.markdown("---")
    st.markdown("<span style='font-size:0.75rem;color:#A8A4B0;'>Capstone ML Project<br>UCI Heart Disease Dataset<br>1,025 patient records</span>", unsafe_allow_html=True)

# ─── Home page ─────────────────────────────────────────────────────────────────
st.markdown("<div class='hero-title'>CardioSense<br><em>Heart Disease Prediction</em></div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>A full-stack machine learning capstone — from raw data to clinical deployment</div>", unsafe_allow_html=True)
st.markdown("<hr class='rule'>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown("""<div class='home-feature'>
        <div class='icon'>🔬</div>
        <h3>Risk Predictor</h3>
        <p>Enter patient vitals and get an instant XGBoost-powered heart disease risk assessment.</p>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""<div class='home-feature'>
        <div class='icon'>📊</div>
        <h3>Model Analysis</h3>
        <p>Deep comparison of Logistic Regression, Random Forest, and XGBoost across all metrics.</p>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown("""<div class='home-feature'>
        <div class='icon'>🚀</div>
        <h3>Deployment Plan</h3>
        <p>Production-ready architecture: API design, data pipeline, monitoring, and scalability.</p>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown("""<div class='home-feature'>
        <div class='icon'>⚖️</div>
        <h3>Ethics & Fairness</h3>
        <p>HIPAA compliance, bias mitigation, explainability, FDA considerations, and accountability.</p>
    </div>""", unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

col_l, col_r = st.columns([3, 2], gap="large")
with col_l:
    st.markdown("<div class='section-eyebrow'>Project Summary</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>What This Project Does</div>", unsafe_allow_html=True)
    st.markdown("""
    This capstone walks the full ML lifecycle for a **binary heart disease classifier**
    trained on the [UCI Heart Disease dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
    (1,025 patient records, 13 clinical features).

    The pipeline covers:
    - **EDA** — histograms, boxplots, correlation heatmaps, categorical breakdowns
    - **Data cleaning** — IQR-based outlier capping, log transformation of cholesterol
    - **Feature engineering** — StandardScaling, one-hot encoding of categoricals
    - **Model selection** — three classifiers evaluated across 5-fold cross-validation
    - **Deployment simulation** — serialized pipeline, preprocessing in production
    - **Ethical analysis** — fairness, privacy, transparency, regulatory compliance
    """)

with col_r:
    st.markdown("<div class='section-eyebrow'>Final Model Results</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-heading'>XGBoost Wins</div>", unsafe_allow_html=True)
    st.markdown("""
    <table class='model-table'>
      <thead><tr><th>Model</th><th>Accuracy</th><th>Recall</th><th>AUC</th></tr></thead>
      <tbody>
        <tr><td>Logistic Regression</td><td>84.9%</td><td>91.4%</td><td>0.93</td></tr>
        <tr><td>Random Forest</td><td>99.0%</td><td>98.1%</td><td>0.99</td></tr>
        <tr class='best'><td>★ XGBoost</td><td>100%</td><td>100%</td><td>1.00</td></tr>
      </tbody>
    </table>
    <p style='font-size:0.8rem;color:#6B6B7B;margin-top:0.8rem;line-height:1.5;'>
    In medical diagnosis, <strong>recall is the critical metric</strong> — a missed
    heart disease case is far more dangerous than a false alarm. XGBoost achieved
    zero false negatives on the held-out test set.
    </p>
    """, unsafe_allow_html=True)

st.markdown("""
<p class='disclaimer'>
⚕️ <strong>Medical disclaimer:</strong> CardioSense is a research and educational tool,
not a substitute for professional medical advice, diagnosis, or treatment.
All predictions must be reviewed by a qualified clinician.
</p>
""", unsafe_allow_html=True)
