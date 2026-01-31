# System Architecture

## ECG-Based Sleep Apnea Detection System

### Architecture Overview

The system follows a microservices architecture with clear separation between frontend, backend, ML services, and databases.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    CLIENT LAYER (Frontend)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Dashboard   │  │ Upload Page  │  │   Reports    │          │
│  │   (React)    │  │   (React)    │  │   (React)    │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                  │                  │                  │
└─────────┼──────────────────┼──────────────────┼──────────────────┘
          │    HTTPS/REST    │                  │
┌─────────▼──────────────────▼──────────────────▼──────────────────┐
│                   API GATEWAY LAYER                              │
│              (Flask/FastAPI with NGINX)                          │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │   Authentication Middleware (JWT)                        │   │
│  │   Rate Limiting & CORS                                   │   │
│  │   Request Validation                                     │   │
│  └──────────────────────────────────────────────────────────┘   │
└────────┬─────────────────┬─────────────────┬─────────────────────┘
         │                 │                 │
    ┌────▼────┐      ┌─────▼─────┐    ┌─────▼─────┐
    │  Auth   │      │Prediction │    │ Analytics │
    │ Service │      │  Service  │    │  Service  │
    └────┬────┘      └─────┬─────┘    └─────┬─────┘
         │                 │                 │
         │          ┌──────▼──────┐          │
         │          │  ML LAYER   │          │
         │          │┌───────────┐│          │
         │          ││Preprocessing││         │
         │          ││  Pipeline  ││          │
         │          │└───────────┘│          │
         │          │┌───────────┐│          │
         │          ││  Feature  ││          │
         │          ││Extraction ││          │
         │          │└───────────┘│          │
         │          │┌───────────┐│          │
         │          ││CNN-LSTM   ││          │
         │          ││  Model    ││          │
         │          │└───────────┘│          │
         │          │┌───────────┐│          │
         │          ││  Random   ││          │
         │          ││  Forest   ││          │
         │          │└───────────┘│          │
         │          └─────────────┘          │
         │                                    │
    ┌────▼──────────────────────────────────▼────┐
    │          DATABASE LAYER                     │
    │  ┌──────────────┐      ┌──────────────┐    │
    │  │ PostgreSQL   │      │  MongoDB     │    │
    │  │ (User Data)  │      │ (Signals)    │    │
    │  │ - Users      │      │ - ECG Data   │    │
    │  │ - Sessions   │      │ - HRV Data   │    │
    │  │ - Results    │      │ - SpO2 Data  │    │
    │  └──────────────┘      └──────────────┘    │
    │  ┌──────────────┐                           │
    │  │    Redis     │                           │
    │  │   (Cache)    │                           │
    │  │ - Sessions   │                           │
    │  │ - Results    │                           │
    │  └──────────────┘                           │
    └─────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend Layer (React.js)

#### Technologies:
- React 18+
- Tailwind CSS + shadcn/ui
- Redux Toolkit for state management
- Recharts/Plotly.js for visualizations
- Axios for API calls

#### Key Components:
- **Dashboard**: Overview of patient history and statistics
- **Upload Page**: ECG signal upload and validation
- **Analysis Page**: Real-time signal processing visualization
- **Results Page**: Apnea detection results with charts
- **Reports Page**: Downloadable PDF reports

### 2. Backend Layer (Flask/FastAPI)

#### Technologies:
- Flask 3.x or FastAPI 0.100+
- SQLAlchemy for ORM
- JWT for authentication
- Celery for async tasks
- NGINX as reverse proxy

#### Microservices:

**Authentication Service**
- User registration/login
- JWT token management
- Role-based access control (RBAC)

**Prediction Service**
- Signal upload handling
- Preprocessing coordination
- Model inference
- Result storage

**Analytics Service**
- Historical data analysis
- Performance metrics
- Report generation

### 3. ML/DL Processing Layer

#### Preprocessing Pipeline:
```python
Input Signal → Noise Filtering → Baseline Correction → 
Normalization → R-Peak Detection → Feature Extraction → 
Model Input
```

#### Models:

**Primary Model: CNN-LSTM Hybrid**
- CNN layers for spatial feature extraction
- LSTM layers for temporal dependencies
- Dropout for regularization
- Softmax output for binary classification

**Secondary Model: Random Forest**
- Ensemble of 100+ decision trees
- Feature importance analysis
- Fallback for real-time predictions

### 4. Database Layer

#### PostgreSQL Schema:

**Users Table**
```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
```

**Patients Table**
```sql
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    name VARCHAR(100) NOT NULL,
    age INTEGER,
    gender VARCHAR(10),
    medical_history TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Sessions Table**
```sql
CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    signal_file_id VARCHAR(100), -- MongoDB ObjectId
    status VARCHAR(20), -- 'processing', 'completed', 'failed'
    processing_time_sec FLOAT
);
```

**Results Table**
```sql
CREATE TABLE results (
    result_id SERIAL PRIMARY KEY,
    session_id INTEGER REFERENCES sessions(session_id),
    prediction VARCHAR(20), -- 'Normal', 'Apnea'
    confidence_score FLOAT,
    apnea_events_count INTEGER,
    severity VARCHAR(20), -- 'Mild', 'Moderate', 'Severe'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### MongoDB Collections:

**ECG_Signals**
```json
{
    "_id": ObjectId,
    "session_id": "reference_to_session",
    "sampling_rate": 100,
    "duration_sec": 3600,
    "signal_data": [array of values],
    "metadata": {
        "device": "string",
        "quality_score": 0.95
    },
    "created_at": ISODate
}
```

**HRV_Features**
```json
{
    "_id": ObjectId,
    "session_id": "reference_to_session",
    "time_domain": {
        "mean_rr": 850,
        "sdnn": 45.2,
        "rmssd": 38.5,
        "pnn50": 12.3
    },
    "frequency_domain": {
        "lf": 125.3,
        "hf": 89.7,
        "lf_hf_ratio": 1.4
    },
    "created_at": ISODate
}
```

### 5. Caching Layer (Redis)

**Cache Strategy:**
- Session data: TTL 24 hours
- Recent predictions: TTL 1 hour
- User preferences: TTL 7 days

## Data Flow

### Upload and Prediction Flow:

```
1. User uploads ECG file (Frontend)
   ↓
2. API Gateway validates file (Backend)
   ↓
3. Store raw signal in MongoDB
   ↓
4. Create session record in PostgreSQL
   ↓
5. Queue preprocessing task (Celery)
   ↓
6. Preprocessing pipeline executes
   ↓
7. Feature extraction
   ↓
8. Model inference (CNN-LSTM)
   ↓
9. Store results in PostgreSQL
   ↓
10. Store processed features in MongoDB
   ↓
11. Cache result in Redis
   ↓
12. Return prediction to frontend
```

## Security Architecture

### Authentication & Authorization:
- JWT tokens with 24-hour expiry
- Refresh tokens for extended sessions
- Password hashing with bcrypt
- HTTPS only communication
- CORS configured for frontend origin

### Data Protection:
- At-rest encryption for sensitive data
- In-transit TLS 1.3
- Input validation and sanitization
- SQL injection prevention via ORM
- Rate limiting: 100 requests/minute per user

## Deployment Architecture

### Development Environment:
```
Docker Compose:
  - Frontend container (React dev server)
  - Backend container (Flask debug mode)
  - PostgreSQL container
  - MongoDB container
  - Redis container
```

### Production Environment:
```
AWS/GCP:
  - Frontend: Vercel/Netlify
  - Backend: EC2/Cloud Run with auto-scaling
  - Database: RDS (PostgreSQL) + MongoDB Atlas
  - Cache: ElastiCache (Redis)
  - Load Balancer: ALB/Cloud Load Balancing
  - Storage: S3/Cloud Storage for models
```

## Scalability Considerations

1. **Horizontal Scaling**: Multiple backend instances behind load balancer
2. **Caching**: Redis for frequently accessed data
3. **Async Processing**: Celery workers for long-running tasks
4. **Database Optimization**: Indexing on frequently queried columns
5. **CDN**: Static assets served via CDN

## Monitoring & Logging

- **Application Monitoring**: Prometheus + Grafana
- **Error Tracking**: Sentry
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Metrics**: API response times, prediction accuracy, user activity

## API Endpoints (Preview)

See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) for complete details.

---

**Last Updated**: January 31, 2026  
**Version**: 1.0
