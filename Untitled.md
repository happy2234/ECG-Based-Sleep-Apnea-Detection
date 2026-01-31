# ECG-Based Sleep Apnea Detection System
## Full-Stack Application Using APNEA HRV+SPO2 Dataset

![Project Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Timeline](https://img.shields.io/badge/Timeline-2.5%20Months-blue)
![Tech Stack](https://img.shields.io/badge/Stack-Full--Stack-green)

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Detailed Roadmap](#detailed-roadmap)
- [Current Progress](#current-progress)
- [Installation & Setup](#installation--setup)
- [Team & Responsibilities](#team--responsibilities)

---

## 🎯 Project Overview

### Objective
Develop an end-to-end full-stack web application for automated detection of sleep apnea episodes using ECG, HRV (Heart Rate Variability), and SpO2 (Blood Oxygen Saturation) signals with machine learning/deep learning models.

### Problem Statement
Sleep apnea is a serious sleep disorder affecting millions globally. Traditional diagnosis requires expensive overnight polysomnography tests. This project aims to create an accessible, automated screening tool using ECG-based signals.

### Key Features
- ✅ Automated sleep apnea detection from ECG signals
- ✅ Real-time signal processing and analysis
- ✅ Interactive web-based user interface
- ✅ Historical data tracking and analytics
- ✅ Comprehensive reporting with visualizations
- ✅ RESTful API for integration capabilities

---

## 📊 Dataset Information

### APNEA HRV+SPO2 Dataset
- **Source**: PhysioNet / MIT-BIH Database
- **Signals**: ECG, Heart Rate Variability (HRV), SpO2
- **Classes**: Apnea episodes vs Normal breathing
- **Format**: Binary/text files with annotations
- **Sample Rate**: Varies (typically 100-250 Hz for ECG)

### Dataset Structure
```
dataset/
├── training/
│   ├── ecg_signals/
│   ├── hrv_features/
│   ├── spo2_data/
│   └── annotations/
├── testing/
│   └── [same structure]
└── metadata.csv
```

---

## 🛠 Technology Stack

### Machine Learning & Data Processing
- **Python 3.8+**: Core programming language
- **NumPy & Pandas**: Data manipulation
- **SciPy**: Signal processing
- **Scikit-learn**: Traditional ML algorithms
- **TensorFlow/Keras or PyTorch**: Deep learning models
- **BiospPy/NeuroKit2**: Biosignal processing
- **WFDB**: ECG data handling

### Backend Development
- **Framework**: Flask or FastAPI
- **Database**: PostgreSQL (relational) + MongoDB (signal storage)
- **Authentication**: JWT tokens
- **API Documentation**: Swagger/OpenAPI
- **Task Queue**: Celery (for async processing)
- **Caching**: Redis

### Frontend Development
- **Framework**: React.js 18+
- **UI Library**: Tailwind CSS + shadcn/ui
- **State Management**: Redux Toolkit or Zustand
- **Charting**: Recharts, Chart.js, or Plotly.js
- **HTTP Client**: Axios
- **Routing**: React Router v6

### DevOps & Deployment
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **CI/CD**: GitHub Actions
- **Cloud Platform**: AWS/GCP/Azure
- **Frontend Hosting**: Vercel/Netlify
- **Backend Hosting**: AWS EC2/Lambda or Heroku
- **Database Hosting**: AWS RDS, MongoDB Atlas

### Development Tools
- **Version Control**: Git & GitHub
- **Code Editor**: VS Code
- **API Testing**: Postman
- **Model Tracking**: MLflow or Weights & Biases
- **Documentation**: Markdown, Jupyter Notebooks

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Dashboard   │  │ Upload Page  │  │   Reports    │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTPS/REST API
┌───────────────────────────▼─────────────────────────────────────┐
│                       BACKEND LAYER                             │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              API Gateway (Flask/FastAPI)                  │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │  │
│  │  │   Auth      │  │  Prediction │  │  Analytics  │      │  │
│  │  │  Service    │  │   Service   │  │   Service   │      │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘      │  │
│  └──────────────────────────────────────────────────────────┘  │
└───────────────┬────────────────────────┬────────────────────────┘
                │                        │
    ┌───────────▼──────────┐  ┌─────────▼──────────┐
    │   ML/DL MODELS       │  │     DATABASES      │
    │  ┌────────────────┐  │  │  ┌──────────────┐  │
    │  │ Preprocessing  │  │  │  │ PostgreSQL   │  │
    │  │    Pipeline    │  │  │  │ (User Data)  │  │
    │  └────────────────┘  │  │  └──────────────┘  │
    │  ┌────────────────┐  │  │  ┌──────────────┐  │
    │  │ Feature Extract│  │  │  │  MongoDB     │  │
    │  └────────────────┘  │  │  │ (Signals)    │  │
    │  ┌────────────────┐  │  │  └──────────────┘  │
    │  │ CNN-LSTM Model │  │  │  ┌──────────────┐  │
    │  └────────────────┘  │  │  │    Redis     │  │
    │  ┌────────────────┐  │  │  │   (Cache)    │  │
    │  │ Random Forest  │  │  │  └──────────────┘  │
    │  └────────────────┘  │  └────────────────────┘
    └─────────────────────┘
```

---

## 🗓 Detailed Roadmap

### **WEEK 1-2: Foundation & Exploration** ✅ **(CURRENT - Show Progress)**

#### Week 1
**Day 1-2: Project Setup**
- [ ] Create GitHub repository with proper structure
- [ ] Set up virtual environment
- [ ] Install required libraries
- [ ] Create project documentation template
- [ ] Set up Jupyter notebooks for exploration

**Day 3-5: Dataset Acquisition & Understanding**
- [ ] Download APNEA HRV+SPO2 dataset
- [ ] Study dataset documentation
- [ ] Understand signal formats and annotations
- [ ] Create data loading scripts
- [ ] Document dataset characteristics

**Day 6-7: Literature Review**
- [ ] Review 10-15 research papers on ECG-based apnea detection
- [ ] Study HRV analysis techniques
- [ ] Research feature extraction methods
- [ ] Document state-of-the-art approaches
- [ ] Identify performance benchmarks

#### Week 2
**Day 1-3: Exploratory Data Analysis (EDA)**
- [ ] Load and parse ECG, HRV, SpO2 signals
- [ ] Visualize sample signals (normal vs apnea)
- [ ] Statistical analysis of signal characteristics
- [ ] Identify data quality issues
- [ ] Analyze class distribution and imbalance
- [ ] Create comprehensive EDA notebook

**Day 4-5: Initial System Design**
- [ ] Design system architecture diagram
- [ ] Define database schema
- [ ] Plan API endpoints
- [ ] Create wireframes for UI
- [ ] Define project milestones

**Day 6-7: Progress Presentation Preparation**
- [ ] Create presentation slides
- [ ] Prepare demo of EDA findings
- [ ] Document technical approach
- [ ] Prepare Q&A for supervisor meeting
- [ ] Update roadmap based on feedback

**📌 Week 2 Deliverables:**
- EDA Jupyter notebook with visualizations
- Project architecture document
- Initial presentation for supervisor
- Updated roadmap and timeline

---

### **WEEK 3-4: Data Preprocessing & Feature Engineering**

#### Week 3
**Day 1-2: Signal Preprocessing Pipeline**
- [ ] Implement ECG filtering (bandpass, notch filters)
- [ ] Noise removal algorithms
- [ ] Baseline wander correction
- [ ] Signal normalization techniques
- [ ] Quality assessment metrics

**Day 3-4: R-Peak Detection & HRV Analysis**
- [ ] Implement Pan-Tompkins algorithm or similar
- [ ] R-peak detection and validation
- [ ] RR interval extraction
- [ ] Calculate time-domain HRV features:
  - SDNN, RMSSD, pNN50, SDSD
  - Mean HR, Min HR, Max HR
- [ ] Calculate frequency-domain HRV features:
  - LF, HF, LF/HF ratio
  - Total power, VLF

**Day 5-7: Feature Extraction**
- [ ] SpO2 feature extraction
- [ ] Statistical features from ECG
- [ ] Morphological features
- [ ] Time-series features
- [ ] Create feature extraction pipeline
- [ ] Save features to CSV/HDF5

#### Week 4
**Day 1-2: Advanced Feature Engineering**
- [ ] Wavelet transform features
- [ ] Entropy-based features
- [ ] Autoregressive model features
- [ ] Feature correlation analysis
- [ ] Feature importance preliminary analysis

**Day 3-4: Data Augmentation & Balancing**
- [ ] SMOTE for class imbalance
- [ ] Signal augmentation techniques:
  - Time warping
  - Magnitude scaling
  - Adding controlled noise
- [ ] Validate augmentation quality

**Day 5-6: Dataset Preparation**
- [ ] Train/Validation/Test split (70/15/15)
- [ ] Create data loaders
- [ ] Implement cross-validation folds
- [ ] Save preprocessed data
- [ ] Document preprocessing pipeline

**Day 7: Code Review & Documentation**
- [ ] Refactor preprocessing code
- [ ] Add comprehensive comments
- [ ] Create preprocessing documentation
- [ ] Unit tests for key functions
- [ ] Version control checkpoint

**📌 Week 3-4 Deliverables:**
- Complete preprocessing pipeline
- Extracted features dataset
- Data augmentation scripts
- Preprocessing documentation
- Clean, versioned codebase

---

### **WEEK 5-6: Model Development & Training**

#### Week 5
**Day 1-2: Baseline Models**
- [ ] Implement Logistic Regression
- [ ] Random Forest classifier
- [ ] Support Vector Machine (SVM)
- [ ] XGBoost/LightGBM
- [ ] Evaluate baseline performance
- [ ] Feature importance analysis

**Day 3-4: Deep Learning Setup**
- [ ] Set up TensorFlow/PyTorch environment
- [ ] Create custom dataset classes
- [ ] Implement data generators
- [ ] Design model training pipeline
- [ ] Set up TensorBoard/logging

**Day 5-7: 1D CNN Models**
- [ ] Design 1D CNN architecture for ECG
- [ ] Implement multi-channel CNN (ECG+HRV+SpO2)
- [ ] Experiment with different architectures:
  - Simple CNN
  - ResNet-inspired 1D architecture
  - Inception-inspired architecture
- [ ] Train and validate models
- [ ] Hyperparameter tuning (learning rate, batch size, etc.)

#### Week 6
**Day 1-3: Recurrent Neural Networks**
- [ ] LSTM model for temporal patterns
- [ ] Bidirectional LSTM
- [ ] GRU architecture
- [ ] Attention mechanisms
- [ ] Compare RNN variants

**Day 4-5: Hybrid Models**
- [ ] CNN-LSTM hybrid architecture
- [ ] CNN for feature extraction + LSTM for temporal
- [ ] Multi-input model (parallel processing)
- [ ] Ensemble methods
- [ ] Fine-tune best performing models

**Day 6-7: Model Evaluation & Selection**
- [ ] Comprehensive evaluation metrics:
  - Accuracy, Precision, Recall, F1-Score
  - ROC-AUC, PR-AUC
  - Confusion matrix
  - Sensitivity, Specificity
- [ ] Cross-validation results
- [ ] Model comparison report
- [ ] Select final model(s)
- [ ] Model serialization (save best models)

**📌 Week 5-6 Deliverables:**
- Trained ML/DL models
- Model evaluation report with metrics
- Saved model files (.h5, .pkl)
- Training notebooks and scripts
- Model comparison documentation

---

### **WEEK 7-8: Backend Development**

#### Week 7
**Day 1-2: Backend Setup**
- [ ] Initialize Flask/FastAPI project
- [ ] Set up project structure (MVC pattern)
- [ ] Configure environment variables
- [ ] Set up logging system
- [ ] Create requirements.txt

**Day 3-4: Database Design & Implementation**
- [ ] Design PostgreSQL schema:
  - Users table
  - Predictions table
  - Reports table
  - Sessions table
- [ ] Set up MongoDB for signal storage
- [ ] Implement database models (SQLAlchemy/Mongoengine)
- [ ] Create database migrations
- [ ] Seed initial data

**Day 5-7: Core API Endpoints**
- [ ] `/api/auth/register` - User registration
- [ ] `/api/auth/login` - User authentication
- [ ] `/api/auth/logout` - Logout
- [ ] `/api/user/profile` - Get/update profile
- [ ] Implement JWT authentication
- [ ] Password hashing (bcrypt)
- [ ] Input validation middleware

#### Week 8
**Day 1-3: Prediction API**
- [ ] `/api/predict/upload` - Upload ECG file
- [ ] `/api/predict/analyze` - Process and predict
- [ ] `/api/predict/result/:id` - Get prediction result
- [ ] Implement model loading and inference
- [ ] Signal preprocessing in API
- [ ] Error handling and validation
- [ ] Response formatting

**Day 4-5: Analytics & History APIs**
- [ ] `/api/history/list` - Get user's prediction history
- [ ] `/api/history/:id` - Get specific prediction details
- [ ] `/api/analytics/stats` - User statistics
- [ ] `/api/analytics/dashboard` - Dashboard data
- [ ] Implement pagination
- [ ] Filtering and sorting options

**Day 6-7: Testing & Documentation**
- [ ] Write unit tests for API endpoints
- [ ] Integration tests
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Postman collection creation
- [ ] Performance testing
- [ ] Security audit (basic)
- [ ] Code optimization

**📌 Week 7-8 Deliverables:**
- Functional REST API
- Database implementation
- API documentation
- Test suite
- Postman collection

---

### **WEEK 9: Frontend Development - Part 1**

**Day 1-2: React Setup & Architecture**
- [ ] Create React app (Vite/Create-React-App)
- [ ] Set up project structure (components, pages, utils)
- [ ] Configure Tailwind CSS
- [ ] Set up routing (React Router)
- [ ] Configure state management (Redux/Zustand)
- [ ] Set up Axios for API calls
- [ ] Create API service layer

**Day 3-4: Authentication Pages**
- [ ] Login page design and implementation
- [ ] Registration page
- [ ] Password reset flow
- [ ] Protected route wrapper
- [ ] Auth context/state management
- [ ] Form validation (Formik/React Hook Form)
- [ ] Error handling UI

**Day 5-7: Dashboard & Navigation**
- [ ] Responsive navigation bar
- [ ] Sidebar menu
- [ ] Main dashboard layout
- [ ] Dashboard statistics cards:
  - Total predictions
  - Recent activity
  - Apnea detection rate
  - Quick actions
- [ ] User profile dropdown
- [ ] Responsive design for mobile/tablet
- [ ] Loading states and skeletons

**📌 Week 9 Deliverables:**
- React application structure
- Authentication flow
- Main dashboard layout
- Responsive navigation

---

### **WEEK 10: Frontend Development - Part 2 & Integration**

**Day 1-2: ECG Upload Interface**
- [ ] File upload component (drag & drop)
- [ ] File validation (format, size)
- [ ] Upload progress indicator
- [ ] Preview uploaded file
- [ ] Manual input form (if applicable)
- [ ] Multi-file upload support
- [ ] Error handling and user feedback

**Day 2-3: Real-time Visualization**
- [ ] ECG signal visualization (line chart)
- [ ] Interactive zoom and pan
- [ ] Apnea event markers
- [ ] HRV visualization
- [ ] SpO2 level chart
- [ ] Signal quality indicator
- [ ] Export visualization (PNG/SVG)

**Day 4-5: Results Display Page**
- [ ] Prediction results layout
- [ ] Confidence score visualization
- [ ] Detailed metrics display
- [ ] Apnea episodes timeline
- [ ] Severity classification
- [ ] Recommendations section
- [ ] Share/download results

**Day 6: History & Reports**
- [ ] Prediction history table
- [ ] Filtering and sorting
- [ ] Search functionality
- [ ] Detailed view modal
- [ ] Comparison between predictions
- [ ] PDF report generation
- [ ] Export to CSV/Excel

**Day 7: Integration & Polish**
- [ ] Connect all pages to backend API
- [ ] Error boundary implementation
- [ ] Toast notifications
- [ ] Loading states everywhere
- [ ] Form validation feedback
- [ ] Accessibility improvements (ARIA labels)
- [ ] Browser compatibility testing

**📌 Week 10 Deliverables:**
- Complete frontend application
- Backend integration
- Working end-to-end flow
- Responsive design

---

### **WEEK 11: Testing, Optimization & Documentation**

**Day 1-2: Testing**
- [ ] Backend unit tests (pytest)
- [ ] Frontend component tests (Jest/React Testing Library)
- [ ] Integration tests
- [ ] End-to-end tests (Cypress/Playwright)
- [ ] API endpoint testing
- [ ] User flow testing
- [ ] Cross-browser testing
- [ ] Mobile responsiveness testing

**Day 3-4: Performance Optimization**
- [ ] Model inference optimization
- [ ] API response time optimization
- [ ] Database query optimization
- [ ] Frontend bundle size reduction
- [ ] Code splitting (React lazy loading)
- [ ] Image optimization
- [ ] Caching implementation (Redis)
- [ ] CDN setup for static assets

**Day 5: Security Audit**
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF tokens
- [ ] Rate limiting
- [ ] Input sanitization
- [ ] Secure headers
- [ ] HTTPS enforcement
- [ ] Environment variables security

**Day 6-7: Documentation**
- [ ] Technical documentation:
  - Architecture overview
  - API documentation
  - Database schema
  - Model architecture
  - Deployment guide
- [ ] User documentation:
  - User manual
  - How-to guides
  - FAQ section
- [ ] Code documentation (docstrings)
- [ ] README update
- [ ] Contributing guidelines
- [ ] License file

**📌 Week 11 Deliverables:**
- Comprehensive test suite
- Optimized application
- Security audit report
- Complete documentation

---

### **WEEK 12: Deployment & Final Presentation**

**Day 1-2: Deployment Preparation**
- [ ] Dockerize application (frontend + backend)
- [ ] Create docker-compose.yml
- [ ] Set up environment configurations
- [ ] Database backup strategy
- [ ] Monitoring setup (logs, errors)
- [ ] Health check endpoints

**Day 3-4: Cloud Deployment**
- [ ] Backend deployment:
  - AWS EC2/Elastic Beanstalk or
  - Google Cloud Run or
  - Heroku
- [ ] Frontend deployment:
  - Vercel/Netlify
- [ ] Database hosting:
  - AWS RDS (PostgreSQL)
  - MongoDB Atlas
- [ ] Configure domain and SSL
- [ ] Set up CI/CD pipeline (GitHub Actions)
- [ ] Environment variables management

**Day 5: Production Testing**
- [ ] Smoke testing in production
- [ ] Load testing
- [ ] User acceptance testing
- [ ] Bug fixes
- [ ] Performance monitoring
- [ ] Error tracking setup (Sentry)

**Day 6-7: Final Presentation Preparation**
- [ ] Project report writing:
  - Abstract
  - Introduction
  - Literature review
  - Methodology
  - Results and discussion
  - Conclusion
  - Future work
  - References
- [ ] Create presentation slides (PPT)
- [ ] Prepare demo script
- [ ] Record demo video
- [ ] Create project poster (if required)
- [ ] Rehearse presentation

**📌 Week 12 Deliverables:**
- Deployed production application
- CI/CD pipeline
- Final project report
- Presentation materials
- Demo video

---

## 📈 Current Progress

### Completed ✅
- [ ] Project planning and roadmap creation
- [ ] Technology stack selection
- [ ] Dataset acquisition

### In Progress 🔄
- [ ] Exploratory Data Analysis
- [ ] Literature review

### Upcoming 📅
- [ ] Data preprocessing pipeline
- [ ] Model development

### Progress Tracking
```
Overall Progress: [██░░░░░░░░] 20%

Week 1-2:  [████████░░] 80%
Week 3-4:  [░░░░░░░░░░] 0%
Week 5-6:  [░░░░░░░░░░] 0%
Week 7-8:  [░░░░░░░░░░] 0%
Week 9-10: [░░░░░░░░░░] 0%
Week 11:   [░░░░░░░░░░] 0%
Week 12:   [░░░░░░░░░░] 0%
```

---

## 🚀 Installation & Setup

### Prerequisites
```bash
# Python 3.8+
python --version

# Node.js 16+
node --version

# Git
git --version

# Docker (optional but recommended)
docker --version
```

### Backend Setup
```bash
# Clone repository
git clone https://github.com/yourusername/ecg-sleep-apnea-detection.git
cd ecg-sleep-apnea-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configurations

# Run database migrations
python manage.py db upgrade

# Start development server
python app.py
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
# Edit .env.local with your API URL

# Start development server
npm run dev
```

### Using Docker
```bash
# Build and run all services
docker-compose up --build

# Access application
# Frontend: http://localhost:3000
# Backend: http://localhost:5000
# API Docs: http://localhost:5000/docs
```

---

## 👥 Team & Responsibilities

### Project Lead
- Overall project coordination
- Technical decision making
- Progress tracking

### Machine Learning Engineer
- Data preprocessing
- Feature engineering
- Model development and training
- Model optimization

### Backend Developer
- API development
- Database design
- Authentication system
- Deployment

### Frontend Developer
- UI/UX design
- React components
- State management
- Integration with backend

### Documentation & Testing
- Technical documentation
- User documentation
- Test case development
- Quality assurance

---

## 📊 Evaluation Metrics

### Model Performance
- **Accuracy**: Overall correctness
- **Sensitivity (Recall)**: True apnea detection rate
- **Specificity**: True normal detection rate
- **Precision**: Positive predictive value
- **F1-Score**: Harmonic mean of precision and recall
- **AUC-ROC**: Area under ROC curve
- **AUC-PR**: Area under Precision-Recall curve

### Application Performance
- **API Response Time**: < 2 seconds
- **Model Inference Time**: < 1 second
- **Frontend Load Time**: < 3 seconds
- **Uptime**: > 99%

---

## 🔮 Future Enhancements

- [ ] Mobile application (React Native)
- [ ] Real-time ECG monitoring with wearable devices
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Integration with hospital management systems
- [ ] AI-powered report generation
- [ ] Telemedicine consultation integration
- [ ] Severity prediction and trend analysis

---

## 📚 References

1. PhysioNet - APNEA database documentation
2. Pan, J., & Tompkins, W. J. (1985). A real-time QRS detection algorithm
3. Relevant research papers (add as you review)
4. TensorFlow/PyTorch documentation
5. React.js best practices

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

---

## 📧 Contact

**Student Name**: [Your Name]  
**Email**: [your.email@university.edu]  
**Supervisor**: [Ma'am's Name]  
**Institution**: [Your University]  
**Project Duration**: 2.5 Months (January - March 2026)

---

**Last Updated**: January 31, 2026  
**Version**: 1.0  
**Status**: Week 2 - Initial Progress Presentation

---

## 🎯 Quick Start Checklist for Tomorrow's Presentation

- [ ] Review this roadmap thoroughly
- [ ] Prepare 3-4 sample ECG visualizations
- [ ] Create system architecture diagram
- [ ] Show dataset statistics table
- [ ] Prepare mock-up of final UI
- [ ] List all technologies with justification
- [ ] Practice 10-minute presentation
- [ ] Prepare answers for potential questions
- [ ] Print handout of roadmap for ma'am
- [ ] Bring laptop with Jupyter notebook ready

**Good luck with your presentation! 🚀**