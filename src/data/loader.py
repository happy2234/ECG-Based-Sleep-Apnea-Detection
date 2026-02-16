import numpy as np
import scipy.io
from pathlib import Path
from typing import Tuple, Optional, Dict, List, Any
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APNEADataLoader:
    """
    Data loader for APNEA HRV+SPO2 dataset using .mat files.
    """
    
    def __init__(self, data_dir: str):
        """
        Initialize the data loader.
        
        Args:
            data_dir: Path to directory containing APNEA dataset (root with RR, SAT, LABELS)
        """
        self.data_dir = Path(data_dir)
        
        if not self.data_dir.exists():
            logger.warning(f"Data directory {self.data_dir} does not exist")
    
    def get_record_list(self) -> List[str]:
        """Get list of available records (filenames without extension)."""
        rr_dir = self.data_dir / "RR"
        if not rr_dir.exists():
            return []
        mat_files = list(rr_dir.glob('*.mat'))
        return sorted([f.stem for f in mat_files])
    
    def load_mat_data(self, record_name: str, subfolder: str) -> Optional[np.ndarray]:
        """Load data from a specific .mat file."""
        path = self.data_dir / subfolder / f"{record_name}.mat"
        if not path.exists():
            return None
            
        try:
            mat = scipy.io.loadmat(str(path))
            # Find the first key that doesn't start with __
            keys = [k for k in mat.keys() if not k.startswith('__')]
            if not keys:
                return None
            
            data = mat[keys[0]]
            # Handle potential cell arrays or nested structures
            if data.dtype == 'O':
                valid = [c.flatten() for c in data.flatten() if c.size > 0]
                if valid:
                    return np.concatenate(valid)
                return None
            return data.flatten()
        except Exception as e:
            logger.error(f"Error loading {path}: {e}")
            return None

    def segment_signal(self, signal: np.ndarray, segment_size: int, overlap: int = 0) -> np.ndarray:
        """Segment 1D signal into windows."""
        if len(signal) < segment_size:
            return np.array([])
            
        step = segment_size - overlap
        n_segments = (len(signal) - overlap) // step
        
        segments = []
        for i in range(n_segments):
            start = i * step
            end = start + segment_size
            segments.append(signal[start:end])
            
        return np.array(segments)

    def get_segmented_dataset(self, record_names: List[str], segment_seconds: int = 60) -> Tuple[np.ndarray, np.ndarray]:
        """Load and segment records into sequences."""
        X_segments = []
        y_labels = []
        
        for name in record_names:
            # We use RR as the primary signal for CNN-LSTM sequence
            # Sampling rate for RR is effectively 1Hz for this dataset's processing?
            # Actually, let's assume 1 sample per second as a baseline for the RR sequence
            rr_signal = self.load_mat_data(name, "RR")
            if rr_signal is None or len(rr_signal) < segment_seconds:
                continue
            
            # Label from filename prefix: C=0, D/ND=1
            label = 0 if name.startswith('C') else 1
            
            # Segment RR signal
            segments = self.segment_signal(rr_signal, segment_seconds)
            if len(segments) > 0:
                X_segments.extend(segments)
                y_labels.extend([label] * len(segments))
                
        return np.array(X_segments), np.array(y_labels)

def load_dataset_summary(data_dir: str) -> Dict:
    """Load summary information for entire dataset."""
    loader = APNEADataLoader(data_dir)
    records = loader.get_record_list()
    return {
        'total_records': len(records),
        'record_names': records
    }
