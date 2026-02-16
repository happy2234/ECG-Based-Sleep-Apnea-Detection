import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pickle
import os
import logging

class SleepApneaRFModel:
    def __init__(self, n_estimators=100, max_depth=None, random_state=42):
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state,
            class_weight='balanced'
        )
        self.scaler = StandardScaler()
        self.logger = logging.getLogger(__name__)

    def preprocess(self, df):
        """Preprocess features: separate X, y and scale features."""
        # Drop filename and handle label
        if 'filename' in df.columns:
            df = df.drop(columns=['filename'])
        
        X = df.drop(columns=['label'])
        y = df['label']
        
        X_scaled = self.scaler.fit_transform(X)
        return X_scaled, y

    def train(self, X_train, y_train):
        """Train the Random Forest model."""
        self.logger.info("Training Random Forest model...")
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """Evaluate the model and return metrics."""
        y_pred = self.model.predict(X_test)
        report = classification_report(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        return report, cm

    def save_model(self, path):
        """Save the model and scaler to a pickle file."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump({'model': self.model, 'scaler': self.scaler}, f)
        self.logger.info(f"Model saved to {path}")

    @staticmethod
    def load_model(path):
        """Load the model and scaler from a pickle file."""
        with open(path, 'rb') as f:
            data = pickle.load(f)
        return data['model'], data['scaler']
