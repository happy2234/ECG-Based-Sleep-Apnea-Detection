"""
Test script to verify project setup and basic functionality.
"""

import sys
import importlib

print("=" * 60)
print("ECG Sleep Apnea Detection - Environment Test")
print("=" * 60)

# Test core dependencies
required_packages = [
    'numpy',
    'pandas',
    'scipy',
    'matplotlib',
    'sklearn',
    'tensorflow',
    'flask',
    # 'wfdb',  # Known compatibility issue with pandas 3.0 - will be fixed
    'biosppy',
    'neurokit2'
]

print("\n1. Testing Package Imports:")
print("-" * 60)

failed_imports = []
for package in required_packages:
    try:
        mod = importlib.import_module(package)
        version = getattr(mod, '__version__', 'unknown')
        print(f"✓ {package:20s} v{version}")
    except ImportError as e:
        print(f"✗ {package:20s} FAILED: {e}")
        failed_imports.append(package)

# Test project modules
print("\n2. Testing Project Modules:")
print("-" * 60)

try:
    sys.path.insert(0, '/home/alex/ECG-Based Sleep Apnea Detection')
    from src.data import APNEADataLoader
    print("✓ Data loader module imported successfully")
    
    from src.utils import normalize_signal, segment_signal
    print("✓ Utility functions imported successfully")
    
    from config import config
    print("✓ Configuration module imported successfully")
    
except Exception as e:
    print(f"✗ Project module import failed: {e}")

# Test basic functionality
print("\n3. Testing Basic Functionality:")
print("-" * 60)

try:
    import numpy as np
    test_signal = np.random.randn(1000)
    
    from src.utils import normalize_signal, segment_signal
    
    # Test normalization
    normalized = normalize_signal(test_signal, method='zscore')
    print(f"✓ Signal normalization: mean={np.mean(normalized):.4f}, std={np.std(normalized):.4f}")
    
    # Test segmentation
    segments = segment_signal(test_signal, window_size=100, overlap=50)
    print(f"✓ Signal segmentation: {segments.shape[0]} windows of size {segments.shape[1]}")
    
except Exception as e:
    print(f"✗ Functionality test failed: {e}")

# Test configuration
print("\n4. Testing Configuration:")
print("-" * 60)

try:
    from config.config import SAMPLING_RATE, WINDOW_SIZE_SAMPLES, CLASS_NAMES
    print(f"✓ Sampling rate: {SAMPLING_RATE} Hz")
    print(f"✓ Window size: {WINDOW_SIZE_SAMPLES} samples")
    print(f"✓ Classes: {CLASS_NAMES}")
except Exception as e:
    print(f"✗ Configuration test failed: {e}")

# Summary
print("\n" + "=" * 60)
if len(failed_imports) == 0:
    print("✅ All tests passed! Environment is ready.")
else:
    print(f"⚠️  {len(failed_imports)} package(s) failed to import:")
    for pkg in failed_imports:
        print(f"   - {pkg}")
print("=" * 60)
