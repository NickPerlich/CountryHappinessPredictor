import numpy as np
import pandas as pd
from abc import ABC, abstractmethod

class BaseRegressor(ABC):
    """Base class for all regression models."""

    def __init__(self, name: str):
        self.name = name
        self.model = None

    @abstractmethod
    def fit(self, X_train: pd.DataFrame, y_train: pd.Series):
        """Train the regression model."""
        pass

    @abstractmethod
    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """Predict values (continuous)."""
        pass