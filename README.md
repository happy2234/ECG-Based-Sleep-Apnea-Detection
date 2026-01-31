# ECG-Based Sleep Apnea Detection System

![Project Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Timeline](https://img.shields.io/badge/Timeline-2.5%20Months-blue)
![Tech Stack](https://img.shields.io/badge/Stack-Full--Stack-green)

## 🎯 Project Overview

An end-to-end full-stack web application for automated detection of sleep apnea episodes using ECG, HRV (Heart Rate Variability), and SpO2 (Blood Oxygen Saturation) signals with machine learning/deep learning models.

### Problem Statement
Sleep apnea is a serious sleep disorder affecting millions globally. Traditional diagnosis requires expensive overnight polysomnography tests. This project aims to create an accessible, automated screening tool using ECG-based signals.

### Key Features
- ✅ Automated sleep apnea detection from ECG signals
- ✅ Real-time signal processing and analysis
- ✅ Interactive web-based user interface
- ✅ Historical data tracking and analytics
- ✅ Comprehensive reporting with visualizations
- ✅ RESTful API for integration capabilities

## 📊 Dataset

**APNEA HRV+SPO2 Dataset**
- Source: PhysioNet / MIT-BIH Database
- Signals: ECG, Heart Rate Variability (HRV), SpO2
- Classes: Apnea episodes vs Normal breathing

## 🛠 Technology Stack

### Machine Learning & Data Processing
- Python 3.8+, NumPy, Pandas, SciPy
- Scikit-learn, TensorFlow/Keras
- BiospPy, NeuroKit2, WFDB

### Backend Development
- Framework: Flask/FastAPI
- Database: PostgreSQL + MongoDB
- Authentication: JWT tokens
- Task Queue: Celery, Redis

### Frontend Development
- React.js 18+
- Tailwind CSS + shadcn/ui
- State Management: Redux Toolkit
- Charting: Recharts, Plotly.js

## 📁 Project Structure

```
ECG-Based Sleep Apnea Detection/
├── data/
│   ├── raw/              # Raw dataset files
│   ├── processed/        # Preprocessed data
│   └── external/         # External datasets
├── notebooks/            # Jupyter notebooks for EDA
├── src/
│   ├── data/            # Data loading and processing
│   ├── features/        # Feature extraction
│   ├── models/          # ML/DL models
│   ├── api/             # Backend API
│   └── utils/           # Utility functions
├── tests/               # Unit tests
├── docs/                # Documentation
├── config/              # Configuration files
├── frontend/            # React frontend
├── backend/             # Flask/FastAPI backend
├── requirements.txt     # Python dependencies
└── README.md
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Setup Instructions

1. **Clone the repository**
```bash
git clone <repository-url>
cd "ECG-Based Sleep Apnea Detection"
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download dataset**
- Visit PhysioNet APNEA database
- Place files in `data/raw/` directory

5. **Run initial setup**
```bash
# Run data exploration notebook
jupyter notebook notebooks/01_EDA.ipynb
```

## 📈 Current Progress

### Week 1-2: Foundation & Exploration ✅ (In Progress)

#### Week 1 Completed
- [x] Project setup and structure
- [x] GitHub repository initialization
- [x] Virtual environment setup
- [x] Requirements installation
- [ ] Dataset acquisition
- [ ] Literature review

#### Week 2 In Progress
- [ ] Exploratory Data Analysis
- [ ] Signal visualization
- [ ] Statistical analysis
- [ ] System design documentation

## 🗺 Roadmap

- **Week 1-2**: Foundation & Exploration (Current)
- **Week 3-4**: Data Preprocessing & Feature Engineering
- **Week 5-6**: Model Development & Training
- **Week 7-8**: Backend Development
- **Week 9**: Frontend Development
- **Week 10**: Integration & Testing

## 📝 Documentation

- [Project Plan](./Untitled.md) - Full roadmap and timeline
- [Dataset Info](./docs/dataset.md) - Dataset details (Coming soon)
- [API Documentation](./docs/api.md) - API endpoints (Coming soon)

## 🧪 Testing

```bash
# Run tests
pytest tests/

# With coverage
pytest --cov=src tests/
```

## 🤝 Contributing

This is an academic/research project. For collaboration inquiries, please reach out.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

**Author**: happy2234  
**Email**: gauravjangra1110@gmail.com

For questions or collaboration, please contact the project team.

---

**Last Updated**: January 31, 2026
