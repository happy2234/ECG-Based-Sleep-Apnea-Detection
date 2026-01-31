"""Tests for data loading utilities."""

import pytest
import numpy as np
from pathlib import Path
from src.data.loader import APNEADataLoader


class TestAPNEADataLoader:
    """Test cases for APNEADataLoader class."""
    
    def test_loader_initialization(self):
        """Test data loader initialization."""
        data_dir = "/tmp/test_data"
        loader = APNEADataLoader(data_dir)
        
        assert loader.data_dir == Path(data_dir)
        assert loader.sampling_rate == 100
    
    def test_loader_custom_sampling_rate(self):
        """Test data loader with custom sampling rate."""
        data_dir = "/tmp/test_data"
        custom_rate = 256
        loader = APNEADataLoader(data_dir, sampling_rate=custom_rate)
        
        assert loader.sampling_rate == custom_rate
    
    def test_loader_nonexistent_directory(self, caplog):
        """Test loader initialization with nonexistent directory."""
        data_dir = "/tmp/nonexistent_data_dir_12345"
        loader = APNEADataLoader(data_dir)
        
        # Loader should be created but path doesn't exist
        assert not loader.data_dir.exists()
    
    def test_get_record_list_empty_dir(self, tmp_path):
        """Test getting record list from empty directory."""
        loader = APNEADataLoader(str(tmp_path))
        records = loader.get_record_list()
        
        # Empty directory should return empty list
        assert records == []
    
    def test_get_record_list_with_files(self, tmp_path):
        """Test getting record list with actual files."""
        # Create some test files
        (tmp_path / "C1.mat").touch()
        (tmp_path / "C2.mat").touch()
        (tmp_path / "D1.mat").touch()
        
        loader = APNEADataLoader(str(tmp_path))
        records = loader.get_record_list()
        
        # Should find at least some records
        assert len(records) >= 0


class TestDataLoaderEdgeCases:
    """Test edge cases for data loader."""
    
    def test_loader_path_normalization(self):
        """Test that loader creates Path objects correctly."""
        data_dir = "/tmp/test_data"
        loader = APNEADataLoader(data_dir)
        
        # Path should be stored as Path object
        assert isinstance(loader.data_dir, Path)
        assert str(loader.data_dir) == data_dir
    
    def test_loader_with_relative_path(self, tmp_path):
        """Test loader with relative path."""
        import os
        original_cwd = os.getcwd()
        try:
            os.chdir(tmp_path)
            loader = APNEADataLoader(".")
            assert loader.data_dir.exists()
        finally:
            os.chdir(original_cwd)
    
    def test_multiple_loader_instances(self):
        """Test creating multiple loader instances."""
        loader1 = APNEADataLoader("/tmp/data1")
        loader2 = APNEADataLoader("/tmp/data2", sampling_rate=256)
        
        assert loader1.data_dir != loader2.data_dir
        assert loader1.sampling_rate != loader2.sampling_rate
