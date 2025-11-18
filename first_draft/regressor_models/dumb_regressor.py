import numpy as np
import pandas as pd
from base_regressor import BaseRegressor

class DumbIncomeRegressor(BaseRegressor):
    """
    Uses Adjusted Net National Income (current US$) as the
    sole predictor of Happiness Score using simple linear regression.
    """

    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
        self.feature_name = "Adjusted net national income (current US$)"

    def fit(self, df):
        # X = income, y = happiness
        X = df[self.feature_name].values
        y = df["Happiness Score"].values

        # Handle missing values (drop them for this dumb model)
        mask = ~np.isnan(X) & ~np.isnan(y)
        X = X[mask]
        y = y[mask]

        # Simple linear regression math
        X_mean = X.mean()
        y_mean = y.mean()
        cov = ((X - X_mean) * (y - y_mean)).sum()
        var = ((X - X_mean) ** 2).sum()

        self.coef_ = cov / var
        self.intercept_ = y_mean - self.coef_ * X_mean

    def predict(self, df):
        X = df[self.feature_name].fillna(0).values
        return self.intercept_ + self.coef_ * X
