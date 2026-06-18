import streamlit as st

st.set_page_config(page_title="Model Analysis · CardioSense", page_icon="📊", layout="wide")

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
.card h3{font-family:'DM Serif Display',serif;font-size:1.2rem;color:#1A1A2E;margin-bottom:0.5rem;}
.card p,.card li{font-size:0.88rem;color:#4A4A5A;line-height:1.7;}
.card ul{padding-left:1.2rem;margin:0.5rem 0;}
.badge{display:inline-block;border-radius:6px;padding:0.2rem 0.65rem;font-size:0.72rem;font-weight:600;margin-right:0.3rem;margin-bottom:0.3rem;}
.badge-red{background:#FDECEA;color:#C0392B;}
.badge-green{background:#E8F5E9;color:#1B5E20;}
.badge-blue{background:#EBF5FB;color:#1A5276;}
.badge-amber{background:#FFF3E0;color:#784212;}
.badge-gray{background:#F2F3F4;color:#4A4A5A;}
.metric-big{font-family:'DM Serif Display',serif;font-size:2.8rem;color:#C0392B;line-height:1;}
.metric-label{font-size:0.75rem;color:#6B6B7B;text-transform:uppercase;letter-spacing:0.08em;margin-top:0.2rem;}
.cv-table{width:100%;border-collapse:collapse;font-size:0.84rem;}
.cv-table th{text-align:left;font-size:0.68rem;letter-spacing:0.1em;text-transform:uppercase;color:#9A9AA8;padding:0.5rem 0.7rem;border-bottom:2px solid #D9D5CE;}
.cv-table td{padding:0.6rem 0.7rem;border-bottom:1px solid #E8E4DC;color:#4A4A5A;font-family:'JetBrains Mono',monospace;font-size:0.8rem;}
.cv-table tr.best td{color:#1A1A2E;font-weight:600;background:#FEF9F9;}
.cv-table td:first-child{font-family:'Inter',sans-serif;font-weight:500;color:#1A1A2E;}
.winner-banner{background:linear-gradient(135deg,#1A1A2E 0%,#2C2C4A 100%);border-radius:12px;padding:2rem 2.2rem;color:#E8E4DC;margin-bottom:1.5rem;}
.winner-banner h2{font-family:'DM Serif Display',serif;font-size:2rem;color:white;margin-bottom:0.3rem;}
.winner-banner p{font-size:0.9rem;color:#A8A4B0;line-height:1.6;}
.winner-banner .accent{color:#E85D5D;}
.step-num{display:inline-block;background:#C0392B;color:white;border-radius:50%;width:24px;height:24px;text-align:center;line-height:24px;font-size:0.75rem;font-weight:700;margin-right:0.5rem;flex-shrink:0;}
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

st.markdown("<div class='hero-title'>Model<br><em>Analysis & Selection</em></div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>A rigorous comparison of three classifiers across performance, interpretability, and clinical suitability</div>", unsafe_allow_html=True)
st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Section 1: Why this problem needs careful model selection ──────────────────
st.markdown("<div class='section-eyebrow'>The Problem</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Why Model Selection Matters in Medical AI</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    In clinical settings, the cost of model errors is **asymmetric**. A false negative —
    telling a patient with heart disease that they're healthy — can be fatal. A false positive
    — flagging a healthy patient for further testing — causes anxiety and cost, but is
    recoverable.

    This asymmetry means we cannot simply optimize for accuracy. **Recall (sensitivity)**
    is the primary clinical metric: it measures how many actual disease cases the model catches.
    A model with 95% accuracy but 70% recall could miss 30% of real heart disease patients.

    The dataset used is the [UCI Heart Disease dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset):
    1,025 patient records, 13 clinical features, binary target (disease / no disease).
    After preprocessing, three fundamentally different model families were evaluated.
    """)
with c2:
    st.markdown("""
    <div style='background:white;border-radius:12px;padding:1.4rem 1.6rem;border:1px solid #E8E4DC;'>
        <div style='font-size:0.7rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:#9A9AA8;margin-bottom:1rem;'>Error Cost Analysis</div>
        <div style='margin-bottom:1rem;padding:0.8rem;background:#FDECEA;border-radius:8px;border-left:3px solid #C0392B;'>
            <div style='font-weight:600;font-size:0.88rem;color:#7B1010;'>False Negative (Worst case)</div>
            <div style='font-size:0.82rem;color:#4A4A5A;margin-top:0.3rem;'>Patient with heart disease classified as healthy. No follow-up. Potentially fatal.</div>
        </div>
        <div style='padding:0.8rem;background:#FFF8E1;border-radius:8px;border-left:3px solid #E67E22;'>
            <div style='font-weight:600;font-size:0.88rem;color:#784212;'>False Positive (Recoverable)</div>
            <div style='font-size:0.82rem;color:#4A4A5A;margin-top:0.3rem;'>Healthy patient flagged for testing. Causes anxiety and cost, but diagnosis corrected.</div>
        </div>
        <div style='margin-top:1rem;padding:0.8rem;background:#E8F5E9;border-radius:8px;border-left:3px solid #27AE60;'>
            <div style='font-weight:600;font-size:0.88rem;color:#1B5E20;'>Primary Goal</div>
            <div style='font-size:0.82rem;color:#4A4A5A;margin-top:0.3rem;'>Maximize Recall. Zero false negatives is the gold standard for this use case.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Section 2: The three models ────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Candidate Models</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Three Classifiers, Three Philosophies</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📈 Logistic Regression", "🌲 Random Forest", "⚡ XGBoost"])

with tab1:
    c1, c2 = st.columns([3,2], gap="large")
    with c1:
        st.markdown("#### What It Does")
        st.markdown("""
        Logistic Regression models the **log-odds of the positive class** as a linear combination
        of input features. It estimates a probability directly, making it naturally suited for
        binary classification. The decision boundary is always a hyperplane — straight in feature space.

        It was chosen as the **baseline model** because it is well-understood, fast, and its
        coefficients are directly interpretable as feature contributions to log-odds.
        """)
        st.markdown("#### Strengths")
        st.markdown("""
        - Coefficients directly show feature importance and direction
        - Outputs true probability estimates (useful for risk stratification)
        - Fast training — sub-second on this dataset
        - No hyperparameter tuning required
        - Minimal risk of overfitting with proper regularization
        - Works well on standardized, linearly separable features
        """)
        st.markdown("#### Weaknesses")
        st.markdown("""
        - Assumes linear relationship between features and log-odds — violated here
        - Cannot capture interactions between features without manual engineering
        - Sensitive to feature scaling (requires StandardScaler, already applied)
        - Underperforms when decision boundaries are complex
        """)
        st.markdown("#### Why It Falls Short for This Problem")
        st.markdown("""
        Heart disease risk involves **non-linear interactions**: a patient with both high CA
        (vessel narrowing) and low thalach (max heart rate) is disproportionately higher risk
        than either factor alone would suggest. Logistic Regression treats each feature's effect
        as additive and independent, missing these interactions entirely.

        The result: **9 false negatives** on the 205-sample test set — patients told they were
        healthy when they had heart disease. In a clinical deployment this would be unacceptable.
        """)
    with c2:
        st.markdown("#### Test Set Results")
        st.markdown("""
        <div style='background:white;border-radius:10px;padding:1.2rem;border:1px solid #E8E4DC;margin-bottom:1rem;'>
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;'>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#1A1A2E;'>84.9%</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>Accuracy</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#E67E22;'>91.4%</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>Recall</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#1A1A2E;'>0.93</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>ROC-AUC</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#C0392B;'>9</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>False Negatives</div></div>
        </div></div>
        """, unsafe_allow_html=True)
        st.markdown("#### CV Stability (5-Fold)")
        st.markdown("""
        <table class='cv-table'>
          <thead><tr><th>Metric</th><th>Mean</th><th>Std Dev</th></tr></thead>
          <tbody>
            <tr><td>Accuracy</td><td>0.851</td><td>±0.021</td></tr>
            <tr><td>Recall</td><td>0.886</td><td>±0.038</td></tr>
            <tr><td>ROC-AUC</td><td>0.928</td><td>±0.019</td></tr>
          </tbody>
        </table>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style='margin-top:1rem;padding:0.8rem 1rem;background:#FDECEA;border-radius:8px;font-size:0.82rem;color:#7B1010;border-left:3px solid #C0392B;'>
        <strong>Verdict:</strong> Solid baseline, acceptable stability, but the 9 false negatives
        make it unsuitable for clinical deployment without significant post-processing.
        </div>
        """, unsafe_allow_html=True)

with tab2:
    c1, c2 = st.columns([3,2], gap="large")
    with c1:
        st.markdown("#### What It Does")
        st.markdown("""
        Random Forest builds an **ensemble of decision trees**, each trained on a random
        bootstrap sample of the data and a random subset of features. Final predictions are
        made by majority vote. This bagging approach reduces variance dramatically compared
        to a single decision tree.

        Each tree independently partitions the feature space, capturing non-linear patterns
        and feature interactions that Logistic Regression cannot model. The ensemble averages
        out individual trees' errors.
        """)
        st.markdown("#### Strengths")
        st.markdown("""
        - Handles non-linear relationships and feature interactions naturally
        - Provides feature importance rankings from impurity reduction
        - Robust to outliers — individual trees vote, outliers can only affect a few
        - No feature scaling required (though scaling was applied)
        - Less prone to overfitting than single decision trees
        - Fast inference — trees are independent and parallelizable
        """)
        st.markdown("#### Weaknesses")
        st.markdown("""
        - Less interpretable than Logistic Regression ("black box" ensemble)
        - Requires hyperparameter tuning (n_estimators, max_depth, min_samples_split)
        - Can overfit on noisy datasets if trees are too deep
        - Memory-intensive — stores all trees simultaneously
        """)
        st.markdown("#### Why It's Strong But Not the Best")
        st.markdown("""
        Random Forest dramatically improved on Logistic Regression by capturing non-linear
        patterns. It achieved **zero false positives** (100% precision) — no healthy patients
        were incorrectly flagged. However, it still produced **2 false negatives**: two patients
        with heart disease were classified as healthy.

        In a clinical context with thousands of patients, 2 missed diagnoses per 205 cases
        represents a ~1% miss rate that is still clinically concerning. The model's bagging
        approach averages predictions — it can smooth over the subtle patterns in edge cases
        that gradient boosting iteratively corrects.
        """)
    with c2:
        st.markdown("#### Test Set Results")
        st.markdown("""
        <div style='background:white;border-radius:10px;padding:1.2rem;border:1px solid #E8E4DC;margin-bottom:1rem;'>
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;'>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#1A1A2E;'>99.0%</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>Accuracy</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#E67E22;'>98.1%</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>Recall</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#1A1A2E;'>0.99</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>ROC-AUC</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#E67E22;'>2</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>False Negatives</div></div>
        </div></div>
        """, unsafe_allow_html=True)
        st.markdown("#### CV Stability (5-Fold)")
        st.markdown("""
        <table class='cv-table'>
          <thead><tr><th>Metric</th><th>Mean</th><th>Std Dev</th></tr></thead>
          <tbody>
            <tr><td>Accuracy</td><td>0.987</td><td>±0.009</td></tr>
            <tr><td>Recall</td><td>0.983</td><td>±0.012</td></tr>
            <tr><td>ROC-AUC</td><td>0.998</td><td>±0.003</td></tr>
          </tbody>
        </table>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style='margin-top:1rem;padding:0.8rem 1rem;background:#FFF8E1;border-radius:8px;font-size:0.82rem;color:#784212;border-left:3px solid #E67E22;'>
        <strong>Verdict:</strong> Excellent performance and very low variance. The 2 false
        negatives keep it from being the clinical gold standard. Strong production candidate
        if XGBoost proves to overfit on new data.
        </div>
        """, unsafe_allow_html=True)

with tab3:
    c1, c2 = st.columns([3,2], gap="large")
    with c1:
        st.markdown("#### What It Does")
        st.markdown("""
        XGBoost (eXtreme Gradient Boosting) builds trees **sequentially**, where each tree
        is trained to correct the residual errors of all previous trees. Unlike Random Forest's
        parallel bagging, XGBoost uses **gradient descent in function space** — each new tree
        fits the gradient of the loss function with respect to the current ensemble's predictions.

        This iterative error-correction means XGBoost focuses disproportionate learning capacity
        on the hardest-to-classify examples — exactly the kind of borderline cases that produce
        false negatives in simpler models.
        """)
        st.markdown("#### Strengths")
        st.markdown("""
        - Iterative boosting catches errors that ensemble averaging misses
        - Built-in L1/L2 regularization prevents overfitting
        - Subsample and colsample parameters add controlled randomness
        - Feature importance via gain, coverage, and frequency metrics
        - Handles missing values natively
        - Highly competitive performance across tabular ML benchmarks
        """)
        st.markdown("#### Weaknesses")
        st.markdown("""
        - Requires careful hyperparameter tuning to avoid overfitting
        - Less interpretable without SHAP or LIME explanations
        - Slower training than Logistic Regression (though fast on this dataset)
        - Sequential nature means less parallelizable during training
        """)
        st.markdown("#### Why It Wins")
        st.markdown("""
        XGBoost's gradient boosting framework allowed it to **focus on the borderline patients**
        that Random Forest incorrectly classified. Where a forest of 100 independent trees
        votes and averages, XGBoost's 100 sequential trees each specifically reduce the
        errors left by the previous 99.

        The result was **zero false negatives** and **zero false positives** on the held-out
        test set — perfect recall and precision simultaneously. The 5-fold cross-validation
        confirmed this wasn't overfitting: CV recall of 98.81% with the lowest standard
        deviation of all three models indicates stable, generalizable performance.

        **Hyperparameters used:** n_estimators=100, max_depth=6, learning_rate=0.1,
        subsample=0.8, colsample_bytree=0.8. The subsampling parameters introduce
        controlled randomness that prevents the sequential trees from memorizing the training data.
        """)
    with c2:
        st.markdown("#### Test Set Results")
        st.markdown("""
        <div style='background:white;border-radius:10px;padding:1.2rem;border:1px solid #E8E4DC;margin-bottom:1rem;'>
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;'>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#27AE60;'>100%</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>Accuracy</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#27AE60;'>100%</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>Recall</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#27AE60;'>1.00</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>ROC-AUC</div></div>
          <div><div style='font-family:DM Serif Display,serif;font-size:2rem;color:#27AE60;'>0</div><div style='font-size:0.72rem;color:#9A9AA8;text-transform:uppercase;letter-spacing:0.08em;'>False Negatives</div></div>
        </div></div>
        """, unsafe_allow_html=True)
        st.markdown("#### CV Stability (5-Fold)")
        st.markdown("""
        <table class='cv-table'>
          <thead><tr><th>Metric</th><th>Mean</th><th>Std Dev</th></tr></thead>
          <tbody>
            <tr class='best'><td>Accuracy</td><td>0.994</td><td>±0.006</td></tr>
            <tr class='best'><td>Recall</td><td>0.988</td><td>±0.009</td></tr>
            <tr class='best'><td>ROC-AUC</td><td>0.999</td><td>±0.001</td></tr>
          </tbody>
        </table>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style='margin-top:1rem;padding:0.8rem 1rem;background:#E8F5E9;border-radius:8px;font-size:0.82rem;color:#1B5E20;border-left:3px solid #27AE60;'>
        <strong>Verdict:</strong> Best performance on all metrics with lowest variance.
        Zero false negatives on test set. Selected as the final production model.
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Section 3: Head-to-head comparison ────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Head to Head</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Full Metric Comparison</div>", unsafe_allow_html=True)

st.markdown("""
<table class='cv-table' style='margin-bottom:1.5rem;'>
  <thead>
    <tr>
      <th>Metric</th>
      <th>Logistic Regression</th>
      <th>Random Forest</th>
      <th>XGBoost ★</th>
      <th>Why it matters</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Test Accuracy</td><td>84.9%</td><td>99.0%</td><td style='color:#1A1A2E;font-weight:700;'>100%</td><td style='font-family:Inter,sans-serif;color:#6B6B7B;font-size:0.8rem;'>Overall correctness</td></tr>
    <tr><td>Test Recall</td><td>91.4%</td><td>98.1%</td><td style='color:#27AE60;font-weight:700;'>100%</td><td style='font-family:Inter,sans-serif;color:#C0392B;font-size:0.8rem;font-weight:600;'>← Primary clinical metric</td></tr>
    <tr><td>Test Precision</td><td>83.1%</td><td>100%</td><td style='color:#1A1A2E;font-weight:700;'>100%</td><td style='font-family:Inter,sans-serif;color:#6B6B7B;font-size:0.8rem;'>Avoids false alarms</td></tr>
    <tr><td>Test F1-Score</td><td>87.1%</td><td>99.0%</td><td style='color:#1A1A2E;font-weight:700;'>100%</td><td style='font-family:Inter,sans-serif;color:#6B6B7B;font-size:0.8rem;'>Precision-recall balance</td></tr>
    <tr><td>Test ROC-AUC</td><td>0.93</td><td>0.99</td><td style='color:#1A1A2E;font-weight:700;'>1.00</td><td style='font-family:Inter,sans-serif;color:#6B6B7B;font-size:0.8rem;'>Ranking quality</td></tr>
    <tr><td>False Negatives</td><td style='color:#C0392B;font-weight:600;'>9</td><td style='color:#E67E22;font-weight:600;'>2</td><td style='color:#27AE60;font-weight:700;'>0</td><td style='font-family:Inter,sans-serif;color:#C0392B;font-size:0.8rem;font-weight:600;'>← Missed diagnoses (critical)</td></tr>
    <tr><td>False Positives</td><td style='color:#E67E22;'>22</td><td style='color:#27AE60;'>0</td><td style='color:#27AE60;font-weight:700;'>0</td><td style='font-family:Inter,sans-serif;color:#6B6B7B;font-size:0.8rem;'>Unnecessary tests</td></tr>
    <tr><td>CV Accuracy (mean)</td><td>85.1%</td><td>98.7%</td><td style='color:#1A1A2E;font-weight:700;'>99.4%</td><td style='font-family:Inter,sans-serif;color:#6B6B7B;font-size:0.8rem;'>Generalization</td></tr>
    <tr><td>CV Accuracy (std)</td><td>±2.1%</td><td>±0.9%</td><td style='color:#27AE60;font-weight:700;'>±0.6%</td><td style='font-family:Inter,sans-serif;color:#6B6B7B;font-size:0.8rem;'>Stability (lower = better)</td></tr>
  </tbody>
</table>
""", unsafe_allow_html=True)

# ── Section 4: A note on perfect scores ───────────────────────────────────────
st.markdown("<hr class='rule'>", unsafe_allow_html=True)
st.markdown("<div class='section-eyebrow'>Important Caveat</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>On Perfect Test Set Scores</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    A 100% test set score should always prompt scrutiny — in real-world ML it is rare and
    sometimes indicates data leakage or dataset peculiarities. In this case, several factors
    explain the result:

    **Why XGBoost achieves 100% here:**
    - The UCI heart disease dataset is relatively small (1,025 rows) and well-curated
    - The 13 features are well-chosen clinical markers with high discriminative power
    - XGBoost's gradient boosting is particularly strong on structured tabular data
    - Cross-validation recall of 98.81% (not 100%) on training folds shows the test score
      reflects genuine strong performance, not memorization
    """)
with c2:
    st.markdown("""
    **What this means for deployment:**
    - The 5-fold CV score (~99.4% accuracy, ~98.8% recall) is the more realistic
      estimate of real-world performance on unseen patient data
    - On a larger, more diverse clinical dataset, some performance degradation is expected
    - Continuous monitoring of live prediction accuracy is essential
    - Retraining on hospital-specific data before deployment would be strongly recommended

    The cross-validation results — not the test set score — are what the deployment plan
    is based on. See the Deployment Plan page for monitoring strategy.
    """)

st.markdown("<hr class='rule'>", unsafe_allow_html=True)

# ── Section 5: KNN / SVM ──────────────────────────────────────────────────────
st.markdown("<div class='section-eyebrow'>Also Considered</div>", unsafe_allow_html=True)
st.markdown("<div class='section-heading'>Models Not Selected & Why</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="large")
with c1:
    st.markdown("""
    <div class='card card-amber'>
    <h3>K-Nearest Neighbors (KNN)</h3>
    <p><strong>How it works:</strong> Classifies each point by the majority label of its k nearest
    neighbors in feature space. No explicit training phase — all computation happens at inference time.</p>
    <p><strong>Why not selected:</strong> With 13 features, KNN suffers from the
    <em>curse of dimensionality</em> — distances become increasingly uniform in high-dimensional
    space, reducing discriminative power. Prediction is also slow (must compute distances to all
    training points) and the optimal k requires tuning.</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class='card card-blue'>
    <h3>Support Vector Machine (SVM)</h3>
    <p><strong>How it works:</strong> Finds the maximum-margin hyperplane separating classes.
    With an RBF kernel, can learn non-linear boundaries by projecting data to higher-dimensional
    space.</p>
    <p><strong>Why not selected:</strong> While SVM would likely perform well on this dataset,
    it offers less interpretability than tree-based models (no feature importances), is
    computationally expensive to tune (grid search over C and gamma), and provides no probability
    calibration by default — a significant limitation for medical risk scoring.</p>
    </div>
    """, unsafe_allow_html=True)
