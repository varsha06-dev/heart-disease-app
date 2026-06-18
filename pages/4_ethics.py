import streamlit as st

st.set_page_config(page_title="Ethics & Fairness · CardioSense", page_icon="⚖️", layout="wide")

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
.card h4{font-weight:600;font-size:0.9rem;color:#1A1A2E;margin:0.8rem 0 0.3rem;}
.card p,.card li{font-size:0.87rem;color:#4A4A5A;line-height:1.7;}
.card ul{padding-left:1.2rem;margin:0.4rem 0;}
.badge{display:inline-block;border-radius:6px;padding:0.2rem 0.65rem;font-size:0.72rem;font-weight:600;margin-right:0.3rem;margin-bottom:0.3rem;}
.badge-red{background:#FDECEA;color:#C0392B;}
.badge-green{background:#E8F5E9;color:#1B5E20;}
.badge-blue{background:#EBF5FB;color:#1A5276;}
.badge-amber{background:#FFF3E0;color:#784212;}
.badge-gray{background:#F2F3F4;color:#4A4A5A;}
.badge-purple{background:#F5EEF8;color:#6C3483;}
.principle-row{display:flex;gap:1rem;padding:1rem 0;border-bottom:1px solid #E8E4DC;align-items:flex-start;}
.principle-row:last-child{border-bottom:none;}
.principle-icon{font-size:1.4rem;flex-shrink:0;margin-top:0.1rem;}
.principle-body h4{font-weight:600;font-size:0.9rem;color:#1A1A2E;margin-bottom:0.3rem;}
.principle-body p{font-size:0.84rem;color:#4A4A5A;line-height:1.6;margin:0;}
.safeguard-grid{display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;}
.safeguard{background:#F7F5F2;border-radius:8px;padding:0.9rem 1rem;border:1px solid #E8E4DC;}
.safeguard h5{font-weight:600;font-size:0.82rem;color:#1A1A2E;margin-bottom:0.3rem;}
.safeguard p{font-size:0.78rem;color:#6B6B7B;line-height:1.5;margin:0;}
.fda-step{background:white;border-radius:8px;padding:0.9rem 1rem;border:1px solid #E8E4DC;margin-bottom:0.6rem;display:flex;gap:0.8rem;align-items:flex-start;}
.fda-num{background:#1A1A2E;color:white;border-radius:4px;padding:0.15rem 0.5rem;font-size:0.72rem;font-weight:700;flex-shrink:0;margin-top:0.15rem;font-family:'JetBrains Mono',monospace;}
.fda-content h5{font-weight:600;font-size:0.85rem;color:#1A1A2E;margin-bottom:0.2rem;}
.fda-content p{font-size:0.8rem;color:#6B6B7B;line-height:1.5;margin:0;}
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

st.markdown("<div class='hero-title'>Ethics,<br><em>Fairness & Compliance</em></div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>Bias mitigation, privacy, explainability, regulatory compliance, and accountability</div>", unsafe_allow_html=True)
st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Intro ─────────────────────────────────────────────────────────────────────
st.markdown("""
Medical AI carries a unique ethical burden. A model that performs well on average may
systematically underserve specific patient populations. A model that processes Protected
Health Information without proper safeguards creates legal exposure. A model deployed
without regulatory clearance can expose patients to harm and institutions to liability.
This section covers how each of these risks must be addressed before CardioSense could
move from a research prototype to clinical deployment.
""")

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── 1. Fairness & Bias ────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>01 / Fairness</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Bias Identification & Mitigation</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    <div class='card card-amber'>
    <h3>Sources of Bias in This Dataset</h3>
    <div class='principle-row'>
      <div class='principle-icon'>🏥</div>
      <div class='principle-body'><h4>Selection Bias</h4>
      <p>The UCI dataset was collected at hospital cardiology departments. Patients who seek
      cardiac care skew older, more symptomatic, and more likely to have healthcare access.
      The model may underperform on younger patients or those with atypical presentations
      who would be less represented in training data.</p></div>
    </div>
    <div class='principle-row'>
      <div class='principle-icon'>📐</div>
      <div class='principle-body'><h4>Measurement Bias</h4>
      <p>Different clinical facilities measure and record values differently. Cholesterol
      testing protocols vary. ECG interpretation can differ between technicians. These
      variations aren't captured in the dataset and can cause systematic errors when
      the model is applied to new settings.</p></div>
    </div>
    <div class='principle-row'>
      <div class='principle-icon'>📜</div>
      <div class='principle-body'><h4>Historical Bias</h4>
      <p>Historical diagnostic patterns reflect prior inequities in healthcare. If certain
      groups were historically underdiagnosed, the training labels themselves may encode
      systemic bias — the model learns to replicate past diagnostic patterns, not ground truth.</p></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card card-green'>
    <h3>Mitigation Strategies</h3>
    <div class='principle-row'>
      <div class='principle-icon'>📊</div>
      <div class='principle-body'><h4>Stratified Validation</h4>
      <p>Before deployment, evaluate model performance separately for: age groups (under 50,
      50–65, over 65), sex (male/female), and any available ethnicity data. A model that
      achieves 99% overall recall but 85% recall for women would not be acceptable.</p></div>
    </div>
    <div class='principle-row'>
      <div class='principle-icon'>🔢</div>
      <div class='principle-body'><h4>Fairness Metrics</h4>
      <p>Compute <strong>Disparate Impact Ratio</strong> (DI) across subgroups. A DI below 0.8
      for any group triggers mandatory review. Track both FNR (missed diagnoses) and FPR
      (unnecessary tests) per subgroup — these can diverge in ways overall accuracy hides.</p></div>
    </div>
    <div class='principle-row'>
      <div class='principle-icon'>🔄</div>
      <div class='principle-body'><h4>Ongoing Auditing</h4>
      <p>Quarterly fairness reports generated automatically from logged predictions.
      Any subgroup with FNR exceeding the overall FNR by more than 10 percentage points
      triggers a model review cycle and potential retraining with reweighted samples.</p></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── 2. Privacy ────────────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>02 / Privacy</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>HIPAA Compliance & Data Security</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")
with col1:
    st.markdown("""
    <div class='card card-blue'>
    <h3>🔒 Technical Safeguards</h3>
    <ul>
      <li><strong>AES-256</strong> encryption for all data at rest in the model store, feature database, and audit logs</li>
      <li><strong>TLS 1.3</strong> for all data in transit between services</li>
      <li><strong>RBAC</strong> (Role-Based Access Control) — clinicians see patient predictions, IT staff see operational metrics, neither sees the other's data</li>
      <li><strong>MFA</strong> (Multi-Factor Authentication) required for all system access</li>
      <li>PHI hashed in audit logs — prediction IDs are traceable by authorized staff only</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class='card card-purple'>
    <h3>📋 Administrative Safeguards</h3>
    <ul>
      <li><strong>Data Use Agreements</strong> with all hospitals governing training data use, model outputs, and patient notification</li>
      <li><strong>Mandatory HIPAA training</strong> for all personnel with system access — renewed annually</li>
      <li><strong>Incident Response Plan</strong> — documented breach notification procedure (72-hour report to HHS under HIPAA)</li>
      <li>Designated HIPAA Privacy Officer responsible for ongoing compliance</li>
      <li>Data retention policy: prediction logs deleted after 7 years (standard medical record retention)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class='card card-dark'>
    <h3>🏗️ Infrastructure Safeguards</h3>
    <ul>
      <li>Deployed on <strong>HIPAA Business Associate Agreement (BAA)-eligible</strong> cloud infrastructure (AWS, Azure, or GCP all offer this)</li>
      <li>Geographically redundant encrypted backups — RPO &lt;1 hour, RTO &lt;4 hours</li>
      <li><strong>PHI minimization:</strong> the model uses only the 13 clinical features needed for prediction — no names, addresses, or identifiers are stored with predictions</li>
      <li>Network isolation — prediction API is not publicly exposed; accessible only from within hospital network or via VPN</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── 3. Explainability ────────────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>03 / Transparency</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Explainability & Clinical Trust</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    XGBoost is a powerful model, but it is not inherently interpretable. Clinicians cannot
    trust a black-box prediction that says "high risk" with no explanation. Two approaches
    are essential for clinical deployment:

    **SHAP (SHapley Additive exPlanations)**

    SHAP decomposes each prediction into the contribution of each individual feature,
    grounded in cooperative game theory. For a patient predicted to be high-risk, a SHAP
    explanation might show:
    - `thal_2` (reversable defect): +0.35 contribution to disease probability
    - `ca` (1 vessel): +0.09 contribution
    - `thalach` (low heart rate): +0.06 contribution
    - `exang` (no exercise angina): -0.04 contribution

    This gives clinicians a specific, feature-level rationale they can cross-check
    against their own clinical assessment. If the model's top features don't match
    clinical intuition, that discrepancy is itself diagnostically valuable.
    """)
with c2:
    st.markdown("""
    **Decision Support, Not Decision Replacement**

    A critical design principle: the model's output is a **risk score, not a diagnosis**.

    - Predictions are displayed as probability scores with a LOW / MODERATE / HIGH
      category — not binary "has disease" / "doesn't have disease"
    - Clinicians can always override the model with documentation — the override rate
      is itself tracked as a signal of model confidence and clinical alignment
    - Confidence thresholds: predictions with probability between 40–60% are
      automatically flagged as "low confidence — manual review required"
    - The system is configured to err toward over-referral rather than under-referral

    **Informed Consent**
    - Patients are informed that AI assists in their diagnostic workup
    - Opt-out option available — patients can request non-AI-assisted diagnosis
    - Patients are entitled to a plain-language explanation of why the model
      flagged their case, on request
    """)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── 4. Regulatory ────────────────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>04 / Regulation</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>FDA & Clinical Validation Requirements</div>", unsafe_allow_html=True)

c1, c2 = st.columns([3,2], gap="large")
with c1:
    st.markdown("""
    **Software as a Medical Device (SaMD)**

    CardioSense as described would likely be classified as a **Software as a Medical Device**
    under FDA guidance, because it provides information used to support clinical decisions
    for a serious condition. This has significant regulatory implications:

    - **FDA 510(k) or De Novo pathway** would likely be required before commercial deployment
    - The intended use statement must be precise: "decision support for cardiologists" vs.
      "patient-facing diagnostic tool" carry very different regulatory burdens
    - Post-market surveillance obligations would apply — performance must be monitored and
      adverse events reported
    """)
    st.markdown("""
    **Clinical Validation**

    A research notebook achieving 100% on a UCI dataset is not sufficient for clinical deployment.
    Regulatory-grade validation requires:
    """)
    for step in [
        ("01", "Multi-site prospective study", "Patients enrolled across multiple hospitals with diverse demographics — not just retrospective analysis of a public dataset."),
        ("02", "Comparator arm", "Model performance compared head-to-head against current standard of care (cardiologist assessment without AI support)."),
        ("03", "Primary endpoint: False Negative Rate", "Statistical power calculation to demonstrate non-inferiority to standard care on missed diagnosis rate."),
        ("04", "IRB approval", "Institutional Review Board approval required for any prospective clinical study involving patient data."),
        ("05", "Post-market surveillance plan", "Ongoing monitoring protocol submitted alongside FDA clearance application."),
    ]:
        st.markdown(f"""
        <div class='fda-step'>
          <div class='fda-num'>{step[0]}</div>
          <div class='fda-content'><h5>{step[1]}</h5><p>{step[2]}</p></div>
        </div>
        """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='card card-red'>
    <h3>Accountability Framework</h3>
    <h4>Who is responsible for what</h4>
    <div class='principle-row' style='padding:0.6rem 0;'>
      <div class='principle-icon'>👨‍⚕️</div>
      <div class='principle-body'><h4>Healthcare Provider</h4>
      <p>Ultimate responsibility for diagnosis and treatment. Cannot delegate clinical judgment to the model.</p></div>
    </div>
    <div class='principle-row' style='padding:0.6rem 0;'>
      <div class='principle-icon'>💻</div>
      <div class='principle-body'><h4>Model Developer</h4>
      <p>Responsible for model accuracy, bias mitigation, ongoing maintenance, and documentation of known limitations.</p></div>
    </div>
    <div class='principle-row' style='padding:0.6rem 0;'>
      <div class='principle-icon'>🏥</div>
      <div class='principle-body'><h4>Healthcare Institution</h4>
      <p>Responsible for proper integration, clinician training, and ensuring AI is used within its validated intended use.</p></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='card card-amber'>
    <h3>Error Handling Protocol</h3>
    <h4>False Negatives (most critical)</h4>
    <p>All negative predictions where the probability is above 30% are flagged for
    secondary clinical review. Patients with negative predictions but concerning symptoms
    receive follow-up testing regardless of model output.</p>
    <h4>False Positives</h4>
    <p>Confidence scores help clinicians assess reliability. Low-confidence positive
    predictions trigger confirmatory testing rather than immediate treatment decisions.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

st.markdown("""
<div style='background:#1A1A2E;border-radius:12px;padding:1.8rem 2rem;color:#E8E4DC;'>
<div style='font-size:0.7rem;font-weight:600;letter-spacing:0.14em;text-transform:uppercase;color:#A8A4B0;margin-bottom:0.5rem;'>Summary Principle</div>
<div style='font-family:DM Serif Display,serif;font-size:1.6rem;color:white;line-height:1.3;margin-bottom:0.8rem;'>
The model is a tool that serves clinicians.<br>Clinicians are the ones who serve patients.
</div>
<p style='font-size:0.88rem;color:#A8A4B0;line-height:1.6;margin:0;'>
No matter how high the accuracy metrics, a medical AI system earns clinical trust gradually —
through transparency about its limitations, rigorous fairness monitoring, robust privacy protections,
and the consistent humility to support rather than replace human judgment.
</p>
</div>
""", unsafe_allow_html=True)
