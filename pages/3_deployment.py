import streamlit as st

st.set_page_config(page_title="Deployment Plan · CardioSense", page_icon="🚀", layout="wide")

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
.section-heading{font-family:'DM Serif Display',serif;font-size:1.5rem;color:#1A1A2E;margin-bottom:0.8rem;line-height:1.2;}
.card{background:white;border-radius:12px;padding:1.6rem 1.8rem;margin-bottom:1.2rem;border:1px solid #E8E4DC;}
.card-red{border-left:4px solid #C0392B;}
.card-green{border-left:4px solid #27AE60;}
.card-blue{border-left:4px solid #2980B9;}
.card-amber{border-left:4px solid #E67E22;}
.card-purple{border-left:4px solid #8E44AD;}
.card-dark{border-left:4px solid #1A1A2E;}
.card h3{font-family:'DM Serif Display',serif;font-size:1.15rem;color:#1A1A2E;margin-bottom:0.5rem;}
.card p,.card li{font-size:0.87rem;color:#4A4A5A;line-height:1.7;}
.card ul{padding-left:1.2rem;margin:0.4rem 0;}
.badge{display:inline-block;border-radius:6px;padding:0.2rem 0.65rem;font-size:0.72rem;font-weight:600;margin-right:0.3rem;margin-bottom:0.3rem;}
.badge-red{background:#FDECEA;color:#C0392B;}
.badge-green{background:#E8F5E9;color:#1B5E20;}
.badge-blue{background:#EBF5FB;color:#1A5276;}
.badge-amber{background:#FFF3E0;color:#784212;}
.badge-gray{background:#F2F3F4;color:#4A4A5A;}
.badge-purple{background:#F5EEF8;color:#6C3483;}
.layer-box{border-radius:10px;padding:1.2rem 1.4rem;margin-bottom:0.8rem;}
.layer-presentation{background:#EBF5FB;border-left:4px solid #2980B9;}
.layer-application{background:#E8F5E9;border-left:4px solid #27AE60;}
.layer-data{background:#FFF3E0;border-left:4px solid #E67E22;}
.layer-box h4{font-weight:600;font-size:0.9rem;color:#1A1A2E;margin-bottom:0.4rem;}
.layer-box p{font-size:0.83rem;color:#4A4A5A;line-height:1.6;margin:0;}
.pipeline-step{display:flex;align-items:flex-start;gap:1rem;padding:0.8rem 0;border-bottom:1px solid #E8E4DC;}
.pipeline-step:last-child{border-bottom:none;}
.step-circle{background:#1A1A2E;color:white;border-radius:50%;width:26px;height:26px;display:flex;align-items:center;justify-content:center;font-size:0.72rem;font-weight:700;flex-shrink:0;margin-top:0.15rem;}
.step-content h4{font-weight:600;font-size:0.88rem;color:#1A1A2E;margin-bottom:0.2rem;}
.step-content p{font-size:0.82rem;color:#6B6B7B;line-height:1.5;margin:0;}
.step-content code{font-family:'JetBrains Mono',monospace;font-size:0.78rem;background:#F2F3F4;padding:1px 5px;border-radius:4px;color:#C0392B;}
.kpi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-bottom:1.5rem;}
.kpi{background:white;border-radius:10px;padding:1.2rem;border:1px solid #E8E4DC;text-align:center;}
.kpi-val{font-family:'DM Serif Display',serif;font-size:2rem;color:#1A1A2E;}
.kpi-label{font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;margin-top:0.2rem;}
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

st.markdown("<div class='hero-title'>Production<br><em>Deployment Plan</em></div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>Architecture, data pipelines, monitoring, and scalability for clinical deployment</div>", unsafe_allow_html=True)
st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── KPIs ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class='kpi-grid'>
  <div class='kpi'><div class='kpi-val'>99.9%</div><div class='kpi-label'>Target Uptime SLA</div></div>
  <div class='kpi'><div class='kpi-val'>&lt;200ms</div><div class='kpi-label'>Max Inference Latency</div></div>
  <div class='kpi'><div class='kpi-val'>HIPAA</div><div class='kpi-label'>Compliance Standard</div></div>
</div>
""", unsafe_allow_html=True)

# ── System Architecture ────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Architecture</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Three-Layer System Design</div>", unsafe_allow_html=True)

st.markdown("""
<div class='layer-box layer-presentation'>
<h4>🖥️ Presentation Layer — What clinicians and staff see</h4>
<p><strong>Clinician Dashboard:</strong> Web-based interface (React or Streamlit) showing patient risk score,
LOW / MODERATE / HIGH category, top contributing features, and a concise recommendation
(e.g. "Order stress test", "Optimize risk factors"). <strong>Never replaces clinical judgment</strong> —
the model's output is advisory only.<br><br>
<strong>Batch Upload Tool:</strong> CSV upload for bulk population screening — outputs a risk-ranked
patient list with probabilities.<br>
<strong>Admin UI:</strong> IT staff dashboard showing model version, deployment status, live metrics, and
data drift alerts.</p>
</div>

<div class='layer-box layer-application'>
<h4>⚙️ Application Layer — The prediction engine</h4>
<p><strong>FastAPI prediction endpoint:</strong> Stateless REST API that loads the frozen preprocessing
pipeline and trained XGBoost model at startup. Accepts raw patient data (same 13 fields as training),
applies the full preprocessing pipeline identically to training, and returns a structured JSON response:<br>
<code>{ prediction_id, timestamp, model_version, risk_category, probability, top_features }</code><br><br>
Input validation enforces data types and clinical ranges before any model call. All requests and
responses are logged with a unique prediction ID for auditability.</p>
</div>

<div class='layer-box layer-data'>
<h4>🗄️ Data & Infrastructure Layer — What keeps it running</h4>
<p><strong>Data sources:</strong> Hospital EHR and lab systems → ETL integration service → curated
patient-feature table.<br>
<strong>Model store:</strong> Versioned artifact registry (model weights, scaler params, feature order,
performance metrics, SHAP baseline).<br>
<strong>Observability stack:</strong> Logs, metrics, traces via Prometheus + Grafana or equivalent.<br>
<strong>Compute:</strong> Containerized (Docker) and orchestrated (Kubernetes) for horizontal
auto-scaling. Stateless API instances behind a load balancer handle traffic spikes.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Pipelines ─────────────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Data Pipelines</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Offline Training vs. Online Inference</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown("#### 🔄 Offline Training Pipeline")
    st.markdown("""
    <div style='background:white;border-radius:10px;padding:1.2rem 1.4rem;border:1px solid #E8E4DC;'>
    <div class='pipeline-step'>
      <div class='step-circle'>1</div>
      <div class='step-content'><h4>Extract from EHR</h4><p>Periodic batch extraction of patient records with lab results and ECG data from hospital systems.</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>2</div>
      <div class='step-content'><h4>Clean & Transform</h4><p>IQR outlier capping on <code>trestbps</code>, <code>thalach</code>. Log1p transform on <code>chol</code>. Clip <code>oldpeak</code> to [0, 4.5].</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>3</div>
      <div class='step-content'><h4>Encode & Scale</h4><p>One-hot encode <code>restecg</code>, <code>cp</code>, <code>thal</code>. StandardScaler fit on training split only — no leakage.</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>4</div>
      <div class='step-content'><h4>Train & Validate</h4><p>5-fold CV with stratification. Hyperparameter tuning if performance degrades. Final fit on full training set.</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>5</div>
      <div class='step-content'><h4>Store Artifacts</h4><p>Serialize model, scaler, feature order, performance metrics, and SHAP baseline to versioned artifact store.</p></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### ⚡ Online Inference Pipeline")
    st.markdown("""
    <div style='background:white;border-radius:10px;padding:1.2rem 1.4rem;border:1px solid #E8E4DC;'>
    <div class='pipeline-step'>
      <div class='step-circle'>1</div>
      <div class='step-content'><h4>Receive Patient Data</h4><p>API receives raw patient values (age, sex, cp, etc.) in JSON. Request validated against schema and clinical range rules.</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>2</div>
      <div class='step-content'><h4>Apply Saved Transforms</h4><p>Same preprocessing steps as training — using the <em>saved</em> scaler (<code>.transform()</code> only, never <code>.fit()</code>). Feature order enforced.</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>3</div>
      <div class='step-content'><h4>Model Inference</h4><p>XGBoost returns class prediction and probability. Confidence threshold applied — borderline cases flagged for manual review.</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>4</div>
      <div class='step-content'><h4>Build Response</h4><p>Structured JSON with prediction ID, timestamp, model version, risk category, probability, and top feature contributions.</p></div>
    </div>
    <div class='pipeline-step'>
      <div class='step-circle'>5</div>
      <div class='step-content'><h4>Log & Audit</h4><p>Full request/response logged with patient ID (hashed), model version, and prediction. Retained for audit trail and drift detection.</p></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Monitoring ─────────────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Monitoring & Governance</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Keeping the Model Trustworthy Over Time</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown("""
    <div class='card card-blue'>
    <h3>📡 Performance Monitoring</h3>
    <ul>
      <li>Track prediction volumes, latency, and error rates in real-time</li>
      <li>Monitor input feature distributions vs. training baseline to detect <strong>data drift</strong></li>
      <li>Monthly re-scoring on a labeled hold-out set to compare live metrics against CV baseline</li>
      <li>Automatic alert if recall drops below 95% threshold</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class='card card-amber'>
    <h3>⚖️ Fairness Monitoring</h3>
    <ul>
      <li>Quarterly confusion matrix breakdown by age group, sex, and ethnicity</li>
      <li>Track False Negative Rate (FNR) and False Positive Rate (FPR) per demographic subgroup</li>
      <li>Disparate impact ratio — alert if any group's FNR exceeds the overall FNR by &gt;10%</li>
      <li>Clinician override rate tracked as a signal of low-confidence predictions</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class='card card-green'>
    <h3>🔁 Retraining Policy</h3>
    <ul>
      <li>Scheduled quarterly retraining with accumulated clinical data</li>
      <li>Automated test suite runs on a fixed panel before any deployment</li>
      <li>Approval workflow — model promoted to production only after clinical review sign-off</li>
      <li>Full rollback capability — previous model version re-deployable in &lt;5 minutes</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Scalability ────────────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Scalability & Maintenance</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Built to Grow with Clinical Demand</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    **Infrastructure scalability:**
    - Stateless FastAPI instances mean horizontal scaling is straightforward —
      add more containers behind the load balancer as request volume grows
    - Kubernetes auto-scaling based on CPU utilization and request latency
    - Asynchronous processing queues (Celery + Redis) for batch upload jobs that
      would otherwise block the real-time API
    - XGBoost inference is fast (~1ms per prediction) — a single instance can
      handle thousands of predictions per second
    """)
with c2:
    st.markdown("""
    **Multi-hospital deployment:**
    - Each hospital gets a logically isolated tenant with separate audit logs
    - Shared model version, hospital-specific preprocessing config (if labs report
      cholesterol in different units, for example)
    - Centralized model registry — all tenants can be updated to a new model
      version in a single controlled rollout
    - Feature store caches frequently accessed patient features to reduce EHR query load
    """)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Simulated deployment demo ──────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Simulation</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>What a Production API Response Looks Like</div>", unsafe_allow_html=True)

st.markdown("The serialized pipeline tested in the notebook produced structured JSON responses like these for clinical cases:")

col1, col2 = st.columns(2, gap="large")
with col1:
    st.markdown("**High-Risk Patient (P-001)**")
    st.code("""{
  "status": "success",
  "prediction_id": "PRED-6598ECBF",
  "timestamp": "2026-06-16 21:06:42",
  "model_version": "1.0.0",
  "patient_id": "P-001-HR",
  "prediction": {
    "class": 1,
    "label": "Heart Disease",
    "probability_healthy": 0.072,
    "probability_disease": 0.928,
    "confidence": "High"
  },
  "risk_assessment": {
    "category": "HIGH",
    "recommendation": "Refer to cardiologist urgently"
  }
}""", language="json")

with col2:
    st.markdown("**Low-Risk Patient (P-002)**")
    st.code("""{
  "status": "success",
  "prediction_id": "PRED-7A12F3C9",
  "timestamp": "2026-06-16 21:07:01",
  "model_version": "1.0.0",
  "patient_id": "P-002-LR",
  "prediction": {
    "class": 0,
    "label": "No Heart Disease",
    "probability_healthy": 0.961,
    "probability_disease": 0.039,
    "confidence": "High"
  },
  "risk_assessment": {
    "category": "LOW",
    "recommendation": "Routine monitoring, healthy lifestyle"
  }
}""", language="json")

st.markdown("""
<div style='background:#EEF0F8;border-radius:8px;padding:1rem 1.2rem;font-size:0.84rem;color:#4A4A5A;line-height:1.6;border-left:3px solid #3D52A0;margin-top:1rem;'>
The <code>prediction_id</code> ties every response to its audit log entry. The <code>model_version</code>
field means any prediction can be reproduced exactly, even after the model is retrained — critical for
regulatory audits and malpractice defense.
</div>
""", unsafe_allow_html=True)
