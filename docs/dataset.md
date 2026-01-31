# Dataset Documentation

## APNEA HRV+SPO2 Dataset

**Official Source**: Mendeley Data - HuGCDN2014-OXI Database  
**URL**: https://data.mendeley.com/datasets/cdxs63gdzc/1  
**DOI**: 10.17632/cdxs63gdzc.1  
**License**: CC BY 4.0  
**File Size**: ~89.7 MB (ZIP format)  
**Version**: 1 (Published: April 25, 2023)

### Dataset Origin
- **Source Institution**: Dr. Negrín University Hospital (Las Palmas de Gran Canaria, Spain)
- **Contributors**: Gabriel Juliá-Serdá, Javier Navarro-Esteva, Antonio G. Ravelo-García
- **Recording Protocol**: Following American Academia of Sleep Medicine (AASM) guidelines
- **Expert Labeling**: Every minute labeled based on simultaneous polysomnography

### Dataset Characteristics

#### Total Subjects: 83 recordings

**Distribution by Group:**
1. **CONTROL Group**: 38 healthy subjects
   - AHI (Apnea-Hypopnea Index): 0-5 (lower than 5)
   - Status: No sleep apnea

2. **DESATURATING PATIENTS**: 34 OSA (Obstructive Sleep Apnea) patients
   - AHI: 30-106.3 (higher than 25)
   - Characteristic: Show desaturations during apneic episodes

3. **NONDESATURATING PATIENTS**: 11 OSA patients
   - AHI: 26.2-87.5 (higher than 25)
   - Characteristic: Do NOT show desaturations during apneic episodes
   - ODI (Oxygen Desaturation Index): Less than 75% of their AHI
   - 75% of this group: ODI < 7.35, Total apneas < 98

### Signal Information

#### ECG Signal
- **Sampling Rate**: 200 Hz
- **Signal Duration**: Full night recordings (~8 hours each)
- **Total Data Points**: ~5.76 million samples per subject

#### SpO2 Signal
- **Sampling Rate**: 50 Hz
- **Parameter**: Arterial oxygen saturation (%)
- **Total Data Points**: ~1.44 million samples per subject

#### Labeling
- **Granularity**: Per minute
- **Classes**: 
  - Apnea episodes (labeled)
  - Non-apnea episodes (labeled)
- **Annotation Method**: Expert polysomnographic review

### Data Format

```
HuGCDN2014-OXI.zip (89.7 MB)
├── Subject_01/
│   ├── ecg_signal.dat      (ECG data)
│   ├── spo2_signal.dat     (SpO2 data)
│   ├── annotations.txt     (Event labels)
│   └── metadata.json       (Subject info)
├── Subject_02/
│   └── [same structure]
...
└── Subject_83/
    └── [same structure]
```

### Key Statistics

| Metric | Value |
|--------|-------|
| Total Subjects | 83 |
| Healthy Controls | 38 (45.8%) |
| OSA Patients | 45 (54.2%) |
| ECG Sampling Rate | 200 Hz |
| SpO2 Sampling Rate | 50 Hz |
| Avg Recording Duration | ~8 hours |
| Total Data Size | ~89.7 MB |
| Classes | 2 (Apnea/Normal) |

### Usage Instructions

1. **Download Dataset**
   - Visit: https://data.mendeley.com/datasets/cdxs63gdzc/1
   - Click "Download All" to get the ZIP file
   - Extract to `data/raw/` directory

2. **File Organization**
   ```bash
   data/
   └── raw/
       └── HuGCDN2014-OXI/
           ├── Subject_01/
           ├── Subject_02/
           ...
           └── Subject_83/
   ```

3. **Load Data in Python**
   ```python
   import numpy as np
   from src.data.loader import APNEADataLoader
   
   loader = APNEADataLoader(data_dir='data/raw/HuGCDN2014-OXI')
   ecg_signal = loader.load_ecg('Subject_01')
   spo2_signal = loader.load_spo2('Subject_01')
   labels = loader.load_annotations('Subject_01')
   ```

### Data Quality Considerations

- **Expert Validation**: All recordings validated by sleep medicine experts
- **Recording Protocol**: Standard AASM guidelines followed
- **Signal Quality**: Clinical-grade ECG and pulse oximetry recordings
- **Class Imbalance**: Slight imbalance towards OSA patients (54% vs 46%)

### Important Notes

- The dataset contains clinical recordings with ground truth labels
- Suitable for training supervised ML/DL models
- Class imbalance may require SMOTE or weighted loss functions
- High temporal resolution (200 Hz ECG) allows for detailed feature extraction
- Mixed patient groups (desaturating vs non-desaturating) provides diverse apnea patterns

### Citations

If you use this dataset, cite as:

```
Juliá-Serdá, Gabriel; Navarro-Esteva, Javier; Ravelo-García, Antonio G. (2023),
"APNEA HRV+SPO2 DATASET", Mendeley Data, V1, 
doi: 10.17632/cdxs63gdzc.1
```

### References

- American Academy of Sleep Medicine (AASM) guidelines
- Polysomnography standard methodology
- Obstructive Sleep Apnea (OSA) classification
