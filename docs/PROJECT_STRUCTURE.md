# Project Structure & Development Roadmap Visualization

## Project Directory Tree

```
ECG-Based Sleep Apnea Detection/
│
├── data/                                   # Data Management Layer
│   ├── raw/                               # Raw dataset files (HuGCDN2014-OXI)
│   ├── processed/                         # Preprocessed signals
│   └── external/                          # External datasets (future)
│
├── src/                                    # Source Code Layer
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py                      # APNEADataLoader class
│   │   └── preprocessor.py                # Signal preprocessing (Week 3-4)
│   │
│   ├── features/
│   │   ├── __init__.py
│   │   ├── hrv_features.py               # HRV extraction
│   │   ├── spo2_features.py              # SpO2 features
│   │   └── signal_features.py            # ECG features
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cnn_lstm.py                   # CNN-LSTM hybrid model
│   │   ├── random_forest.py              # Random Forest baseline
│   │   └── model_trainer.py              # Training pipeline
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py                     # Flask routes
│   │   ├── auth.py                       # JWT authentication
│   │   └── middleware.py                 # API middleware
│   │
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py                    # normalize_signal, segment_signal
│       ├── signal_processing.py          # Advanced signal processing
│       └── validators.py                 # Input validation
│
├── notebooks/                             # Analysis & Experimentation
│   ├── 01_EDA_Week2.ipynb                # Exploratory Data Analysis
│   ├── 02_Preprocessing.ipynb            # Preprocessing pipeline
│   ├── 03_Feature_Engineering.ipynb      # Feature extraction (Week 3-4)
│   └── 04_Model_Development.ipynb        # Model training (Week 5-6)
│
├── tests/                                 # Testing Layer
│   ├── __init__.py
│   ├── test_data.py                      # Data loading tests
│   ├── test_features.py                  # Feature extraction tests
│   ├── test_models.py                    # Model tests
│   └── test_api.py                       # API endpoint tests
│
├── docs/                                  # Documentation
│   ├── ARCHITECTURE.md                   # System architecture
│   ├── API_DOCUMENTATION.md              # REST API endpoints
│   ├── DATABASE_SCHEMA.md                # PostgreSQL & MongoDB schemas
│   ├── dataset.md                        # Dataset specifications
│   ├── WEEK2_PRESENTATION.md             # Week 2 findings
│   └── PROJECT_STRUCTURE.md              # This file
│
├── config/                                # Configuration
│   ├── __init__.py
│   └── config.py                         # Central configuration (SAMPLING_RATE, etc.)
│
├── scripts/                               # Utility Scripts
│   ├── download_dataset.py               # Dataset download automation
│   ├── preprocess_data.py                # Batch preprocessing
│   └── train_models.py                   # Training pipeline
│
├── frontend/                              # React Frontend (Week 9)
│   ├── src/
│   │   ├── components/                   # React components
│   │   ├── pages/                        # Page components
│   │   ├── services/                     # API services
│   │   └── App.js
│   ├── public/
│   └── package.json
│
├── backend/                               # Flask/FastAPI Backend (Week 7-8)
│   ├── app.py                            # Main application
│   ├── requirements.txt                  # Backend dependencies
│   └── docker/                           # Docker configuration
│
├── requirements.txt                       # Python dependencies (50+ packages)
├── .gitignore                            # Git ignore rules
├── LICENSE                               # MIT License
├── README.md                             # Project documentation
└── test_setup.py                         # Environment validation script
```

## Component Interaction Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     Frontend Layer (React)                       │
│              Dashboard | Upload | Analysis | Reports            │
└──────────────────────────────┬──────────────────────────────────┘
                               │ HTTP/REST
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API Gateway (NGINX)                         │
│              Rate Limiting | Load Balancing | CORS              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
    ┌────────┐            ┌────────┐            ┌────────┐
    │  Auth  │            │ Signal │            │Results │
    │Service │            │Process │            │Service │
    │        │            │ Service│            │        │
    └─────┬──┘            └───┬────┘            └───┬────┘
          │                   │                     │
          │        ┌──────────┼─────────────┐       │
          │        │          │             │       │
          ▼        ▼          ▼             ▼       ▼
    ┌──────────────────────────────────────────────────────┐
    │           ML/Prediction Pipeline                      │
    │  Preprocessing │ Features │ Models │ Classification  │
    └──────────────────────────────────────────────────────┘
          │
    ┌─────┴──────┬──────────────┐
    │            │              │
    ▼            ▼              ▼
┌─────────┐ ┌──────────┐ ┌──────────┐
│PostgreSQL│ │ MongoDB  │ │  Redis   │
│  (User   │ │ (Signals │ │ (Cache)  │
│  Data)   │ │ & Results│ │ (Sessions│
└─────────┘ └──────────┘ └──────────┘
```

## Development Roadmap Timeline

```
WEEK 1-2: FOUNDATION & DOCUMENTATION (COMPLETED)
════════════════════════════════════════════════════════════════

Week 1: Setup & Infrastructure
├─ Project structure setup                           [COMPLETE]
├─ GitHub repository & version control              [COMPLETE]
├─ Python environment (venv, 50+ packages)          [COMPLETE]
├─ Core modules (loader, utils, config)             [COMPLETE]
└─ Testing & documentation                          [COMPLETE]

Week 2: Design & Architecture
├─ System architecture document                      [COMPLETE]
├─ API specification (25+ endpoints)                [COMPLETE]
├─ Database schema design                           [COMPLETE]
├─ Presentation & project planning                  [COMPLETE]
└─ Dataset documentation                            [COMPLETE]


WEEK 3-4: PREPROCESSING & FEATURE ENGINEERING (NEXT)
════════════════════════════════════════════════════════════════

Week 3: Signal Processing
├─ ECG preprocessing (filtering, baseline correction)    [ IN QUEUE ]
├─ R-peak detection algorithm implementation             [ IN QUEUE ]
├─ Noise removal & signal quality assessment             [ IN QUEUE ]
└─ Signal segmentation and windowing                     [ IN QUEUE ]

Week 4: Feature Extraction
├─ Time-domain HRV features (SDNN, RMSSD, pNN50)        [ IN QUEUE ]
├─ Frequency-domain features (LF, HF, LF/HF ratio)      [ IN QUEUE ]
├─ SpO2 feature extraction (desaturation events)        [ IN QUEUE ]
├─ Statistical ECG features                             [ IN QUEUE ]
└─ Feature pipeline & validation                        [ IN QUEUE ]


WEEK 5-6: MODEL DEVELOPMENT & TRAINING
════════════════════════════════════════════════════════════════

Week 5: Model Implementation
├─ CNN-LSTM architecture design & implementation        [ PLANNED ]
├─ Random Forest baseline implementation                [ PLANNED ]
├─ Hyperparameter configuration                         [ PLANNED ]
└─ Loss functions & optimization setup                 [ PLANNED ]

Week 6: Training & Evaluation
├─ Dataset splitting (70/15/15 train/val/test)         [ PLANNED ]
├─ Cross-validation framework                          [ PLANNED ]
├─ Model training with early stopping                  [ PLANNED ]
├─ Performance evaluation (accuracy, precision, recall)[ PLANNED ]
└─ Model comparison & selection                        [ PLANNED ]


WEEK 7-8: BACKEND DEVELOPMENT
════════════════════════════════════════════════════════════════

Week 7: API Implementation
├─ Flask/FastAPI backend setup                        [ PLANNED ]
├─ JWT authentication system                          [ PLANNED ]
├─ Database integration (PostgreSQL, MongoDB)         [ PLANNED ]
└─ API endpoint implementation                        [ PLANNED ]

Week 8: Backend Features
├─ File upload & processing system                    [ PLANNED ]
├─ Async task queue (Celery + Redis)                 [ PLANNED ]
├─ Caching & session management                       [ PLANNED ]
└─ Error handling & logging                           [ PLANNED ]


WEEK 9: FRONTEND DEVELOPMENT
════════════════════════════════════════════════════════════════

Frontend Implementation
├─ React.js dashboard setup                          [ PLANNED ]
├─ Component architecture                            [ PLANNED ]
├─ Authentication UI (login/register)                [ PLANNED ]
├─ Patient management interface                      [ PLANNED ]
├─ Signal upload & processing UI                     [ PLANNED ]
├─ Results visualization & reporting                 [ PLANNED ]
└─ Redux state management                            [ PLANNED ]


WEEK 10: INTEGRATION & TESTING
════════════════════════════════════════════════════════════════

Integration & Deployment
├─ End-to-end system integration                     [ PLANNED ]
├─ Comprehensive testing suite                       [ PLANNED ]
├─ Performance optimization                          [ PLANNED ]
├─ Security audit & hardening                        [ PLANNED ]
├─ Docker containerization                           [ PLANNED ]
├─ Deployment preparation                            [ PLANNED ]
└─ Final documentation & handover                    [ PLANNED ]
```

## Technology Implementation Timeline

```
LAYER                TECHNOLOGY              TIMELINE        STATUS
═════════════════════════════════════════════════════════════════════

Data Layer
  • Raw Files        HuGCDN2014-OXI         Week 1-2      READY
  • Processing       Python Scripts         Week 3-4      QUEUED
  • Storage          File System            Week 1+       ACTIVE

Feature Layer
  • Extraction       BiospPy, NeuroKit2     Week 3-4      QUEUED
  • Engineering      Custom Algorithms      Week 3-4      QUEUED
  • Validation       Scikit-learn           Week 5        QUEUED

ML/DL Layer
  • Preprocessing    TensorFlow Pipeline    Week 5-6      QUEUED
  • CNN-LSTM Model   TensorFlow/Keras       Week 5-6      QUEUED
  • Random Forest    Scikit-learn           Week 5-6      QUEUED
  • Evaluation       Scikit-learn metrics   Week 6        QUEUED

Backend Layer
  • Framework        Flask 3.1.2            Week 7-8      QUEUED
  • Database         PostgreSQL/MongoDB     Week 7-8      QUEUED
  • Cache            Redis                  Week 8        QUEUED
  • Queue            Celery                 Week 8        QUEUED
  • Auth             JWT                    Week 7        QUEUED

Frontend Layer
  • UI Framework     React 18+              Week 9        QUEUED
  • Styling          Tailwind CSS           Week 9        QUEUED
  • Charts           Recharts/Plotly        Week 9        QUEUED
  • State            Redux Toolkit          Week 9        QUEUED

DevOps Layer
  • Container        Docker                 Week 10       QUEUED
  • CI/CD            GitHub Actions         Week 10       QUEUED
  • Testing          Pytest                 Weeks 5-10    QUEUED
  • Documentation    Markdown/API Docs      All weeks     IN PROGRESS
```

## Data Flow Architecture

```
INPUT SOURCES
    │
    ├─── Raw ECG Signals (200 Hz)
    │    ├─ Duration: 8 hours
    │    └─ Size: ~5.76M samples/subject
    │
    └─── SpO2 Signals (50 Hz)
         ├─ Duration: 8 hours
         └─ Size: ~1.44M samples/subject

         │
         ▼

PREPROCESSING STAGE (Week 3)
    ├─ Filtering (Bandpass 0.5-40 Hz)
    ├─ Noise removal
    ├─ Baseline wander correction
    ├─ R-peak detection
    └─ Segmentation & windowing

         │
         ▼

FEATURE EXTRACTION (Week 4)
    ├─ Time-domain HRV: SDNN, RMSSD, pNN50
    ├─ Frequency-domain HRV: LF, HF, LF/HF
    ├─ SpO2 features: Desaturation events, mean, std
    ├─ ECG features: Statistical measures
    └─ Feature normalization & scaling

         │
         ▼

ML PIPELINE (Week 5-6)
    ├─ Data splitting: 70/15/15
    ├─ Cross-validation: K-fold
    ├─ Model training: CNN-LSTM + Random Forest
    ├─ Hyperparameter tuning
    └─ Performance evaluation

         │
         ▼

CLASSIFICATION LAYER
    ├─ Ensemble prediction
    ├─ Confidence scoring
    ├─ Apnea event detection
    └─ Risk stratification

         │
         ▼

OUTPUT LAYER (Week 7-8)
    ├─ API Response: JSON format
    ├─ Database Storage: PostgreSQL + MongoDB
    ├─ Report Generation: PDF with findings
    ├─ Dashboard Visualization: React UI
    └─ User Notification: Email/Alert system
```

## Testing Strategy Timeline

```
WEEK 1-2: Unit Tests (Foundation)
  ├─ Data loader tests
  ├─ Signal processing tests
  ├─ Configuration tests
  └─ Status: COMPLETE

WEEK 3-4: Integration Tests (Features)
  ├─ Preprocessing pipeline tests
  ├─ Feature extraction tests
  ├─ End-to-end signal processing
  └─ Status: QUEUED

WEEK 5-6: Model Tests
  ├─ Model training tests
  ├─ Prediction accuracy tests
  ├─ Cross-validation tests
  └─ Status: QUEUED

WEEK 7-8: API Tests
  ├─ Endpoint tests
  ├─ Authentication tests
  ├─ Database integration tests
  └─ Status: QUEUED

WEEK 9: End-to-End Tests
  ├─ Frontend UI tests
  ├─ API-frontend integration
  └─ Status: QUEUED

WEEK 10: Production Readiness
  ├─ Performance tests
  ├─ Security tests
  ├─ Load tests
  └─ Status: QUEUED
```

## Deliverables Checklist

```
WEEK 1-2 DELIVERABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[X] Project structure and organization
[X] GitHub repository with CI/CD setup
[X] Python environment (3.13) with 50+ packages
[X] Core modules and utilities
[X] System architecture documentation
[X] API specification (25+ endpoints)
[X] Database schema design
[X] Dataset documentation
[X] Testing infrastructure


WEEK 3-4 DELIVERABLES (UPCOMING)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Preprocessing pipeline implementation
[ ] Feature extraction module
[ ] Jupyter notebooks with examples
[ ] Feature engineering report
[ ] Performance metrics documentation


WEEK 5-6 DELIVERABLES (PLANNED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Trained CNN-LSTM model
[ ] Trained Random Forest model
[ ] Model evaluation report
[ ] Cross-validation results
[ ] Prediction pipeline


WEEK 7-8 DELIVERABLES (PLANNED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Flask/FastAPI backend
[ ] Database integration
[ ] API endpoints
[ ] Authentication system
[ ] Async task processing


WEEK 9 DELIVERABLES (PLANNED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] React.js frontend
[ ] Dashboard interface
[ ] User authentication UI
[ ] Data visualization


WEEK 10 DELIVERABLES (PLANNED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Complete system integration
[ ] Comprehensive testing suite
[ ] Docker deployment
[ ] Production documentation
[ ] Deployment guide
```

## Development Velocity

```
WEEK 1-2: Foundation Phase
  Lines of Code: ~2,500
  Modules: 8
  Documentation Pages: 6
  Status: COMPLETE (100%)

WEEK 3-4: Feature Engineering Phase
  Estimated Lines of Code: ~3,500
  Modules: 12
  Notebooks: 2
  Status: NEXT PHASE

WEEK 5-6: ML Development Phase
  Estimated Lines of Code: ~4,000
  Models: 2
  Test Cases: 50+
  Status: PLANNED

WEEK 7-8: Backend Development Phase
  Estimated Lines of Code: ~3,000
  API Endpoints: 25+
  Status: PLANNED

WEEK 9: Frontend Development Phase
  Estimated Lines of Code: ~2,500
  React Components: 15+
  Status: PLANNED

WEEK 10: Integration & Testing
  Test Coverage Target: >80%
  Status: PLANNED
```

---

**Last Updated**: February 1, 2026  
**Next Phase**: Week 3-4 (Preprocessing & Feature Engineering)
