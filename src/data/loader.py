"""
Data loading utilities for APNEA HRV+SPO2 dataset.

This module provides functions to load and parse ECG signals,
annotations, and metadata from the PhysioNet APNEA database.
"""

import numpy as np
from pathlib import Path
from typing import Tuple, Optional, Dict, List
import wfdb
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APNEADataLoader:
    """
    Data loader for APNEA HRV+SPO2 dataset from PhysioNet.
    
    Attributes:
        data_dir (Path): Directory containing the raw data files
        sampling_rate (int): Expected sampling rate for ECG signals
    """
    
    def __init__(self, data_dir: str, sampling_rate: int = 100):
        """
        Initialize the data loader.
        
        Args:
            data_dir: Path to directory containing APNEA dataset
            sampling_rate: Expected sampling rate (default: 100 Hz)
        """
        self.data_dir = Path(data_dir)
        self.sampling_rate = sampling_rate
        
        if not self.data_dir.exists():
            logger.warning(f"Data directory {self.data_dir} does not exist")
    
    def get_record_list(self) -> List[str]:
        """
        Get list of available records in the data directory.
        
        Returns:
            List of record names (without extensions)
        """
        # Look for .hea files which indicate record names
        header_files = list(self.data_dir.glob('*.hea'))
        record_names = [f.stem for f in header_files]
        
        logger.info(f"Found {len(record_names)} records")
        return sorted(record_names)
    
    def load_record(
        self, 
        record_name: str, 
        channels: Optional[List[int]] = None
    ) -> Tuple[Optional[wfdb.Record], Optional[wfdb.Annotation]]:
        """
        Load a single ECG record with its annotations.
        
        Args:
            record_name: Name of the record (without extension)
            channels: List of channel indices to load (None = all)
        
        Returns:
            Tuple of (record, annotation) or (None, None) if error
        """
        try:
            record_path = str(self.data_dir / record_name)
            
            # Load record
            record = wfdb.rdrecord(record_path, channels=channels)
            logger.info(f"Loaded record {record_name}: {record.sig_len} samples")
            
            # Load annotations
            try:
                annotation = wfdb.rdann(record_path, 'apn')
                logger.info(f"Loaded {len(annotation.sample)} annotations")
            except FileNotFoundError:
                logger.warning(f"No annotations found for {record_name}")
                annotation = None
            
            return record, annotation
            
        except Exception as e:
            logger.error(f"Error loading record {record_name}: {e}")
            return None, None
    
    def extract_signals(
        self, 
        record: wfdb.Record
    ) -> Dict[str, np.ndarray]:
        """
        Extract signals from a WFDB record.
        
        Args:
            record: WFDB record object
        
        Returns:
            Dictionary mapping signal names to arrays
        """
        signals = {}
        
        for i, sig_name in enumerate(record.sig_name):
            signals[sig_name] = record.p_signal[:, i]
        
        return signals
    
    def extract_annotations(
        self, 
        annotation: wfdb.Annotation
    ) -> Dict[str, List]:
        """
        Extract annotation information.
        
        Args:
            annotation: WFDB annotation object
        
        Returns:
            Dictionary with annotation details
        """
        if annotation is None:
            return {'samples': [], 'symbols': [], 'types': []}
        
        return {
            'samples': annotation.sample.tolist(),
            'symbols': annotation.symbol,
            'types': annotation.aux_note if hasattr(annotation, 'aux_note') else []
        }
    
    def get_record_info(self, record_name: str) -> Dict:
        """
        Get metadata for a record without loading full signal.
        
        Args:
            record_name: Name of the record
        
        Returns:
            Dictionary with record metadata
        """
        try:
            record_path = str(self.data_dir / record_name)
            record = wfdb.rdheader(record_path)
            
            return {
                'record_name': record_name,
                'n_sig': record.n_sig,
                'sig_len': record.sig_len,
                'fs': record.fs,
                'sig_name': record.sig_name,
                'units': record.units,
                'duration_min': record.sig_len / record.fs / 60
            }
        except Exception as e:
            logger.error(f"Error reading header for {record_name}: {e}")
            return {}


def load_dataset_summary(data_dir: str) -> Dict:
    """
    Load summary information for entire dataset.
    
    Args:
        data_dir: Path to data directory
    
    Returns:
        Dictionary with dataset summary statistics
    """
    loader = APNEADataLoader(data_dir)
    records = loader.get_record_list()
    
    summary = {
        'total_records': len(records),
        'record_names': records,
        'records_info': []
    }
    
    for record_name in records[:5]:  # Sample first 5
        info = loader.get_record_info(record_name)
        if info:
            summary['records_info'].append(info)
    
    return summary


if __name__ == "__main__":
    # Example usage
    data_dir = "../data/raw"
    
    loader = APNEADataLoader(data_dir)
    records = loader.get_record_list()
    
    print(f"Found {len(records)} records")
    
    if records:
        # Load first record
        record, annotation = loader.load_record(records[0])
        
        if record:
            signals = loader.extract_signals(record)
            print(f"Extracted signals: {list(signals.keys())}")
            
            if annotation:
                ann_data = loader.extract_annotations(annotation)
                print(f"Number of annotations: {len(ann_data['samples'])}")
