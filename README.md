# ECG-Based Sleep Apnea Detection System

![Project Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python Version](https://img.shields.io/badge/Python-3.13-blue)
![Tech Stack](https://img.shields.io/badge/Stack-Full--Stack-green)
![License](https://img.shields.io/badge/License-MIT-brightgreen)
![ML Framework](https://img.shields.io/badge/ML-TensorFlow-orange)
![Database](https://img.shields.io/badge/Database-PostgreSQL%20%2B%20MongoDB-informational)
[![Tests](https://github.com/happy2234/ECG-Based-Sleep-Apnea-Detection/workflows/Python%20Tests%20%26%20Code%20Quality/badge.svg)](https://github.com/happy2234/ECG-Based-Sleep-Apnea-Detection/actions)

## Project Overview

An end-to-end full-stack web application for automated detection of sleep apnea episodes using ECG (Electrocardiogram), HRV (Heart Rate Variability), and SpO2 (Blood Oxygen Saturation) signals with machine learning and deep learning models.

### Problem Statement

Sleep apnea is a serious sleep disorder affecting an estimated 1 billion people worldwide. Traditional diagnosis requires expensive overnight polysomnography (PSG) tests costing $1,000-$3,000+ per session, making screening inaccessible for many. This project develops an automated, cost-effective screening tool leveraging non-invasive ECG-based signals to detect sleep apnea patterns.

### Solution Overview

By combining signal processing techniques with machine learning models (CNN-LSTM and Random Forest), this system:
- Processes continuous ECG and SpO2 recordings
- Extracts clinically-relevant features (HRV metrics, desaturation events)
- Delivers real-time apnea event detection
- Provides web-based accessibility for clinicians and patients

### Key Features

- Automated sleep apnea episode detection from ECG and SpO2 signals
- Real-time signal processing and analysis (200 Hz ECG, 50 Hz SpO2)
- Interactive web-based user dashboard
- Multi-user support with role-based access control
- Historical data tracking and patient analytics
- Comprehensive PDF report generation with findings and recommendations
- RESTful API for integration with healthcare systems
- Hybrid database design for structured and signal data

## Dataset

**APNEA HRV+SPO2 Dataset** (HuGCDN2014-OXI)

- **Source**: Mendeley Data, Dr. Negrín University Hospital (Las Palmas de Gran Canaria, Spain)
- **DOI**: 10.17632/cdxs63gdzc.1
- **URL**: https://data.mendeley.com/datasets/cdxs63gdzc/1
- **Subjects**: 83 clinical recordings
  - 38 healthy controls (AHI < 5)
  - 45 OSA patients with AHI > 25
- **Signals**: 
  - ECG at 200 Hz (5.76M samples/subject)
  - SpO2 at 50 Hz (1.44M samples/subject)
- **Duration**: Full night recordings (~8 hours each)
- **Annotation**: Expert-labeled per AASM guidelines (per-minute resolution)
- **License**: CC BY 4.0
- **Size**: ~89.7 MB compressed

For detailed dataset information, see [Dataset Documentation](./docs/dataset.md).

## Technology Stack

### Core Technologies

| Category | Technologies | Version |
|----------|--------------|---------|
| **Language** | Python | 3.13 |
| **Data Processing** | NumPy, Pandas, SciPy | Latest |
| **Signal Processing** | BiospPy, NeuroKit2, WFDB | Latest |
| **ML/DL Frameworks** | Scikit-learn, TensorFlow/Keras | Latest |
| **Backend API** | Flask/FastAPI | 3.1+ |
| **Databases** | PostgreSQL, MongoDB, Redis | Latest |
| **Frontend** | React.js | 18+ |
| **Authentication** | JWT, OAuth2 | Standard |
| **Task Queue** | Celery | 5.3+ |
| **Testing** | Pytest | 7.0+ |

### Architecture

- **Microservices Architecture**: Independent services for authentication, signal processing, prediction
- **Containerization**: Docker for consistent deployment
- **API Gateway**: NGINX for routing and load balancing
- **Async Processing**: Celery + Redis for long-running tasks
- **Caching**: Redis for session and result caching

## Project Structure & Architecture

### Directory Organization

```
ECG-Based Sleep Apnea Detection/
├── data/                     # Data Management Layer
│   ├── raw/                 # Raw dataset files (HuGCDN2014-OXI)
│   ├── processed/           # Preprocessed signals
│   └── external/            # External datasets
├── src/                     # Source Code Layer
│   ├── data/               # Data loading and preprocessing
│   ├── features/           # Feature extraction pipeline
│   ├── models/             # ML/DL model implementations
│   ├── api/                # REST API endpoints
│   └── utils/              # Utility functions and helpers
├── notebooks/              # Jupyter notebooks for analysis
│   ├── 01_Exploratory_Data_Analysis.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   └── 04_Model_Results.ipynb
├── tests/                  # Unit and integration tests
├── docs/                   # Documentation
│   ├── ARCHITECTURE.md     # System design
│   ├── API_DOCUMENTATION.md
│   ├── DATABASE_SCHEMA.md
│   ├── dataset.md
│   ├── WEEK2_PRESENTATION.md
│   └── PROJECT_STRUCTURE.md
├── config/                 # Configuration files
├── scripts/                # Utility scripts
├── frontend/               # React frontend (planned)
├── backend/                # Flask/FastAPI backend (planned)
├── requirements.txt        # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

### System Architecture

```
Frontend Layer (React)
  Dashboard | Upload | Analysis | Reports
         |
         | HTTP/REST
         ▼
API Gateway (NGINX)
  Rate Limiting | Load Balancing | CORS
         |
    ┌────┼────┬────┐
    ▼    ▼    ▼    ▼
  Auth  Signal Results
Service Process Service
        Service
         |
    ML Pipeline
  Preprocessing → Features → Models → Classification
         |
    ┌────┼────┬────┐
    ▼    ▼    ▼    ▼
PostgreSQL MongoDB Redis
  (User)   (Signals) (Cache)
```

## Installation & Setup

### Prerequisites

- Python 3.13 or higher
- pip package manager (usually included with Python)
- Git version control
- Virtual environment support (venv)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/happy2234/ECG-Based-Sleep-Apnea-Detection.git
   cd "ECG-Based Sleep Apnea Detection"
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate on Linux/macOS
   source venv/bin/activate
   
   # Activate on Windows
   # venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download and set up dataset**
   ```bash
   # Visit: https://data.mendeley.com/datasets/cdxs63gdzc/1
   # Download HuGCDN2014-OXI.zip (~89.7 MB)
   # Extract to: data/raw/
   
   mkdir -p data/raw
   # Extract dataset here
   ```

5. **Verify installation**
   ```bash
   python test_setup.py
   ```
   All core packages should import successfully.

6. **Launch Jupyter notebook for analysis**
   ```bash
   jupyter notebook notebooks/01_EDA_Week2.ipynb
   ```

## Installed Dependencies

### Core Data Science
- NumPy 2.4.1 - Numerical computing
- Pandas 3.0.0 - Data manipulation
- SciPy 1.17.0 - Scientific computing
- Scikit-learn 1.8.0 - Machine learning

### Signal Processing
- BiospPy 2.1.2 - ECG processing
- NeuroKit2 0.2.12 - Physiological signal analysis
- WFDB 4.3.0 - ECG data loading

### Deep Learning
- TensorFlow 2.20.0 - Deep learning framework
- Keras - Neural network API

### Backend/API
- Flask 3.1.2 - Web framework
- SQLAlchemy 2.0 - Database ORM
- Celery 5.6.0 - Async task queue
- Redis 5.0.1 - Caching and messaging

### Visualization & Analysis
- Matplotlib 3.10.0 - Plotting library
- Seaborn 0.13.0 - Statistical visualization
- Plotly 6.5.0 - Interactive charts

### Development & Testing
- Jupyter Lab 4.5.0 - Interactive notebook environment
- Pytest 9.0.0 - Testing framework
- IPython 8.30.0 - Enhanced Python shell

See [requirements.txt](./requirements.txt) for complete dependency list.

## Current Progress

### Completed Work

#### Week 1-2: Foundation & Documentation (100% Complete)

**Week 1 Deliverables**
- Project structure and organization
- GitHub repository setup with MIT license
- Python 3.13 virtual environment configuration
- 50+ package dependencies installed and tested
- Core modules: data loader, signal processing utilities, configuration management
- Environment validation script with all tests passing

**Week 2 Deliverables**
- Complete system architecture documentation
- REST API specification (25+ endpoints)
- Database schema design (6 PostgreSQL tables + 4 MongoDB collections)
- Week 2 presentation with EDA framework
- Comprehensive dataset documentation
- README updates with project-relevant information

#### Test Status
- Environment validation: PASSED
- Signal processing utilities: VALIDATED
- Core package imports: 9/9 SUCCESS

## Development Roadmap

### 10-Week Implementation Timeline

```
WEEK 1-2: Foundation & Documentation (COMPLETED)
════════════════════════════════════════════════════════════════
Week 1: Setup & Infrastructure
  [X] Project structure & organization
  [X] GitHub repository & version control
  [X] Python 3.13 environment (50+ packages)
  [X] Core modules & testing framework

Week 2: Design & Architecture
  [X] System architecture documentation
  [X] API specification (25+ endpoints)
  [X] Database schema design
  [X] Dataset documentation & specifications


WEEK 3-4: Preprocessing & Feature Engineering (IN PROGRESS)
════════════════════════════════════════════════════════════════
Week 3: Signal Processing & Features (COMPLETED)
  [X] ECG preprocessing (filtering, baseline correction)
  [X] R-peak detection & Signal quality assessment
  [X] Time-domain HRV features (SDNN, RMSSD, pNN50)
  [X] Frequency-domain features (LF, HF, LF/HF ratio)
  [X] SpO2 feature extraction (ODI, Mean, Min)
  [X] Feature pipeline validation

Week 4: Model Development (IN PROGRESS)
  [X] Dataset splitting (Train/Test/Val)
  [/] Model Selection (Random Forest, CNN-LSTM)
  [/] Training pipeline setup
  [ ] Performance evaluation


WEEK 5-6: Model Development & Training
════════════════════════════════════════════════════════════════
Week 5: Model Implementation
  [ ] CNN-LSTM architecture design
  [ ] Random Forest baseline model
  [ ] Hyperparameter configuration
  [ ] Training pipeline setup

Week 6: Training & Evaluation
  [ ] Dataset splitting (70/15/15)
  [ ] Cross-validation framework
  [ ] Model training with early stopping
  [ ] Performance evaluation & metrics


WEEK 7-8: Backend Development
════════════════════════════════════════════════════════════════
Week 7: API Implementation
  [ ] Flask/FastAPI backend setup
  [ ] JWT authentication system
  [ ] Database integration
  [ ] API endpoint implementation

Week 8: Backend Features
  [ ] File upload & async processing
  [ ] Caching & session management
  [ ] Error handling & logging
  [ ] API documentation & testing


WEEK 9: Frontend Development
════════════════════════════════════════════════════════════════
  [ ] React.js dashboard
  [ ] User authentication UI
  [ ] Patient management interface
  [ ] Signal upload & visualization
  [ ] Results & reporting display


WEEK 10: Integration & Testing
════════════════════════════════════════════════════════════════
  [ ] End-to-end system integration
  [ ] Comprehensive testing suite
  [ ] Performance optimization
  [ ] Security audit
  [ ] Docker containerization
  [ ] Deployment & documentation
```

### Progress Dashboard

| Phase | Timeline | Completion | Status |
|-------|----------|-----------|--------|
| Foundation | Week 1-2 | 100% | Complete |
| Features | Week 3 | 100% | Complete |
| Modeling | Week 4-6 | 30% | In Progress |
| Backend | Week 7-8 | 0% | Planned |
| Frontend | Week 9 | 0% | Planned |
| Integration | Week 10 | 0% | Planned |

See [Project Structure & Roadmap](./docs/PROJECT_STRUCTURE.md) for detailed breakdown.

## Documentation

Complete documentation is available in the [docs/](./docs/) directory:

- **[System Architecture](./docs/ARCHITECTURE.md)** - Complete system design with component interactions and deployment strategy
- **[API Reference](./docs/API_DOCUMENTATION.md)** - All REST endpoints with request/response formats and authentication
- **[Database Design](./docs/DATABASE_SCHEMA.md)** - PostgreSQL and MongoDB schemas with relationships
- **[Dataset Information](./docs/dataset.md)** - Full dataset specifications, download instructions, and usage examples
- **[Week 2 Presentation](./docs/WEEK2_PRESENTATION.md)** - Comprehensive progress report and findings
- **[Project Structure & Roadmap](./docs/PROJECT_STRUCTURE.md)** - Detailed visualization of structure and timeline
- **[CI/CD & Testing](./docs/CI_CD.md)** - Automated testing and continuous integration setup

## Running Tests

### Online Testing (GitHub Actions)

Automated testing runs on every push and pull request:

- **Platform**: GitHub Actions
- **Python Versions**: 3.11, 3.12, 3.13
- **Test Coverage**: Unit tests with coverage reporting
- **Code Quality**: Black, isort, Pylint, Bandit
- **Security**: Vulnerability scanning

View workflow status: [GitHub Actions](https://github.com/happy2234/ECG-Based-Sleep-Apnea-Detection/actions)

### Local Testing

```bash
# Install test dependencies
pip install pytest pytest-cov pytest-xdist

# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=src --cov-report=html

# Run tests in parallel
pytest tests/ -n auto

# Run specific test file
pytest tests/test_data.py -v
```

### Code Quality Checks

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint check
pylint src/

# Security check
bandit -r src/
```

For detailed testing setup, see [CI/CD & Testing](./docs/CI_CD.md).


## Project Quality Standards

- Comprehensive documentation for all modules
- Type hints for Python functions
- Unit tests for core functionality
- Clean code with PEP 8 compliance
- Git history with meaningful commit messages

## Contributing

This is an academic research project developed for sleep apnea detection. Contributions, suggestions, and collaboration inquiries are welcome.

For contribution guidelines or questions, please contact the project team.

## Citation

If you use this project or dataset in research, please cite:

```
Juliá-Serdá, Gabriel; Navarro-Esteva, Javier; Ravelo-García, Antonio G. (2023).
"APNEA HRV+SPO2 DATASET". Mendeley Data, V1.
DOI: 10.17632/cdxs63gdzc.1
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The included dataset uses CC BY 4.0 license. See [Dataset Documentation](./docs/dataset.md) for attribution requirements.

## Contact & Support

**Project Lead**: happy2234  
**Email**: gauravjangra1110@gmail.com  
**Repository**: https://github.com/happy2234/ECG-Based-Sleep-Apnea-Detection

For questions, suggestions, or collaboration opportunities, please reach out via email.

---

**Last Updated**: February 1, 2026  
**Python Version**: 3.13  
**Project Status**: In Active Development
