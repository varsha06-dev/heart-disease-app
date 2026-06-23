## Project Description

**CardioSense** is a full-stack machine learning capstone project that predicts the likelihood of heart disease in a patient based on 13 clinical features. Built on the UCI Heart Disease dataset (1,025 patient records), the project covers the complete ML lifecycle — from raw data exploration through production deployment simulation — and presents all findings through a polished, multi-page web application.

The core product is an XGBoost binary classifier that takes patient vitals, lab results, and diagnostic test data as input and outputs a structured risk assessment (LOW / MODERATE / HIGH) with a calibrated disease probability score. The app is designed as a clinical decision-support tool: it assists cardiologists rather than replacing them, with explainability, auditability, and regulatory compliance built into the architecture from the start.

---

## Tech Stack

**Machine Learning & Data**
- Python 3.12
- XGBoost — final production model (gradient boosted trees)
- Scikit-learn — Logistic Regression, Random Forest, preprocessing pipeline (StandardScaler, train/test split, cross-validation)
- Pandas & NumPy — data cleaning, feature engineering, outlier handling
- Joblib — model serialization and deployment artifact management

**Web Application**
- Streamlit — multi-page web app framework
- Custom CSS with Google Fonts (DM Serif Display, Inter, JetBrains Mono) — full visual design system built from scratch

**Development Environment**
- Google Colab — model development, EDA, training, and deployment simulation
- JSON — structured API response format for the production deployment simulation

---

## Key Features

**Data Processing Pipeline**
- IQR-based outlier capping on resting blood pressure and max heart rate
- Log1p transformation on serum cholesterol to normalize right-skewed distribution
- Clipping of ST depression (oldpeak) to clinically valid range [0, 4.5]
- StandardScaler normalization of all five continuous features, fit on training data only to prevent leakage
- One-hot encoding of three categorical features (chest pain type, resting ECG, thalassemia)
- Full pipeline serialized to `final_heart_model.pkl` and reproduced identically at inference time

**Model Training & Evaluation**
- Three classifiers evaluated: Logistic Regression (baseline), Random Forest (ensemble), XGBoost (selected)
- 5-fold stratified cross-validation on all models
- Primary evaluation metric: Recall — minimizing false negatives (missed diagnoses) was the clinical priority
- XGBoost achieved 100% test accuracy, 100% recall, and 1.00 ROC-AUC with zero false negatives
- Cross-validation results (98.8% recall, ±0.9%) used as the realistic deployment performance estimate

**Deployment Simulation**
- Production `predict_patient_production()` function accepting raw patient dictionaries
- Structured JSON responses with prediction ID, timestamp, model version, risk category, probability, and top contributing features
- Four clinical test cases validated: high-risk, low-risk, moderate-risk, and a validation case from the actual test set

**Multi-Page Streamlit Application**
- **Home** — project overview, model comparison summary, navigation hub
- **Risk Predictor** — live patient input form (sliders and dropdowns for all 13 features), real-time XGBoost inference, color-coded risk card, probability bar, and a per-feature clinical flag breakdown (concern / borderline / normal)
- **Model Analysis** — tabbed deep-dive into all three classifiers covering methodology, strengths, weaknesses, and clinical suitability; full head-to-head metric table; discussion of perfect test scores and what they mean
- **Deployment Plan** — three-layer production architecture (presentation, application, data), offline training vs. online inference pipeline, monitoring strategy including drift detection and fairness auditing, scalability approach, and the actual API response format
- **Ethics & Fairness** — bias source identification (selection, measurement, historical), HIPAA compliance (technical, administrative, and infrastructure safeguards), SHAP-based explainability plan, FDA Software as a Medical Device classification, clinical validation requirements, and an accountability framework
