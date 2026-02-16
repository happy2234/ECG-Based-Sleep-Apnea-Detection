import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import logging
import os

class SleepApneaCNNLSTMModel:
    def __init__(self, input_shape):
        """
        Initialize the CNN-LSTM model.
        
        Args:
            input_shape: Tuple (time_steps, n_features)
        """
        self.input_shape = input_shape
        self.model = self._build_model()
        self.logger = logging.getLogger(__name__)

    def _build_model(self):
        """Build the CNN-LSTM architecture."""
        model = models.Sequential()
        
        # CNN layers for spatial/local features
        model.add(layers.Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=self.input_shape))
        model.add(layers.MaxPooling1D(pool_size=2))
        model.add(layers.Dropout(0.2))
        
        model.add(layers.Conv1D(filters=128, kernel_size=3, activation='relu'))
        model.add(layers.MaxPooling1D(pool_size=2))
        model.add(layers.Dropout(0.2))
        
        # LSTM layer for temporal dependencies
        model.add(layers.LSTM(units=100, return_sequences=False))
        model.add(layers.Dropout(0.2))
        
        # Fully connected layers
        model.add(layers.Dense(50, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))
        
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, X_val, y_val, epochs=50, batch_size=32):
        """Train the model."""
        self.logger.info("Training CNN-LSTM model...")
        history = self.model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=epochs,
            batch_size=batch_size,
            callbacks=[
                tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True)
            ]
        )
        return history

    def evaluate(self, X_test, y_test):
        """Evaluate the model."""
        return self.model.evaluate(X_test, y_test)

    def predict(self, X):
        """Predict labels for input data."""
        return (self.model.predict(X) > 0.5).astype(int)

    def save_model(self, path):
        """Save the model to a file."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.model.save(path)
        self.logger.info(f"Model saved to {path}")

    @staticmethod
    def load_model(path):
        """Load a saved model."""
        return tf.keras.models.load_model(path)
