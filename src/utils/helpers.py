"""Utility functions for the ECG Sleep Apnea Detection project."""

import numpy as np
from typing import Tuple


def normalize_signal(signal: np.ndarray, method: str = 'zscore') -> np.ndarray:
    """
    Normalize a signal using specified method.
    
    Args:
        signal: Input signal array
        method: Normalization method ('zscore', 'minmax', 'robust')
    
    Returns:
        Normalized signal
    """
    if method == 'zscore':
        return (signal - np.mean(signal)) / np.std(signal)
    elif method == 'minmax':
        return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))
    elif method == 'robust':
        median = np.median(signal)
        mad = np.median(np.abs(signal - median))
        return (signal - median) / mad
    else:
        raise ValueError(f"Unknown normalization method: {method}")


def segment_signal(
    signal: np.ndarray, 
    window_size: int, 
    overlap: int = 0
) -> np.ndarray:
    """
    Segment signal into overlapping windows.
    
    Args:
        signal: Input signal
        window_size: Size of each window
        overlap: Number of samples to overlap
    
    Returns:
        Array of shape (n_windows, window_size)
    """
    step = window_size - overlap
    n_windows = (len(signal) - window_size) // step + 1
    
    segments = np.array([
        signal[i*step:i*step+window_size] 
        for i in range(n_windows)
    ])
    
    return segments


def calculate_snr(signal: np.ndarray, noise: np.ndarray) -> float:
    """
    Calculate Signal-to-Noise Ratio.
    
    Args:
        signal: Clean signal
        noise: Noise signal
    
    Returns:
        SNR in dB
    """
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    
    if noise_power == 0:
        return float('inf')
    
    snr = 10 * np.log10(signal_power / noise_power)
    return snr
