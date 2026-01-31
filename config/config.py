"""
Configuration settings for the ECG Sleep Apnea Detection project.
"""

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories if they don't exist
for dir_path in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, LOGS_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Signal processing parameters
SAMPLING_RATE = 100  # Hz
WINDOW_SIZE_SEC = 60  # seconds
WINDOW_SIZE_SAMPLES = SAMPLING_RATE * WINDOW_SIZE_SEC
OVERLAP = 0.5  # 50% overlap

# Preprocessing parameters
BANDPASS_LOW = 0.5  # Hz
BANDPASS_HIGH = 40  # Hz
NOTCH_FREQ = 60  # Hz (power line interference)

# Feature extraction
HRV_FEATURES = [
    'mean_rr', 'std_rr', 'rmssd', 'sdnn',
    'pnn50', 'lfhf_ratio', 'total_power'
]

# Model parameters
TRAIN_TEST_SPLIT = 0.2
VALIDATION_SPLIT = 0.2
RANDOM_SEED = 42
BATCH_SIZE = 32
EPOCHS = 100
LEARNING_RATE = 0.001

# Class names
CLASS_NAMES = ['Normal', 'Apnea']
N_CLASSES = len(CLASS_NAMES)

# API settings
API_HOST = "0.0.0.0"
API_PORT = 5000
DEBUG = True

# Database settings (for future use)
DB_CONFIG = {
    'postgres': {
        'host': 'localhost',
        'port': 5432,
        'database': 'apnea_db',
        'user': 'postgres',
        'password': 'password'
    },
    'mongodb': {
        'host': 'localhost',
        'port': 27017,
        'database': 'apnea_signals'
    }
}
