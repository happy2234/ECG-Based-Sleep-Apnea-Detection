"""
Download APNEA dataset from PhysioNet.

This script downloads the APNEA-ECG database from PhysioNet.
"""

import os
import sys
from pathlib import Path
import urllib.request
import tarfile
from tqdm import tqdm


class DownloadProgressBar(tqdm):
    """Progress bar for downloads."""
    
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url: str, output_path: str):
    """Download file with progress bar."""
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)


def download_apnea_dataset(output_dir: str = "../data/raw"):
    """
    Download APNEA dataset from PhysioNet.
    
    Args:
        output_dir: Directory to save downloaded files
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("=" * 60)
    print("APNEA Dataset Download from PhysioNet")
    print("=" * 60)
    
    # PhysioNet APNEA database URL
    base_url = "https://physionet.org/static/published-projects/apnea-ecg/apnea-ecg-database-1.0.0.zip"
    
    print(f"\nDataset will be downloaded to: {output_path.absolute()}")
    print(f"Source: {base_url}")
    
    # Download
    zip_file = output_path / "apnea-ecg.zip"
    
    if zip_file.exists():
        print(f"\n✓ File already exists: {zip_file}")
        response = input("Re-download? (y/n): ")
        if response.lower() != 'y':
            print("Skipping download.")
            return
    
    print("\nDownloading dataset...")
    try:
        download_url(base_url, str(zip_file))
        print(f"\n✓ Download complete: {zip_file}")
    except Exception as e:
        print(f"\n✗ Download failed: {e}")
        print("\nPlease manually download from:")
        print("https://physionet.org/content/apnea-ecg/1.0.0/")
        return
    
    # Extract
    print("\nExtracting files...")
    try:
        import zipfile
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(output_path)
        print("✓ Extraction complete")
    except Exception as e:
        print(f"✗ Extraction failed: {e}")
        return
    
    print("\n" + "=" * 60)
    print("Dataset download complete!")
    print("=" * 60)
    print(f"\nFiles location: {output_path.absolute()}")
    print("\nNext steps:")
    print("1. Run EDA notebook: notebooks/01_EDA.ipynb")
    print("2. Check data structure with: python -m src.data.loader")


if __name__ == "__main__":
    download_apnea_dataset()
