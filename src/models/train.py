import pandas as pd
import numpy as np
import argparse
import logging
from sklearn.model_selection import StratifiedKFold
from src.models.random_forest_model import SleepApneaRFModel
from src.models.cnn_lstm_model import SleepApneaCNNLSTMModel
from src.data.loader import APNEADataLoader
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def train_rf(data_path, model_output_path):
    """Train and evaluate Random Forest model using 5-fold cross-validation."""
    logger.info(f"Loading data from {data_path}")
    df = pd.read_csv(data_path)
    
    rf_wrapper = SleepApneaRFModel()
    X, y = rf_wrapper.preprocess(df)
    
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    fold_reports = []
    
    for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):
        logger.info(f"Training fold {fold + 1}/5")
        X_train, X_val = X[train_idx], X[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
        
        rf_wrapper.train(X_train, y_train)
        report, cm = rf_wrapper.evaluate(X_val, y_val)
        
        fold_reports.append(report)
        logger.info(f"Fold {fold + 1} Evaluation:\n{report}")

    # Train on full dataset for final model
    logger.info("Training final model on full dataset...")
    rf_wrapper.train(X, y)
    rf_wrapper.save_model(model_output_path)
    
    return fold_reports

def train_cnn_lstm(data_dir, model_output_path, segment_seconds=60, epochs=20):
    """Train and evaluate CNN-LSTM model."""
    logger.info(f"Loading and segmenting data from {data_dir}")
    loader = APNEADataLoader(data_dir)
    records = loader.get_record_list()
    
    # Stratified split by record to avoid data leakage
    train_recs, test_recs = StratifiedKFold(n_splits=5, shuffle=True, random_state=42).split(records, [1 if 'apn' in r.lower() else 0 for r in records]).__next__()
    
    train_record_names = [records[i] for i in train_recs]
    test_record_names = [records[i] for i in test_recs]
    
    logger.info("Loading training segments...")
    X_train, y_train = loader.get_segmented_dataset(train_record_names, segment_seconds=segment_seconds)
    logger.info("Loading testing segments...")
    X_test, y_test = loader.get_segmented_dataset(test_record_names, segment_seconds=segment_seconds)
    
    # Reshape for CNN-LSTM: (samples, time_steps, features)
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
    
    model_wrapper = SleepApneaCNNLSTMModel(input_shape=(X_train.shape[1], 1))
    model_wrapper.train(X_train, y_train, X_test, y_test, epochs=epochs)
    model_wrapper.save_model(model_output_path)
    
    loss, acc = model_wrapper.evaluate(X_test, y_test)
    logger.info(f"CNN-LSTM Test Accuracy: {acc:.4f}")
    return acc

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Sleep Apnea Detection Models")
    parser.add_argument("--model_type", type=str, default="rf", help="Type of model to train (rf)")
    parser.add_argument("--data_path", type=str, default="processed_data/extracted_features.csv", help="Path to feature CSV")
    parser.add_argument("--output_path", type=str, default="models/rf_baseline.pkl", help="Path to save model")
    
    args = parser.parse_args()
    
    if args.model_type == "rf":
        train_rf(args.data_path, args.output_path)
    elif args.model_type == "cnn_lstm":
        # For CNN-LSTM, data_path is expected to be the raw data directory
        raw_data_dir = "APNEA HRV+SPO2 DATASET/HuGCDN2014-OXI"
        train_cnn_lstm(raw_data_dir, args.output_path)
    else:
        logger.error(f"Unsupported model type: {args.model_type}")
