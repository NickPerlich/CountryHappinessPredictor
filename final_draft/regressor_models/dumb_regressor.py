import numpy as np
import pandas as pd
from .base_regressor import BaseRegressor

class DumbRegressor(BaseRegressor):
    """
    A very simple regressor that predicts happiness score based only on
    log(GDP per capita, constant 2015 US$).
    This is intentionally simple and meant only as a baseline heuristic.
    """

    def __init__(self):
        super().__init__(name="DumbRegressor")
        self.feature_name = "GDP per capita (constant 2015 US$)"
        self.log_mean = None
        self.log_std = None

    def fit(self, X_train: pd.DataFrame, y_train: pd.Series):
        """
        This model does not learn a real regression.
        It stores the mean and std of log-GDP so predictions scale similarly.
        """
        # Take log (add epsilon to avoid log(0))
        log_gdp = np.log(X_train[self.feature_name] + 1e-9)

        self.log_mean = log_gdp.mean()
        self.log_std = log_gdp.std()

        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Happiness prediction = 5 + z-score(log GDP)
        z = (logGDP - mean) / std
        This produces values roughly in the 0-10 happiness range.
        """

        log_gdp = np.log(X[self.feature_name] + 1e-9)

        z = (log_gdp - self.log_mean) / (self.log_std + 1e-9)

        preds = 5 + z
        preds = preds.clip(0, 10)

        return preds.values