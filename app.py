"""
COMPREHENSIVE DRUG DESIGN & DEVELOPMENT PLATFORM
From Target Selection to Clinical Phases

For GM sir - Complete Drug Discovery Pipeline
"""
import streamlit as st
import pandas as pd
import requests
import webbrowser
from datetime import datetime

st.set_page_config(
    page_title="Drug Design & Development Platform",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with beautiful aesthetic dark theme
st.markdown("""
<style>
    /* Beautiful dark theme with purple/cyan accents */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --bg-primary: #0f0f1a;
        --bg-secondary: #1a1a2e;
        --bg-card: #16213e;
        --bg-card-hover: #1f2b4d;
        --accent-1: #e94560;
        --accent-2: #0f3460;
        --accent-3: #00d9ff;
        --accent-4: #a855f7;
        --text-primary: #f8fafc;
        --text-secondary: #94a3b8;
        --text-muted: #64748b;
        --border-color: #2d3748;
        --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        --gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        --gradient-5: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    }
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: var(--bg-primary);
        color: var(--text-primary);
    }
    
    /* Headers */
    .main-header {
        background: var(--gradient-1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        padding: 1.5rem 0;
        letter-spacing: -0.02em;
    }
    
    .section-header {
        color: var(--accent-3);
        font-size: 1.5rem;
        font-weight: 600;
        padding: 1rem 0;
        border-bottom: 2px solid var(--accent-3);
        margin-bottom: 1rem;
    }
    
    /* Cards */
    .module-card {
        background: var(--bg-card);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.75rem 0;
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    
    .module-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,217,255,0.15);
        border-color: var(--accent-3);
    }
    
    .tool-card {
        background: linear-gradient(145deg, #1a1a2e, #252542);
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid;
        border-image: var(--gradient-3) 1;
        transition: all 0.3s ease;
    }
    
    .tool-card:hover {
        background: linear-gradient(145deg, #252542, #2d2d4a);
        transform: translateX(5px);
    }
    
    .db-card {
        background: var(--bg-secondary);
        border-radius: 10px;
        padding: 0.75rem 1rem;
        margin: 0.3rem 0;
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
    }
    
    .db-card:hover {
        background: var(--accent-2);
        border-color: var(--accent-4);
    }
    
    .stage-card {
        background: linear-gradient(145deg, var(--bg-card), var(--accent-2));
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid var(--accent-4);
        box-shadow: 0 10px 40px rgba(168,85,247,0.1);
    }
    
    .pipeline-step {
        background: var(--bg-secondary);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        border-left: 4px solid var(--accent-3);
        transition: all 0.3s ease;
    }
    
    .pipeline-step:hover {
        background: var(--accent-2);
        border-left-color: var(--accent-1);
    }
    
    .step-number {
        background: var(--gradient-1);
        color: white;
        font-weight: 700;
        padding: 0.4rem 1rem;
        border-radius: 50%;
        display: inline-block;
        margin-right: 0.75rem;
        box-shadow: 0 4px 15px rgba(102,126,234,0.4);
    }
    
    .status-badge {
        background: var(--gradient-4);
        color: #0f172a;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .category-badge {
        background: var(--gradient-5);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    
    .reference-link {
        color: var(--accent-3);
        text-decoration: none;
        padding: 0.3rem 0.8rem;
        border-radius: 8px;
        background: rgba(0,217,255,0.1);
        transition: all 0.3s ease;
    }
    
    .reference-link:hover {
        background: rgba(0,217,255,0.2);
        color: white;
    }
    
    .big-metric {
        font-size: 2.5rem;
        font-weight: 700;
        background: var(--gradient-3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .metric-label {
        color: var(--text-secondary);
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .divider {
        border-top: 2px solid var(--accent-4);
        margin: 1.5rem 0;
    }
    
    /* Sidebar styling */
    .stSidebar {
        background: var(--bg-secondary) !important;
        border-right: 1px solid var(--border-color);
    }
    
    .stSidebar .stRadio > label {
        color: var(--text-primary);
        font-weight: 500;
    }
    
    /* Button styling */
    .stButton > button {
        background: var(--gradient-1);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102,126,234,0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102,126,234,0.4);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: var(--bg-card);
        border-radius: 10px;
        color: var(--text-primary);
    }
    
    /* Table styling */
    .dataframe {
        background: var(--bg-card) !important;
        border-radius: 12px;
    }
    
    /* Metrics */
    div[data-testid="stMetric"] {
        background: var(--bg-card);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid var(--border-color);
    }
    
    /* Links */
    a {
        color: var(--accent-3);
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    a:hover {
        color: var(--accent-4);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: var(--bg-secondary);
        border-radius: 12px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        color: var(--text-secondary);
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--gradient-1);
        color: white;
    }
    
    /* Success/Info boxes */
    .success-box {
        background: linear-gradient(145deg, rgba(67,233,123,0.1), rgba(56,249,215,0.1));
        border: 1px solid #43e97b;
        border-radius: 12px;
        padding: 1rem;
    }
    
    .info-box {
        background: linear-gradient(145deg, rgba(0,217,255,0.1), rgba(168,85,247,0.1));
        border: 1px solid var(--accent-3);
        border-radius: 12px;
        padding: 1rem;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--bg-primary);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--accent-2);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: var(--accent-3);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: var(--text-muted);
        border-top: 1px solid var(--border-color);
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🧬 DRUG DESIGN & DEVELOPMENT PLATFORM</h1>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding: 0.5rem 0;">
    <span style="background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 1.1rem;">
        From Target Selection → Clinical Trials → Approval → Post-Marketing
    </span>
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# Import drug discovery engine
from drug_discovery_engine import *

# Sidebar - Pipeline Navigation
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem;">
    <h2 style="background: linear-gradient(135deg, #e94560, #a855f7); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🎯 PIPELINE STAGES</h2>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("---")

pipeline_stages = [
    "1️⃣ Target Selection",
    "2️⃣ Target Validation",
    "3️⃣ Hit Identification",
    "4️⃣ Lead Optimization",
    "5️⃣ Preclinical Dev",
    "6️⃣ Phase I Trials",
    "7️⃣ Phase II Trials",
    "8️⃣ Phase III Trials",
    "9️⃣ Approval & Launch",
    "🔄 Phase IV Monitoring",
]

selected_stage = st.sidebar.radio("Select Stage:", pipeline_stages)

# Quick links in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="padding: 1rem; background: linear-gradient(145deg, #1a1a2e, #252542); border-radius: 12px; margin-top: 1rem;">
    <h4 style="color: #00d9ff; margin-bottom: 0.75rem;">🔗 DATABASE LINKS</h4>
    <div style="display: grid; gap: 0.5rem;">
        <a href="https://www.ebi.ac.uk/chembl" target="_blank" style="color: #e94560;">📊 ChEMBL</a>
        <a href="https://pubchem.ncbi.nlm.nih.gov" target="_blank" style="color: #a855f7;">🧪 PubChem</a>
        <a href="https://www.drugbank.ca" target="_blank" style="color: #43e97b;">💊 DrugBank</a>
        <a href="https://www.rcsb.org" target="_blank" style="color: #4facfe;">🧬 PDB</a>
        <a href="https://alphafold.ebi.ac.uk" target="_blank" style="color: #fee140;">🔮 AlphaFold</a>
        <a href="https://clinicaltrials.gov" target="_blank" style="color: #fa709a;">🏥 ClinicalTrials</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# STAGE 1: TARGET SELECTION
# ============================================
if selected_stage == "1️⃣ Target Selection":
    st.markdown("## 🎯 STAGE 1: TARGET IDENTIFICATION & SELECTION", unsafe_allow_html=False)
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🧬 Protein Target Classes")
        for cls, proteins in PROTEIN_CLASSES.items():
            with st.expander(f"**{cls}** ({len(proteins)} types)"):
                for prot in proteins:
                    st.markdown(f"- {prot}")
    
    with col2:
        st.markdown("### 🦠 Disease Pathways")
        for disease, pathways in list(DISEASE_PATHWAYS.items())[:5]:
            with st.expander(f"**{disease}**"):
                for pathway in pathways:
                    st.markdown(f"- {pathway}")
    
    with col3:
        st.markdown("### 🗄️ Target Databases")
        for db, url in TARGET_DATABASES.items():
            st.markdown(f"""
            <div class="db-card">
                <a href="{url}" target="_blank" style="color: #00d9ff;">{db}</a>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔬 Target Selection Criteria")
    st.markdown("""
    <div class="info-box">
    | Criterion | Description |
    |------------|-------------|
    | **Druggability** | Protein class, binding site, expression |
    | **Disease relevance** | Genetic evidence, pathway role |
    | **Safety** | Tissue distribution, off-target potential |
    | **Assay feasibility** | Developability, screening capability |
    | **IP landscape** | Patent freedom to operate |
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🛠️ Computational Tools for Target Selection")
    
    tool_col1, tool_col2 = st.columns(2)
    
    with tool_col1:
        st.markdown("#### 📊 Structure Prediction")
        st.markdown("""
        - **AlphaFold2** - DeepMind's protein structure prediction
        - **RoseTTAFold** - Baker lab's version
        - **ESMFold** - Meta's evolution-scale modeling
        - **I-TASSER** - Iterative threading
        - **SWISS-MODEL** - Homology modeling
        """)
        
        st.markdown("#### 🔗 Network Analysis")
        st.markdown("""
        - **STRING** - Protein-protein interactions
        - **BioGRID** - Genetic/protein interactions
        - **IntAct** - Molecular interaction data
        - **Cytoscape** - Network visualization
        """)
    
    with tool_col2:
        st.markdown("#### 📈 Expression & Disease")
        st.markdown("""
        - **GTEx** - Gene expression atlas
        - **TCGA** - Cancer genomics atlas
        - **OpenTargets** - Disease associations
        - **DisGeNET** - Disease-gene associations
        - **CTD** - Comparative toxicogenomics
        """)
        
        st.markdown("#### 🧪 Cheminformatics")
        st.markdown("""
        - **RDKit** - Molecular fingerprints, descriptors
        - **Open Babel** - Format conversion
        - **PyMOL** - Molecular visualization
        - **Chimera** - UCSF visualization
        """)

# ============================================
# STAGE 2: TARGET VALIDATION
# ============================================
elif selected_stage == "2️⃣ Target Validation":
    st.markdown("## 🔬 STAGE 2: TARGET VALIDATION", unsafe_allow_html=False)
    st.markdown("---")
    
    st.markdown("### ✅ Validation Methods")
    
    method_col1, method_col2 = st.columns(2)
    
    with method_col1:
        st.markdown("#### 🧫 Genetic Manipulation")
        for method in TARGET_VALIDATION_METHODS[:4]:
            st.markdown(f"- {method}")
    
    with method_col2:
        st.markdown("#### 🐁 Model Systems")
        for method in TARGET_VALIDATION_METHODS[4:]:
            st.markdown(f"- {method}")
    
    st.markdown("---")
    st.markdown("### 📊 Validation Workflow")
    
    workflow_data = [
        {"Step": 1, "Method": "Bioinformatics analysis", "Tools": "GTEx, TCGA, OpenTargets", "Duration": "2-4 weeks"},
        {"Step": 2, "Method": "In silico knockdown", "Tools": "RNAi, CRISPR design", "Duration": "2-4 weeks"},
        {"Step": 3, "Method": "Cell-based validation", "Tools": "siRNA, CRISPR", "Duration": "4-8 weeks"},
        {"Step": 4, "Method": "Phenotypic assays", "Tools": "Disease models", "Duration": "8-12 weeks"},
        {"Step": 5, "Method": "Animal model", "Tools": "KO/KI mice", "Duration": "12-24 weeks"},
    ]
    
    df = pd.DataFrame(workflow_data)
    st.table(df)

# ============================================
# STAGE 3: HIT IDENTIFICATION
# ============================================
elif selected_stage == "3️⃣ Hit Identification":
    st.markdown("## 🎯 STAGE 3: HIT IDENTIFICATION", unsafe_allow_html=False)
    st.markdown("---")
    
    hit_col1, hit_col2 = st.columns(2)
    
    with hit_col1:
        st.markdown("### 🔍 Virtual Screening Methods")
        
        for category, methods in VIRTUAL_SCREENING_METHODS.items():
            with st.expander(f"**{category}**"):
                for method in methods:
                    st.markdown(f"- {method}")
    
    with hit_col2:
        st.markdown("### 🌿 Natural Product Sources")
        for source in NATURAL_PRODUCT_SOURCES[:8]:
            st.markdown(f"- {source}")
        
        st.markdown("### 📊 HTS Analysis")
        for analysis, desc in HTS_ANALYSIS.items():
            st.markdown(f"**{analysis}:** {desc}")
    
    st.markdown("---")
    st.markdown("### 🗄️ Screening Compound Databases")
    
    db_col1, db_col2, db_col3 = st.columns(3)
    
    with db_col1:
        st.markdown("""
        #### Commercial
        - ZINC (22M compounds)
        - Enamine (2M+ compounds)
        - ChemBridge (1M+ compounds)
        - Maybridge (53K compounds)
        - ASDC (4M+ compounds)
        """)
    
    with db_col2:
        st.markdown("""
        #### Free/Academic
        - ChEMBL (2M compounds)
        - PubChem (110M+ compounds)
        - eDrugPortal (200K+)
        - SuperDrug2 (3000)
        - DrugBank (13K drugs)
        """)
    
    with db_col3:
        st.markdown("""
        #### Focused Libraries
        - Fragment library (1000-5000)
        - Kinase inhibitor library
        - GPCR library
        - Ion channel library
        - Epigenetic library
        """)

# ============================================
# STAGE 4: LEAD OPTIMIZATION
# ============================================
elif selected_stage == "4️⃣ Lead Optimization":
    st.markdown("## ⚗️ STAGE 4: LEAD OPTIMIZATION", unsafe_allow_html=False)
    st.markdown("---")
    
    lo_col1, lo_col2 = st.columns(2)
    
    with lo_col1:
        st.markdown("### 📈 SAR Analysis Tools")
        for tool in SAR_ANALYSIS_TOOLS:
            st.markdown(f"- {tool}")
        
        st.markdown("### 🔄 Bioisostere Replacements")
        for category, pairs in BIOISOSTERE_REPLACEMENTS.items():
            with st.expander(f"**{category}**"):
                for original, replacement in pairs:
                    st.markdown(f"- {original} → {replacement}")
    
    with lo_col2:
        st.markdown("### 🧪 ADMET Properties")
        for property_cat, tests in ADMET_PROPERTIES.items():
            with st.expander(f"**{property_cat}**"):
                for test in tests:
                    st.markdown(f"- {test}")
        
        st.markdown("### 🎯 Property Targets")
        for rule, values in PROPERTY_TARGETS.items():
            with st.expander(f"**{rule}**"):
                for param, val in values.items():
                    st.markdown(f"- {param}: {val}")
    
    st.markdown("---")
    st.markdown("### 🛠️ Molecular Docking Tools")
    
    dock_col1, dock_col2 = st.columns(2)
    
    with dock_col1:
        st.markdown("""
        #### Structure-Based
        - **AutoDock Vina** - Fast, open-source
        - **Glide** - High accuracy (Schrödinger)
        - **GOLD** - Flexible docking
        - **PLANTS** - PLP-based scoring
        - **Dock6** - Amber scoring
        """)
    
    with dock_col2:
        st.markdown("""
        #### Ligand-Based
        - **ROCS** - Shape-based
        - **Phase** - Pharmacophore
        - **Catalyst** - Pharmacophore
        - **Molecular fingerprints** - Tanimoto similarity
        - **GNN-based** - Deep learning
        """)
    
    st.markdown("---")
    st.markdown("### 🧬 Retrosynthesis Tools")
    st.markdown("""
    <div class="success-box">
    | Tool | Type | Accuracy | Availability |
    |------|------|----------|--------------|
    | **IBM RXN** | AI Cloud | ~85% | Commercial |
    | **ASKCos** | AI Local | ~80% | Free/Open |
    | **ChemAI** | AI Cloud | ~75% | Commercial |
    | **NeuMMA** | AI Cloud | ~78% | Commercial |
    | **RDChiral** | Rule-based | ~60% | Free/Open |
    </div>
    """, unsafe_allow_html=True)

# ============================================
# STAGE 5: PRECLINICAL DEVELOPMENT
# ============================================
elif selected_stage == "5️⃣ Preclinical Dev":
    st.markdown("## 🐁 STAGE 5: PRECLINICAL DEVELOPMENT", unsafe_allow_html=False)
    st.markdown("---")
    
    pre_col1, pre_col2 = st.columns(2)
    
    with pre_col1:
        st.markdown("### 🧫 In Vitro Assays")
        for category, assays in IN_VITRO_ASSAYS.items():
            with st.expander(f"**{category}**"):
                for assay in assays:
                    st.markdown(f"- {assay}")
        
        st.markdown("### 🔬 Toxicology Prediction")
        for category, tools in TOXICOLOGY_PREDICTION.items():
            with st.expander(f"**{category}**"):
                for tool in tools:
                    st.markdown(f"- {tool}")
    
    with pre_col2:
        st.markdown("### 🐀 In Vivo Models")
        for disease, models in IN_VIVO_MODELS.items():
            with st.expander(f"**{disease}**"):
                for model in models:
                    st.markdown(f"- {model}")
        
        st.markdown("### 📊 PK/PD Modeling")
        for param_cat, params in PKPD_MODELING.items():
            with st.expander(f"**{param_cat}**"):
                for param in params:
                    st.markdown(f"- {param}")
    
    st.markdown("---")
    st.markdown("### 📈 IND-Enabling Studies Timeline")
    st.markdown("""
    <div class="info-box">
    | Study | Duration | Purpose |
    |-------|----------|---------|
    | In vitro pharmacology | 3-6 months | Mechanism, selectivity |
    | PK/ADME | 6-9 months | Absorption, metabolism |
    | Safety pharmacology | 3-6 months | Core battery |
    | Genetic toxicology | 3-6 months | Ames, micronucleus |
    | 28-day toxicology | 3-4 months | Dose-range finding |
    | 90-day toxicology | 4-6 months | GLP toxicology |
    | CMC | 6-12 months | Formulation, manufacturing |
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PHASE I CLINICAL TRIALS
# ============================================
elif selected_stage == "6️⃣ Phase I Trials":
    st.markdown("## 🏥 STAGE 6: PHASE I CLINICAL TRIALS", unsafe_allow_html=False)
    st.markdown("---")
    
    p1_col1, p1_col2 = st.columns(2)
    
    with p1_col1:
        st.markdown("""
        <div class="stage-card">
        ### 📋 Phase I Overview
        **Purpose:** Safety, tolerability, PK/PD
        
        **Population:** 20-100 healthy volunteers
        
        **Duration:** 6-12 months
        
        **Primary Endpoints:**
        - Dose-limiting toxicity (DLT)
        - Maximum tolerated dose (MTD)
        - Adverse events (AEs)
        - Serious adverse events (SAEs)
        </div>
        """, unsafe_allow_html=True)
    
    with p1_col2:
        st.markdown("""
        <div class="stage-card">
        ### 🧪 Phase I Study Designs
        
        **Single ascending dose (SAD)**
        - Cohort 1: 1 subject active, 1 placebo
        - Escalate dose until MTD
        
        **Multiple ascending dose (MAD)**
        - 7-14 days dosing
        - Assess accumulation
        
        **Food effect**
        - Fed vs fasted
        - Drug-drug interaction
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 First-in-Human Dose Calculation")
    st.markdown("""
    <div class="success-box">
    | Method | Description |
    |--------|-------------|
    | **Allometric scaling** | Scale from animal PK |
    | **Pharmacodynamic** | Based on animal efficacy |
    | **Safety** | 1/10 to 1/100 of NOAEL |
    | **MABEL** | Minimal anticipated biological effect level |
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PHASE II CLINICAL TRIALS
# ============================================
elif selected_stage == "7️⃣ Phase II Trials":
    st.markdown("## 🏥 STAGE 7: PHASE II CLINICAL TRIALS", unsafe_allow_html=False)
    st.markdown("---")
    
    p2_col1, p2_col2 = st.columns(2)
    
    with p2_col1:
        st.markdown("""
        <div class="stage-card">
        ### 📋 Phase II Overview
        **Purpose:** Efficacy, dose-finding
        
        **Population:** 100-500 patients
        
        **Duration:** 12-24 months
        
        **Primary Endpoints:**
        - Clinical response rate
        - Biomarker modulation
        - Optimal dose selection
        - Proof of concept (POC)
        </div>
        """, unsafe_allow_html=True)
    
    with p2_col2:
        st.markdown("""
        <div class="stage-card">
        ### 🎯 Phase II Study Designs
        
        **Randomized controlled trial (RCT)**
        - Drug vs placebo
        - 2:1 or 3:1 randomization
        
        **Dose-response**
        - Parallel groups
        - Dose-ranging
        
        **Adaptive designs**
        - Seamless Phase II/III
        - Simon 2-stage
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📈 Sample Size Calculation")
    st.markdown("""
    <div class="info-box">
    | Parameter | Typical Value |
    |-----------|--------------|
    | Alpha (Type I error) | 0.05 (two-sided) |
    | Power (1-beta) | 80-90% |
    | Expected response | 20-40% |
    | Minimum clinically meaningful | 10-15% |
    | Dropout rate | 15-20% |
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PHASE III CLINICAL TRIALS
# ============================================
elif selected_stage == "8️⃣ Phase III Trials":
    st.markdown("## 🏥 STAGE 8: PHASE III CLINICAL TRIALS", unsafe_allow_html=False)
    st.markdown("---")
    
    p3_col1, p3_col2 = st.columns(2)
    
    with p3_col1:
        st.markdown("""
        <div class="stage-card">
        ### 📋 Phase III Overview
        **Purpose:** Confirm efficacy, safety
        
        **Population:** 1000-5000 patients
        
        **Duration:** 24-48 months
        
        **Primary Endpoints:**
        - Clinical outcome
        - Overall survival (OS)
        - Progression-free survival (PFS)
        - Quality of life
        </div>
        """, unsafe_allow_html=True)
    
    with p3_col2:
        st.markdown("""
        <div class="stage-card">
        ### 🏆 Pivotal Trial Design
        
        **Required for NDA/BLA:**
        - Two independent pivotal studies
        - Statistically significant efficacy
        - Acceptable safety profile
        
        **Multi-regional trials (MRT)**
        - Global participation
        - Regulatory harmonization
        
        **Real-world evidence**
        - Post-marketing commitments
        - Registry studies
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 Regulatory Submission Checklist")
    st.markdown("""
    <div class="success-box">
    | Component | Description |
    |----------|-------------|
    | **CMC** | Manufacturing, quality control |
    | **Preclinical** | Pharmacology, toxicology |
    | **Clinical** | Phase I-III data |
    | **Statistical** | Efficacy, safety analysis |
    | **Labeling** | Prescribing information |
    | **Risk management** | REMS, EU-RMP |
    </div>
    """, unsafe_allow_html=True)

# ============================================
# APPROVAL & LAUNCH
# ============================================
elif selected_stage == "9️⃣ Approval & Launch":
    st.markdown("## ✅ STAGE 9: REGULATORY APPROVAL & LAUNCH", unsafe_allow_html=False)
    st.markdown("---")
    
    reg_col1, reg_col2 = st.columns(2)
    
    with reg_col1:
        st.markdown("""
        <div class="stage-card">
        ### 🏛️ Regulatory Agencies
        
        **Major:**
        - **FDA** (US) - 10 months priority, 12 months standard
        - **EMA** (EU) - 210 days
        
        **Other:**
        - **PMDA** (Japan)
        - **Health Canada**
        - **TGA** (Australia)
        - **CDSCO** (India)
        - **NMPA** (China)
        </div>
        """, unsafe_allow_html=True)
    
    with reg_col2:
        st.markdown("""
        <div class="stage-card">
        ### 📋 Submission Components
        
        **NDA/BLA:**
        - Executive summary
        - Quality (CMC)
        - Nonclinical pharmacology
        - Clinical pharmacology
        - Clinical efficacy
        - Clinical safety
        - Post-marketing risk management
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🚀 Launch Preparation")
    st.markdown("""
    <div class="info-box">
    | Activity | Timeline |
    |----------|----------|
    | Market research | 6-12 months pre-launch |
    | Medical affairs setup | 6 months pre-launch |
    | Sales force training | 3 months pre-launch |
    | Distribution logistics | 3 months pre-launch |
    | Reimbursement/Payer strategy | Ongoing |
    | Phase IV commitments | Post-launch |
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PHASE IV MONITORING
# ============================================
elif selected_stage == "🔄 Phase IV Monitoring":
    st.markdown("## 📊 STAGE 10: PHASE IV POST-MARKETING", unsafe_allow_html=False)
    st.markdown("---")
    
    pv_col1, pv_col2 = st.columns(2)
    
    with pv_col1:
        st.markdown("""
        <div class="stage-card">
        ### 👁️ Pharmacovigilance
        
        **Spontaneous reporting:**
        - FAERS (FDA)
        - EudraVigilance (EU)
        - VigiBase (WHO)
        
        **Active surveillance:**
        - Sentinel system
        - Mini-Sentinel
        - Real-world evidence
        
        **Risk management:**
        - REMS (Risk Evaluation Mitigation Strategy)
        - EU-RMP
        - Post-authorization safety study (PASS)
        </div>
        """, unsafe_allow_html=True)
    
    with pv_col2:
        st.markdown("""
        <div class="stage-card">
        ### 📈 Real-World Evidence
        
        **Data sources:**
        - Electronic health records (EHR)
        - Claims databases
        - Disease registries
        - Patient-reported outcomes
        
        **Analytics:**
        - Active surveillance
        - Comparative effectiveness
        - Safety signal detection
        - Drug-drug interactions
        
        **Outcomes research:**
        - Quality of life
        - Economic burden
        - Treatment patterns
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔬 New Indications")
    st.markdown("""
    <div class="success-box">
    **Post-marketing research can lead to:**
    - New disease indications
    - Pediatric populations
    - Combination therapies
    - Line extension (new formulations)
    - Adjuvant/neoadjuvant use
    - Breakthrough therapy designation
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <p style="font-size: 1.2rem;">🧬 <strong>Comprehensive Drug Design & Development Platform</strong></p>
    <p style="font-size: 0.9rem;">From Target Selection → Clinical Trials → Approval → Post-Marketing</p>
    <p style="font-size: 0.75rem; color: #64748b;">For GM sir | Data from ChEMBL, PubChem, DrugBank, FDA, EMA, ClinicalTrials.gov</p>
</div>
""", unsafe_allow_html=True)