# API Documentation

## ECG-Based Sleep Apnea Detection - REST API

**Base URL**: `http://localhost:5000/api/v1`  
**Production URL**: `https://api.apnea-detection.com/v1`

---

## Authentication

All API requests (except login/register) require JWT authentication.

### Headers:
```
Authorization: Bearer <jwt_token>
Content-Type: application/json
```

---

## Endpoints

### 1. Authentication

#### POST /auth/register
Register a new user account.

**Request:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePassword123!",
  "role": "user"
}
```

**Response:** `201 Created`
```json
{
  "success": true,
  "message": "User registered successfully",
  "user_id": 123,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

#### POST /auth/login
Authenticate user and receive JWT token.

**Request:**
```json
{
  "email": "john@example.com",
  "password": "SecurePassword123!"
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 86400,
  "user": {
    "user_id": 123,
    "username": "john_doe",
    "email": "john@example.com",
    "role": "user"
  }
}
```

---

#### POST /auth/refresh
Refresh JWT token using refresh token.

**Request:**
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 86400
}
```

---

### 2. Patients

#### POST /patients
Create a new patient record.

**Request:**
```json
{
  "name": "Jane Smith",
  "age": 45,
  "gender": "female",
  "medical_history": "Hypertension, Type 2 Diabetes"
}
```

**Response:** `201 Created`
```json
{
  "success": true,
  "patient_id": 456,
  "message": "Patient created successfully"
}
```

---

#### GET /patients
Get all patients for the authenticated user.

**Response:** `200 OK`
```json
{
  "success": true,
  "count": 2,
  "patients": [
    {
      "patient_id": 456,
      "name": "Jane Smith",
      "age": 45,
      "gender": "female",
      "created_at": "2026-01-31T10:30:00Z"
    }
  ]
}
```

---

#### GET /patients/{patient_id}
Get specific patient details.

**Response:** `200 OK`
```json
{
  "success": true,
  "patient": {
    "patient_id": 456,
    "name": "Jane Smith",
    "age": 45,
    "gender": "female",
    "medical_history": "Hypertension, Type 2 Diabetes",
    "created_at": "2026-01-31T10:30:00Z",
    "total_sessions": 5,
    "last_session": "2026-01-31T15:20:00Z"
  }
}
```

---

### 3. Signal Upload & Processing

#### POST /upload/ecg
Upload ECG signal file for analysis.

**Request:** `multipart/form-data`
```
patient_id: 456
file: ecg_signal.dat (binary)
metadata: {
  "sampling_rate": 100,
  "duration_sec": 3600,
  "device": "Holter Monitor X200"
}
```

**Response:** `202 Accepted`
```json
{
  "success": true,
  "session_id": 789,
  "message": "File uploaded successfully. Processing started.",
  "status_url": "/api/v1/sessions/789/status"
}
```

---

#### GET /sessions/{session_id}/status
Check processing status of uploaded signal.

**Response:** `200 OK`
```json
{
  "success": true,
  "session_id": 789,
  "status": "processing",
  "progress": 65,
  "estimated_time_remaining_sec": 45,
  "current_step": "Feature extraction"
}
```

**Possible status values:**
- `uploaded`: File received
- `preprocessing`: Signal cleaning in progress
- `feature_extraction`: Extracting HRV and other features
- `prediction`: Running ML models
- `completed`: Analysis complete
- `failed`: Processing error occurred

---

### 4. Predictions & Results

#### GET /results/{session_id}
Get prediction results for a completed session.

**Response:** `200 OK`
```json
{
  "success": true,
  "result": {
    "result_id": 1001,
    "session_id": 789,
    "prediction": "Apnea",
    "confidence_score": 0.87,
    "severity": "Moderate",
    "apnea_events": {
      "total_count": 42,
      "per_hour": 7.0,
      "average_duration_sec": 18.5
    },
    "hrv_metrics": {
      "mean_rr": 825,
      "sdnn": 35.2,
      "rmssd": 28.1,
      "lf_hf_ratio": 2.3
    },
    "created_at": "2026-01-31T16:45:00Z"
  }
}
```

---

#### GET /patients/{patient_id}/results
Get all results for a specific patient.

**Query Parameters:**
- `limit`: Number of results (default: 10, max: 100)
- `offset`: Pagination offset (default: 0)
- `sort`: Sort order (`asc` or `desc`, default: `desc`)

**Response:** `200 OK`
```json
{
  "success": true,
  "count": 5,
  "results": [
    {
      "result_id": 1001,
      "session_id": 789,
      "prediction": "Apnea",
      "confidence_score": 0.87,
      "created_at": "2026-01-31T16:45:00Z"
    }
  ]
}
```

---

### 5. Analytics

#### GET /analytics/overview
Get overall system analytics (admin only).

**Response:** `200 OK`
```json
{
  "success": true,
  "analytics": {
    "total_users": 1250,
    "total_patients": 3420,
    "total_sessions": 8750,
    "total_predictions": 8500,
    "apnea_detection_rate": 0.42,
    "average_processing_time_sec": 125.3,
    "model_accuracy": 0.94
  }
}
```

---

#### GET /analytics/patient/{patient_id}/history
Get patient's historical analysis data.

**Response:** `200 OK`
```json
{
  "success": true,
  "patient_id": 456,
  "history": [
    {
      "date": "2026-01-31",
      "prediction": "Apnea",
      "apnea_events_per_hour": 7.0,
      "confidence_score": 0.87
    },
    {
      "date": "2026-01-15",
      "prediction": "Normal",
      "apnea_events_per_hour": 2.1,
      "confidence_score": 0.92
    }
  ],
  "trends": {
    "improving": false,
    "average_events_per_hour": 5.2
  }
}
```

---

### 6. Reports

#### GET /reports/{session_id}/pdf
Generate and download PDF report.

**Response:** `200 OK`
- Content-Type: `application/pdf`
- Content-Disposition: `attachment; filename="apnea_report_789.pdf"`

---

#### POST /reports/{session_id}/email
Email report to patient or doctor.

**Request:**
```json
{
  "recipient_email": "doctor@hospital.com",
  "include_raw_data": false,
  "message": "Patient report attached"
}
```

**Response:** `200 OK`
```json
{
  "success": true,
  "message": "Report sent successfully to doctor@hospital.com"
}
```

---

### 7. Model Information

#### GET /models/info
Get information about deployed ML models.

**Response:** `200 OK`
```json
{
  "success": true,
  "models": [
    {
      "name": "CNN-LSTM Hybrid",
      "version": "2.1.0",
      "accuracy": 0.94,
      "precision": 0.92,
      "recall": 0.91,
      "f1_score": 0.915,
      "last_updated": "2026-01-15T00:00:00Z",
      "is_active": true
    },
    {
      "name": "Random Forest",
      "version": "1.5.2",
      "accuracy": 0.89,
      "is_active": true,
      "use_case": "Fallback model"
    }
  ]
}
```

---

## Error Responses

### Standard Error Format:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input parameters",
    "details": {
      "field": "email",
      "issue": "Invalid email format"
    }
  }
}
```

### Error Codes:

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `UNAUTHORIZED` | 401 | Invalid or missing authentication token |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `NOT_FOUND` | 404 | Resource not found |
| `VALIDATION_ERROR` | 400 | Invalid request parameters |
| `PROCESSING_ERROR` | 500 | Error during signal processing |
| `MODEL_ERROR` | 500 | ML model inference failed |
| `DATABASE_ERROR` | 500 | Database operation failed |
| `RATE_LIMIT_EXCEEDED` | 429 | Too many requests |

---

## Rate Limiting

- **Authenticated users**: 100 requests/minute
- **File uploads**: 10 uploads/hour per user
- **Report generation**: 20 reports/day per user

Rate limit headers included in all responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1643657400
```

---

## Pagination

For endpoints returning lists:

**Query Parameters:**
- `limit`: Items per page (default: 10, max: 100)
- `offset`: Starting position (default: 0)

**Response includes:**
```json
{
  "success": true,
  "pagination": {
    "total": 250,
    "limit": 10,
    "offset": 0,
    "has_more": true
  },
  "data": [...]
}
```

---

## WebSocket Support (Future)

Real-time processing updates via WebSocket:

```javascript
const ws = new WebSocket('ws://localhost:5000/ws/session/789');

ws.onmessage = (event) => {
  const update = JSON.parse(event.data);
  console.log('Processing progress:', update.progress);
};
```

---

**Last Updated**: January 31, 2026  
**API Version**: 1.0  
**Contact**: gauravjangra1110@gmail.com
