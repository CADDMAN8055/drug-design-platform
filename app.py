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

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0a1628 0%, #1a2744 100%); }
    .main-header { color: #00d4ff; font-size: 2.5rem; font-weight: bold; text-align: center; }
    .section-header { color: #00ff88; font-size: 1.5rem; font-weight: bold; padding: 1rem 0; }
    .module-card { background: rgba(0,212,255,0.1); border-radius: 15px; padding: 1.5rem; margin: 0.75rem 0; border-left: 4px solid #00d4ff; }
    .tool-card { background: rgba(255,165,0,0.1); border-radius: 10px; padding: 1rem; margin: 0.5rem 0; border-left: 3px solid #ffa500; }
    .db-card { background: rgba(138,43,226,0.1); border-radius: 10px; padding: 0.75rem; margin: 0.3rem 0; border-left: 3px solid #8a2be2; }
    .stage-card { background: linear-gradient(135deg, rgba(0,255,136,0.1), rgba(0,212,255,0.1)); border-radius: 15px; padding: 1.5rem; margin: 1rem 0; border: 1px solid #00ff88; }
    .pipeline-step { background: rgba(255,255,255,0.05); border-radius: 10px; padding: 1rem; margin: 0.5rem 0; }
    .step-number { background: #00d4ff; color: #0a1628; font-weight: bold; padding: 0.3rem 0.8rem; border-radius: 50%; display: inline-block; }
    .status-badge { background: #27ae60; color: white; padding: 0.2rem 0.6rem; border-radius: 15px; font-size: 0.75rem; }
    .category-badge { background: #9b59b6; color: white; padding: 0.2rem 0.6rem; border-radius: 15px; font-size: 0.75rem; }
    .reference-link { color: #00d4ff; text-decoration: none; padding: 0.2rem 0.5rem; }
    .reference-link:hover { color: #00ff88; }
    .big-metric { font-size: 2rem; font-weight: bold; color: #00d4ff; }
    .metric-label { color: #888; font-size: 0.9rem; }
    .divider { border-top: 2px solid #00d4ff; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🧬 DRUG DESIGN & DEVELOPMENT PLATFORM</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#888;">From Target Selection → Hit ID → Lead Optimization → Preclinical → Clinical Trials</p>', unsafe_allow_html=True)
st.markdown("---")

# Import drug discovery engine
from drug_discovery_engine import *

# Sidebar - Pipeline Navigation
st.sidebar.markdown("## 🎯 PIPELINE STAGES")
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

# Quick links
st.sidebar.markdown("---")
st.sidebar.markdown("## 🔗 DATABASE LINKS")
st.sidebar.markdown("""
- [ChEMBL](https://www.ebi.ac.uk/chembl)
- [PubChem](https://pubchem.ncbi.nlm.nih.gov)
- [DrugBank](https://www.drugbank.ca)
- [PDB](https://www.rcsb.org)
- [AlphaFold](https://alphafold.ebi.ac.uk)
- [ClinicalTrials.gov](https://clinicaltrials.gov)
""")

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
                <a href="{url}" target="_blank">{db}</a>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔬 Target Selection Criteria")
    st.markdown("""
    | Criterion | Description |
    |------------|-------------|
    | **Druggability** | Protein class, binding site, expression |
    | **Disease relevance** | Genetic evidence, pathway role |
    | **Safety** | Tissue distribution, off-target potential |
    | **Assay feasibility** | Developability, screening capability |
    | **IP landscape** | Patent freedom to operate |
    """)
    
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
        
        st.markdown("#### 🧮 cheminformatics")
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
    | Tool | Type | Accuracy | Availability |
    |------|------|----------|--------------|
    | **IBM RXN** | AI Cloud | ~85% | Commercial |
    | **ASKCos** | AI Local | ~80% | Free/Open |
    | **ChemAI** | AI Cloud | ~75% | Commercial |
    | **NeuMMA** | AI Cloud | ~78% | Commercial |
    | **RDChiral** | Rule-based | ~60% | Free/Open |
    """)

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
    | Study | Duration | Purpose |
    |-------|----------|---------|
    | In vitro pharmacology | 3-6 months | Mechanism, selectivity |
    | PK/ADME | 6-9 months | Absorption, metabolism |
    | Safety pharmacology | 3-6 months | Core battery |
    | Genetic toxicology | 3-6 months | Ames, micronucleus |
    | 28-day toxicology | 3-4 months | Dose-range finding |
    | 90-day toxicology | 4-6 months | GLP toxicology |
    | CMC | 6-12 months | Formulation, manufacturing |
    """)

# ============================================
# PHASE I CLINICAL TRIALS
# ============================================
elif selected_stage == "6️⃣ Phase I Trials":
    st.markdown("## 🏥 STAGE 6: PHASE I CLINICAL TRIALS", unsafe_allow_html=False)
    st.markdown("---")
    
    p1_col1, p1_col2 = st.columns(2)
    
    with p1_col1:
        st.markdown("""
        ### 📋 Phase I Overview
        **Purpose:** Safety, tolerability, PK/PD
        
        **Population:** 20-100 healthy volunteers
        
        **Duration:** 6-12 months
        
        **Primary Endpoints:**
        - Dose-limiting toxicity (DLT)
        - Maximum tolerated dose (MTD)
        - Adverse events (AEs)
        - Serious adverse events (SAEs)
        """)
    
    with p1_col2:
        st.markdown("""
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
        """)
    
    st.markdown("---")
    st.markdown("### 📊 First-in-Human Dose Calculation")
    st.markdown("""
    | Method | Description |
    |--------|-------------|
    | **Allometric scaling** | Scale from animal PK |
    | **Pharmacodynamic** | Based on animal efficacy |
    | **Safety** | 1/10 to 1/100 of NOAEL |
    | **MABEL** | Minimal anticipated biological effect level |
    """)

# ============================================
# PHASE II CLINICAL TRIALS
# ============================================
elif selected_stage == "7️⃣ Phase II Trials":
    st.markdown("## 🏥 STAGE 7: PHASE II CLINICAL TRIALS", unsafe_allow_html=False)
    st.markdown("---")
    
    p2_col1, p2_col2 = st.columns(2)
    
    with p2_col1:
        st.markdown("""
        ### 📋 Phase II Overview
        **Purpose:** Efficacy, dose-finding
        
        **Population:** 100-500 patients
        
        **Duration:** 12-24 months
        
        **Primary Endpoints:**
        - Clinical response rate
        - Biomarker modulation
        - Optimal dose selection
        - Proof of concept (POC)
        """)
    
    with p2_col2:
        st.markdown("""
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
        """)
    
    st.markdown("---")
    st.markdown("### 📈 Sample Size Calculation")
    st.markdown("""
    | Parameter | Typical Value |
    |-----------|--------------|
    | Alpha (Type I error) | 0.05 (two-sided) |
    | Power (1-beta) | 80-90% |
    | Expected response | 20-40% |
    | Minimum clinically meaningful | 10-15% |
    | Dropout rate | 15-20% |
    """)

# ============================================
# PHASE III CLINICAL TRIALS
# ============================================
elif selected_stage == "8️⃣ Phase III Trials":
    st.markdown("## 🏥 STAGE 8: PHASE III CLINICAL TRIALS", unsafe_allow_html=False)
    st.markdown("---")
    
    p3_col1, p3_col2 = st.columns(2)
    
    with p3_col1:
        st.markdown("""
        ### 📋 Phase III Overview
        **Purpose:** Confirm efficacy, safety
        
        **Population:** 1000-5000 patients
        
        **Duration:** 24-48 months
        
        **Primary Endpoints:**
        - Clinical outcome
        - Overall survival (OS)
        - Progression-free survival (PFS)
        - Quality of life
        """)
    
    with p3_col2:
        st.markdown("""
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
        """)
    
    st.markdown("---")
    st.markdown("### 📊 Regulatory Submission Checklist")
    st.markdown("""
    | Component | Description |
    |----------|-------------|
    | **CMC** | Manufacturing, quality control |
    | **Preclinical** | Pharmacology, toxicology |
    | **Clinical** | Phase I-III data |
    | **Statistical** | Efficacy, safety analysis |
    | **Labeling** | Prescribing information |
    | **Risk management** | REMS, EU-RMP |
    """)

# ============================================
# APPROVAL & LAUNCH
# ============================================
elif selected_stage == "9️⃣ Approval & Launch":
    st.markdown("## ✅ STAGE 9: REGULATORY APPROVAL & LAUNCH", unsafe_allow_html=False)
    st.markdown("---")
    
    reg_col1, reg_col2 = st.columns(2)
    
    with reg_col1:
        st.markdown("""
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
        """)
    
    with reg_col2:
        st.markdown("""
        ### 📋 Submission Components
        
        **NDA/BLA:**
        - Executive summary
        - Quality (CMC)
        - Nonclinical pharmacology
        - Clinical pharmacology
        - Clinical efficacy
        - Clinical safety
        - Post-marketing risk management
        """)
    
    st.markdown("---")
    st.markdown("### 🚀 Launch Preparation")
    st.markdown("""
    | Activity | Timeline |
    |----------|----------|
    | Market research | 6-12 months pre-launch |
    | Medical affairs setup | 6 months pre-launch |
    | Sales force training | 3 months pre-launch |
    | Distribution logistics | 3 months pre-launch |
    | Reimbursement/Payer strategy | Ongoing |
    | Phase IV commitments | Post-launch |
    """)

# ============================================
# PHASE IV MONITORING
# ============================================
elif selected_stage == "🔄 Phase IV Monitoring":
    st.markdown("## 📊 STAGE 10: PHASE IV POST-MARKETING", unsafe_allow_html=False)
    st.markdown("---")
    
    pv_col1, pv_col2 = st.columns(2)
    
    with pv_col1:
        st.markdown("""
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
        """)
    
    with pv_col2:
        st.markdown("""
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
        """)
    
    st.markdown("---")
    st.markdown("### 🔬 New Indications")
    st.markdown("""
    **Post-marketing research can lead to:**
    - New disease indications
    - Pediatric populations
    - Combination therapies
    - Line extension (new formulations)
    - Adjuvant/neoadjuvant use
    - Breakthrough therapy designation
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#666; padding:1rem;">
    <p>🧬 <strong>Comprehensive Drug Design & Development Platform</strong></p>
    <p style="font-size:0.8rem;">From Target Selection → Clinical Trials → Approval → Post-Marketing</p>
    <p style="font-size:0.75rem;">For GM sir | Data from ChEMBL, PubChem, DrugBank, FDA, EMA, ClinicalTrials.gov</p>
</div>
""", unsafe_allow_html=True)
