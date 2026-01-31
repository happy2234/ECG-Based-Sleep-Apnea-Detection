# Dataset Information

## APNEA HRV+SPO2 Dataset

### Overview
The dataset contains ECG, Heart Rate Variability (HRV), and SpO2 signals for sleep apnea detection.

### Source
- **Database**: PhysioNet / MIT-BIH APNEA Database
- **URL**: https://physionet.org/content/apnea-ecg/

### Dataset Characteristics

#### Signals Included
1. **ECG (Electrocardiogram)**
   - Sampling rate: 100 Hz
   - Duration: Full night recordings
   
2. **HRV (Heart Rate Variability)**
   - Derived from ECG R-R intervals
   
3. **SpO2 (Blood Oxygen Saturation)**
   - Continuous monitoring throughout sleep

#### Classes
- **Normal**: Regular breathing patterns
- **Apnea**: Sleep apnea episodes

### Dataset Structure

```
data/raw/
├── training/
│   ├── *.dat        # ECG signal files
│   ├── *.hea        # Header files
│   └── *.apn        # Annotation files
└── testing/
    └── (same structure)
```

### Preprocessing Requirements

1. Signal cleaning and noise removal
2. R-peak detection
3. HRV feature extraction
4. SpO2 event detection
5. Window-based segmentation

### Citation

Please cite the original dataset:
```
Penzel T, Moody GB, Mark RG, Goldberger AL, Peter JH. 
The Apnea-ECG Database. 
Computers in Cardiology 2000;27:255-258.
```

---

**Note**: Download the dataset from PhysioNet and place files in the appropriate directories before running preprocessing scripts.
