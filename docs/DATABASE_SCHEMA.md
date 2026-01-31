# Database Schema Documentation

## Overview

The system uses a hybrid database approach:
- **PostgreSQL**: Structured relational data (users, sessions, results)
- **MongoDB**: Unstructured signal data (ECG, HRV, SpO2)
- **Redis**: Caching and session management

---

## PostgreSQL Schema

### 1. Users Table

Stores user authentication and profile information.

```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'user' CHECK (role IN ('user', 'admin', 'doctor')),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT username_length CHECK (LENGTH(username) >= 3),
    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
```

**Columns:**
- `user_id`: Auto-incrementing primary key
- `username`: Unique username (min 3 chars)
- `email`: Unique email address
- `password_hash`: Bcrypt hashed password
- `role`: User role (user/admin/doctor)
- `is_active`: Account status
- `created_at`: Registration timestamp
- `last_login`: Last login timestamp
- `updated_at`: Last profile update

---

### 2. Patients Table

Stores patient demographic and medical information.

```sql
CREATE TABLE patients (
    patient_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE,
    age INTEGER,
    gender VARCHAR(10) CHECK (gender IN ('male', 'female', 'other')),
    height_cm DECIMAL(5,2),
    weight_kg DECIMAL(5,2),
    bmi DECIMAL(4,2),
    medical_history TEXT,
    allergies TEXT,
    current_medications TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT age_range CHECK (age >= 0 AND age <= 150)
);

CREATE INDEX idx_patients_user_id ON patients(user_id);
CREATE INDEX idx_patients_name ON patients(name);
```

**Columns:**
- `patient_id`: Auto-incrementing primary key
- `user_id`: Reference to owning user
- `name`: Patient full name
- `date_of_birth`: Birth date
- `age`: Calculated or manual age
- `gender`: Patient gender
- `height_cm`: Height in centimeters
- `weight_kg`: Weight in kilograms
- `bmi`: Body Mass Index
- `medical_history`: Relevant medical conditions
- `allergies`: Known allergies
- `current_medications`: Current medication list

---

### 3. Sessions Table

Stores ECG analysis session information.

```sql
CREATE TABLE sessions (
    session_id SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(patient_id) ON DELETE CASCADE,
    signal_file_id VARCHAR(100), -- MongoDB ObjectId reference
    upload_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    processing_started_at TIMESTAMP,
    processing_completed_at TIMESTAMP,
    processing_time_sec FLOAT,
    status VARCHAR(20) DEFAULT 'uploaded' CHECK (status IN 
        ('uploaded', 'preprocessing', 'feature_extraction', 
         'prediction', 'completed', 'failed')),
    error_message TEXT,
    device_info JSONB,
    sampling_rate INTEGER,
    duration_sec INTEGER,
    signal_quality_score DECIMAL(3,2),
    
    CONSTRAINT valid_quality_score CHECK (signal_quality_score >= 0 AND signal_quality_score <= 1)
);

CREATE INDEX idx_sessions_patient_id ON sessions(patient_id);
CREATE INDEX idx_sessions_status ON sessions(status);
CREATE INDEX idx_sessions_upload_timestamp ON sessions(upload_timestamp DESC);
```

**Columns:**
- `session_id`: Auto-incrementing primary key
- `patient_id`: Reference to patient
- `signal_file_id`: MongoDB ObjectId for signal data
- `upload_timestamp`: When file was uploaded
- `processing_started_at`: Processing start time
- `processing_completed_at`: Processing completion time
- `processing_time_sec`: Total processing duration
- `status`: Current processing status
- `error_message`: Error details if failed
- `device_info`: JSON metadata about recording device
- `sampling_rate`: Signal sampling rate (Hz)
- `duration_sec`: Signal duration in seconds
- `signal_quality_score`: Automated quality assessment (0-1)

---

### 4. Results Table

Stores prediction results and analysis outcomes.

```sql
CREATE TABLE results (
    result_id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL UNIQUE REFERENCES sessions(session_id) ON DELETE CASCADE,
    prediction VARCHAR(20) NOT NULL CHECK (prediction IN ('Normal', 'Apnea')),
    confidence_score DECIMAL(5,4) NOT NULL,
    severity VARCHAR(20) CHECK (severity IN ('None', 'Mild', 'Moderate', 'Severe')),
    apnea_events_count INTEGER DEFAULT 0,
    apnea_events_per_hour DECIMAL(5,2),
    average_event_duration_sec DECIMAL(5,2),
    longest_event_duration_sec DECIMAL(5,2),
    oxygen_desaturation_index DECIMAL(5,2),
    model_used VARCHAR(50),
    model_version VARCHAR(20),
    features_file_id VARCHAR(100), -- MongoDB ObjectId for extracted features
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT valid_confidence CHECK (confidence_score >= 0 AND confidence_score <= 1),
    CONSTRAINT valid_event_count CHECK (apnea_events_count >= 0)
);

CREATE INDEX idx_results_session_id ON results(session_id);
CREATE INDEX idx_results_prediction ON results(prediction);
CREATE INDEX idx_results_created_at ON results(created_at DESC);
```

**Columns:**
- `result_id`: Auto-incrementing primary key
- `session_id`: One-to-one reference to session
- `prediction`: Binary classification result
- `confidence_score`: Model confidence (0-1)
- `severity`: Apnea severity classification
- `apnea_events_count`: Total number of events detected
- `apnea_events_per_hour`: AHI (Apnea-Hypopnea Index)
- `average_event_duration_sec`: Mean event duration
- `longest_event_duration_sec`: Maximum event duration
- `oxygen_desaturation_index`: ODI metric
- `model_used`: Name of ML model used
- `model_version`: Version of model
- `features_file_id`: MongoDB reference for features

---

### 5. HRV_Metrics Table

Stores detailed Heart Rate Variability metrics.

```sql
CREATE TABLE hrv_metrics (
    hrv_id SERIAL PRIMARY KEY,
    session_id INTEGER NOT NULL UNIQUE REFERENCES sessions(session_id) ON DELETE CASCADE,
    
    -- Time-domain metrics
    mean_rr_ms DECIMAL(8,2),
    sdnn_ms DECIMAL(8,2),
    rmssd_ms DECIMAL(8,2),
    pnn50_percent DECIMAL(5,2),
    sdsd_ms DECIMAL(8,2),
    mean_hr_bpm DECIMAL(5,2),
    min_hr_bpm DECIMAL(5,2),
    max_hr_bpm DECIMAL(5,2),
    
    -- Frequency-domain metrics
    lf_power DECIMAL(10,2),
    hf_power DECIMAL(10,2),
    lf_hf_ratio DECIMAL(6,3),
    total_power DECIMAL(10,2),
    vlf_power DECIMAL(10,2),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_hrv_session_id ON hrv_metrics(session_id);
```

**Columns:**
- Time-domain: SDNN, RMSSD, pNN50, heart rate stats
- Frequency-domain: LF, HF, LF/HF ratio, total power

---

### 6. Audit_Log Table

Stores system audit trail for security and compliance.

```sql
CREATE TABLE audit_log (
    log_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE SET NULL,
    action VARCHAR(50) NOT NULL,
    resource_type VARCHAR(50),
    resource_id INTEGER,
    ip_address INET,
    user_agent TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details JSONB
);

CREATE INDEX idx_audit_user_id ON audit_log(user_id);
CREATE INDEX idx_audit_timestamp ON audit_log(timestamp DESC);
CREATE INDEX idx_audit_action ON audit_log(action);
```

---

## MongoDB Collections

### 1. ecg_signals Collection

Stores raw ECG signal data.

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439011"),
  session_id: 789,
  sampling_rate: 100,
  duration_sec: 3600,
  signal_data: {
    ecg: [Array of signal values],  // Compressed or chunked
    timestamps: [Array of timestamps]
  },
  metadata: {
    device: "Holter Monitor X200",
    software_version: "2.1.0",
    recording_location: "Hospital ABC",
    quality_score: 0.95,
    noise_level: "low"
  },
  preprocessing: {
    filtered: true,
    baseline_corrected: true,
    normalized: true,
    filters_applied: ["bandpass_0.5-40Hz", "notch_60Hz"]
  },
  created_at: ISODate("2026-01-31T16:30:00Z"),
  updated_at: ISODate("2026-01-31T16:35:00Z")
}
```

**Indexes:**
```javascript
db.ecg_signals.createIndex({ session_id: 1 }, { unique: true });
db.ecg_signals.createIndex({ created_at: -1 });
```

---

### 2. hrv_features Collection

Stores extracted HRV and other features.

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439012"),
  session_id: 789,
  
  time_domain_features: {
    mean_rr: 850.5,
    sdnn: 45.2,
    rmssd: 38.5,
    pnn50: 12.3,
    sdsd: 35.1,
    nn50: 156,
    nn20: 289
  },
  
  frequency_domain_features: {
    vlf_power: 245.3,
    lf_power: 125.3,
    hf_power: 89.7,
    lf_hf_ratio: 1.4,
    total_power: 460.3,
    lf_nu: 58.3,
    hf_nu: 41.7
  },
  
  nonlinear_features: {
    sd1: 27.3,
    sd2: 56.8,
    sd1_sd2_ratio: 0.48,
    sample_entropy: 1.23,
    approximate_entropy: 0.98,
    dfa_alpha1: 1.12,
    dfa_alpha2: 0.87
  },
  
  morphological_features: {
    qrs_duration_avg: 95.2,
    qt_interval_avg: 385.4,
    pr_interval_avg: 165.3,
    p_wave_amplitude_avg: 0.12,
    t_wave_amplitude_avg: 0.35
  },
  
  created_at: ISODate("2026-01-31T16:35:00Z")
}
```

**Indexes:**
```javascript
db.hrv_features.createIndex({ session_id: 1 }, { unique: true });
```

---

### 3. spo2_data Collection

Stores SpO2 (oxygen saturation) data.

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439013"),
  session_id: 789,
  sampling_rate: 1,  // 1 Hz typical for SpO2
  duration_sec: 3600,
  
  spo2_values: [98, 97, 98, 96, 94, 92, 91, 93, ...],  // Array of percentages
  timestamps: [Array of corresponding timestamps],
  
  statistics: {
    mean_spo2: 95.3,
    min_spo2: 85,
    max_spo2: 99,
    std_spo2: 3.2,
    desaturation_events_count: 15,
    time_below_90_percent: 240  // seconds
  },
  
  desaturation_events: [
    {
      start_time: 1200,
      duration_sec: 18,
      min_spo2: 85,
      baseline_spo2: 96,
      recovery_time_sec: 45
    }
  ],
  
  created_at: ISODate("2026-01-31T16:35:00Z")
}
```

---

### 4. model_predictions Collection

Stores detailed prediction information and intermediate results.

```javascript
{
  _id: ObjectId("507f1f77bcf86cd799439014"),
  session_id: 789,
  result_id: 1001,
  
  model_info: {
    name: "CNN-LSTM Hybrid",
    version: "2.1.0",
    architecture: "cnn_lstm_v2"
  },
  
  prediction: {
    class: "Apnea",
    confidence: 0.87,
    probabilities: {
      Normal: 0.13,
      Apnea: 0.87
    }
  },
  
  event_timeline: [
    {
      timestamp: 1234,
      event_type: "apnea",
      duration_sec: 18,
      confidence: 0.92
    }
  ],
  
  feature_importance: {
    lf_hf_ratio: 0.23,
    mean_rr: 0.18,
    spo2_mean: 0.15,
    ...
  },
  
  created_at: ISODate("2026-01-31T16:40:00Z")
}
```

---

## Redis Cache Structure

### Session Cache
```
Key: session:{user_id}:{token_hash}
Value: {user_id, username, role, exp}
TTL: 86400 (24 hours)
```

### Result Cache
```
Key: result:{session_id}
Value: {prediction, confidence, apnea_count, ...}
TTL: 3600 (1 hour)
```

### Rate Limiting
```
Key: ratelimit:{user_id}:{endpoint}
Value: request_count
TTL: 60 (1 minute)
```

---

## Database Relationships

```
users (1) ──→ (N) patients
patients (1) ──→ (N) sessions
sessions (1) ──→ (1) results
sessions (1) ──→ (1) hrv_metrics
sessions (1) ──→ (1) ecg_signals [MongoDB]
sessions (1) ──→ (1) hrv_features [MongoDB]
sessions (1) ──→ (1) spo2_data [MongoDB]
```

---

## Backup and Maintenance

### PostgreSQL
- Daily full backups
- Point-in-time recovery enabled
- Retention: 30 days

### MongoDB
- Daily snapshots
- Replica set with 3 nodes
- Oplog retention: 7 days

### Redis
- RDB snapshots every 6 hours
- AOF for durability

---

**Last Updated**: January 31, 2026  
**Schema Version**: 1.0
