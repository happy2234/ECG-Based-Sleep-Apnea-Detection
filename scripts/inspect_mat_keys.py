import glob
import scipy.io
import os

DATA_PATH = 'APNEA HRV+SPO2 DATASET/HuGCDN2014-OXI'
FOLDERS = ['C', 'D', 'ND']

for folder in FOLDERS:
    folder_path = os.path.join(DATA_PATH, folder)
    if not os.path.exists(folder_path):
        continue
    
    files = glob.glob(os.path.join(folder_path, '*.mat'))
    if files:
        sample_file = files[0]
        try:
            mat = scipy.io.loadmat(sample_file)
            keys = [k for k in mat.keys() if not k.startswith('__')]
            print(f"Folder {folder}: Sample file {os.path.basename(sample_file)} Keys: {keys}")
            
            # Print structure of first key
            if keys:
                val = mat[keys[0]]
                print(f"  Shape: {val.shape}, Dtype: {val.dtype}")
        except Exception as e:
            print(f"Error loading {sample_file}: {e}")
