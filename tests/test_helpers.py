"""Tests for utility helper functions."""

import numpy as np
import pytest
from src.utils.helpers import normalize_signal, segment_signal


class TestNormalizeSignal:
    """Test cases for normalize_signal function."""
    
    def test_normalize_signal_zscore(self):
        """Test z-score normalization."""
        signal = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        normalized = normalize_signal(signal, method='zscore')
        
        # Check mean is close to 0
        assert np.isclose(np.mean(normalized), 0, atol=1e-10)
        # Check std is close to 1
        assert np.isclose(np.std(normalized), 1, atol=1e-10)
    
    def test_normalize_signal_minmax(self):
        """Test min-max normalization."""
        signal = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        normalized = normalize_signal(signal, method='minmax')
        
        # Check range is [0, 1]
        assert np.isclose(np.min(normalized), 0)
        assert np.isclose(np.max(normalized), 1)
    
    def test_normalize_signal_robust(self):
        """Test robust normalization."""
        signal = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        normalized = normalize_signal(signal, method='robust')
        
        # Check that it returns valid output
        assert len(normalized) == len(signal)
        assert np.all(np.isfinite(normalized))
    
    def test_normalize_signal_invalid_method(self):
        """Test invalid normalization method raises error."""
        signal = np.array([1.0, 2.0, 3.0])
        
        with pytest.raises(ValueError, match="Unknown normalization method"):
            normalize_signal(signal, method='invalid')
    
    def test_normalize_signal_constant_signal_zscore(self):
        """Test z-score normalization with constant signal."""
        signal = np.array([5.0, 5.0, 5.0, 5.0])
        # Constant signal will have std=0, resulting in NaN
        normalized = normalize_signal(signal, method='zscore')
        assert np.all(np.isnan(normalized))


class TestSegmentSignal:
    """Test cases for segment_signal function."""
    
    def test_segment_signal_no_overlap(self):
        """Test signal segmentation without overlap."""
        signal = np.arange(100, dtype=float)
        window_size = 10
        segments = segment_signal(signal, window_size, overlap=0)
        
        # Should have 10 segments
        assert segments.shape == (10, 10)
        # First segment should match first 10 samples
        assert np.array_equal(segments[0], signal[:10])
    
    def test_segment_signal_with_overlap(self):
        """Test signal segmentation with overlap."""
        signal = np.arange(100, dtype=float)
        window_size = 10
        overlap = 5
        segments = segment_signal(signal, window_size, overlap=overlap)
        
        # Each segment should be window_size
        assert segments.shape[1] == window_size
        # Check that overlap is correct
        assert np.array_equal(segments[0, 5:], segments[1, :5])
    
    def test_segment_signal_single_segment(self):
        """Test segmentation resulting in single segment."""
        signal = np.arange(10, dtype=float)
        window_size = 10
        segments = segment_signal(signal, window_size, overlap=0)
        
        assert segments.shape == (1, 10)
        assert np.array_equal(segments[0], signal)
    
    def test_segment_signal_small_overlap(self):
        """Test segmentation with signal smaller than window."""
        signal = np.arange(5, dtype=float)
        window_size = 10
        segments = segment_signal(signal, window_size, overlap=0)
        
        # No complete windows, so should have 0 segments
        assert segments.shape[0] == 0


class TestIntegration:
    """Integration tests for helper functions."""
    
    def test_normalize_and_segment(self):
        """Test normalizing and segmenting a signal."""
        signal = np.random.randn(1000)
        normalized = normalize_signal(signal, method='zscore')
        segments = segment_signal(normalized, window_size=100, overlap=50)
        
        # Check dimensions
        assert len(segments.shape) == 2
        assert segments.shape[1] == 100
        
        # Check normalized signal properties
        assert np.isclose(np.mean(normalized), 0, atol=1e-10)
        assert np.isclose(np.std(normalized), 1, atol=1e-10)
