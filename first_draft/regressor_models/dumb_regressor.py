import numpy as np
import pandas as pd
from .base_regressor import BaseRegressor

class DumbRegressor(BaseRegressor):
    """
    A very simple regressor that predicts happiness score based only on
    Adjusted net national income (current US$).
    This is intentionally simple and meant only as a baseline heuristic.
    """

    def __init__(self):
        super().__init__(name="DumbIncomeRegressor")
        # will store scale info so prediction works later
        self.income_mean = None
        self.income_std = None

    def fit(self, X_train: pd.DataFrame, y_train: pd.Series):
        """
        This model does not actually learn parameters.
        It only stores mean/std of the income column so predictions use similar scaling.
        """
        income_col = "Adjusted net national income (current US$)"

        self.income_mean = X_train[income_col].mean()
        self.income_std = X_train[income_col].std()

        # No real training happens
        return self

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predicts happiness as a normalized version of national income.
        (mean + std normalization brings values roughly into 0-10 range)
        """

        income_col = "Adjusted net national income (current US$)"
        income = X[income_col]

        # basic scaling to make numbers roughly in 0–10 range
        z = (income - self.income_mean) / (self.income_std + 1e-9)

        # shift into a plausible happiness range and clip outliers
        preds = 5 + z
        preds = np.clip(preds, 0, 10)

        return preds.values
